import pytest
from unittest.mock import Mock, patch


@pytest.fixture(scope="session")
def mock_chat_openai():
    """Session-scoped mock for OpenAI chat"""
    with patch('llm_app_test.semantic_assert.llm_config.llm_factory.ChatOpenAI') as mock:
        mock_instance = Mock()
        mock.return_value = mock_instance
        yield mock

@pytest.fixture(scope="session")
def mock_chat_anthropic():
    """Session-scoped mock for Anthropic chat"""
    with patch('llm_app_test.semantic_assert.llm_config.llm_factory.ChatAnthropic') as mock:
        mock_instance = Mock()
        mock.return_value = mock_instance
        yield mock