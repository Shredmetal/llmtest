# Testing Patterns

This guide demonstrates common semantic testing patterns using llm-app-test. For API reference and syntax, see [API Documentation](api/semantic-assertion.md).

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
- Fails because the actual statement is about sky color
- Expected behavior asks for weather forecast information
- Demonstrates how semantic mismatches are caught
- Shows when assertions will fail in your tests
