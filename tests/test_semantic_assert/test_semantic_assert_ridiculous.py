import os
import pytest
from llmtest.semanticassert.semantic_assert import SemanticAssertion
from llmtest.exceptions.test_exceptions import (
    SemanticAssertionError
)


class TestRidiculousSemanticAssertion:
    @pytest.fixture
    def asserter(self):
        return SemanticAssertion(api_key=os.getenv("OPENAI_API_KEY"))

    def test_100_emojis(self, asserter):
        """Test recognition of a pile of meaningless emojis"""
        actual = "🤖" * 100
        expected = "A lot of emojis"
        asserter.assert_semantic_match(actual, expected)

    def test_expect_few_but_get_a_ton_of_emojis(self, asserter):
        """Test recognition of a pile of meaningless emojis"""
        actual = "🤖" * 100
        expected = "Only a few emojis"
        with pytest.raises(SemanticAssertionError) as excinfo:
            asserter.assert_semantic_match(actual, expected)
        assert "Semantic assertion failed" in str(excinfo.value)