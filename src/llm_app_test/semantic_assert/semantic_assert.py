import functools
import sys
import warnings
from typing import Optional, Union

from langchain_core.language_models import BaseLanguageModel

from llm_app_test.behavioral_assert.asserter_prompts.asserter_prompt_injector import AsserterPromptInjector
from llm_app_test.behavioral_assert.behavioral_assert import BehavioralAssertion
from llm_app_test.behavioral_assert.llm_config.llm_provider_enum import LLMProvider


def deprecated(func):
    """This decorator marks functions and classes as deprecated"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        warnings.warn(
            f"{func.__name__} is deprecated. Use behavioral testing methods instead. "
            f"{func.__name__} will be removed in version 1.0.0 or the first update "
            f"after 1 June 2025, whichever comes later",
            category=UserWarning,
            stacklevel=2
        )
        print(f"\nWARNING: {func.__name__} is deprecated. Use behavioral testing methods instead. "
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
            prompt_injector: Optional[AsserterPromptInjector] = None
    ):
        """
           Initialise the semantic assertion tester.

           This class supports both direct configuration through parameters and environment variables.
           Environment variables take precedence in the following order:
           1. Explicitly passed parameters
           2. Environment variables
           3. Default values

           Supported environment variables:
               - OPENAI_API_KEY / ANTHROPIC_API_KEY: API keys for respective providers
               - LLM_PROVIDER: The LLM provider to use ('openai' or 'anthropic')
               - LLM_MODEL: Model name to use
               - LLM_TEMPERATURE: Temperature setting (0.0 to 1.0)
               - LLM_MAX_TOKENS: Maximum tokens for response
               - LLM_MAX_RETRIES: Maximum number of retries for API calls

           Args:
               api_key: API key for the LLM provider (overrides environment variable)
               llm: Optional pre-configured LLM (bypasses all other configuration)
               provider: LLM provider (openai or anthropic)
               model: Model name to use
               temperature: Temperature setting (0.0 to 1.0)
               max_tokens: Maximum tokens for response
               max_retries: Maximum number of retries for API calls

           Raises:
               LLMConfigurationError: If configuration is invalid or required values are missing
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
                prompt_injector,
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