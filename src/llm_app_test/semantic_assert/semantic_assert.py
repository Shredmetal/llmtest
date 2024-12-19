import functools
import sys
import warnings
from typing import Optional, Union, Tuple, Type

from langchain_core.language_models import BaseLanguageModel
from langchain_core.runnables import Runnable

from llm_app_test.behavioral_assert.asserter_prompts.asserter_prompt_configurator import AsserterPromptConfigurator
from llm_app_test.behavioral_assert.behavioral_assert import BehavioralAssertion
from llm_app_test.behavioral_assert.llm_config.llm_provider_enum import LLMProvider


def deprecated(func):
    """This decorator marks functions and classes as deprecated"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        warnings.warn(
            f"{func.__name__} is deprecated. Use behavioral testing methods such as BehavioralAssert.assert_behavioral_match(actual, expected) instead. "
            f"{func.__name__} will be removed in version 1.0.0 or the first update "
            f"after 1 June 2025, whichever comes later",
            category=UserWarning,
            stacklevel=2
        )
        print(
            f"\nWARNING: {func.__name__} is deprecated. Use behavioral testing methods such as BehavioralAssert.assert_behavioral_match(actual, expected) instead. "
            f"{func.__name__} will be removed in version 1.0.0 or the first update "
            f"after 1 June 2025, whichever comes later\n",
            file=sys.stderr)
        return func(*args, **kwargs)

    return wrapper


@deprecated
class SemanticAssertion(BehavioralAssertion):
    """Deprecated: Use BehavioralAssertion instead. This class is maintained for backward compatibility."""

    def __init__(
            self,
            api_key: Optional[str] = None,
            llm: Optional[Runnable] = None,
            provider: Optional[Union[str, LLMProvider]] = None,
            model: Optional[str] = None,
            temperature: Optional[float] = None,
            max_tokens: Optional[int] = None,
            max_retries: Optional[int] = None,
            timeout: Optional[float] = None,
            custom_prompts: Optional[AsserterPromptConfigurator] = None,
            use_rate_limiter: bool = False,
            rate_limiter_requests_per_second: Optional[float] = None,
            rate_limiter_check_every_n_seconds: Optional[float] = None,
            rate_limiter_max_bucket_size: Optional[float] = None,
            langchain_with_retry: Optional[bool] = None,
            retry_if_exception_type: Optional[Tuple[Type[BaseException], ...]] = None,
            wait_exponential_jitter: Optional[bool] = None,
            stop_after_attempt: Optional[int] = None
    ):
        """
            Initializes an object with configuration parameters for interacting with
            a language model or API. The attributes define the API credentials, model
            specifications, retry logic, request settings, rate-limiter configurations,
            and other optional functionalities.

            Arguments:
            ----------
            api_key : Optional[str]
                The API key for authenticating with the language model provider.
                If not provided, tries to obtain it from environment variables.

            llm : Optional[BaseLanguageModel]
                Pre-configured language model instance. If provided, bypasses
                the configuration process and sets this instance as the
                language model.

            provider : Optional[Union[str, LLMProvider]]
                The language model provider. Accepts either a string or an
                instance of the LLMProvider enumeration. Defaults to a
                provider from environment variables if not provided.

            model : Optional[str]
                The specific language model to use. If not specified, a
                default model for the selected provider is used.

            temperature : Optional[float]
                Controls the randomness of the outputs from the language model.
                Loaded from environment variables or defaults if not provided.

            max_tokens : Optional[int]
                The maximum number of tokens generated per response. Defaults
                to environment values or predefined constants.

            max_retries : Optional[int]
                Number of retry attempts for failed API requests. Loaded from
                defaults or environment variables.

            timeout : Optional[float]
                Timeout in seconds for API requests. Fetched from environment
                variables or defaults.

            custom_prompts : Optional[AsserterPromptConfigurator]
                Configurator for customizing prompts to the language model.

            use_rate_limiter : bool
                Whether to enable a rate-limiting mechanism for API requests.
                Defaults to False.

            rate_limiter_requests_per_second : Optional[float]
                The maximum number of allowable API requests per second,
                applicable if rate limiting is enabled.

            rate_limiter_check_every_n_seconds : Optional[float]
                Interval in seconds between checking for rate-limiting
                compliance, when enabled.

            rate_limiter_max_bucket_size : Optional[float]
                The maximum bucket size for rate limiting. Determines the
                number of requests that can be queued momentarily.

            langchain_with_retry: Optional[bool] = None
                Whether to use the Langchain Runnable object with_retry method.

            retry_if_exception_type: Optional[Tuple[Type[BaseException], ...]]
                Exception types to retry on. If not provided, retries on all

            wait_exponential_jitter: Optional[bool]
                Whether to use exponential backoff with jitter. If not provided,
                defaults to True

            stop_after_attempt: Optional[int]
                Number of attempts after which to stop retrying. If not provided,
                defaults to 3

            Raises:
                None
        """

        super().__init__(
            api_key,
            llm,
            provider,
            model,
            temperature,
            max_tokens,
            max_retries,
            timeout,
            custom_prompts,
            use_rate_limiter,
            rate_limiter_requests_per_second,
            rate_limiter_check_every_n_seconds,
            rate_limiter_max_bucket_size,
            langchain_with_retry,
            retry_if_exception_type,
            wait_exponential_jitter,
            stop_after_attempt
        )

    @deprecated
    def assert_semantic_match(
            self,
            actual: str,
            expected_behavior: str
    ) -> None:
        """
            Assert that actual output semantically matches expected behavior

            Args:
                actual: The actual output to test
                expected_behavior: The expected behavior description

            Raises:
                TypeError: If inputs are None
                SemanticAssertionError: If outputs don't match semantically
                LLMConnectionError: If LLM service fails
                LLMConfigurationError: If LLM is not properly configured
            """
        return self.assert_behavioral_match(actual, expected_behavior)
