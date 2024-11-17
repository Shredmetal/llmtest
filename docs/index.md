# llm_app_test

A semantic testing framework for LLM applications that uses LLMs to validate semantic equivalence in test outputs. 

✨ Test your LLM apps in minutes, not hours

🚀 CI/CD ready out of the box

💰 Cost-effective testing solution

🔧 No infrastructure needed

## ⚠️ Important Note About Anthropic API

When running multiple tests in parallel with the Anthropic provider, you may encounter rate limiting issues (401 errors). This is due to Anthropic's rate limits:

- 50 requests per minute (RPM)
- 40,000 tokens per minute (TPM) for Claude 3.5 Sonnet
- 1,000,000 tokens per day (TPD)

### Recommendations
1. Add delays between tests when using Anthropic
2. Consider using OpenAI for large test suites
3. Split test suites into smaller batches

We are working on implementing rate limiting handlers in future releases. For now, if you encounter 401 errors with Anthropic:
- Add delays between tests
- Reduce parallel test execution
- Switch to OpenAI for large test suites

## Current Version: 0.1.0b3post3

## Need testing ideas? Check out the tests we used to test llm-app-test [here](https://github.com/Shredmetal/llmtest/tree/main/tests)

## What llm_test Does
- Tests LLM applications (not the LLMs themselves)
- Validates system message + prompt template outputs
- Ensures semantic equivalence of responses
- Tests the parts YOU control in your LLM application

## What llm_test Doesn't Do
- Test LLM model performance (that's the provider's responsibility)
- Validate base model capabilities
- Test model reliability
- Handle model safety features

## When to Use llm_test
- Testing application-level LLM integration
- Validating prompt engineering
- Testing system message effectiveness
- Ensuring consistent response patterns

## When Not to Use llm_test
- Testing base LLM performance
- Evaluating model capabilities
- Testing model safety features

## Quick Links
- [Installation](getting-started/installation.md)
- [Quick Start](getting-started/quickstart.md)
- [API Reference](api/semantic-assertion.md)

## Documentation

- [Installation](getting-started/installation.md)
- [Quick Start](getting-started/quickstart.md)
- [CI/CD Integration](guides/ci-cd.md)
- [Best Practices](guides/best-practices.md)
- [API Reference](api/semantic-assertion.md)

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Shredmetal/llmtest/blob/main/LICENSE) file for details.
