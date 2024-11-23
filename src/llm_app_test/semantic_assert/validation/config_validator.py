from typing import Optional, Set
from llm_app_test.exceptions.test_exceptions import LLMConfigurationError
from llm_app_test.semantic_assert.llm_config.llm_provider_enum import LLMProvider
from llm_app_test.semantic_assert.validation.validator_config import ValidationConfig


class ConfigValidator:
    """Validator for LLM configuration parameters"""

    @staticmethod
    def validate(config: ValidationConfig) -> LLMProvider:
        """
        Validate all configuration parameters

        Args:
            config: ValidationConfig containing all parameters to validate

        Returns:
            Validated LLMProvider

        Raises:
            LLMConfigurationError: If any validation fails
        """
        ConfigValidator._validate_api_key(config.api_key)
        provider = ConfigValidator._validate_provider(config.provider)
        ConfigValidator._validate_model(config.model, config.valid_models)
        ConfigValidator._validate_temperature(config.temperature)
        ConfigValidator._validate_max_tokens(config.max_tokens)
        ConfigValidator._validate_timeout(config.timeout)
        return provider

    @staticmethod
    def _validate_api_key(api_key: Optional[str]) -> None:
        if not api_key:
            raise LLMConfigurationError(
                "API key must be provided",
                reason="API key must be provided"
            )

    @staticmethod
    def _validate_model(model: str, valid_models: Set[str]) -> None:
        if model not in valid_models:
            raise LLMConfigurationError(
                f"Invalid model: {model}",
                reason=f"Invalid model - supported models for provider: {list(valid_models)}"
            )

    @staticmethod
    def _validate_temperature(temperature: Optional[float]) -> None:
        if temperature is not None and not (0 <= temperature <= 1):
            raise LLMConfigurationError(
                f"Invalid temperature value: {temperature}",
                reason="Temperature must be between 0 and 1"
            )

    @staticmethod
    def _validate_max_tokens(max_tokens: Optional[int]) -> None:
        if max_tokens is not None and max_tokens <= 0:
            raise LLMConfigurationError(
                f"Invalid max_tokens value: {max_tokens}",
                reason="max_tokens must be positive"
            )

    @staticmethod
    def _validate_timeout(timeout: float) -> None:
        if timeout is not None and timeout <= 0:
            raise LLMConfigurationError(
                f"Invalid timeout value: {timeout}",
                reason="timeout must be positive"
            )

    @staticmethod
    def _validate_provider(provider: str) -> LLMProvider:
        try:
            return LLMProvider(provider.lower())
        except ValueError:
            raise LLMConfigurationError(
                f"Invalid provider: {provider}",
                reason="Invalid provider"
            )