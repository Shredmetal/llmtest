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

```# Good
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

1. **Keep Tests Focused**:

```
# Good
def test_greeting_behavior(): """Test greeting behavior only"""
def test_personalization_behavior(): """Test name usage separately"""

# Bad - testing too much
def test_everything_about_greeting(): """Testing multiple aspects at once"""
```

2. **Clear Test Names**:

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
4. Use appropriate model tiers

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
