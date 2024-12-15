[← Back to Home](../index.md)

# BehavioralAssertion

Core class for behavioral testing of LLM applications.

## Constructor

```python

BehavioralAssertion(api_key: Optional[str] = None, 
                    llm: Optional[BaseLanguageModel] = None, 
                    provider: Optional[Union[str, LLMProvider]] = None, 
                    model: Optional[str] = None, 
                    temperature: Optional[float] = None, 
                    max_tokens: Optional[int] = None, 
                    max_retries: Optional[int] = None,
                    timeout: Optional[float] = None,
                    custom_prompts: Optional[AsserterPromptConfigurator] = None),
                    use_rate_limiter=False,
                    rate_limiter_requests_per_second=1.0, 
                    rate_limiter_check_every_n_seconds=0.1, 
                    rate_limiter_max_bucket_size=1.0 
```


### Parameters

All parameters are optional (except for API key) and will use environment variables or defaults if not specified:

- **api_key**: API key for the LLM provider

    - Environment: OPENAI_API_KEY or ANTHROPIC_API_KEY
    - Default: None (must be provided via environment or parameter unless using custom LLM, see `llm` parameter)
    - If using default provider: use OPENAI_API_KEY since default provider is openai

- **llm**: Pre-configured LLM instance (must be of type `langchain_core.language_models import BaseLanguageModel`)
    
    - Default: None (if provided, bypasses all other configuration)

- **provider**: LLM provider ('openai' or 'anthropic')

    - Environment: LLM_PROVIDER
    - Default: 'openai'

- **model**: Model name to use

    - Environment: LLM_MODEL
        - Default: 'gpt-4o' for OpenAI, 'claude-3-5-sonnet-latest' for Anthropic

- **temperature**: Temperature setting for LLM responses

    - Environment: LLM_TEMPERATURE
  
        - Default: 0.0
        - Range: 0.0 to 1.0

- **max_tokens**: Maximum tokens for response

    - Environment: LLM_MAX_TOKENS
        - Default: 4096

- **max_retries**: Maximum number of API call retries

    - Environment: LLM_MAX_RETRIES
        - Default: 2

- **timeout**: Timeout for API calls in seconds

    - Environment: LLM_TIMEOUT
        - Default: 60.0

- **custom_prompts**: Custom prompts for asserter

    - Default: None (uses default AsserterPromptConfigurator)
    - Intentional added friction for custom prompts
    - Please refer to [this documentation](custom-prompt-configuration.md) on how to use it.

- **use_rate_limiter**: Enable or disable rate limiting

    - Environment: USE_RATE_LIMITER
    - Default: False

- **rate_limiter_requests_per_second**: Maximum requests per second for rate limiting

    - Environment: RATE_LIMITER_REQUESTS_PER_SECOND
    - Default: 1.0

- **rate_limiter_check_every_n_seconds**: Interval to check rate limit (in seconds)

    - Environment: RATE_LIMITER_CHECK_EVERY_N_SECONDS
    - Default: 0.1

- **rate_limiter_max_bucket_size**: Maximum bucket size for rate limiting

    - Environment: RATE_LIMITER_MAX_BUCKET_SIZE
    - Default: 1.0

## Methods

### assert_behavioral_match

```python
def assert_behavioral_match(actual: str, expected_behavior: str ) -> None
```

Asserts that actual output exhibits the expected behavior.

#### Parameters

- **actual**: The actual output to test
- **expected_behavior**: Natural language description of expected behavior

#### Raises

- **BehavioralAssertionError**: If output doesn't exhibit expected behavior
- **LLMConnectionError**: If LLM service fails
- **LLMConfigurationError**: If configuration is invalid
- **TypeError**: If inputs are None

## Examples

### Basic Usage

```python
asserter = BehavioralAssertion() # Uses environment variables 
asserter.assert_behavioral_match(
    actual="Hello Alice, how are you?", # In practice, use the output from your LLM application
    expected_behavior="A greeting addressing Alice" 
)
```

### Custom Configuration

```python
asserter = BehavioralAssertion(
    provider="anthropic", 
    model="claude-3-5-sonnet-latest", # Look I can't stop you from burning a hole in your wallet but please don't use Claude 3 Opus. 
    temperature=0.1,
    timeout=15.0
)
```

## Navigation

- [Back to Home](../index.md)
- [Installation Guide](../getting-started/installation.md)
- [Quick Start Guide](../getting-started/quickstart.md)
- [Configuration Reference](configuration.md)