## Testing Hierarchy

We recommend a testing hierarchy for LLM applications:

1. **Behavioral Testing (llm-app-test)**

    - Validates if the LLM application is doing the RIGHT thing
    - Tests core functionality and behavior
    - Must pass before proceeding to benchmarking
    - Failure indicates fundamental problems with the application

2. **Benchmarking (much slower and much more expensive)**

    - Only run AFTER behavioral tests pass
    - Measures HOW WELL the application performs
    - Tests performance metrics
    - Used for optimization

> [!IMPORTANT]
> Always ensure behavioral tests pass before running benchmarks. 
> A failing behavioral test indicates your application is fundamentally 
> broken - no amount of performance optimization will fix incorrect behavior.

### Example Flow:

```
# 1. First, run behavioral tests
behavioral_asserter.assert_behavioral_match(result, "Expected behavior description")

# 2. Only if behavioral tests pass, run benchmarks
if behavioral_tests_pass: 
    run_performance_benchmarks()
```

This hierarchy ensures:

- Core functionality is correct before optimization
- Clear separation of behavior and performance testing
- Efficient use of compute resources and API calls
- Structured approach to LLM application testing

