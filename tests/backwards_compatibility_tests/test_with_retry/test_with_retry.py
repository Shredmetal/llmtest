import os
from unittest.mock import patch, Mock

from llm_app_test.semantic_assert.semantic_assert import SemanticAssertion


class TestWithRetryInSemanticAssertion:

    def test_semantic_assert_defaults(self):
        with patch.dict(os.environ, {}, clear=True):  # Ensure no env variables affect the test
            asserter = SemanticAssertion(api_key="test_key")  # api_key is required

        assert not hasattr(asserter, 'retry_config'), "retry_config should not be set by default"

    @patch('llm_app_test.behavioral_assert.behavioral_assert.LLMFactory')
    def test_semantic_assert_with_retry(self, mock_llm_factory):
        mock_llm = Mock()
        mock_llm_factory.create_llm.return_value = mock_llm

        with patch.dict(os.environ, {}, clear=True):
            asserter = SemanticAssertion(api_key="test_key", langchain_with_retry=True)

        assert hasattr(asserter, 'retry_config'), "retry_config should be set when langchain_with_retry is True"
        assert asserter.retry_config is not None
        assert asserter.retry_config.retry_if_exception_type == (Exception,)
        assert asserter.retry_config.wait_exponential_jitter == True
        assert asserter.retry_config.stop_after_attempt == 3

    @patch('llm_app_test.behavioral_assert.behavioral_assert.LLMFactory')
    def test_semantic_assert_custom_retry(self, mock_llm_factory):
        mock_llm = Mock()
        mock_llm_factory.create_llm.return_value = mock_llm

        with patch.dict(os.environ, {}, clear=True):
            asserter = SemanticAssertion(
                api_key="test_key",
                langchain_with_retry=True,
                retry_if_exception_type=(ValueError,),
                wait_exponential_jitter=False,
                stop_after_attempt=5
            )

        assert hasattr(asserter, 'retry_config'), "retry_config should be set when langchain_with_retry is True"
        assert asserter.retry_config is not None
        assert asserter.retry_config.retry_if_exception_type == (ValueError,)
        assert asserter.retry_config.wait_exponential_jitter == False
        assert asserter.retry_config.stop_after_attempt == 5

    @patch('llm_app_test.behavioral_assert.behavioral_assert.LLMFactory')
    def test_semantic_assert_env_vars(self, mock_llm_factory):
        mock_llm = Mock()
        mock_llm_factory.create_llm.return_value = mock_llm

        env_vars = {
            'LANGCHAIN_WITH_RETRY': 'true',
            'ASSERTER_WAIT_EXPONENTIAL_JITTER': 'false',
            'ASSERTER_STOP_AFTER_ATTEMPT': '7'
        }

        with patch.dict(os.environ, env_vars, clear=True):
            asserter = SemanticAssertion(api_key="test_key")

        assert hasattr(asserter, 'retry_config'), "retry_config should be set when LANGCHAIN_WITH_RETRY is 'true'"
        assert asserter.retry_config is not None
        assert asserter.retry_config.retry_if_exception_type == (Exception,)
        assert asserter.retry_config.wait_exponential_jitter == False
        assert asserter.retry_config.stop_after_attempt == 7

    @patch('llm_app_test.behavioral_assert.behavioral_assert.LLMFactory')
    def test_semantic_assert_env_vars_override(self, mock_llm_factory):
        mock_llm = Mock()
        mock_llm_factory.create_llm.return_value = mock_llm

        env_vars = {
            'LANGCHAIN_WITH_RETRY': 'true',
            'ASSERTER_WAIT_EXPONENTIAL_JITTER': 'false',
            'ASSERTER_STOP_AFTER_ATTEMPT': '7'
        }

        with patch.dict(os.environ, env_vars, clear=True):
            asserter = SemanticAssertion(
                api_key="test_key",
                wait_exponential_jitter=True,
                stop_after_attempt=5
            )

        assert hasattr(asserter, 'retry_config'), "retry_config should be set when LANGCHAIN_WITH_RETRY is 'true'"
        assert asserter.retry_config is not None
        assert asserter.retry_config.retry_if_exception_type == (Exception,)
        assert asserter.retry_config.wait_exponential_jitter == True
        assert asserter.retry_config.stop_after_attempt == 5
