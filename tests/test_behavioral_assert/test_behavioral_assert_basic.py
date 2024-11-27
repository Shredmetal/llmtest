import pytest

from llm_app_test.behavioral_assert.llm_config.llm_provider_enum import LLMProvider
from llm_app_test.behavioral_assert.behavioral_assert import BehavioralAssertion
from llm_app_test.exceptions.test_exceptions import (
    BehavioralAssertionError,
    LLMConnectionError
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
            asserter = BehavioralAssertion(api_key="invalid_key")
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

    def test_empty_inputs(self, asserter):
        """Test empty inputs"""
        with pytest.raises(BehavioralAssertionError) as excinfo:
            asserter.assert_behavioral_match("", "")
        assert "Behavioral assertion failed" in str(excinfo.value)

    def test_none_inputs(self, asserter):
        """Test None inputs raise TypeError"""
        with pytest.raises(TypeError) as excinfo:
            asserter.assert_behavioral_match(None, None)
        assert "Inputs cannot be None" in str(excinfo.value)
