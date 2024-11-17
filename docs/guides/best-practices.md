[← Back to Home](../index.md)

# Best Practices

Guidelines for effective semantic testing with llm_app_test.

## Understanding Semantic Testing

Semantic testing focuses on meaning rather than exact matches. For example:

```
# THESE ARE SEMANTICALLY EQUIVALENT

actual_1 = "Hello Alice, how are you today?" 
actual_2 = "Hi Alice! Hope you're doing well!" 
expected = "A polite greeting addressing Alice"
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

2. **Focus on Requirements**:

```
# Good

expected_behavior = """ An error message that:
                    Explains the API key is invalid
                    Provides steps to fix the issue """

# Bad - testing exact wording - DO NOT USE llm_app_test FOR THIS, JUST USE REGULAR PYTEST

expected_behavior = "Should say 'Invalid API key'"
```


## When to Use Semantic Testing

Good Use Cases:
- Testing LLM outputs
- Validating natural language responses
- Testing content generation

Not Suitable For:
- Exact string matching
- Numerical comparisons
- Binary conditions

## Test Structure

1. **Keep Tests Focused**:

```
# Good

def test_greeting_format(): """Test greeting format only"""

def test_greeting_personalization(): """Test name usage separately"""

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

## Cost Optimization

1. Use specific, focused tests
2. Group related semantic tests
3. Consider test importance vs cost
4. Use appropriate model tiers

---
## Closing words

In general, this is a complete different type of testing designed to mimic a human testing your LLM application. 
You might need to use your brain a little bit to figure out to instruct your assistant on what to check.

---
## Navigation

- [Back to Home](../index.md)
- [Installation Guide](../getting-started/installation.md)
- [Quick Start Guide](../getting-started/quickstart.md)
- [API Reference](../api/semantic-assertion.md)
