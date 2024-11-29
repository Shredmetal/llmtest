[← Back to Home](../index.md)

# Custom Prompt Configuration - Understanding the Options

⚠️ **Important Notice**
Custom prompt configuration is an advanced feature that can affect the reliability of your testing framework if not used carefully. We strongly recommend using the default prompts unless you have a specific, well-understood need for customization.

## Default Prompts

The library uses these carefully designed default prompts that have been tested across thousands (>30,000) of iterations:

System Prompt:
```
You are a testing system. Your job is to determine if an actual output matches the expected behavior.

Important: You can only respond with EXACTLY: 
1. 'PASS' if it matches, or 
2. 'FAIL: <reason>' if it doesn't match.

Any other type of response will mean disaster which as a testing system, you are meant to prevent.

Be strict but consider semantic meaning rather than exact wording.
```

```
Human Prompt:
Expected Behavior: {expected_behavior}

Actual Output: {actual}

Does the actual output match the expected behavior? Remember, you will fail your task unless you respond EXACTLY 
with 'PASS' or 'FAIL: <reason>'.
```

## Why Custom Prompts Require Careful Consideration

1. Format Reliability:

    - Custom prompts might not enforce the strict PASS/FAIL format
    - This leads to runtime errors when the LLM returns unexpected formats
    - The default prompts are specifically designed to maintain format compliance
    - Format compliance is critical - any deviation can cause immediate test failure

2. Testing Consistency:

    - Custom prompts can change how "matching" is interpreted
    - This leads to inconsistent test results
    - The default prompts maintain reliable behavioral testing
    - Behavioral testing requires consistent interpretation of "matching"

3. Non-determinism:

    - Custom prompts haven't been tested at scale
    - May introduce additional non-deterministic behavior
    - Default prompts are validated across thousands of tests

## Why Allow Custom Prompts?

While custom prompts are risky, we recognise that some testing scenarios might require specialized evaluation criteria. However, this should be extremely rare - the default prompts have been proven reliable across a wide range of testing scenarios.

## If You Must Use Custom Prompts

If you absolutely need to use custom prompts:

1. Maintain Format Requirements:

    - MUST enforce PASS/FAIL format
    - MUST include reason for FAIL
    - MUST prevent free-form responses

2. Test Extensively:

    - Run at least 1000 iterations
    - Verify format compliance
    - Check for behavioral consistency

3. Documentation:

    - Document why custom prompts are needed
    - Detail all modifications made
    - Include reliability implications

## Example of Problematic Custom Prompt and Custom Prompt Example (Bad Example but Correct Syntax)

DO NOT USE - For Illustration Only:

```
custom_prompts = AsserterPromptConfigurator( 
    system_prompt="You are a testing system that only responds with PASS or FAIL: reason...", 
    human_prompt="Compare:\nExpected: {expected_behavior}\nActual: {actual}" 
    )
    
asserter = BehavioralAssertion(
    provider="openai",
    custom_prompts=custom_prompts
)

# The assertion works the same way

asserter.assert_behavioral_match(
    actual="Hello, world!",
    expected_behavior="Should greet the world"
)
```


This example is problematic because it:
- Doesn't enforce strict format requirements
- Lacks behavioral evaluation guidance
- Missing format compliance constraints
- No safeguards against non-determinism

## Recommended Approach

1. Start with default prompts
2. Document why they don't meet your needs
3. Consult the development team
4. Consider alternative solutions
5. Only then, if absolutely necessary, create custom prompt configurations

## Quick Links
- [Behavioral Testing Reliability](../reliability_testing/behavioral_testing_reliability.md)
- [Format Compliance](../reliability_testing/format_compliance.md)
- [Testing Best Practices](../guides/best-practices.md)
