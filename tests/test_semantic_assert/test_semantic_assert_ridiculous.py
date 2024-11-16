import os
import pytest
from llmtest.semanticassert.semantic_assert import SemanticAssertion
from llmtest.exceptions.test_exceptions import (
    SemanticAssertionError
)


class TestComplexSemanticAssertion:
    @pytest.fixture
    def asserter(self):
        return SemanticAssertion(api_key=os.getenv("OPENAI_API_KEY"))

    def test_100_emojis(self, asserter):
        """Test recognition of a pile of meaningless emojis"""
        actual = "🤖" * 100
        expected = "A lot of emojis"
        asserter.assert_semantic_match(actual, expected)