import os
from typing import Optional, Union
from dotenv import load_dotenv
from langchain_core.language_models import BaseLanguageModel
from langchain.schema import HumanMessage, SystemMessage

from llm_app_test.semantic_assert.asserter_prompts.asserter_prompt_injector import AsserterPromptInjector
from llm_app_test.semantic_assert.llm_config.llm_config import LLMConfig
from llm_app_test.semantic_assert.llm_config.llm_factory import LLMFactory
from llm_app_test.semantic_assert.llm_config.llm_provider_enum import LLMProvider
from llm_app_test.exceptions.test_exceptions import (
    SemanticAssertionError,
    catch_llm_errors,
)
from llm_app_test.semantic_assert.semantic_assert_config.semantic_assert_constants import ModelConstants, LLMConstants
from llm_app_test.semantic_assert.validation.config_validator import ConfigValidator
from llm_app_test.semantic_assert.validation.validator_config import ValidationConfig


class SemanticAssertion:
    """Core class for semantic testing using LLMs"""

    def __init__(
            self,
            api_key: Optional[str] = None,
            llm: Optional[BaseLanguageModel] = None,
            provider: Optional[Union[str, LLMProvider]] = None,
            model: Optional[str] = None,
            temperature: Optional[float] = None,
            max_tokens: Optional[int] = None,
            max_retries: Optional[int] = None,
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

        validation_config = ValidationConfig(
            api_key=api_key,
            provider=provider_value,
            model=model,
            valid_models=valid_models,
            temperature=temperature,
            max_tokens=max_tokens
        )

        provider = ConfigValidator.validate(validation_config)

        config = LLMConfig(
            provider=provider,
            api_key=api_key,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            max_retries=max_retries
        )

        self.llm = LLMFactory.create_llm(config)

    @catch_llm_errors
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
            raise SemanticAssertionError(
                "Semantic assertion failed",
                reason=result.split("FAIL: ")[1]
            )

# I guess use it like this?
# # Normal usage (default prompts)
# asserter = SemanticAssertion(provider="openai")
#
# # Advanced usage with custom prompts
# custom_prompts = AsserterPromptInjector(
#     system_prompt="You are a testing system that only responds with PASS or FAIL: reason...",
#     human_prompt="Compare:\nExpected: {expected_behavior}\nActual: {actual}"
# )
# asserter = SemanticAssertion(
#     provider="openai",
#     prompt_injector=custom_prompts
# )
#
# # The assertion itself works the same way
# asserter.assert_semantic_match(
#     actual="Hello, world!",
#     expected_behavior="Should greet the world"
# )