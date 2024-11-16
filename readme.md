# llmtest

A semantic testing framework for LLM applications that uses LLMs to validate semantic equivalence in test outputs. 

✨ Test your LLM apps in minutes, not hours

🚀 CI/CD ready out of the box

💰 Cost-effective testing solution

🔧 No infrastructure needed

You can click [here](#documentation) to go straight to the docs.

## Why llmtest?

Testing LLM applications is challenging because:
- Outputs are non-deterministic
- Semantic meaning matters more than exact matches
- Traditional testing approaches don't work well
- Integration into CI/CD pipelines is complex

llmtest solves these challenges by:
- Using LLMs to evaluate semantic equivalence
- Providing a clean, maintainable testing framework
- Offering simple CI/CD integration
- Supporting multiple LLM providers

## Quick Example

```
from llmtest.semanticassert.semantic_assert import SemanticAssertion

semantic_assert = SemanticAssertion() 
semantic_assert.assert_semantic_match(actual="Hello Alice, how are you?", 
                                      expected_behavior="A polite greeting addressing Alice" 
                                      )
```


## Installation

```
pip install git+https://github.com/Shredmetal/llmtest.git
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

Please adhere to clean code principles and include appropriate tests.
