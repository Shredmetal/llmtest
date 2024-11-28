# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0b1] - 2024-11-30

#### Breaking Changes
1. Renamed base error class:
- Old: LLMTestError
- New: LLMAppTestError
- No impact on users as this is just a template class other errors inherit from

#### Deprecations
1. Deprecated `SemanticAssertion` in favor of `BehavioralAssertion`:
- Same underlying implementation
- Only terminology change
- Using `SemanticAssertion` will trigger deprecation warnings:
  - stderr prints
  - pytest warnings

#### New Features
1. Custom Prompt Injection:
- New capability to override SystemMessage and HumanMessage
- Extra friction implemented through required `AsserterPrompts` object
- Marked as dangerous action in documentation

#### Configuration Updates
1. Added `LLM_TIMEOUT` environment variable:
- Sets `request_timeout` in default ChatOpenAI object
- Sets `default_request_timeout` in default ChatAnthropic object
- Can be passed directly to asserter as `timeout` argument
- Recommended to use environment variable instead of direct parameter

### Summary
This release focuses on:
1. Better terminology (Semantic → Behavioral)
2. Advanced configuration options
3. Custom prompt capabilities (with safety guardrails)
4. Improved timeout handling


## [0.1.0b4] - 2024-11-18

### Added
- An enormous pile of new unit tests because I forgot to test stuff other than the semantic asserter
- Some documentation regarding API rate limits for both OpenAI and Anthropic
- Rollback instructions in documentation in case I mess this version up

### Changed
- Enhanced documentation with rate limit tables and recommendations
- Improved test organisation and structure

## [0.1.0b3.post3] - 2024-11-17

### Added
- Initial beta release
- Basic semantic assertion functionality
- Support for OpenAI and Anthropic LLMs

### Notes
- This version serves as the stable fallback version