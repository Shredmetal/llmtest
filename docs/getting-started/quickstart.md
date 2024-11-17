[← Back to Home](../index.md)

# Quick Start

Get up and running with llm_app_test in under 5 minutes.

## 1. Set Up Environment

Create a `.env` file in your project root:

```
# For OpenAI

OPENAI_API_KEY=your-openai-api-key-here

# OR for Anthropic

ANTHROPIC_API_KEY=your-anthropic-key-here
```

## 2. Write Your First Test

```

from llm_app_test.semanticassert.semantic_assert import SemanticAssertion

def my_first_semantic_test(): 

    # Initialize asserter 
    semantic_assert = SemanticAssertion()
    
    # Your LLM output
    actual_output = "The sky is blue"
    
    # Expected behavior in natural language
    expected_behavior = "A statement about the color of the sky"
    
    # Test semantic equivalence
    semantic_assert.assert_semantic_match(
        actual=actual_output,
        expected_behavior=expected_behavior
)
    
```

## 3. Run Your Test

```
pytest my_first_semantic_test.py
```

## Next Steps

- [CI/CD Integration](../guides/ci-cd.md) - Set up automated testing
- [Configuration](../api/configuration.md) - Configure llm_app_test for your needs

## Additional notes:

## Real World Example
> Want to see llm_app_test in action? Here's a real test from our test suite:

```

from llm_app_test.semanticassert.semantic_assert import SemanticAssertion 
from llm_app_test.tests.test_content_generators.test_greeting_bot import SimpleGreetingBot

def test_greeting_semantic(): 

    semantic_assert = SemanticAssertion()
    
    bot = SimpleGreetingBot()
    actual_output = bot.generate_greeting("Alice")
    
    expected_behavior = """
    A polite greeting that:
    1. Addresses the person by name (Alice)
    2. Asks about their wellbeing
    """
    
    semantic_assert.assert_semantic_match(
        actual=actual_output,
        expected_behavior=expected_behavior
    )
    
```

You can find this example in our repository: [test_greeting.py](https://github.com/Shredmetal/llmtest/blob/main/tests/actual_usage_tests/test_greeting.py)

It can be run from this project root with the following command:

```
pytest tests/actual_usage_tests/test_greeting.py

```

You can find and run this example:

```
# Clone the repository

git clone https://github.com/Shredmetal/llmtest.git

# Run the test

pytest tests/actual_usage_tests/test_greeting.py
```