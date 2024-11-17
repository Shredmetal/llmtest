import os
import pytest
from llm_app_test.semantic_assert.semantic_assert import SemanticAssertion
from llm_app_test.exceptions.test_exceptions import (
    SemanticAssertionError,
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
        with pytest.raises(SemanticAssertionError) as excinfo:
            asserter.assert_semantic_match(actual, expected)
        assert "Semantic assertion failed" in str(excinfo.value)

    def test_invalid_api_key(self):
        """Test invalid API key raises correct exception"""
        with pytest.raises(LLMConnectionError) as excinfo:
            asserter = SemanticAssertion(api_key="invalid_key")
            asserter.assert_semantic_match("test", "test")
        assert "Error code: 401" in str(excinfo.value)

    def test_empty_inputs(self, asserter):
        """Test empty inputs"""
        with pytest.raises(SemanticAssertionError) as excinfo:
            asserter.assert_semantic_match("", "")
        assert "Semantic assertion failed" in str(excinfo.value)

    def test_none_inputs(self, asserter):
        """Test None inputs raise TypeError"""
        with pytest.raises(TypeError) as excinfo:
            asserter.assert_semantic_match(None, None)
        assert "Inputs cannot be None" in str(excinfo.value)
