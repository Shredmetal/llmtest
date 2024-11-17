[← Back to Home](../index.md)

# Error Handling

llm_app_test provides specific exceptions for different error scenarios to help you handle errors gracefully in your tests.

## Exception Hierarchy

```
LLMTestError # Base exception for all llm_app_test errors 
├── SemanticAssertionError # When semantic matching fails 
├── LLMConfigurationError # When configuration is invalid 
├── LLMConnectionError # When LLM service fails 
└── InvalidPromptError # When prompt construction fails - not currently in use, code left in situ for future development
```

## Exception Details

### SemanticAssertionError
Raised when the semantic assertion fails:

```
try: 
    semantic_assert.assert_semantic_match(actual="Hello Bob", 
                                          expected_behavior="A greeting for Alice") 
except SemanticAssertionError as e: 
    print(f"Test failed: {e}") # Includes detailed reason why outputs don't match
```

### LLMConfigurationError
Raised when configuration is invalid:

```
try: 
    semantic_assert = SemanticAssertion(provider="invalid_provider") 
except LLMConfigurationError as e: 
    print(f"Configuration error: {e}") # Details about invalid configuration
```

### LLMConnectionError
Raised when LLM service fails:

```
try: 
    semantic_assert.assert_semantic_match(...) 
except LLMConnectionError as e: 
    print(f"Service error: {e}") # Contains original provider error details
```


### InvalidPromptError (NOT CURRENTLY IN USE)
Raised when prompt construction fails:

```
try: semantic_assert.assert_semantic_match(actual=None, # Invalid input 
                                            expected_behavior="Some behavior") 
except InvalidPromptError as e: 
    print(f"Prompt error: {e}")
```


## Error Information

All exceptions should provide:
- Clear error message
- Detailed reason (when available)
- Additional context in details dictionary

Example:

```
try: 
    semantic_assert.assert_semantic_match(...) 
except LLMTestError as e: 
    print(f"Message: {e.message}") print(f"Reason: {e.reason}") print(f"Details: {e.details}")
```

## Best Practices

1. Always catch specific exceptions rather than the base LLMTestError
2. Log the full error information for debugging
3. Handle LLMConnectionError for retry logic
4. Use error details for test reporting

---

Note: All exceptions properly chain to their root cause, preserving the full error context.


## Navigation

- [Back to Home](../index.md)
- [Installation Guide](../getting-started/installation.md)
- [Quick Start Guide](../getting-started/quickstart.md)
- [API Reference](semantic-assertion.md)
