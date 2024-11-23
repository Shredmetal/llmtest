from unittest.mock import patch
from llm_app_test.semantic_assert.semantic_assert import SemanticAssertion
from llm_app_test.semantic_assert.semantic_assert_config.semantic_assert_constants import LLMConstants

class TestSemanticAssertionTimeout:
    """Test suite for SemanticAssertion timeout configuration"""

    @patch('llm_app_test.semantic_assert.llm_config.llm_factory.ChatOpenAI')
    def test_timeout_configuration(self, mock_chat):
        """Test that timeout is properly configured"""
        asserter = SemanticAssertion(
            api_key="test_key",
            timeout=5.0
        )

        # Verify ChatOpenAI was called with correct timeout
        mock_chat.assert_called_once()
        assert mock_chat.call_args[1]['request_timeout'] == 5.0

    @patch('llm_app_test.semantic_assert.llm_config.llm_factory.ChatOpenAI')
    def test_default_timeout_configuration(self, mock_chat):
        """Test that default timeout is properly configured"""
        asserter = SemanticAssertion(api_key="test_key")

        # Verify ChatOpenAI was called with default timeout
        mock_chat.assert_called_once()
        assert mock_chat.call_args[1]['request_timeout'] == LLMConstants.DEFAULT_TIMEOUT
