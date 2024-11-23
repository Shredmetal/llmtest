# Semantic Boundary Analysis

## Overview

During our real-world style testing, we encountered an interesting semantic boundary case that highlighted both the sophistication and limitations of LLM-based testing. 

This was discovered during the initial 500 runs of our real-world test suite, as only this one test demonstrated non-determinism.

This case provides valuable insights into how LLMs interpret semantic requirements.

## The Case

This is our healthcare test case:

```
def test_patient_education_diabetes_management(self, asserter):
        """Test semantic matching for patient education content about diabetes management. Failure is expected because
        this does not contain emergency response steps."""
        actual = """
        Understanding and Managing Type 2 Diabetes
    
        Type 2 diabetes is a chronic condition that affects how your body processes blood sugar (glucose). 
        While this condition is serious, it can be effectively managed through lifestyle changes and, 
        when necessary, medication. This guide will help you understand the key aspects of diabetes 
        management.
    
        Blood Sugar Monitoring:
        Regular blood sugar monitoring is essential. Your target blood glucose levels should typically 
        be 80-130 mg/dL before meals and less than 180 mg/dL two hours after meals. However, your 
        healthcare provider may set different targets based on your individual needs. Keep a log of 
        your readings to identify patterns and adjust your management strategy accordingly.
    
        Dietary Considerations:
        A balanced diet is crucial for managing type 2 diabetes. Focus on:
        - Controlling portion sizes
        - Choosing high-fiber, low-glycemic foods
        - Limiting refined carbohydrates and processed sugars
        - Including lean proteins and healthy fats
        - Spacing meals evenly throughout the day
    
        Physical Activity:
        Regular exercise helps control blood sugar levels by improving insulin sensitivity. Aim for:
        - At least 150 minutes of moderate-intensity aerobic activity weekly
        - Resistance training 2-3 times per week
        - Daily movement, even if just short walks
        Always check your blood sugar before and after exercise, and carry a fast-acting 
        carbohydrate source.
    
        Medication Management:
        If prescribed, take diabetes medications as directed. Common medications include:
        - Metformin (helps reduce glucose production)
        - Sulfonylureas (increase insulin production)
        - DPP-4 inhibitors (help maintain blood sugar control)
        Never adjust or stop medications without consulting your healthcare provider.
    
        Warning Signs:
        Learn to recognize and respond to:
        - Hypoglycemia (low blood sugar): shakiness, sweating, confusion
        - Hyperglycemia (high blood sugar): increased thirst, frequent urination, fatigue
        Seek immediate medical attention if you experience severe symptoms or sustained 
        high blood sugar levels.
    
        Regular Health Monitoring:
        Schedule regular check-ups with your healthcare team, including:
        - HbA1c tests every 3-6 months
        - Annual eye examinations
        - Regular foot checks
        - Kidney function tests
        - Cholesterol level monitoring
    
        Remember, diabetes management is a journey, not a destination. Small, consistent 
        steps in the right direction can lead to significant improvements in your health 
        and quality of life.
        """

        expected = """A medical education document that must:
        1. Contain an overview section explaining the condition
        2. List specific numerical guidelines (blood sugar ranges, exercise minutes)
        3. Include structured sections for diet, exercise, and medication
        4. Provide clear warning signs AND detailed emergency response procedures
        5. End with follow-up care instructions"""

        with pytest.raises(SemanticAssertionError) as excinfo:
            asserter.assert_semantic_match(actual, expected)
        assert "Semantic assertion failed" in str(excinfo.value)
```

The relevant portions are here as follows:

In `actual` (i.e. the simulated LLM output):
```
Warning Signs:
Learn to recognize and respond to:
- Hypoglycemia (low blood sugar): shakiness, sweating, confusion
- Hyperglycemia (high blood sugar): increased thirst, frequent urination, fatigue
Seek immediate medical attention if you experience severe symptoms or sustained 
high blood sugar levels.
```
In `expected_behavior` (i.e. the specification we expect developers to write when using our library):

Version that led to non-determinism:
```
4. Provide clear warning signs and emergency response steps
```

Updated version that led to determinism:
```
4. Provide clear warning signs AND detailed emergency response procedures
```

## Test Configuration

All tests used library defaults:

```
LLM_PROVIDER=openai
LLM_MODEL=gpt-4o 
LLM_TEMPERATURE=0.0 
LLM_MAX_TOKENS=4096 
LLM_MAX_RETRIES=2 
LLM_TIMEOUT=10.0 # Added for OpenAI in 0.1.0b5 using the underlying Langchain implementation 
```
The `semantic_assert_match` function also saw slight modification:

```
        if result.startswith("FAIL"):
            raise SemanticAssertionError(
                "Semantic assertion failed",
                reason=result.split("FAIL: ")[1]
            )
            
        # Section below added to cause failure in the event of format violation    
            
        elif result.startswith("PASS"):
            pass
        else:
            raise RuntimeError(
                f"Format Non-compliance Detected {result}"
            )
```

The prompts to the asserter LLM (that sits behind `semantic_assert_match`) were:

```
DEFAULT_SYSTEM_PROMPT = """You are a testing system. Your job is to determine if an actual output matches the expected behavior.

Important: You can only respond with EXACTLY: 
1. 'PASS' if it matches, or 
2. 'FAIL: <reason>' if it doesn't match.

Any other type of response will mean disaster which as a testing system, you are meant to prevent.

Be strict but consider semantic meaning rather than exact wording."""

DEFAULT_HUMAN_PROMPT = """
Expected Behavior: {expected_behavior}

Actual Output: {actual}

Does the actual output match the expected behavior? Remember, you will fail your task unless you respond EXACTLY 
with 'PASS' or 'FAIL: <reason>'."""
```

## Testing Results

This particular test was run 600 times.

It was run 500 times in a wider test of the entire suite it is a part of and 100 times on its own with the following results:

- PASS: 586
- FAIL: 14

The 100 individual tests were run when the non-determinism was noticed.

API response times were noticeable faster when it started failing. 

Test suite execution times for 100 iterations (so 1,000 individual tests):

- ~1550s - 1750s when it appeared to deterministically pass the test
- ~1350s when it began to exhibit non-determinism

We are unable to determine what longer API response times mean, and unless if OpenAI wades in, it is unlikely that we will find out.

Logs can be found in the reliability_testing_real_world directory of the [0.1.0b5 branch](https://github.com/Shredmetal/llmtest/tree/release/0.1.0b5/reliability_testing_real_world) of the github repo.

## Analysis

Upon careful analysis (Library author's note: I had to read the test case several times to pick up on it, and I'm a lawyer by training with 3 years of litigation experience), we identified a subtle but critical semantic boundary in the original requirement:

1. The Semantic Boundary:
   - Original text: "emergency response steps" (plural)
   - Test content provided: "seek medical attention" (singular)
   - Question: Does a single, obvious response step satisfy a requirement for "steps"?

2. The Test Content:
   - Clearly provided warning signs
   - Had one emergency response ("seek medical attention")
   - Lacked detailed, multiple-step emergency procedures

3. Interpretation Analysis:

   A. Argument for Single-Step Sufficiency:
   - The content is patient-focused, not for medical professionals
   - "Seek medical attention" is a complete, actionable instruction
   - In an emergency, simplicity and clarity are paramount
   - Additional steps might confuse or delay the critical action

   B. Argument for Multiple-Step Requirement:
   - The plural "steps" grammatically implies multiple procedures
   - Medical context demands comprehensive guidance
   - "Seek medical attention" is too obvious to constitute meaningful instruction
   - Patients need interim steps while medical help is en route

   C. Resolution:
   - While both interpretations have merit, the requirement for multiple steps is substantially stronger because:
     1. The plural form explicitly requests multiple procedures
     2. Medical documentation should err on the side of completeness
     3. Interim guidance can be critical during emergency response
     4. Self-evident instructions add no value to emergency protocols

4. Key Insight:
   The non-deterministic behavior of the LLM in this case reveals a genuine semantic boundary in medical documentation - the balance between simplicity and comprehensiveness in emergency instructions.

## Key Learnings

1. LLM Sophistication:
   - The LLM detected the semantic ambiguity
   - Demonstrated surprisingly strong interpretation capabilities
   - Highlighted the importance of precise requirements

2. Testing Implications:
   - Requirements must be unambiguous
   - Precision in language can improve test reliability (seriously, this is natural language, you can throw writing the `expected_behavior` to the non-technical PM)
   - Literal interpretations should ALWAYS be preferred. Try to think like a lawyer - it's how I picked up why the test case was being incorrectly accepted (note that I am testing a negative test, so FAIL means that it was incorrectly passed by `assert_semantic_match`)

## Impact on Library Usage

When writing semantic test cases:
1. Be explicit about conjunctive requirements
2. Use "AND" when both elements are required
3. Consider potential semantic ambiguities
4. Test requirements for potential boundary cases

## Quick Links
- [Semantic Reliability Testing](semantic_reliability.md)
- [Format Compliance](./format_compliance.md)
- [Quick Start](../getting-started/quickstart.md)


