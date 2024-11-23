from unittest.mock import patch, Mock
from llm_app_test.semantic_assert.semantic_assert import SemanticAssertion
from llm_app_test.semantic_assert.semantic_assert_config.semantic_assert_constants import LLMConstants

class TestSemanticAssertionTimeout:
    """Test suite for SemanticAssertion timeout configuration"""

    @patch('llm_app_test.semantic_assert.llm_config.llm_factory.ChatOpenAI')
    def test_timeout_configuration(self, mock_chat):
        """Test that timeout is properly configured"""
        # Setup mock
        mock_instance = Mock()
        mock_instance.invoke.return_value = Mock(content="PASS")
        mock_chat.return_value = mock_instance

        # Create asserter with custom timeout
        custom_timeout = 5.0
        asserter = SemanticAssertion(
            api_key="test_key",
            timeout=custom_timeout
        )

        # Actually use the asserter
        asserter.assert_semantic_match(
            actual="test content",
            expected_behavior="test expectation"
        )

        # Verify ChatOpenAI was created with correct args
        create_args = mock_chat.call_args.kwargs
        assert create_args['request_timeout'] == custom_timeout
        assert create_args['api_key'] == "test_key"

    @patch('llm_app_test.semantic_assert.llm_config.llm_factory.ChatOpenAI')
    def test_default_timeout_configuration(self, mock_chat):
        """Test that default timeout is properly configured"""
        # Setup mock
        mock_instance = Mock()
        mock_instance.invoke.return_value = Mock(content="PASS")
        mock_chat.return_value = mock_instance

        # Create and use asserter
        asserter = SemanticAssertion(api_key="test_key")

        asserter.assert_semantic_match(
            actual="test content",
            expected_behavior="test expectation"
        )

        # Verify ChatOpenAI was created with correct args
        create_args = mock_chat.call_args.kwargs
        assert create_args['request_timeout'] == LLMConstants.DEFAULT_TIMEOUT
        assert create_args['api_key'] == "test_key"
