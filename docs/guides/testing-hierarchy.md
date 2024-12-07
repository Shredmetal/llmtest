## Testing Hierarchy

llm-app-test is designed to complement existing approaches. We recommend this testing hierarchy:

1. **Behavioral Testing (llm-app-test)**

    - Fast, cost-effective first line of testing
    - Validates IF your LLM application is even working as intended
    - Tests core functionality and behavior
    - Must pass before proceeding to benchmarking
    - Failure indicates fundamental problems with the application

2. **Benchmarking and Performance Evaluation**

    - Much slower and more expensive
    - Only run AFTER behavioral tests pass
    - Measures HOW WELL the application performs (in our view, this blurs the lines into LLM evaluation but it should still be done, just not as the first line of defence against broken apps due to the time and cost required)
    - Tests performance metrics, response quality
    - Used for optimization and model selection

> [!IMPORTANT]
> Always ensure behavioral tests pass before running benchmarks. 
> A failing behavioral test indicates your application is fundamentally 
> broken - no amount of performance optimization will fix incorrect behavior.

### Example Flow:

![Testing Hierarchy](https://i.imgur.com/TFPJa9M.png "LLM Application Testing Flow")

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

