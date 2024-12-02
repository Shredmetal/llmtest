from unittest.mock import Mock

import pytest
from langchain_core.language_models import BaseLanguageModel

from llm_app_test.behavioral_assert.llm_config.llm_provider_enum import LLMProvider
from llm_app_test.behavioral_assert.behavioral_assert import BehavioralAssertion
from llm_app_test.exceptions.test_exceptions import (
    BehavioralAssertionError,
    LLMConnectionError, LLMAppTestError
)


class TestBehavioralAssertion:
    """Test suite for BehavioralAssertion class"""

    @pytest.fixture
    def asserter(self):
        """Fixture providing a BehavioralAssertion instance"""
        return BehavioralAssertion()

    def test_basic_behavioral_match(self, asserter):
        """Test basic behavioral matching"""
        actual = "The sky is blue"
        expected = "A statement about the color of the sky"
        asserter.assert_behavioral_match(actual, expected)

    def test_behavioral_mismatch(self, asserter):
        """Test behavioral mismatch raises correct exception"""
        actual = "The sky is blue"
        expected = "A statement about the weather forecast"
        with pytest.raises(BehavioralAssertionError) as excinfo:
            asserter.assert_behavioral_match(actual, expected)
        assert "Behavioral assertion failed" in str(excinfo.value)

    def test_openai_api_error(self):
        """Test OpenAI API error handling"""
        with pytest.raises(LLMConnectionError) as exc_info:
            asserter = BehavioralAssertion(
                provider=LLMProvider.OPENAI,
                api_key="invalid_key")
            asserter.assert_behavioral_match("test", "test")
        assert "OpenAI API error occurred" in str(exc_info.value)

    def test_anthropic_api_error(self):
        """Test Anthropic API error handling"""
        with pytest.raises(LLMConnectionError) as exc_info:
            asserter = BehavioralAssertion(
                provider=LLMProvider.ANTHROPIC,
                api_key="invalid_key"
            )
            asserter.assert_behavioral_match("test", "test")
        assert "Anthropic API error occurred" in str(exc_info.value)

    def test_generic_llm_error(self, asserter):
        """Test handling of generic LLM errors"""
        mock_llm = Mock(spec=BaseLanguageModel)
        mock_llm.invoke.side_effect = ValueError("Generic LLM error")

        asserter.llm = mock_llm

        with pytest.raises(LLMConnectionError) as exc_info:
            asserter.assert_behavioral_match("test", "test")

        assert "LLM operation failed in assert_behavioral_match" in str(exc_info.value)
        assert "Generic LLM error" in str(exc_info.value)

    def test_empty_inputs(self, asserter):
        """Test empty inputs"""
        with pytest.raises(BehavioralAssertionError) as excinfo:
            asserter.assert_behavioral_match("", "")
        assert "Behavioral assertion failed" in str(excinfo.value)

    def test_llm_app_test_error_with_details(self):
        """Test LLMAppTestError with details dictionary"""
        details = {"error_code": 500, "timestamp": "2024-11-29"}
        error = LLMAppTestError(
            message="Test error",
            reason="Something went wrong",
            details=details
        )

        assert error.message == "Test error"
        assert error.reason == "Something went wrong"
        assert error.details == details

        error_str = str(error)
        assert "Test error" in error_str
        assert "Something went wrong" in error_str
        assert "{'error_code': 500" in error_str
        assert "'timestamp': '2024-11-29'" in error_str

    def test_llm_app_test_error_propagation(self):
        """Test LLMAppTestError propagation through the decorator"""
        mock_llm = Mock(spec=BaseLanguageModel)
        details = {"error_code": 500, "timestamp": "2024-11-29"}
        mock_llm.invoke.side_effect = LLMAppTestError(
            message="Custom error",
            reason="Test reason",
            details=details
        )

        asserter = BehavioralAssertion()
        asserter.llm = mock_llm

        with pytest.raises(LLMAppTestError) as exc_info:
            asserter.assert_behavioral_match("test", "test")

        assert exc_info.value.message == "Custom error"
        assert exc_info.value.reason == "Test reason"
        assert exc_info.value.details == details

