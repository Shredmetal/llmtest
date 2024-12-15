[← Back to Home](../index.md)

# Rate Limiter

llm-app-test uses [LangChain's InMemoryRateLimiter](https://api.python.langchain.com/en/latest/core/rate_limiters/langchain_core.rate_limiters.InMemoryRateLimiter.html) to provide rate limiting functionality. This feature helps manage API usage and prevent exceeding rate limits imposed by LLM providers.

## Overview

The rate limiter is based on a token bucket algorithm. It's an in-memory rate limiter that is thread-safe and can be used in both synchronous and asynchronous contexts. However, it cannot rate limit across different processes.

**Note**: The "tokens" used by this rate limiter are not related to LLM tokens. They simply represent the number of requests that can be made in a given time period.

## Configuration

You can configure the rate limiter using environment variables or by passing parameters directly to the BehavioralAssertion constructor.

### Environment Variables

```
USE_RATE_LIMITER=true # Use rate limiter or not, default is false
RATE_LIMITER_REQUESTS_PER_SECOND=4.0 # Sets maximum request per second, default is 1.0
RATE_LIMITER_CHECK_EVERY_N_SECONDS=0.2 # Sets interval to check rate limit (seconds), default is 0.1
RATE_LIMITER_MAX_BUCKET_SIZE=10.0 # Sets maximum bucket size for rate limiting, default is 1.0
```

### Direct Configuration

```python
from llm_app_test.behavioral_assert.behavioral_assert import BehavioralAssertion

asserter = BehavioralAssertion(
    use_rate_limiter=True,
    rate_limiter_requests_per_second=4.0,
    rate_limiter_check_every_n_seconds=0.2,
    rate_limiter_max_bucket_size=10.0
)
```

## Parameters

- use_rate_limiter (bool): Enable or disable the rate limiter.
- rate_limiter_requests_per_second (float): The number of tokens added to the bucket per second. This effectively sets the maximum number of requests allowed per second.
- rate_limiter_check_every_n_seconds (float): How often the rate limiter checks if tokens are available. Can be a fraction of a second.
- rate_limiter_max_bucket_size (float): The maximum number of tokens that can accumulate in the bucket. This controls the maximum burst size.

## How It Works

1. The rate limiter maintains a token bucket that fills at the specified rate (requests_per_second).
2. Each API request consumes one token from the bucket.
3. If there are not enough tokens in the bucket, the request is blocked until enough tokens are available.
4. The max_bucket_size parameter prevents excessive token accumulation, which could lead to large bursts of requests.

## Limitations

- The rate limiter only supports time-based rate limiting. It does not consider the size or complexity of individual requests.
- It cannot rate limit across different processes, as it's an in-memory solution.

## Best Practices

1. Set the requests_per_second slightly below the actual rate limit of your API provider to account for potential variations in request timing.

    - Note on this - Langchain's InMemoryRateLimiter has a Docstring that says this:
   
    ```
    
   
        Args:
            requests_per_second: The number of tokens to add per second to the bucket.
                Must be at least 1. The tokens represent "credit" that can be used
                to make requests.
   
    ```
   
    - However, this is the provided example:
   
    ```python
    import time
      
    from langchain_core.rate_limiters import InMemoryRateLimiter
      
    rate_limiter = InMemoryRateLimiter(
        requests_per_second=0.1,  # <-- Can only make a request once every 10 seconds!!
        check_every_n_seconds=0.1,  # Wake up every 100 ms to check whether allowed to make a request,
        max_bucket_size=10,  # Controls the maximum burst size.
    )
      
    from langchain_anthropic import ChatAnthropic
    model = ChatAnthropic(
        model_name="claude-3-opus-20240229",
        rate_limiter=rate_limiter
    )
      
    for _ in range(5):
        tic = time.time()
        model.invoke("hello")
        toc = time.time()
        print(toc - tic)
    ```
    - We are not entirely sure which is correct so we do not raise exceptions if a value between 0 and 1 is provided, and you do so at your own risk, please complain to Langchain if you run into problems here

2. Adjust check_every_n_seconds based on your application's needs. Smaller values provide more precise timing but may increase CPU usage.
3. Set max_bucket_size to allow for reasonable bursts while preventing excessive request spikes.

## Example Usage with Pytest Fixtures

To effectively use the rate limiter across multiple tests, it's important to use a shared fixture with an appropriate scope. Here's an example of how to set this up:

```python
import pytest
from llm_app_test.behavioral_assert.behavioral_assert import BehavioralAssertion
from llm_app_test.exceptions.test_exceptions import BehavioralAssertionError

class TestRateLimiterScoped:

    @pytest.fixture(scope="class")
    def shared_asserter(self):
        return BehavioralAssertion(use_rate_limiter=True,
                                   rate_limiter_requests_per_second=2,
                                   rate_limiter_check_every_n_seconds=1,
                                   rate_limiter_max_bucket_size=2)

    def test_basic_behavioral_match(self, shared_asserter):
        """Test basic behavioral matching with rate limiting enabled"""
        actual = "The sky is blue"
        expected = "A statement about the color of the sky"
        shared_asserter.assert_behavioral_match(actual, expected)

    def test_behavioral_mismatch(self, shared_asserter):
        """Test behavioral mismatch raises correct exception with rate limiting enabled"""
        actual = "The sky is blue"
        expected = "A statement about the weather forecast"
        with pytest.raises(BehavioralAssertionError) as excinfo:
            shared_asserter.assert_behavioral_match(actual, expected)
        assert "Behavioral assertion failed" in str(excinfo.value)
```

In this example:

1. We create a `shared_asserter` fixture with `scope="class"`. This ensures that the same BehavioralAssertion instance (and thus the same rate limiter) is used for all tests in the class.

2. The `shared_asserter` is configured with rate limiting enabled and specific rate limiting parameters.

3. Each test method uses this shared asserter, ensuring that the rate limiting applies across all tests in the class.

4. However, you should be aware that doing so means there may be some shared state between tests, therefore, we suggest thinking through whether you really need a rate limiter or not.

Note: If you use a fixture with `scope="function"` (the default), a new rate limiter will be created for each test function, which may not provide the desired rate limiting across your entire test suite.

To verify that the same rate limiter is being used across tests, you can add a test like this:

```python
    def test_shared_rate_limiter(self, shared_asserter):
        rate_limiter_id = id(shared_asserter.llm.rate_limiter)
        assert rate_limiter_id is not None
        assert hasattr(self, 'first_rate_limiter_id'), "First test didn't run"
        assert rate_limiter_id == self.first_rate_limiter_id, "Rate limiter instance changed"

    @pytest.fixture(autouse=True)
    def store_first_rate_limiter_id(self, shared_asserter):
        if not hasattr(self, 'first_rate_limiter_id'):
            self.first_rate_limiter_id = id(shared_asserter.llm.rate_limiter)
```

This setup ensures that your tests use a shared rate limiter, allowing you to effectively manage and test rate-limited behavior across multiple test cases.

---

## Navigation

- [Back to Home](../index.md)
- [Configuration](configuration.md)
- [API Reference](behavioral-assertion.md)
