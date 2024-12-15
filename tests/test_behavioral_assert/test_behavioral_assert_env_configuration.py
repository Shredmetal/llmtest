import os

import pytest
from unittest.mock import Mock, patch
from llm_app_test.behavioral_assert.behavioral_assert import BehavioralAssertion
from llm_app_test.behavioral_assert.behavioral_assert_config.behavioral_assert_constants import (
    LLMConstants, ModelConstants
)


class TestBehavioralAssertionEnvironmentConfiguration:
    """Test suite for BehavioralAssertion environment variable configuration"""

    @pytest.fixture
    def mock_chat(self, monkeypatch):
        """Fixture to provide a mock chat instance"""
        mock_instance = Mock()
        mock_instance.invoke.return_value = Mock(content="PASS")
        return mock_instance

    @pytest.fixture
    def clean_env_with_fake_api(self):
        original_env = dict(os.environ)
        os.environ.clear()
        os.environ['OPENAI_API_KEY'] = 'fake-api-key-for-testing'
        yield
        os.environ.clear()
        os.environ.update(original_env)

    def test_env_var_precedence_openai(self, monkeypatch, mock_chat):
        """Test that environment variables are properly loaded with correct precedence"""
        # Set environment variables
        monkeypatch.setenv('OPENAI_API_KEY', 'env_test_key')
        monkeypatch.setenv('LLM_PROVIDER', 'openai')
        monkeypatch.setenv('LLM_MODEL', 'gpt-4o')
        monkeypatch.setenv('LLM_TEMPERATURE', '0.7')
        monkeypatch.setenv('LLM_MAX_TOKENS', '2000')
        monkeypatch.setenv('LLM_MAX_RETRIES', '5')
        monkeypatch.setenv('LLM_TIMEOUT', '10.0')

        mock_instance = Mock()
        mock_instance.invoke.return_value = Mock(content="PASS")

        with patch('llm_app_test.behavioral_assert.llm_config.llm_factory.ChatOpenAI') as mock_openai:

            mock_openai.return_value = mock_instance

            asserter = BehavioralAssertion(
                api_key="explicit_key",  # Should override env var
                temperature=0.3,  # Should override env var
            )

            asserter.assert_behavioral_match(
                actual="test content",
                expected_behavior="test expectation"
            )

            create_args = mock_openai.call_args.kwargs
            assert create_args['openai_api_key'] == "explicit_key"  # From constructor
            assert create_args['model_name'] == "gpt-4o"  # From env var
            assert create_args['temperature'] == 0.3  # From constructor
            assert create_args['max_tokens'] == 2000  # From env var
            assert create_args['max_retries'] == 5  # From env var
            assert create_args['request_timeout'] == 10.0  # From env var

    def test_env_var_fallbacks(self, clean_env_with_fake_api):
        """Test that default values are used when env vars are not set"""

        with patch('llm_app_test.behavioral_assert.behavioral_assert.load_dotenv'):
            mock_instance = Mock()
            mock_instance.invoke.return_value = Mock(content="PASS")

            with patch('llm_app_test.behavioral_assert.llm_config.llm_factory.ChatOpenAI') as mock_openai:
                mock_openai.return_value = mock_instance

                asserter = BehavioralAssertion()

                asserter.assert_behavioral_match(
                    actual="test content",
                    expected_behavior="test expectation"
                )

                create_args = mock_openai.call_args.kwargs
                assert create_args['model_name'] == ModelConstants.DEFAULT_OPENAI_MODEL
                assert create_args['temperature'] == LLMConstants.DEFAULT_TEMPERATURE
                assert create_args['max_tokens'] == LLMConstants.DEFAULT_MAX_TOKENS
                assert create_args['max_retries'] == LLMConstants.DEFAULT_MAX_RETRIES
                assert create_args['request_timeout'] == LLMConstants.DEFAULT_TIMEOUT
                assert create_args['openai_api_key'] == 'fake-api-key-for-testing'

    def test_anthropic_env_vars(self, monkeypatch, mock_chat):
        """Test environment variable handling for Anthropic provider"""
        monkeypatch.setenv('ANTHROPIC_API_KEY', 'env_test_key')
        monkeypatch.setenv('LLM_PROVIDER', 'anthropic')
        monkeypatch.setenv('LLM_MODEL', 'claude-3-5-sonnet-latest')
        monkeypatch.setenv('LLM_TEMPERATURE', '0.7')
        monkeypatch.setenv('LLM_MAX_TOKENS', '2000')
        monkeypatch.setenv('LLM_MAX_RETRIES', '5')
        monkeypatch.setenv('LLM_TIMEOUT', '10.0')

        mock_instance = Mock()
        mock_instance.invoke.return_value = Mock(content="PASS")

        with patch('llm_app_test.behavioral_assert.llm_config.llm_factory.ChatAnthropic') as mock_anthropic:
            mock_anthropic.return_value = mock_instance

            asserter = BehavioralAssertion()

            asserter.assert_behavioral_match(
                actual="test content",
                expected_behavior="test expectation"
            )

            create_args = mock_anthropic.call_args.kwargs
            assert create_args['anthropic_api_key'] == "env_test_key"
            assert create_args['model'] == "claude-3-5-sonnet-latest"
            assert create_args['temperature'] == 0.7  # From constructor
            assert create_args['max_tokens'] == 2000  # From env var
            assert create_args['max_retries'] == 5  # From env var
            assert create_args['default_request_timeout'] == 10.0  # From env var

    def test_env_var_type_conversion(self, monkeypatch, mock_chat):
        """Test that environment variables are correctly converted to their types"""
        monkeypatch.setenv('LLM_TEMPERATURE', '0.7')
        monkeypatch.setenv('LLM_MAX_TOKENS', '1000')
        monkeypatch.setenv('LLM_TIMEOUT', '30.0')
        monkeypatch.setenv('OPENAI_API_KEY', 'test_key')
        monkeypatch.setenv('LLM_PROVIDER', 'openai')

        with patch('llm_app_test.behavioral_assert.llm_config.llm_factory.ChatOpenAI') as mock_openai:
            mock_openai.return_value = mock_chat

            asserter = BehavioralAssertion()

            create_args = mock_openai.call_args.kwargs
            assert isinstance(create_args['temperature'], float)
            assert isinstance(create_args['max_tokens'], int)
            assert isinstance(create_args['request_timeout'], float)

            assert create_args['temperature'] == 0.7
            assert create_args['max_tokens'] == 1000
            assert create_args['request_timeout'] == 30.0

