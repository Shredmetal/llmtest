# llmtest

A semantic testing framework for LLM applications that uses LLMs to validate semantic equivalence in test outputs.

## Why llmtest?

Testing LLM applications is hard because:
- Outputs are non-deterministic
- Semantic meaning matters more than exact matches
- Traditional testing approaches don't work well

llmtest solves this by using LLMs themselves to evaluate semantic equivalence, providing a natural and effective way to test LLM applications.

Imagine this (well you don't have to imagine, this is the test package actually doing its job):

Asserting on something that passes:

![test_pass.jpg](test_pass.jpg)

Asserting on something that fails:

![test_fail.jpg](test_fail.jpg)

Reliably in the test package of your LLM App. This is what llmtest is for.

## Installation

```
pip install llmtest
```


## Quick Start

1. Create a `.env` file in your project root:

```
OPENAI_API_KEY=your-api-key-here
```

2. Use in your tests:



```
from llmtest.core.semantic_assert import SemanticAssertion

# API key will be loaded from environment

asserter = SemanticAssertion()

# Test semantic equivalence

asserter.assert_semantic_match(actual="The sky is blue", 
                               expected_behavior="A statement about the color of the sky" )
```

## Usage with pytest

```
import pytest 
from llmtest.core.semantic_assert import SemanticAssertion

class TestMyLLMApp: 

    @pytest.fixture 
    def asserter(self): # API key loaded from .env 
        return SemanticAssertion()
        
    def test_my_llm_function(self, asserter):
    result = my_llm_function()
    asserter.assert_semantic_match(
        actual=result,
        expected_behavior="Should provide a coherent answer about Python"
    )

```

## Features

- Semantic equivalence testing
- Integration with pytest
- Proper error handling
- Support for different LLM models (to a point... This still needs work)
- Clear error messages with reasons (ish?)

## Error Handling

The library provides specific exceptions for different scenarios:
- `SemanticAssertionError`: When semantic matching fails
- `LLMConnectionError`: When LLM service fails
- `LLMConfigurationError`: When configuration is invalid

## Configuration

Configuration via environment variables (in `.env`):

```
OPENAI_API_KEY=your-api-key-here 
OPENAI_MODEL=gpt-4o # optional, defaults to gpt-4o 
OPENAI_TEMPERATURE=0.0 # optional, defaults to 0.0
```

Or programmatically (not recommended for API keys):

```
asserter = SemanticAssertion(model="gpt-4", # default 
                             temperature=0.0 # default, recommended for testing 
                             )
```

## Contributing

This is an early-stage project and contributions are welcome! Some areas that need work:
- Additional test cases
- Support for more whatever you can think of, we really need something like this to test our LLM apps so they don't bite us in the bum with some business person calling us at 3am.
- Performance optimisations
- Documentation improvements
- Test result caching

## License

MIT

## Acknowledgments

This project was inspired by the fact that I felt naked deploying LLM apps with no testing.