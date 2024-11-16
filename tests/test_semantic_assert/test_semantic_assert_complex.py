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

    def test_multilingual_equivalence(self, asserter):
        """Test semantic matching across different languages"""
        actual = "Bonjour, comment allez-vous?"
        expected = "A polite greeting asking about wellbeing"
        asserter.assert_semantic_match(actual, expected)

    def test_complex_technical_explanation(self, asserter):
        """Test matching of technical explanations"""
        actual = """The TCP handshake is a three-way process where the client 
                 sends SYN, server responds with SYN-ACK, and client confirms with ACK"""
        expected = "An explanation of the TCP connection establishment process"
        asserter.assert_semantic_match(actual, expected)

    def test_contextual_understanding(self, asserter):
        """Test understanding of context-dependent statements"""
        actual = "The bank was steep and covered in wildflowers"
        expected = "A description of a riverbank or hillside, not a financial institution"
        asserter.assert_semantic_match(actual, expected)

    def test_complex_sentiment_analysis(self, asserter):
        """Test understanding of subtle emotional content"""
        actual = "While the presentation wasn't perfect, it showed promise"
        expected = "A constructive criticism with mixed but generally positive sentiment"
        asserter.assert_semantic_match(actual, expected)

    def test_long_form_comparison(self, asserter):
        """Test handling of longer text passages"""
        actual = """Machine learning is a subset of artificial intelligence 
                 that enables systems to learn and improve from experience without 
                 explicit programming. It focuses on developing computer programs 
                 that can access data and use it to learn for themselves."""
        expected = "A comprehensive definition of machine learning emphasizing autonomous learning and data usage"
        asserter.assert_semantic_match(actual, expected)

    def test_subtle_sentiment_mismatch(self, asserter):
        """Test mismatch in subtle sentiment differences"""
        actual = "The project was completed on time, though there were some hiccups"
        expected = "A statement expressing complete satisfaction with project execution"
        with pytest.raises(SemanticAssertionError) as excinfo:
            asserter.assert_semantic_match(actual, expected)
        assert "Semantic assertion failed" in str(excinfo.value)

    def test_technical_context_mismatch(self, asserter):
        """Test mismatch in technical context interpretation"""
        actual = "The function returns a pointer to the memory address"
        expected = "A description of a function that returns the value stored at a memory location"
        with pytest.raises(SemanticAssertionError) as excinfo:
            asserter.assert_semantic_match(actual, expected)
        assert "Semantic assertion failed" in str(excinfo.value)

    def test_ambiguous_reference_mismatch(self, asserter):
        """Test mismatch in ambiguous references"""
        actual = "The bank processed the transaction after reviewing the account"
        expected = "A description of a riverbank's geological formation process"
        with pytest.raises(SemanticAssertionError) as excinfo:
            asserter.assert_semantic_match(actual, expected)
        assert "Semantic assertion failed" in str(excinfo.value)

    def test_temporal_context_mismatch(self, asserter):
        """Test mismatch in temporal context"""
        actual = "I will have completed the task by tomorrow"
        expected = "A statement about a task that was completed in the past"
        with pytest.raises(SemanticAssertionError) as excinfo:
            asserter.assert_semantic_match(actual, expected)
        assert "Semantic assertion failed" in str(excinfo.value)

    def test_logical_implication_mismatch(self, asserter):
        """Test mismatch in logical implications"""
        actual = "If it rains, the ground will be wet"
        expected = "A statement indicating that wet ground always means it has rained"
        with pytest.raises(SemanticAssertionError) as excinfo:
            asserter.assert_semantic_match(actual, expected)
        assert "Semantic assertion failed" in str(excinfo.value)