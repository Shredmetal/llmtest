[← Back to Home](../index.md)

# Error Handling

llm-app-test provides specific exceptions for different error scenarios to help you handle errors gracefully in your tests.

## Exception Hierarchy

```
LLMAppTestError # Base exception for all llm-app-test errors 
├── BehavioralAssertionError # When behavioral matching fails 
├── LLMConfigurationError # When configuration is invalid 
└── LLMConnectionError # When LLM service fails 
```

## Exception Details

### BehavioralAssertionError
Raised when the behavioral assertion fails:

```
try:
    behavioral_assert.assert_behavioral_match(
        actual="Hello Bob", 
        expected_behavior="A greeting for Alice"
    ) 
except BehavioralAssertionError as e:
    print(f"Test failed: {e}") # Includes detailed reason why outputs don't match
```

### LLMConfigurationError
Raised when configuration is invalid:

```
try:
    behavioral_assert = BehavioralAssertion(provider="invalid_provider") 
except LLMConfigurationError as e:
    print(f"Configuration error: {e}") # Details about invalid configuration
```

### LLMConnectionError
Raised when LLM service fails:

```
try:
    behavioral_assert.assert_behavioral_match(...) 
except LLMConnectionError as e:
    print(f"Service error: {e}") # Contains original provider error details
```


## Error Information

All exceptions provide:

- Clear error message
- Detailed reason (when available)
- Additional context in details dictionary

Example:

```

try:
    behavioral_assert.assert_behavioral_match(...) 
except LLMAppTestError as e:
    print(f"Message: {e.message}")
    print(f"Reason: {e.reason}")
    print(f"Details: {e.details}")

```

## Best Practices

1. Always catch specific exceptions rather than the base LLMAppTestError
2. Log the full error information for debugging
3. Handle LLMConnectionError for retry logic
4. Use error details for test reporting

Note: All exceptions properly chain to their root cause, preserving the full error context.

## Navigation

- [Back to Home](../index.md)
- [Installation Guide](../getting-started/installation.md)
- [Quick Start Guide](../getting-started/quickstart.md)
- [API Reference](behavioral-assertion.md)