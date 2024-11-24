[← Back to Home](../index.md)

# Format Compliance - yes we are brute forcing it with thousands upon thousands of tests

This page documents the ongoing efforts to validate the reliability of llm-app-test.

There are two parts to ensure:

- ensure that there are no format violations; and
- ensure that llm-app-test maintains consistency in passing / failing the tests appropriately.

It also contains information on how much running thousands of tests cost us. Short answer: Very little, actually.

This is likely due to how we constrained the model: The temperature is set to 0.0, and it has strict instructions to only respond with "PASS" or "FAIL <reason>". This constrains the much more expensive output token usage.

Running the test suite of 13 tests below 100 times (so 1,300 tests), cost us a total of US$0.79, using OpenAI's GPT-4o.

Upon observing the cost of throwing thousands of API calls at OpenAI, we decided to just sod it and throw 13,000 API calls at them for the grand sum of... US$7.90. 

The purpose of these 13,000 runs was primarily to test the reliability of this library insofar as **format violations** were concerned, and get some insight as to the reliability of the semantic comparison.

Based on the testing documented in this page however, we are quite confident that llm-app-test will adhere to the format requirements in most situations and not throw stupid errors by failing to adhere to the requirements. Based on these results, we are also reasonably confident that it is adequate for semantic comparisons in most real world use cases.

However, in the interests of ensuring that all of us can trust this library (ourselves included), we are currently in the process of cooking up a new test suite of industry-specific inputs and expected behaviours to put through the wringer with another 1,000 runs of that suite.

Be that as it may, we are still relying on an LLM for behavioural testing of an app, so we would still recommend running the test suite that you write for your app using llm-app-test at least twice. It's not going to break the bank as long as you take advantage of the economy of scale of OpenAI's/Anthropic's datacenters.

## The actual tests

We used the test suite within our existing test package (as of 21 November 2024) which we felt most reflected what assert_semantic_match would have to deal with in the real world:

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

We ran this suite 1,000 times. 

At 13 tests (8 positive, 5 negative) per run, this worked out to 13,000 tests. 

We experienced a pass rate of 100%.

The test logs for the 13,000 tests can be found in the reliability_testing directory of the repository, currently in the [release/0.1.0b5](https://github.com/Shredmetal/llmtest/tree/release/0.1.0b5/reliability_testing) branch, which will move to main upon release of 0.1.0b5 on PyPI.

As mentioned previously, we remain unable to guarantee 100% reliability due to the nature of LLMs. 

However, our testing indicates that there is clear evidence indicating that assert_semantic_match is working as intended, we feel that it can be relied on for most real-world use cases by Software Engineers who need to validate their app behaviour (Data Scientists validating model performance, please do not use this library, you need to validate model performance not application behaviour, which requires skills software engineers like us may not have).

As stated previously, the total cost of running these 13,000 tests was US$7.90 using GPT-4o. This is an absolute pittance for the confidence value this provided to us in terms of trusting our own library, as well as the thought of OpenAI going "WHO THE HELL TURNED OUR LLM INTO A BINARY CLASSIFIER?!" 🤣.

## Model Configuration:

We used our library defaults:

```
DEFAULT_TEMPERATURE=0.0
DEFAULT_MAX_TOKENS=4096
DEFAULT_MAX_RETRIES=2
LLM_PROVIDER=opnenai
LLM_MODEL=gpt-4o
```

The asserter prompts were as follows:

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

For the purposes of this test, we added an additional error case in the asserter in order to catch any format violations:

```
result = self.llm.invoke(messages).content

        if result.startswith("FAIL"):
            raise SemanticAssertionError(
                "Semantic assertion failed",
                reason=result.split("FAIL: ")[1]
            )
        elif result.startswith("PASS"):
            pass
        else:
            raise SemanticAssertionError(
                "Format Violation Detected",
                reason=result
            )
```

## Next steps

We will move forward and develop 10 more test cases with the sort of long form content that is likely to be produced by LLM-based apps in real-world use by industry.

As always, if you experience any issues, especially with library reliability - please let us know, thanks!

## Quick Links
- [Installation](../getting-started/installation.md)
- [Quick Start](../getting-started/quickstart.md)
- [API Reference](../api/semantic-assertion.md)