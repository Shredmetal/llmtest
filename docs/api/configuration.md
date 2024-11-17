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
from llm_app_test.semanticassert.semantic_assert import SemanticAssertion

asserter = SemanticAssertion(api_key="your-api-key", # Strongly advised against, use env vars 
                             provider="openai", # or 'anthropic' 
                             model="gpt-4o", # See Supported Models 
                             temperature=0.0, # Default: 0.0 
                             max_tokens=4096, # Default: 4096 
                             max_retries=2 # Default: 2 
                             )
```


## Supported Models

Model supported is restricted due to poorer semantic matching performance of less advanced models.

### OpenAI
- gpt-4o
- gpt-4-turbo

### Anthropic
- claude-3-5-sonnet-latest
- claude-3-opus-latest (EXPENSIVE!!!)

## Configuration Priority

Configuration values are resolved in this order:

1. Directly passed parameters
2. Environment variables
3. Default values

## Best Practices

1. Use environment variables for API keys
2. Keep temperature at 0.0 for consistent testing
3. Use default max_tokens unless you have specific needs
4. Start with default max_retries (2)

---

Note: llm_app_test validates all configuration values at startup to prevent runtime errors.

## Navigation

- [Back to Home](../index.md)
- [Installation Guide](../getting-started/installation.md)
- [Quick Start Guide](../getting-started/quickstart.md)
- [API Reference](semantic-assertion.md)
