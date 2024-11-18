import pytest
from llm_app_test.exceptions.test_exceptions import LLMConfigurationError
from llm_app_test.semantic_assert.llm_config.llm_provider_enum import LLMProvider
from llm_app_test.semantic_assert.validation.config_validator import ConfigValidator
from llm_app_test.semantic_assert.validation.validator_config import ValidationConfig


class TestConfigValidator:
    """Test suite for ConfigValidator class"""

    @pytest.fixture
    def valid_config(self):
        """Fixture for valid configuration"""
        return ValidationConfig(
            api_key="test-key",
            provider="openai",
            model="gpt-4o",
            valid_models={"gpt-4o"},
            temperature=0.7,
            max_tokens=100
        )

    def test_valid_configuration(self, valid_config):
        """Test that valid configuration passes validation"""
        provider = ConfigValidator.validate(valid_config)
        assert provider == LLMProvider.OPENAI

    def test_missing_api_key(self, valid_config):
        """Test validation with missing API key"""
        valid_config.api_key = None
        with pytest.raises(LLMConfigurationError) as exc_info:
            ConfigValidator.validate(valid_config)
        assert "API key must be provided" in str(exc_info.value)

    def test_invalid_provider(self, valid_config):
        """Test validation with invalid provider"""
        valid_config.provider = "invalid_provider"
        with pytest.raises(LLMConfigurationError) as exc_info:
            ConfigValidator.validate(valid_config)
        assert "Invalid provider" in str(exc_info.value)

    def test_invalid_model(self, valid_config):
        """Test validation with invalid model"""
        valid_config.model = "invalid-model"
        with pytest.raises(LLMConfigurationError) as exc_info:
            ConfigValidator.validate(valid_config)
        assert "Invalid model" in str(exc_info.value)
        assert "supported models for provider" in str(exc_info.value)

    @pytest.mark.parametrize("temperature", [-0.1, 1.1, 2.0])
    def test_invalid_temperature(self, valid_config, temperature):
        """Test validation with invalid temperature values"""
        valid_config.temperature = temperature
        with pytest.raises(LLMConfigurationError) as exc_info:
            ConfigValidator.validate(valid_config)
        assert "Temperature must be between 0 and 1" in str(exc_info.value)

    @pytest.mark.parametrize("max_tokens", [0, -1, -100])
    def test_invalid_max_tokens(self, valid_config, max_tokens):
        """Test validation with invalid max_tokens values"""
        valid_config.max_tokens = max_tokens
        with pytest.raises(LLMConfigurationError) as exc_info:
            ConfigValidator.validate(valid_config)
        assert "max_tokens must be positive" in str(exc_info.value)

    def test_case_insensitive_provider(self, valid_config):
        """Test that provider validation is case-insensitive"""
        valid_config.provider = "OPENAI"
        provider = ConfigValidator.validate(valid_config)
        assert provider == LLMProvider.OPENAI

    def test_optional_temperature(self, valid_config):
        """Test that temperature can be None"""
        valid_config.temperature = None
        ConfigValidator.validate(valid_config)

    def test_optional_max_tokens(self, valid_config):
        """Test that max_tokens can be None"""
        valid_config.max_tokens = None
        ConfigValidator.validate(valid_config)

    @pytest.mark.parametrize("provider,model,valid_models", [
        ("openai", "gpt-4o", {"gpt-4o", "gpt-4-turbo"}),
        ("anthropic", "claude-3-5-sonnet-latest", {"claude-3-5-sonnet-latest", "claude-3-opus"})
    ])
    def test_provider_specific_models(self, valid_config, provider, model, valid_models):
        """Test validation with different provider-specific models"""
        valid_config.provider = provider
        valid_config.model = model
        valid_config.valid_models = valid_models
        ConfigValidator.validate(valid_config)