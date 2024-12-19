import os
from typing import Optional, Union, Tuple, Type
from dotenv import load_dotenv
from langchain.schema import HumanMessage, SystemMessage
from langchain_core.runnables import Runnable

from llm_app_test.behavioral_assert.asserter_prompts.asserter_prompt_configurator import AsserterPromptConfigurator
from llm_app_test.behavioral_assert.llm_config.llm_config import LLMConfig
from llm_app_test.behavioral_assert.llm_config.llm_factory import LLMFactory
from llm_app_test.behavioral_assert.llm_config.llm_provider_enum import LLMProvider
from llm_app_test.behavioral_assert.validation.behavioral_assert_input_validator import AssertBehavioralMatchValidator
from llm_app_test.behavioral_assert.validation.with_retry_config_validator import WithRetryConfigValidator
from llm_app_test.exceptions.test_exceptions import (
    catch_llm_errors,
    BehavioralAssertionError
)
from llm_app_test.behavioral_assert.behavioral_assert_config.behavioral_assert_constants import ModelConstants, \
    LLMConstants
from llm_app_test.behavioral_assert.validation.config_validator import ConfigValidator
from llm_app_test.behavioral_assert.validation.config_validator_config import ConfigValidatorConfig

from llm_app_test.rate_limiter.rate_limiter_handler import LLMInMemoryRateLimiter
from llm_app_test.with_retry.with_retry_config import WithRetryConfig


class BehavioralAssertion:
    """Core class for behavioral testing of LLM applications.

    This class provides functionality to test LLM application behavior using natural
    language specifications. It supports both direct configuration and environment
    variables for LLM setup.
    """

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
            langchain_with_retry: Optional[bool] = False,
            retry_if_exception_type: Optional[Tuple[Type[BaseException], ...]] = None,
            wait_exponential_jitter: Optional[bool] = None,
            stop_after_attempt: Optional[int] = None
    ):

        """
            Initializes an instance of a class responsible for configuring and managing
            language model integrations, including attributes for API keys, models,
            temperature, and rate limiting. It supports different language model
            providers, validates the configuration, and creates an instance of the
            language model based on the specified or default parameters.

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

            Returns:
            --------
            None

            Raises:
            -------
            ValidationError
                Raised if the provided configuration is invalid.

            EnvironmentError
                Raised if required environment variables are missing and no
                corresponding values are provided.

            KeyError
                Raised if necessary keys for provider configuration are not
                found in the environment dictionary.

            Dependencies:
            -------------
            - os: Used for retrieving environment variables.
            - load_dotenv: Loads environment variable definitions from a .env
              file.
            - ConfigValidator and ConfigValidatorConfig: Validate the provided
              configuration values.
            - LLMFactory and LLMConfig: Used to create language model instances.
            - LLMInMemoryRateLimiter: Implements rate-limiting functionality.

            Notes:
            ------
            - This class initializes a pre-configured LLM instance if a custom
              LLM is passed as `llm`.
            - If a provider is not explicitly specified, `openai` is used as
              the default.
            - Defaults for temperature, tokens, retries, and timeout values
              are fetched using constants or environment variables if not
              explicitly provided.
            - Environment variables support dynamic reconfiguration without
              hardcoding values.
        """

        load_dotenv()

        self.custom_prompts = custom_prompts or AsserterPromptConfigurator()

        if llm:
            self.llm = llm
            return

        provider_value = provider.value if isinstance(provider, LLMProvider) else (
                provider or os.getenv('LLM_PROVIDER', 'openai'))

        if provider_value.lower() == LLMProvider.OPENAI.value:
            api_key = api_key or os.getenv('OPENAI_API_KEY')
            default_model = ModelConstants.DEFAULT_OPENAI_MODEL
            valid_models = ModelConstants.OPENAI_MODELS
        else:
            api_key = api_key or os.getenv('ANTHROPIC_API_KEY')
            default_model = ModelConstants.DEFAULT_ANTHROPIC_MODEL
            valid_models = ModelConstants.ANTHROPIC_MODELS

        model = model or os.getenv('LLM_MODEL', default_model)
        temperature = temperature if temperature is not None else float(
            os.getenv('LLM_TEMPERATURE', str(LLMConstants.DEFAULT_TEMPERATURE)))
        max_tokens = max_tokens if max_tokens is not None else int(
            os.getenv('LLM_MAX_TOKENS', str(LLMConstants.DEFAULT_MAX_TOKENS)))
        max_retries = max_retries if max_retries is not None else int(
            os.getenv('LLM_MAX_RETRIES', str(LLMConstants.DEFAULT_MAX_RETRIES)))
        timeout = timeout if timeout is not None else float(
            os.getenv('LLM_TIMEOUT', str(LLMConstants.DEFAULT_TIMEOUT)))

        validation_config = ConfigValidatorConfig(
            api_key=api_key,
            provider=provider_value,
            model=model,
            valid_models=valid_models,
            temperature=temperature,
            max_tokens=max_tokens,
            timeout=timeout
        )

        provider = ConfigValidator.validate(validation_config)

        config = LLMConfig(
            provider=provider,
            api_key=api_key,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            max_retries=max_retries,
            timeout=timeout
        )

        use_rate_limiter = use_rate_limiter or os.getenv('USE_RATE_LIMITER', 'False').lower() == 'true'

        if use_rate_limiter:
            llm_in_memory_rate_limiter = LLMInMemoryRateLimiter(
                requests_per_second=rate_limiter_requests_per_second,
                check_every_n_seconds=rate_limiter_check_every_n_seconds,
                max_bucket_size=rate_limiter_max_bucket_size
            ).get_rate_limiter
        else:
            llm_in_memory_rate_limiter = None

        self.llm = LLMFactory.create_llm(config, llm_in_memory_rate_limiter)

        if langchain_with_retry:

            # TODO: Figure out how to resolve configs for this in line with the config resolution hierarchy

            retry_config = WithRetryConfigValidator.validate(
                WithRetryConfig(
                    retry_if_exception_type=retry_if_exception_type,
                    wait_exponential_jitter=wait_exponential_jitter,
                    stop_after_attempt=stop_after_attempt
                )
            )

            self.llm = self.llm.with_retry(
                retry_if_exception_type=retry_config.retry_if_exception_type,
                wait_exponential_jitter=retry_config.wait_exponential_jitter,
                stop_after_attempt=retry_config.stop_after_attempt
            )

    @catch_llm_errors
    def assert_behavioral_match(
            self,
            actual: str,
            expected_behavior: str
    ) -> None:
        """Assert that actual output matches expected behavior.

        Validates that the actual output exhibits the expected behavior using
        natural language specification.

        Args:
            actual: The actual output to test
            expected_behavior: Natural language specification of expected behavior

        Raises:
            TypeError: If inputs are None
            BehavioralAssertionError: If output doesn't match expected behavior
            LLMConnectionError: If LLM service fails
            LLMConfigurationError: If LLM is not properly configured
        """
        AssertBehavioralMatchValidator.validate(actual, expected_behavior)

        prompts = self.custom_prompts.prompts

        messages = [
            SystemMessage(content=prompts.system_prompt),
            HumanMessage(content=prompts.human_prompt.format(
                expected_behavior=expected_behavior,
                actual=actual
            ))
        ]

        result = self.llm.invoke(messages).content

        if result.startswith("FAIL"):
            raise BehavioralAssertionError(
                "Behavioral Assertion Failed: ",
                reason=result.split("FAIL: ")[1]
            )
