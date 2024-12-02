import pytest
from unittest.mock import Mock
from langchain_core.language_models import BaseLanguageModel
from llm_app_test.exceptions.test_exceptions import InvalidPromptError
from llm_app_test.behavioral_assert.behavioral_assert import BehavioralAssertion


class TestBehavioralAssertionValidation:
    """Test suite for validation in BehavioralAssertion"""

    @pytest.fixture
    def mock_llm(self):
        """Fixture providing a mocked LLM"""
        mock = Mock(spec=BaseLanguageModel)
        mock.invoke.return_value.content = "PASS"
        return mock

    @pytest.fixture
    def asserter(self, mock_llm):
        """Fixture providing a BehavioralAssertion instance with mocked LLM"""
        asserter = BehavioralAssertion()
        asserter.llm = mock_llm
        return asserter

    def test_valid_inputs(self, asserter):
        """Test validation passes with valid string inputs"""
        asserter.assert_behavioral_match("actual output", "expected behavior")
        # If we get here without exception, the test passes

    def test_none_actual(self, asserter):
        """Test validation fails with None actual parameter"""
        with pytest.raises(InvalidPromptError) as exc_info:
            asserter.assert_behavioral_match(None, "expected behavior")
        assert "actual must be a string and cannot be None" in str(exc_info.value.reason)

    def test_none_expected(self, asserter):
        """Test validation fails with None expected parameter"""
        with pytest.raises(InvalidPromptError) as exc_info:
            asserter.assert_behavioral_match("actual output", None)
        assert "expected_behavior must be a string and cannot be None" in str(exc_info.value.reason)

    def test_non_string_actual(self, asserter):
        """Test validation fails with non-string actual parameter"""
        with pytest.raises(InvalidPromptError) as exc_info:
            asserter.assert_behavioral_match(123, "expected behavior")
        assert "actual must be a string, got int" in str(exc_info.value.reason)

    def test_non_string_expected(self, asserter):
        """Test validation fails with non-string expected parameter"""
        with pytest.raises(InvalidPromptError) as exc_info:
            asserter.assert_behavioral_match("actual output", 123)
        assert "expected_behavior must be a string, got int" in str(exc_info.value.reason)

    @pytest.mark.parametrize("invalid_input", [
        123, 1.23, True, [], {}, set()
    ])
    def test_various_invalid_types_actual(self, asserter, invalid_input):
        """Test validation fails with various non-string types for actual"""
        with pytest.raises(InvalidPromptError) as exc_info:
            asserter.assert_behavioral_match(invalid_input, "expected behavior")
        assert f"actual must be a string, got {type(invalid_input).__name__}" in str(exc_info.value.reason)

    @pytest.mark.parametrize("invalid_input", [
        123, 1.23, True, [], {}, set()
    ])
    def test_various_invalid_types_expected(self, asserter, invalid_input):
        """Test validation fails with various non-string types for expected"""
        with pytest.raises(InvalidPromptError) as exc_info:
            asserter.assert_behavioral_match("actual output", invalid_input)
        assert f"expected_behavior must be a string, got {type(invalid_input).__name__}" in str(exc_info.value.reason)
