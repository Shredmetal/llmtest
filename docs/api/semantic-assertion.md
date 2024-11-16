[← Back to Home](../index.md)

# SemanticAssertion

Core class for semantic testing of LLM applications.

## Constructor

```
SemanticAssertion(api_key: Optional[str] = None, 
                  llm: Optional[BaseLanguageModel] = None, 
                  provider: Optional[Union[str, LLMProvider]] = None, 
                  model: Optional[str] = None, 
                  temperature: Optional[float] = None, 
                  max_tokens: Optional[int] = None, 
                  max_retries: Optional[int] = None )
```


### Parameters

All parameters are optional (except for API key) and will use environment variables or defaults if not specified:

- **api_key**: API key for the LLM provider
    - Environment: `OPENAI_API_KEY` or `ANTHROPIC_API_KEY`
    - Default: None (must be provided via environment or parameter)
    - If using default provider: use `OPENAI_API_KEY` since default provider is `openai`

- **llm**: Pre-configured LLM instance (must be of type `langchain_core.language_models import BaseLanguageModel`)
    - Default: None (if provided, bypasses all other configuration)

- **provider**: LLM provider ('openai' or 'anthropic')
    - Environment: `LLM_PROVIDER`
    - Default: 'openai'

- **model**: Model name to use
  - Environment: `LLM_MODEL`
    - Default: 'gpt-4o' for OpenAI, 'claude-3-5-sonnet-latest' for Anthropic

- **temperature**: Temperature setting for LLM responses
  - Environment: `LLM_TEMPERATURE`
    - Default: 0.0
    - Range: 0.0 to 1.0

- **max_tokens**: Maximum tokens for response
  - Environment: `LLM_MAX_TOKENS`
    - Default: 4096

- **max_retries**: Maximum number of API call retries
  - Environment: `LLM_MAX_RETRIES`
    - Default: 2

## Methods

### assert_semantic_match

```
def assert_semantic_match(actual: str, expected_behavior: str ) -> None
```

Asserts that actual output semantically matches expected behavior.

#### Parameters
- **actual**: The actual output to test
- **expected_behavior**: Natural language description of expected behavior

#### Raises
- **SemanticAssertionError**: If outputs don't match semantically
- **LLMConnectionError**: If LLM service fails
- **LLMConfigurationError**: If configuration is invalid
- **TypeError**: If inputs are None

## Examples

### Basic Usage

```
asserter = SemanticAssertion() # Uses environment variables 
asserter.assert_semantic_match(actual="Hello Alice, how are you?", # In practice, use the output from your LLM application
                               expected_behavior="A greeting addressing Alice" 
                               )
```

### Custom Configuration

```
asserter = SemanticAssertion(provider="anthropic", 
                             model="claude-3-5-sonnet-latest", # Look I can't stop you from burning a hole in your wallet but please don't use Claude 3 Opus. 
                             temperature=0.1 )
```

## Navigation

- [Back to Home](../index.md)
- [Installation Guide](../getting-started/installation.md)
- [Quick Start Guide](../getting-started/quickstart.md)
- [Configuration Reference](configuration.md)