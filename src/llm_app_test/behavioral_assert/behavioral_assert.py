import os
from typing import Optional, Union
from dotenv import load_dotenv
from langchain_core.language_models import BaseLanguageModel
from langchain.schema import HumanMessage, SystemMessage

from llm_app_test.behavioral_assert.asserter_prompts.asserter_prompt_injector import AsserterPromptInjector
from llm_app_test.behavioral_assert.llm_config.llm_config import LLMConfig
from llm_app_test.behavioral_assert.llm_config.llm_factory import LLMFactory
from llm_app_test.behavioral_assert.llm_config.llm_provider_enum import LLMProvider
from llm_app_test.exceptions.test_exceptions import (
    catch_llm_errors,
    BehavioralAssertionError
)
from llm_app_test.behavioral_assert.behavioral_assert_config.behavioral_assert_constants import ModelConstants, LLMConstants
from llm_app_test.behavioral_assert.validation.config_validator import ConfigValidator
from llm_app_test.behavioral_assert.validation.validator_config import ValidationConfig


class BehavioralAssertion:
    """Core class for behavioral testing of LLM applications.

    This class provides functionality to test LLM application behavior using natural
    language specifications. It supports both direct configuration and environment
    variables for LLM setup.
    """

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

        """Initialize the behavioral assertion tester.

        This class supports both direct configuration through parameters and environment
        variables. Environment variables take precedence in the following order:
        1. Explicitly passed parameters
        2. Environment variables
        3. Default values

        Supported environment variables:
            - OPENAI_API_KEY: API key for OpenAI
            - ANTHROPIC_API_KEY: API key for Anthropic
            - LLM_PROVIDER: The LLM provider to use ('openai' or 'anthropic')
            - LLM_MODEL: Model name to use
            - LLM_TEMPERATURE: Temperature setting (0.0 to 1.0)
            - LLM_MAX_TOKENS: Maximum tokens for response
            - LLM_MAX_RETRIES: Maximum number of retries for API calls
            - LLM_TIMEOUT: Timeout for API calls in seconds

        Args:
            api_key: API key for the LLM provider (overrides environment variable)
            llm: Optional pre-configured LLM (bypasses all other configuration)
            provider: LLM provider (openai or anthropic)
            model: Model name to use
            temperature: Temperature setting (0.0 to 1.0)
            max_tokens: Maximum tokens for response
            max_retries: Maximum number of retries for API calls
            timeout: Timeout for API calls in seconds
            prompt_injector: Custom prompt injector for testing (intentional added friction)

        Raises:
            LLMConfigurationError: If configuration is invalid or required values are missing
        """

        load_dotenv()

        self.prompt_injector = prompt_injector or AsserterPromptInjector()

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

        validation_config = ValidationConfig(
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

        self.llm = LLMFactory.create_llm(config)

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
        if actual is None or expected_behavior is None:
            raise TypeError("Inputs cannot be None")

        prompts = self.prompt_injector.prompts

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
