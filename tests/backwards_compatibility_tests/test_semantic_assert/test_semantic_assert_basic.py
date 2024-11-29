from unittest.mock import Mock

import pytest
from langchain_core.language_models import BaseLanguageModel

from llm_app_test.behavioral_assert.llm_config.llm_provider_enum import LLMProvider
from llm_app_test.semantic_assert.semantic_assert import SemanticAssertion
from llm_app_test.exceptions.test_exceptions import (
    BehavioralAssertionError,
    LLMConnectionError
)


class TestSemanticAssertion:
    """Test suite for SemanticAssertion class"""

    @pytest.fixture
    def asserter(self):
        """Fixture providing a SemanticAssertion instance"""
        return SemanticAssertion()

    def test_basic_semantic_match(self, asserter):
        """Test basic semantic matching"""
        actual = "The sky is blue"
        expected = "A statement about the color of the sky"
        asserter.assert_semantic_match(actual, expected)

    def test_semantic_mismatch(self, asserter):
        """Test semantic mismatch raises correct exception"""
        actual = "The sky is blue"
        expected = "A statement about the weather forecast"
        with pytest.raises(BehavioralAssertionError) as excinfo:
            asserter.assert_semantic_match(actual, expected)
        assert "Behavioral assertion failed" in str(excinfo.value)

    def test_openai_api_error(self):
        """Test OpenAI API error handling"""
        with pytest.raises(LLMConnectionError) as exc_info:
            asserter = SemanticAssertion(
                provider=LLMProvider.OPENAI,
                api_key="invalid_key"
            )
            asserter.assert_semantic_match("test", "test")
        assert "OpenAI API error occurred" in str(exc_info.value)

    def test_anthropic_api_error(self):
        """Test Anthropic API error handling"""
        with pytest.raises(LLMConnectionError) as exc_info:
            asserter = SemanticAssertion(
                provider=LLMProvider.ANTHROPIC,
                api_key="invalid_key"
            )
            asserter.assert_semantic_match("test", "test")
        assert "Anthropic API error occurred" in str(exc_info.value)

    def test_generic_llm_error(self, asserter):
        """Test handling of generic LLM errors"""
        mock_llm = Mock(spec=BaseLanguageModel)
        mock_llm.invoke.side_effect = ValueError("Generic LLM error")

        asserter.llm = mock_llm

        with pytest.raises(LLMConnectionError) as exc_info:
            asserter.assert_semantic_match("test", "test")

        assert "LLM operation failed in assert_behavioral_match" in str(exc_info.value)
        assert "Generic LLM error" in str(exc_info.value)

    def test_empty_inputs(self, asserter):
        """Test empty inputs"""
        with pytest.raises(BehavioralAssertionError) as excinfo:
            asserter.assert_semantic_match("", "")
        assert "Behavioral assertion failed" in str(excinfo.value)

    def test_none_inputs(self, asserter):
        """Test None inputs raise TypeError"""
        with pytest.raises(TypeError) as excinfo:
            asserter.assert_semantic_match(None, None)
        assert "Inputs cannot be None" in str(excinfo.value)
