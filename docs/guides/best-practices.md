[← Back to Home](../index.md)

# Best Practices

Guidelines for effective behavioral testing with llm_app_test.

## Understanding Behavioral Testing

When testing LLM applications, focus on describing what your application should do rather than how it should do it.

Behavioral testing focuses on validating that outputs exhibit expected characteristics and behaviors in a declarative manner. For example:

Expected Behavior: 

```
"A response that provides a weather forecast including temperature and conditions"
```

These responses would PASS:

```
actual_1 = "Today will be sunny with a high of 75°F"
actual_2 = "Expect cloudy skies and temperatures around 24°C"
actual_3 = "The forecast shows clear weather, reaching 298K"
```

These would FAIL:

```
fail_1 = "Have a nice day!" (missing forecast elements)
fail_2 = "It's weather time!" (missing required information)
fail_3 = "75 degrees" (incomplete behavior)
```

## Writing Good Expected Behaviors

1. **Be Specific**:

    ```
    # Good
    expected_behavior = """ A polite greeting that:
                        Addresses the person by name (Alice)
                        Asks about their wellbeing """
                        
    # Bad - too vague
    expected_behavior = "A nice greeting"
    ```

2. **Focus on Behaviors**:

    ```
    # Good
    expected_behavior = """ An error message that:
                        Explains the API key is invalid
                        Provides steps to fix the issue """
                        
    # Bad - testing exact wording - DO NOT USE llm_app_test FOR THIS, USE REGULAR PYTEST
    expected_behavior = "Should say 'Invalid API key'"
    ```

## When to Use Behavioral Testing

Good Use Cases:

- Testing LLM outputs
- Validating natural language responses
- Testing content generation
- Checking response behaviors

Not Suitable For:

- Exact string matching
- Numerical comparisons
- Binary conditions

## Test Structure

1. **Test Scope Based on Behavioral Requirements**:

    ```
    # Testing Single Behavior 
    def test_greeting_format(): 
      """Test that greeting follows required format"""
    ```
   
    ```
    # Testing Multiple Related Behaviors
    def test_patient_education_diabetes():
   
       expected = """Test comprehensive diabetes education document including:
        - Overview section
        - Numerical guidelines
        - Structured sections
        - Warning signs
        - Follow-up instructions"""
    ```
   
2. **Choose Test Scope Based on Document Purpose**:
    * Single behavior tests for simple, focused requirements
    * Comprehensive behavior tests for complete documents
    * Let document purpose drive test structure

3. **Clear Test Names**:

    ```
    # Good
    def test_error_message_includes_solution_steps():
    
    # Bad
    def test_error():
    ```

## Common Pitfalls

1. **Over-Specific Expected Behaviors**:

    ```
    # Too specific
    expected = "Must say hello and use exactly these words"
    
    # Better
    expected = "Should be a greeting in conversational English"
    ```

2. **Under-Specific Expected Behaviors**:

    ```
    # Too vague
    expected = "Should be good"
    
    # Better
    expected = """ Response should:
               Answer the user's question
               Use professional language
               Stay on topic """
    ```

## Cost Optimisation

1. Use specific, focused tests
2. Group related behavioral tests
3. Consider test importance vs cost

## Model Selection

We ran extensive tests on our library with GPT-4o, and limited tests with Claude 3.5 Sonnet.

What we found is that Claude is a little more "lax" (for want of a better word). While GPT-4o will adopt a more strict and literal interpretation, Claude has shown a tendency to be more lenient (and seems to try to pass cases based on "intent"), and adopt a less pedantic stance on what constitutes meeting the requirements.

Let's look at the example from our behavioral testing at semantic boundaries documentation:

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

Version that led to non-determinism (14 out of 600 runs with GPT-4o did not fail this test case for not providing emergency response steps):
```
4. Provide clear warning signs and emergency response steps
```

Updated version that led to determinism (1,200 out of 1,200 test runs were correctly failed):
```
4. Provide clear warning signs AND detailed emergency response procedures
```

However, Claude 3.5 Sonnet does not consistently fail this test case even when asked for detailed emergency response procedures (no volume testing done but significant non-determinism observed in <100 runs).

Claude actually needs to specifically be told to look for multi-step emergency response procedures like so:

```
4. Provide clear warning signs AND detailed multi-step emergency response procedures
```

Needless to say, this is generally **NOT** what you want in a testing system, unless if you want to simulate a flexible developer manually testing your bot. We do not recommend this. We recommend writing test cases with the expectation that the LLM will apply a strict literal interpretation.

Therefore, we recommend sticking to the library default of GPT-4o, unless if you have a specific reason for doing otherwise.

---
## Closing words

This testing approach is designed to mimic how a human would validate your LLM application's behavior. 
Think about what behaviors you want to verify and express them clearly in natural language.

---
## Navigation

- [Back to Home](../index.md)
- [Installation Guide](../getting-started/installation.md)
- [Quick Start Guide](../getting-started/quickstart.md)
- [API Reference](../api/behavioral-assertion.md)
