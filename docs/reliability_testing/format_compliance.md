[← Back to Home](../index.md)

# Format Compliance - Brute Force Validation of Format Compliance

## Overview

This page documents our extensive format compliance testing of llm-app-test. We designed these tests to validate the library's ability to maintain consistent format requirements across diverse use cases.

The test suite demonstrated 100% reliability across 13,000 test executions, with zero format violations detected.

The relevant logs can be found [here](https://github.com/Shredmetal/llmtest/tree/release/0.1.0b5/reliability_testing).

## Test Suite Design

The test suite covers 13 distinct test cases:

- 8 positive test cases
- 5 negative test cases

Each test validates different aspects of format compliance across various content types:

1. Multilingual equivalence
2. Complex technical explanations
3. Contextual understanding
4. Complex sentiment analysis
5. Long-form comparisons
6. Subtle sentiment matching
7. Technical context validation
8. Ambiguous reference handling
9. Temporal context verification
10. Logical implication testing
11. Complex multi-hop reasoning
12. Adversarial content handling
13. Long context understanding

## Test Characteristics

Each test was designed to validate:

- Format compliance
- Response structure
- Error handling
- Edge cases
- Content variations

## Test Results

### Format Compliance

- Zero format violations across 13,000 executions
- Consistent PASS/FAIL behavior
- Proper error handling for negative cases

### Response Reliability

- Consistent format across all test types
- Proper error message formatting
- Stable behavior across multiple runs

## Cost Analysis

Running 13,000 tests using GPT-4o cost approximately US$7.90, demonstrating the economic viability of comprehensive format testing even with large test suites.

## Test Configuration

All tests used library defaults:


```
LLM_PROVIDER=openai
LLM_MODEL=gpt-4o 
LLM_TEMPERATURE=0.0 
LLM_MAX_TOKENS=4096 
LLM_MAX_RETRIES=2 
LLM_TIMEOUT=10.0 # Added for OpenAI in 0.1.0b5 using the underlying Langchain implementation 
```
The `semantic_assert_match` function also saw slight modification:

```
        if result.startswith("FAIL"):
            raise SemanticAssertionError(
                "Semantic assertion failed",
                reason=result.split("FAIL: ")[1]
            )
            
        # Section below added to cause failure in the event of format violation    
            
        elif result.startswith("PASS"):
            pass
        else:
            raise RuntimeError(
                f"Format Non-compliance Detected {result}"
            )
```

The prompts to the asserter LLM (that sits behind `semantic_assert_match`) were:

```
DEFAULT_SYSTEM_PROMPT = """You are a testing system. Your job is to determine if an actual output matches the expected behavior.

Important: You can only respond with EXACTLY: 
1. 'PASS' if it matches, or 
2. 'FAIL: <reason>' if it doesn't match.

Any other type of response will mean disaster which as a testing system, you are meant to prevent.

Be strict but consider semantic meaning rather than exact wording."""

DEFAULT_HUMAN_PROMPT = """
Expected Behavior: {expected_behavior}

Actual Output: {actual}

Does the actual output match the expected behavior? Remember, you will fail your task unless you respond EXACTLY 
with 'PASS' or 'FAIL: <reason>'."""
```

## Testing Cost

It actually cost us very little.

This is likely due to how we constrained the model: The temperature is set to 0.0, and it has strict instructions to only respond with "PASS" or "FAIL <reason>". This constrains the much more expensive output token usage.

Running the test suite of 13 tests below 100 times (so 1,300 tests), cost us a total of US$0.79, using OpenAI's GPT-4o.

Upon observing the cost of throwing thousands of API calls at OpenAI, we decided to just sod it and throw 13,000 API calls at them for the grand sum of... US$7.90. 

The purpose of these 13,000 runs was primarily to test the reliability of this library insofar as **format violations** were concerned, and get some insight as to the reliability of the semantic comparison.

Based on the testing documented in this page however, we are quite confident that llm-app-test will adhere to the format requirements in most situations and not throw stupid errors by failing to adhere to the requirements. 

Please refer to the other pages of testing reliability, specifically [Semantic Reliability Testing](semantic_reliability.md) and [Semantic Boundary Analysis](semantic_boundary_analysis.md) for more information on reliability testing of the ability of this library to test for semantic equivalence.



## Test Suite

We used the following test suite for the purposes of format compliance testing:

```
import os
import pytest
from llm_app_test.semantic_assert.semantic_assert import SemanticAssertion
from llm_app_test.exceptions.test_exceptions import (
    SemanticAssertionError
)


class TestComplexSemanticAssertion:
    @pytest.fixture
    def asserter(self):
        return SemanticAssertion()

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

    def test_complex_multi_hop_reasoning(self, asserter):
        """Test complex multi-hop reasoning chains"""
        actual = """When water freezes, it expands by approximately 9% in volume. 
        This expansion creates less dense ice that floats according to Archimedes' principle of displacement. 
        Because Arctic sea ice is already floating in the ocean, its melting doesn't significantly affect sea levels - 
        it's already displacing its weight in water. However, land-based glaciers in places like Greenland 
        aren't currently displacing any ocean water. When these glaciers melt, they add entirely new water volume 
        to the oceans, making them a primary contributor to sea level rise."""

        expected = """A multi-step scientific explanation.
        Must maintain logical consistency across all steps."""
        asserter.assert_semantic_match(actual, expected)

    def test_adversarial_content(self, asserter):
        """Test handling of deliberately ambiguous or contradictory content"""
        actual = "The colorless green ideas sleep furiously"
        expected = "A grammatically correct but semantically nonsensical statement"
        asserter.assert_semantic_match(actual, expected)

    def test_long_context_understanding(self, asserter):
        """Test understanding of long, interconnected narratives"""
        actual = """
        The Roman Empire's rise began with modest origins in central Italy. What started as a small 
        settlement along the Tiber River would eventually become one of history's most influential 
        civilizations. In the early days, Rome was ruled by kings, but this system was overthrown 
        in 509 BCE, giving birth to the Roman Republic.

        During the Republic, Rome expanded its territory through military conquest and diplomatic 
        alliances. The Roman army became increasingly professional, developing innovative tactics 
        and technologies. This military success brought wealth and power, but also internal 
        challenges. Social tensions grew between patricians and plebeians, leading to significant 
        political reforms.

        By the 1st century BCE, the Republic faced severe internal strife. Military commanders 
        like Marius, Sulla, and eventually Julius Caesar accumulated unprecedented power. Caesar's 
        crossing of the Rubicon in 49 BCE marked a point of no return. His assassination in 44 BCE 
        led to another civil war, ultimately resulting in his adopted heir Octavian becoming 
        Augustus, the first Roman Emperor.

        Augustus transformed Rome into an empire while maintaining a facade of republican 
        institutions. He implemented sweeping reforms in administration, military organization, 
        and public works. The Pax Romana that followed brought unprecedented peace and prosperity 
        across the Mediterranean world. Trade flourished, cities grew, and Roman culture spread 
        throughout the empire.
        """
        expected = """A historical narrative that:
        1. Maintains chronological progression
        2. Shows cause-and-effect relationships
        3. Develops consistent themes (power, governance, military)
        4. Connects multiple historical events coherently
        5. Demonstrates character development (e.g., Caesar to Augustus)
        """
        asserter.assert_semantic_match(actual, expected)

```

## Issue reporting

If you experience any issues, especially with library reliability - please let us know, thanks!

## Quick Links
- [Installation](../getting-started/installation.md)
- [Quick Start](../getting-started/quickstart.md)
- [API Reference](../api/semantic-assertion.md)