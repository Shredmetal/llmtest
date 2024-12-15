import functools
import sys
import warnings
from typing import Optional, Union

from langchain_core.language_models import BaseLanguageModel

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
            llm: Optional[BaseLanguageModel] = None,
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
            rate_limiter_max_bucket_size: Optional[float] = None
    ):
        """
            Initializes an object with configuration parameters for interacting with
            a language model or API. The attributes define the API credentials, model
            specifications, retry logic, request settings, rate-limiter configurations,
            and other optional functionalities.

            Parameters:
                api_key (Optional[str]): The API key for authenticating with the
                    language model or API.
                llm (Optional[BaseLanguageModel]): The base language model to be used,
                    if specified.
                provider (Optional[Union[str, LLMProvider]]): The provider or identifier
                    of the language model service.
                model (Optional[str]): Specifies the model name to be used with the
                    provider.
                temperature (Optional[float]): A float value to control randomness in
                    responses from the model. Higher values introduce more variation.
                max_tokens (Optional[int]): Defines the maximum token limit in the
                    model's response.
                max_retries (Optional[int]): The permissible number of retries for
                    failed API calls.
                timeout (Optional[float]): The timeout value, in seconds, for API
                    responses.
                custom_prompts (Optional[AsserterPromptConfigurator]): Custom
                    configurator for prompts to tailor model interactions.
                use_rate_limiter (bool): Specifies whether to enforce rate-limiting
                    policies.
                rate_limiter_requests_per_second (Optional[float]): Requests per second
                    allowed by the rate-limiter.
                rate_limiter_check_every_n_seconds (Optional[float]): Frequency, in
                    seconds, at which the rate-limiter checks the request count.
                rate_limiter_max_bucket_size (Optional[float]): Maximum number of
                    requests allowed to accumulate in the rate-limiter's bucket.

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
            rate_limiter_max_bucket_size
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
