[← Back to Home](../index.md)

# Configuration

llm_app_test provides flexible configuration through environment variables and direct parameters.

## Environment Variables

### Provider Selection

```
LLM_PROVIDER=openai # or 'anthropic'
```

### API Keys

```
# For OpenAI (default provider)

OPENAI_API_KEY=your-openai-key

# For Anthropic

ANTHROPIC_API_KEY=your-anthropic-key
```

### Optional Settings

```
LLM_MODEL=gpt-4o # Model name - default for OpenAI: gpt-4o, default for anthropic: claude-3-5-sonnet-latest
LLM_TEMPERATURE=0.0 # Response randomness (0.0-1.0) 
LLM_MAX_TOKENS=4096 # Maximum response length 
LLM_MAX_RETRIES=2 # API retry attempts
```


## Direct Configuration

You can also configure llm_app_test programmatically:

```
from llm_app_test.semantic_assert.semantic_assert import SemanticAssertion

asserter = SemanticAssertion(api_key="your-api-key", # Strongly advised against, use env vars 
                             provider="openai", # or 'anthropic' 
                             model="gpt-4o", # See Supported Models 
                             temperature=0.0, # Default: 0.0 
                             max_tokens=4096, # Default: 4096 
                             max_retries=2 # Default: 2 
                             )
```


## Supported (and recommended) Models

Model support is restricted due to the complex semantic reasoning required for accurate testing. We've found that only the most advanced models can reliably handle semantic comparison tasks.

### OpenAI
- gpt-4o
- gpt-4-turbo

### Anthropic
- claude-3-5-sonnet-latest
- claude-3-opus-latest (EXPENSIVE!!!)

## Custom LLM Configuration (Advanced Users Only)

While it's possible to inject a custom LLM using Langchain's `BaseLanguageModel`, this is strongly discouraged unless you have extensively tested your model's semantic reasoning capabilities. Smaller or less capable models will likely fail at the semantic testing tasks. If you happen to have a datacenter in your back pocket however, Llama 3.1:405B might be a good bet.

```
# Advanced usage - Only for thoroughly tested models
from llm_app_test.semantic_assert.semantic_assert import SemanticAssertion
from langchain_core.language_models import BaseLanguageModel

custom_llm: BaseLanguageModel = your_custom_llm
asserter = SemanticAssertion(llm=custom_llm)
```

If you pass in a custom llm, it will disable **ALL** other LLM configuration options, and you have to configure that LLM yourself.

## Configuration Priority

Configuration values are resolved in this order:

1. Custom LLM (if provided, disables **ALL** other LLM settings and uses the settings of the Langchain `BaseLanguageModel` object that you have passed)
2. Directly passed parameters
3. Environment variables
4. Default values

Note: if a custom LLM is not passed, llm_app_test validates all configuration values at startup to prevent runtime errors.

## Best Practices

1. Use environment variables for API keys
2. Keep temperature at 0.0 for consistent testing
3. Use default max_tokens unless you have specific needs
4. Start with default max_retries (2)
5. Stick with frontier models for the best results. This library is completely untested with anything other than frontier models.

---

## Navigation

- [Back to Home](../index.md)
- [Installation Guide](../getting-started/installation.md)
- [Quick Start Guide](../getting-started/quickstart.md)
- [API Reference](semantic-assertion.md)
