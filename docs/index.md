# llm_app_test

[![Discord](https://img.shields.io/discord/1307634517766443058?logo=discord&logoColor=white)](https://discord.gg/awy83bZsKf)
[![PyPI Version](https://img.shields.io/pypi/v/llm-app-test?label=pypi%20package)](https://pypi.org/project/llm-app-test/)
![PyPI Downloads](https://img.shields.io/pypi/dm/llm-app-test)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)
[![Documentation](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://Shredmetal.github.io/llmtest/)

A unit testing framework for LLM applications that uses LLMs to validate semantic equivalence in test outputs with a syntax familiar to software engineers.

⚠️ Note on Reliability: While we cannot guarantee 100% reliability (due to the fundamental nature of LLMs), we took the test suite we had which most reflected real-world use and ran it 1,000 times with zero failures. However, past success doesn't guarantee future determinism - this is an unsolvable problem in LLM testing, but we've implemented extensive mitigations to make it as reliable as possible. We are still in the process of validating reliability through brute force testing. Please refer to [this page](development/reliability-testing.md).

✨ Test your LLM apps in minutes, not hours

🚀 CI/CD ready out of the box (Still in beta so, while we're pretty sure it just works™, we're still trying our damnedest to break it in GitHub Actions, GitLab CI, Jenkins, and other CI/CD environments. We'll document any failures we find and their fixes)

💰 Cost-effective testing solution

🔧 No infrastructure needed (Unless if you want to inject a custom LLM, please refer to the configuration page for details)

## Testing Philosophy

When integrating LLMs into your application, treat them as you would any closed-source third-party library:

1. Write tests for expected behaviour
2. Focus on interface boundaries
3. Test application-level functionality
4. Maintain clear separation of concerns

### ⚠️ Important Information on Understanding Responsibilities

This library is built by software engineers give software engineers a tool to validate the behaviour of applications that have had an LLM stuffed in them. It is **NOT** a Data Science tool nor a replacement for model metrics used by Data Science teams to validate model suitability.

#### Software Engineer's Role

- Write tests for expected application behaviour
- Validate inputs and outputs
- Ensure proper integration
- Monitor system performance
- Escalate consistent failures to DS team (as this might indicate a fundamental problem with the model, or perhaps to seek assistance with the `expected_behavior` prompt in the `assert_semantic_match` function)

#### Data Science Team's Role

- Handle model-level issues
- Address consistent test failures
- Evaluate model suitability
- Optimise model performance
- Adjust prompts when needed

### When to Escalate

Escalate to your Data Science team when:

1. Tests consistently fail despite correct implementation
2. Model responses are consistently inappropriate
3. Performance degradation is observed
4. Pattern of failures indicates model-level issues

### 🔍 What Makes This Different?

This is an ENGINEERING tool, not a data science tool. The difference is crucial:

Data Science Tools:
- Test model performance
- Evaluate model accuracy
- Measure model metrics

llm_app_test (Engineering Tool):
- Tests your APPLICATION code
- Validates integration points
- Ensures system behaviour
- Maintains production reliability

Think of it this way: You don't test Redis itself, you test your application's use of Redis. 
Similarly, llm_app_test helps you test your application's use of LLMs.


## In summary:

### What llm_app_test Does

- Tests LLM applications (not the LLMs themselves)
- Validates system message + prompt template outputs
- Ensures semantic equivalence of responses
- Tests the parts YOU control in your LLM application

### What llm_app_test Doesn't Do

- Test LLM model performance (that's the provider's responsibility)
- Validate base model capabilities
- Test model reliability
- Handle model safety features

## When to Use llm_app_test

- Testing application-level LLM integration
- Validating prompt engineering
- Testing system message effectiveness
- Ensuring consistent response patterns

## When Not to Use llm_app_test

- Testing base LLM performance
- Evaluating model capabilities
- Testing model safety features

## Need testing ideas? Check out the tests we used to test llm-app-test [here](https://github.com/Shredmetal/llmtest/tree/main/tests)

## Quick Links
- [Installation](getting-started/installation.md)
- [Quick Start](getting-started/quickstart.md)
- [CI/CD Integration](guides/ci-cd.md)
- [Best Practices](guides/best-practices.md)
- [API Reference](api/semantic-assertion.md)

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Shredmetal/llmtest/blob/main/LICENSE) file for details.

## Reporting Issues

If you encounter issues:

1. Create an issue on our GitHub repository
2. Include your Python version and environment details
3. Describe the problem you encountered with version 0.1.0b4

## 🆘 Support

- Discord: [Join our community](https://discord.gg/awy83bZsKf)
- Issues: [GitHub Issues](https://github.com/Shredmetal/llmtest/issues)
- Documentation: [Full Docs](https://shredmetal.github.io/llmtest/)
- Email: morganj.lee01@gmail.com

## Due to the number of downloads I am seeing on pypistats.org, I am including these instructions in case a beta update breaks something on your end:

### Emergency Rollback Instructions

If you experience issues with version 0.1.0b4, you can roll back to the previous stable version (0.1.0b3.post3) using one of these methods:

#### Method 1: Direct Installation of Previous Version

```
pip uninstall llm-app-test 
pip install llm-app-test==0.1.0b3.post3
```
#### Method 2: Force Reinstall (if Method 1 fails)

```
pip install --force-reinstall llm-app-test==0.1.0b3.post3
```
#### Verification
After rolling back, verify the installation:
```
import llm_app_test 
print(llm_app_test.version) # Should show 0.1.0b3.post3
```

## ⚠️ Important Note About Rate Limits - If Running Large Numbers of Tests:

### Anthropic Rate limits:

Tier 1:

| Model                        | Maximum Requests per minute (RPM) | Maximum Tokens per minute (TPM) | Maximum Tokens per day (TPD) |
|------------------------------|-----------------------------------|---------------------------------|------------------------------|
| Claude 3.5 Sonnet 2024-10-22 | 50                                | 40,000                          | 1,000,000                    |
| Claude 3.5 Sonnet 2024-06-20 | 50                                | 40,000                          | 1,000,000                    |
| Claude 3 Opus                | 50                                | 20,000                          | 1,000,000                    |


Tier 2:

| Model                        | Maximum Requests per minute (RPM) | Maximum Tokens per minute (TPM) | Maximum Tokens per day (TPD) |
|------------------------------|-----------------------------------|---------------------------------|------------------------------|
| Claude 3.5 Sonnet 2024-10-22 | 1,000                             | 80,000                          | 2,500,000                    |
| Claude 3.5 Sonnet 2024-06-20 | 1,000                             | 80,000                          | 2,500,000                    |
| Claude 3 Opus                | 1,000                             | 40,000                          | 2,500,000                    |

### OpenAI Rate Limits

Tier 1

| Model                   | RPM | RPD    | TPM     | Batch Queue Limit |
|-------------------------|-----|--------|---------|-------------------|
| gpt-4o                  | 500 | -      | 30,000  | 90,000            |
| gpt-4o-mini             | 500 | 10,000 | 200,000 | 2,000,000         |
| gpt-4o-realtime-preview | 100 | 100    | 20,000  | -                 |
| gpt-4-turbo             | 500 | -      | 30,000  | 90,000            |


Tier 2:

| Model                   | RPM   | TPM       | Batch Queue Limit |
|-------------------------|-------|-----------|-------------------|
| gpt-4o                  | 5,000 | 450,000   | 1,350,000         |
| gpt-4o-mini             | 5,000 | 2,000,000 | 20,000,000        |
| gpt-4o-realtime-preview | 200   | 40,000    | -                 |
| gpt-4-turbo             | 5,000 | 450,000   | 1,350,000         |
