import pytest
from unittest.mock import patch, Mock
from llmtest.semanticassert.semantic_assert import SemanticAssertion
from llmtest.semanticassert.llmconfig.llm_provider_enum import LLMProvider
from llmtest.exceptions.test_exceptions import (
    LLMConfigurationError
)

class TestSemanticAssertionValidation:
    """Test suite for SemanticAssertion validation"""

    def test_invalid_temperature_range(self):
        """Test that invalid temperature values raise configuration error"""
        with pytest.raises(LLMConfigurationError) as excinfo:
            SemanticAssertion(
                api_key="test_key",
                temperature=1.5
            )
        assert "Temperature must be between 0 and 1" in str(excinfo.value.reason)

        with pytest.raises(LLMConfigurationError) as excinfo:
            SemanticAssertion(
                api_key="test_key",
                temperature=-0.5
            )
        assert "Temperature must be between 0 and 1" in str(excinfo.value.reason)

    def test_invalid_max_tokens(self):
        """Test that invalid max_tokens values raise configuration error"""
        with pytest.raises(LLMConfigurationError) as excinfo:
            SemanticAssertion(
                api_key="test_key",
                max_tokens=-100
            )
        assert "max_tokens must be positive" in str(excinfo.value.reason)

        with pytest.raises(LLMConfigurationError) as excinfo:
            SemanticAssertion(
                api_key="test_key",
                max_tokens=0
            )
        assert "max_tokens must be positive" in str(excinfo.value.reason)

    def test_invalid_provider(self):
        """Test that invalid provider raises configuration error"""
        with pytest.raises(LLMConfigurationError) as excinfo:
            SemanticAssertion(
                api_key="test_key",
                provider="invalid_provider"
            )
        assert "Invalid provider" in str(excinfo.value.reason)

    def test_invalid_openai_model(self):
        """Test that invalid OpenAI model raises configuration error"""
        with pytest.raises(LLMConfigurationError) as excinfo:
            SemanticAssertion(
                api_key="test_key",
                provider=LLMProvider.OPENAI,
                model="invalid-model"
            )
        assert "Invalid model" in str(excinfo.value.reason)
        assert "gpt-4o" in str(excinfo.value.reason)

    def test_invalid_anthropic_model(self):
        """Test that invalid Anthropic model raises configuration error"""
        with pytest.raises(LLMConfigurationError) as excinfo:
            SemanticAssertion(
                api_key="test_key",
                provider=LLMProvider.ANTHROPIC,
                model="invalid-model"
            )
        assert "Invalid model" in str(excinfo.value.reason)
        assert "claude-3" in str(excinfo.value.reason)

    def test_missing_api_key(self):
        """Test that missing API key raises configuration error"""
        mock_getenv = Mock(side_effect=lambda x, default=None: default if default else None)
        with patch('os.getenv', mock_getenv):
            with pytest.raises(LLMConfigurationError) as excinfo:
                SemanticAssertion(api_key=None)
            assert "API key must be provided" in str(excinfo.value.reason)
