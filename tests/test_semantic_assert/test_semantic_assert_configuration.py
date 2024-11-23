from unittest.mock import patch, Mock
from llm_app_test.semantic_assert.semantic_assert import SemanticAssertion
from llm_app_test.semantic_assert.semantic_assert_config.semantic_assert_constants import LLMConstants, ModelConstants


class TestSemanticAssertionConfiguration:
    """Test suite for SemanticAssertion configuration"""

    @patch('llm_app_test.semantic_assert.llm_config.llm_factory.ChatOpenAI')
    def test_all_custom_configurations(self, mock_chat):
        """Test that all custom configurations are properly propagated"""
        # Setup mock
        mock_instance = Mock()
        mock_instance.invoke.return_value = Mock(content="PASS")
        mock_chat.return_value = mock_instance

        # Create asserter with all custom values
        asserter = SemanticAssertion(
            api_key="test_key",
            timeout=5.0,
            temperature=0.5,
            max_tokens=1000,
            max_retries=3,
            model="gpt-4o"
        )

        # Use the asserter
        asserter.assert_semantic_match(
            actual="test content",
            expected_behavior="test expectation"
        )

        # Verify all configurations
        create_args = mock_chat.call_args.kwargs
        assert create_args['api_key'] == "test_key"
        assert create_args['request_timeout'] == 5.0
        assert create_args['temperature'] == 0.5
        assert create_args['max_tokens'] == 1000
        assert create_args['max_retries'] == 3
        assert create_args['model'] == "gpt-4o"

    @patch('llm_app_test.semantic_assert.llm_config.llm_factory.ChatOpenAI')
    def test_all_default_configurations(self, mock_chat):
        """Test that all default configurations are properly set"""
        # Setup mock
        mock_instance = Mock()
        mock_instance.invoke.return_value = Mock(content="PASS")
        mock_chat.return_value = mock_instance

        # Create asserter with only required api_key
        asserter = SemanticAssertion(api_key="test_key")

        # Use the asserter
        asserter.assert_semantic_match(
            actual="test content",
            expected_behavior="test expectation"
        )

        # Verify all default configurations
        create_args = mock_chat.call_args.kwargs
        assert create_args['api_key'] == "test_key"
        assert create_args['request_timeout'] == LLMConstants.DEFAULT_TIMEOUT
        assert create_args['temperature'] == LLMConstants.DEFAULT_TEMPERATURE
        assert create_args['max_tokens'] == LLMConstants.DEFAULT_MAX_TOKENS
        assert create_args['max_retries'] == LLMConstants.DEFAULT_MAX_RETRIES
        assert create_args['model'] == ModelConstants.DEFAULT_OPENAI_MODEL

    @patch('llm_app_test.semantic_assert.llm_config.llm_factory.ChatAnthropic')
    def test_anthropic_default_configurations(self, mock_chat):
        """Test that all default configurations are properly set"""
        # Setup mock
        mock_instance = Mock()
        mock_instance.invoke.return_value = Mock(content="PASS")
        mock_chat.return_value = mock_instance

        # Create asserter with only required api_key
        asserter = SemanticAssertion(
            api_key="test_key",
            provider="anthropic"
        )

        # Use the asserter
        asserter.assert_semantic_match(
            actual="test content",
            expected_behavior="test expectation"
        )

        # Verify all default configurations
        create_args = mock_chat.call_args.kwargs
        assert create_args['anthropic_api_key'] == "test_key"  # Changed from api_key
        assert create_args['temperature'] == LLMConstants.DEFAULT_TEMPERATURE
        assert create_args['max_tokens'] == LLMConstants.DEFAULT_MAX_TOKENS
        assert create_args['max_retries'] == LLMConstants.DEFAULT_MAX_RETRIES
        assert create_args['model'] == ModelConstants.DEFAULT_ANTHROPIC_MODEL
