[← Back to Home](../index.md)

# Configuration

llm-app-test provides flexible configuration through environment variables and direct parameters.

## Environment Variables

### Provider Selection

```
LLM_PROVIDER=openai # or 'anthropic', default is openai
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
LLM_TEMPERATURE=0.0 # Response randomness (0.0-1.0), default is 0.0
LLM_MAX_TOKENS=4096 # Maximum response length, default is 4096
LLM_MAX_RETRIES=2 # API retry attempts, default is 2
LLM_TIMEOUT=60.0 # API timeout in seconds, default is 60.0
USE_RATE_LIMITER=true # Use rate limiter or not, default is false
RATE_LIMITER_REQUESTS_PER_SECOND=4.0 # Sets maximum request per second, default is 1.0
RATE_LIMITER_CHECK_EVERY_N_SECONDS=0.2 # Sets interval to check rate limit (seconds), default is 0.1
RATE_LIMITER_MAX_BUCKET_SIZE=10.0 # Sets maximum bucket size for rate limiting, default is 1.0
LANGCHAIN_WITH_RETRY=true # Sets whether to use Langchain's with_retry method for Runnable objects, default is false
ASSERTER_WAIT_EXPONENTIAL_JITTER=true # Set whether to use exponential backoff with jitter for the with_retry method, default is true
ASSERTER_STOP_AFTER_ATTEMPT=3 # Set how many times to retry before stopping for the with_retry method, default is 3
```
For rate limiting, please refer to the specific documentation on the [rate limiter](./rate-limiter.md)

## Direct Configuration

You can also configure llm_app_test programmatically:

```python
from llm_app_test.behavioral_assert.behavioral_assert import BehavioralAssertion

asserter = BehavioralAssertion(
    api_key="your-api-key", # Strongly advised against, use env vars
    provider="openai", # or 'anthropic'
    model="gpt-4o", # See Supported Models
    temperature=0.0, # Default: 0.0
    max_tokens=4096, # Default: 4096
    max_retries=2, # Default: 2
    timeout=60.0, # Default: 60.0
    use_rate_limiter=False, # Enable/disable rate limiting
    rate_limiter_requests_per_second=1.0, # Requests per second for rate limiting
    rate_limiter_check_every_n_seconds=0.1, # Interval to check rate limit
    rate_limiter_max_bucket_size=1.0, # Maximum bucket size for rate limiting
    langchain_with_retry=True,
    retry_if_exception_type=(Exception,),
    wait_exponential_jitter=False,
    stop_after_attempt=5
)
```
An optional parameter for BehavioralAssertion is `custom_prompts`, see [this page](custom-prompt-configuration.md) for details.

You will note that `retry_if_exception_type` can only be configured from the `BehavioralAssertion` constructor. Please refer to the [BehavioralAssertion](./behavioral-assertion.md) page for the rationale.

You may also be wondering why we added support for this: Simply put, we found the `max_retries` does not seem to do what we thought it did, especially with ChatAnthropic which was giving us 529 errors when we threw lots of API calls at it in a short span of time.

## Supported (and recommended) Models

Model support is restricted due to the complex behavioral reasoning required for accurate testing. We've found that only the most advanced models can reliably handle behavioral comparison tasks.

### OpenAI
- gpt-4o
- gpt-4-turbo

### Anthropic
- claude-3-5-sonnet-latest
- claude-3-opus-latest (EXPENSIVE!!!)

**Note**: GPT-4o is our recommended model because it was what we used to validate reliability, and has demonstrated a level of pedantry and literalism that we find is best for a testing system.

## Custom LLM Configuration (Advanced Users Only)

While it's possible to inject a custom LLM using Langchain's `Runnable`, this is strongly discouraged unless you have extensively tested your model's behavioral reasoning capabilities. Smaller or less capable models will likely fail at the behavioral testing tasks. If you happen to have a datacenter in your back pocket however, Llama 3.1:405B might be a good bet.

```python
# Advanced usage - Only for thoroughly tested models
from llm_app_test.behavioral_assert.behavioral_assert import BehavioralAssertion
from langchain_core.runnables import Runnable

custom_llm: Runnable = your_custom_llm
asserter = BehavioralAssertion(llm=custom_llm)
```

If you pass in a custom llm, it will disable **ALL** other LLM configuration options, and you have to configure that LLM yourself.

## Configuration Priority

Configuration values are resolved in this order:

1. Custom LLM (if provided, disables **ALL** other LLM settings and uses the settings of the Langchain Runnable object that you have passed)
2. Directly passed parameters
3. Environment variables
4. Default values

Note: if a custom LLM is not passed, llm-app-test validates all configuration values at startup to prevent runtime errors.

## Best Practices

1. Use environment variables for API keys
2. Keep temperature at 0.0 for consistent testing
3. Use default max_tokens unless you have specific needs
4. Start with default max_retries (2)
5. Stick with foundation models for the best results. This library is completely untested with anything other than foundation models.

---

## Navigation

- [Back to Home](../index.md)
- [Installation Guide](../getting-started/installation.md)
- [Quick Start Guide](../getting-started/quickstart.md)
- [API Reference](behavioral-assertion.md)
