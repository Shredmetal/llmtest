from unittest.mock import patch, Mock

import pytest
from llm_app_test.semantic_assert.llm_config.llm_config import LLMConfig
from llm_app_test.semantic_assert.llm_config.llm_factory import LLMFactory
from llm_app_test.semantic_assert.llm_config.llm_provider_enum import LLMProvider


@pytest.fixture
def openai_config():
    """Fixture for OpenAI configuration with all parameters set"""
    return LLMConfig(
        provider=LLMProvider.OPENAI,
        api_key="test-key",
        model="gpt-4o",
        temperature=0.0,
        max_tokens=4096,
        max_retries=2,
        timeout=10.0
    )


@pytest.fixture
def minimal_openai_config():
    """Fixture for minimal OpenAI configuration"""
    return LLMConfig(provider=LLMProvider.OPENAI)


@pytest.fixture
def anthropic_config():
    """Fixture for Anthropic configuration with all parameters set"""
    return LLMConfig(
        provider=LLMProvider.ANTHROPIC,
        api_key="anthropic-key",
        model="claude-3-5-sonnet",
        temperature=0.0,
        max_tokens=4096,
        max_retries=2
    )


class TestLLMFactory:
    """Test suite for LLMFactory class"""

    @patch('llm_app_test.semantic_assert.llm_config.llm_factory.ChatOpenAI')
    def test_create_openai_llm_with_full_config(self, mock_chat_openai, openai_config):
        """Test creation of OpenAI LLM with full configuration"""
        mock_instance = Mock()
        mock_chat_openai.return_value = mock_instance

        llm = LLMFactory.create_llm(openai_config)

        mock_chat_openai.assert_called_once_with(
            temperature=0.0,
            model_name="gpt-4o",
            openai_api_key="test-key",
            max_retries=2,
            max_tokens=4096,
            request_timeout=10.0
        )
        assert llm == mock_instance

    @patch('llm_app_test.semantic_assert.llm_config.llm_factory.ChatAnthropic')
    def test_create_anthropic_llm_with_full_config(self, mock_chat_anthropic, anthropic_config):
        """Test creation of Anthropic LLM with full configuration"""
        mock_instance = Mock()
        mock_chat_anthropic.return_value = mock_instance

        llm = LLMFactory.create_llm(anthropic_config)

        mock_chat_anthropic.assert_called_once_with(
            temperature=0.0,
            model="claude-3-5-sonnet",
            anthropic_api_key="anthropic-key",
            max_retries=2,
            max_tokens=4096
        )
        assert llm == mock_instance

    @patch('llm_app_test.semantic_assert.llm_config.llm_factory.ChatOpenAI')
    def test_create_llm_with_minimal_config(self, mock_chat_openai, minimal_openai_config):
        """Test creation of LLM with minimal configuration"""
        mock_instance = Mock()
        mock_chat_openai.return_value = mock_instance

        llm = LLMFactory.create_llm(minimal_openai_config)

        mock_chat_openai.assert_called_once_with(
            temperature=None,
            model_name=None,
            openai_api_key=None,
            max_retries=None,
            max_tokens=None,
            request_timeout=None
        )
        assert llm == mock_instance
