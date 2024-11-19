# Testing Patterns

This guide demonstrates common semantic testing patterns using llm-app-test. For API reference and syntax, see [API Documentation](../api/semantic-assertion.md).

## Pattern: Basic Semantic Equivalence

**Scenario:** Testing simple greeting behaviour

**Implementation:**

```
actual = "Hello Alice, how are you today?" 
 
expected_behavior = """ A polite greeting that:
    Addresses the person by name (Alice)
    Asks about their wellbeing """

semantic_assert.assert_semantic_match(actual, expected_behavior)
```

**Result:** ✅ PASS

- Recognises personal address
- Identifies greeting context
- Validates wellbeing inquiry

## Pattern: Basic Semantic Matching

**Scenario**: Testing simple factual statements

Implementation:

```
actual = "The sky is blue"

expected_behavior = "A statement about the color of the sky"

semantic_assert.assert_semantic_match(actual, expected_behavior)
```
**Result:** ✅ PASS

- Shows direct semantic matching
- Clear relationship between statement and expectation
- Passes when meaning aligns

## Pattern: Expected Semantic Mismatch

**Scenario**: Validating semantic mismatch detection

Implementation:

```
actual = "The sky is blue"

expected_behavior = "A statement about the weather forecast"

semantic_assert.assert_semantic_match(actual, expected_behavior)
```
Result: ❌ FAIL

- Fails because the actual statement is about sky colour
- Expected behaviour asks for weather forecast information
- Demonstrates how semantic mismatches are caught
- Shows when assertions will fail in your tests

## Pattern: Multilingual Semantic Testing

**Scenario**: Testing semantic understanding across languages

Implementation:

```
actual = "Bonjour, comment allez-vous?"

expected_behavior = "A polite greeting asking about wellbeing"

semantic_assert.assert_semantic_match(actual, expected_behavior)
```
Result: ✅ PASS

- Demonstrates language-agnostic understanding
- Shows cross-language semantic matching
- Validates international content handling

## Pattern: Technical Documentation Testing

**Scenario**: Testing technical concept explanations

Implementation:

```
actual = """The TCP handshake is a three-way process where the client 
         sends SYN, server responds with SYN-ACK, and client confirms with ACK"""
         
expected_behavior = "An explanation of the TCP connection establishment process"

semantic_assert.assert_semantic_match(actual, expected_behavior)
```
Result: ✅ PASS

- Validates technical accuracy
- Handles specialised terminology
- Maintains semantic precision

## Pattern: Contextual Disambiguation

**Scenario**: Testing understanding of ambiguous terms

Implementation:

```
actual = "The bank was steep and covered in wildflowers"

expected_behavior = "A description of a riverbank or hillside, not a financial institution"

semantic_assert.assert_semantic_match(actual, expected_behavior)
```
Result: ✅ PASS

- Shows contextual understanding
- Handles ambiguous terms
- Validates specific meaning exclusions

## Pattern: Sentiment Analysis

**Scenario**: Testing subtle emotional content

Implementation:

```
actual = "While the presentation wasn't perfect, it showed promise"

expected_behavior = "A constructive criticism with mixed but generally positive sentiment"

semantic_assert.assert_semantic_match(actual, expected_behavior)
```
Result: ✅ PASS

- Detects nuanced sentiment
- Understands mixed emotions
- Validates overall tone

## Pattern: Long-Form Content

**Scenario**: Testing comprehension of detailed explanations

Implementation:

```
actual = """Machine learning is a subset of artificial intelligence 
         that enables systems to learn and improve from experience without 
         explicit programming. It focuses on developing computer programs 
         that can access data and use it to learn for themselves."""
         
expected_behavior = "A comprehensive definition of machine learning emphasizing autonomous learning and data usage"

semantic_assert.assert_semantic_match(actual, expected_behavior)
```
Result: ✅ PASS

- Handles longer text
- Maintains context
- Captures key concepts

## Pattern: Subtle Sentiment Mismatch

**Scenario**: Testing detection of subtle sentiment differences

Implementation:

```
actual = "The project was completed on time, though there were some hiccups"

expected_behavior = "A statement expressing complete satisfaction with project execution"

semantic_assert.assert_semantic_match(actual, expected_behavior)
```
Result: ❌ FAIL

- Fails because actual statement indicates mixed satisfaction
- Expected behaviour suggests complete satisfaction
- Shows sensitivity to subtle emotional differences

## Pattern: Technical Context Mismatch

**Scenario**: Testing technical meaning precision

Implementation:

```
actual = "The function returns a pointer to the memory address"

expected_behavior = "A description of a function that returns the value stored at a memory location"

semantic_assert.assert_semantic_match(actual, expected_behavior)
```
Result: ❌ FAIL

- Fails because returning a pointer is different from returning a stored value
- Shows precision in technical context
- Validates technical accuracy

## Pattern: Ambiguous Reference Testing

**Scenario**: Testing handling of context-dependent terms

Implementation:

```
actual = "The bank processed the transaction after reviewing the account"

expected_behavior = "A description of a riverbank's geological formation process"

semantic_assert.assert_semantic_match(actual, expected_behavior)
```
Result: ❌ FAIL

- Fails because contexts are completely different
- Shows strong contextual understanding
- Validates semantic boundaries

## Pattern: Temporal Context

**Scenario**: Testing time-based semantic understanding

Implementation:

```
actual = "I will have completed the task by tomorrow"

expected_behavior = "A statement about a task that was completed in the past"

semantic_assert.assert_semantic_match(actual, expected_behavior)
```
Result: ❌ FAIL

- Fails because of tense mismatch
- Shows temporal awareness
- Validates time context

## Pattern: Logical Implication

**Scenario**: Testing logical relationship understanding

Implementation:

```
actual = "If it rains, the ground will be wet"

expected_behavior = "A statement indicating that wet ground always means it has rained"

semantic_assert.assert_semantic_match(actual, expected_behavior)
```
Result: ❌ FAIL

- Fails because of reversed logical implication
- Shows logical relationship understanding
- Validates causality direction

## Pattern: Multi-Step Reasoning

**Scenario**: Testing complex logical chains

Implementation:

```
actual = """When water freezes, it expands by approximately 9% in volume. 
This expansion creates less dense ice that floats according to Archimedes' principle of displacement. 
Because Arctic sea ice is already floating in the ocean, its melting doesn't significantly affect sea levels - 
it's already displacing its weight in water. However, land-based glaciers in places like Greenland 
aren't currently displacing any ocean water. When these glaciers melt, they add entirely new water volume 
to the oceans, making them a primary contributor to sea level rise."""

expected_behavior = """A multi-step scientific explanation.
Must maintain logical consistency across all steps."""

semantic_assert.assert_semantic_match(actual, expected_behavior)
```
Result: ✅ PASS

- Handles complex logical chains
- Maintains consistency across steps
- Validates scientific reasoning

## Pattern: Nonsensical Content

**Scenario**: Testing handling of grammatically correct but meaningless content

Implementation:

```
actual = "The colorless green ideas sleep furiously"

expected_behavior = "A grammatically correct but semantically nonsensical statement"

semantic_assert.assert_semantic_match(actual, expected_behavior)
```
Result: ✅ PASS

- Recognizes grammatical structure
- Identifies semantic nonsense
- Validates meta-understanding

## Pattern: Extended Narrative

**Scenario**: Testing long-form narrative understanding

Implementation:

```
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

expected_behavior = """A historical narrative that:
1. Maintains chronological progression
2. Shows cause-and-effect relationships
3. Develops consistent themes (power, governance, military)
4. Connects multiple historical events coherently
5. Demonstrates character development (e.g., Caesar to Augustus)
"""

semantic_assert.assert_semantic_match(actual, expected_behavior)

```
Result: ✅ PASS

- Handles extended narratives
- Maintains thematic consistency
- Validates complex relationships
- Shows chronological understanding

## Pattern: Emoji Quantity Testing

**Scenario**: Testing recognition of repeated emojis

Implementation:

```
actual = "🤖" * 100

expected_behavior = "A lot of emojis"

semantic_assert.assert_semantic_match(actual, expected_behavior)
```

Result: ✅ PASS

- Handles repeated Unicode characters
- Recognises quantity concepts
- Validates emoji processing

## Pattern: Emoji Quantity Mismatch

**Scenario**: Testing quantity recognition accuracy

Implementation:

```
actual = "🤖" * 100

expected_behavior = "Only a few emojis"

semantic_assert.assert_semantic_match(actual, expected_behavior)
```
Result: ❌ FAIL

- Fails due to quantity mismatch
- Shows quantity awareness
- Validates numerical understanding

## Pattern: Mixed Unicode Content ⚠️ Known Reliability Issue

**Scenario**: Testing complex Unicode combinations and repetitive patterns

### Observed Behavior

**Test Case 1: Strict Pattern Matching**

```
actual = "🤖👾" * 50 + "こんにちは" * 20 + "🌈" * 30

expected_behavior = "A mix of emojis and Japanese text"

semantic_assert.assert_semantic_match(actual, expected_behavior)
```

**Results**:
- ✅ Success Rate: 96% (48/50 runs)
- ❌ Failure Rate: 4% (2/50 runs)
- 🔍 Failure Analysis:
  - Occurs primarily during increased API latency
  - GPT-4o occasionally interprets sequential patterns as "distinct collections" rather than "mixed content"
  - Failure message example: "This is not a mix as there is a distinct collection of emojis followed by Japanese text and then a collection of rainbows"

### Recommended Implementation

**Test Case 2: Pattern-Agnostic Matching**

```
actual = "🤖👾" * 50 + "こんにちは" * 20 + "🌈" * 30

expected = "More than one type of emoji and Japanese text regardless of order"

asserter.assert_semantic_match(actual, expected)
```

**Results**:
- ✅ Success Rate: 100% (preliminary)
- ⚠️ Extended testing in progress
- 🔍 Monitoring prompt effectiveness across different test scenarios

### Best Practices
1. Use pattern-agnostic assertions for repetitive Unicode content
2. Consider implementing retry logic for critical tests
3. Monitor API response times during failures
4. Use enhanced prompts for complex Unicode pattern testing

### Ongoing Investigation
- Testing various prompt configurations to improve reliability
- Monitoring performance impact of different prompt strategies
- Collecting data on failure patterns with different prompt versions

## Pattern: Multilingual Emoji Spam

**Scenario**: Testing repeated multilingual content

Implementation:

```
actual = "Hello你好Bonjour🌈" * 50

expected_behavior = "A repetitive greeting in multiple languages with rainbows"

semantic_assert.assert_semantic_match(actual, expected_behavior)
```
Result: ✅ PASS

- Handles multilingual text
- Recognises repetitive patterns
- Validates mixed content types

## Pattern: ASCII Art Recognition

**Scenario**: Testing complex ASCII art patterns

Implementation:

```
actual = """
(╯°□°)╯︵ ┻━┻
""" * 20

expected_behavior = "Multiple instances of table-flipping ASCII art"

semantic_assert.assert_semantic_match(actual, expected_behavior)
```
Result: ✅ PASS

- Recognises ASCII art patterns
- Understands visual representations
- Validates repeated patterns

## Pattern: Extreme Whitespace

**Scenario**: Testing handling of excessive spacing

Implementation:

```
actual = "hello    " + " " * 1000 + "    world" + "\n" * 500

expected_behavior = "A greeting with excessive spacing"

semantic_assert.assert_semantic_match(actual, expected_behavior)
```
Result: ✅ PASS

- Handles extreme whitespace
- Maintains semantic meaning
- Validates text normalisation

## Pattern: Number Pattern Recognition

**Scenario**: Testing numerical pattern understanding

Implementation:

```
actual = "".join([str(i % 10) for i in range(1000)])

expected_behavior = "A long sequence of repeating numbers"

semantic_assert.assert_semantic_match(actual, expected_behavior)
```
Result: ✅ PASS

- Recognises numerical patterns
- Handles long repetitive sequences
- Validates pattern understanding
