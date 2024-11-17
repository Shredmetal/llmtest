import os
import pytest
from llm_app_test.semantic_assert.semantic_assert import SemanticAssertion
from llm_app_test.exceptions.test_exceptions import (
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

    def test_unicode_mess(self, asserter):
        """Test handling of unicode chaos"""
        actual = "🤖👾" * 50 + "こんにちは" * 20 + "🌈" * 30
        expected = "A mix of emojis and Japanese text"
        asserter.assert_semantic_match(actual, expected)

    def test_mixed_language_emoji_spam(self, asserter):
        """Test handling of multilingual emoji spam"""
        actual = "Hello你好Bonjour🌈" * 50
        expected = "A repetitive greeting in multiple languages with rainbows"
        asserter.assert_semantic_match(actual, expected)

    def test_ascii_art(self, asserter):
        """Test handling of ASCII art"""
        actual = """
        (╯°□°)╯︵ ┻━┻
        """ * 20
        expected = "Multiple instances of table-flipping ASCII art"
        asserter.assert_semantic_match(actual, expected)

    def test_whitespace_madness(self, asserter):
        """Test handling of excessive whitespace"""
        actual = "hello    " + " " * 1000 + "    world" + "\n" * 500
        expected = "A greeting with excessive spacing"
        asserter.assert_semantic_match(actual, expected)

    def test_number_spam(self, asserter):
        """Test handling of number spam"""
        actual = "".join([str(i % 10) for i in range(1000)])
        expected = "A long sequence of repeating numbers"
        asserter.assert_semantic_match(actual, expected)