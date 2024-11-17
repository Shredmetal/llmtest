# llm_app_test

[![Discord](https://img.shields.io/discord/1307634517766443058?logo=discord&logoColor=white)](https://discord.gg/awy83bZsKf)
![PyPI Version](https://img.shields.io/pypi/v/llm-app-test?label=pypi%20package)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)
[![Documentation](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://Shredmetal.github.io/llmtest/)


A semantic testing framework for LLM applications that uses LLMs to validate semantic equivalence in test outputs. 

✨ Test your LLM apps in minutes, not hours

🚀 CI/CD ready out of the box

💰 Cost-effective testing solution

🔧 No infrastructure needed

> ⚠️ **Note**: When using Anthropic as the provider, you may encounter rate limiting (401 errors) with large test suites. Consider adding delays between tests or using OpenAI for extensive testing. See documentation for details.

You can click [here](https://Shredmetal.github.io/llmtest/) to go straight to the docs.

## What llm_app_test Does
- Tests LLM applications (not the LLMs themselves)
- Validates system message + prompt template outputs
- Ensures semantic equivalence of responses
- Tests the parts YOU control in your LLM application

## What llm_app_test Doesn't Do
- Test LLM model performance (that's the provider's responsibility)
- Validate base model capabilities
- Test model reliability
- Handle model safety features

## Screenshots

What if you could just use:

```
semantic_assert.assert_semantic_match(
        actual=actual_output,
        expected_behavior=expected_behavior
    )
```
and get a pass/fail to test your LLM apps? Well, that's what I'm trying to do. Anyway, seeing is believing so:

Here's llm_app_test passing a test case:

![test_pass.jpg](test_pass.jpg)

Here's llm_app_test failing a test case (and providing the reason why it failed):

![test_fail.jpg](test_fail.jpg)

Finally, here's llm_app_test passing a test case with a complex reasoning chain with the simple, natural language 
instruction of:

```
A complex, multi-step, scientific explanation.
Must maintain logical consistency across all steps.
```

![complex_reasoning_chain_pass.jpg](complex_reasoning_chain_pass.jpg)

## Why llm_app_test?

Testing LLM applications is challenging because:
- Outputs are non-deterministic
- Semantic meaning matters more than exact matches
- Traditional testing approaches don't work well
- Integration into CI/CD pipelines is complex

llm_app_test solves these challenges by:
- Using LLMs to evaluate semantic equivalence
- Providing a clean, maintainable testing framework
- Offering simple CI/CD integration
- Supporting multiple LLM providers

## When to Use llm_app_test
- Testing application-level LLM integration
- Validating prompt engineering
- Testing system message effectiveness
- Ensuring consistent response patterns

## When Not to Use llm_app_test
- Testing base LLM performance
- Evaluating model capabilities
- Testing model safety features

## Quick Example

```
from llm_app_test.semanticassert.semantic_assert import SemanticAssertion

semantic_assert = SemanticAssertion() 
semantic_assert.assert_semantic_match(actual="Hello Alice, how are you?", 
                                      expected_behavior="A polite greeting addressing Alice" 
                                      )
```


## Installation

```
pip install llm-app-test
```


## Documentation

Full documentation available at: [https://Shredmetal.github.io/llmtest/](https://Shredmetal.github.io/llmtest/)

- Installation Guide
- Quick Start Guide
- API Reference
- Best Practices
- CI/CD Integration
- Configuration Options

## License

MIT

## Contributing

This project is at an early stage and aims to be an important testing library for LLM applications. 

Want to contribute? Great! Some areas we're looking for help:
- Additional LLM provider support
- Performance optimizations
- Test coverage improvements
- Documentation
- CI/CD integration examples
- Test result caching
- Literally anything else you can think of, I'm all out of ideas, I'm not even sure starting this project was a smart one.

Please:
1. Fork the repository
2. Create a feature branch
3. Submit a Pull Request

For major changes, please open an issue first to discuss what you would like to change, or YOLO in a PR, bonus points if you can insult me in a way that makes me laugh.

Please adhere to clean code principles and include appropriate tests... or else. 🗡️

## Contact

morganj.lee01@gmail.com