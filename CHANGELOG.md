# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0b3] - 2024-12-19

### Added
- Support for Langchain's `with_retry` functionality
  - New `LANGCHAIN_WITH_RETRY` environment variable to enable/disable with_retry
  - New `ASSERTER_WAIT_EXPONENTIAL_JITTER` environment variable to configure exponential backoff with jitter
  - New `ASSERTER_STOP_AFTER_ATTEMPT` environment variable to set the number of retry attempts
- `WithRetryConfigValidator` class for validating with_retry configuration
- New `retry_config` attribute in `BehavioralAssertion` class to store validated retry configuration

### Changed
- Updated `BehavioralAssertion` class to incorporate `with_retry` functionality
- Improved error handling for retry configuration
- Enhanced test coverage to include `with_retry` functionality and its configuration
- Changed `llm` parameter in `BehavioralAssertion` to accept `Runnable` instead of `BaseLanguageModel` to prevent IDE warnings when passing in `ChatOpenAI().with_retry()`

### Fixed
- None

### Deprecated
- None

### Removed
- None

### Security
- None

This release introduces Langchain's `with_retry` functionality to improve resilience against API errors, particularly addressing issues encountered with ChatAnthropic. The new feature allows for more granular control over retry behavior and better handles transient errors like 529 responses. The `llm` parameter in `BehavioralAssertion` now explicitly accepts `Runnable` objects, which resolves IDE warnings when using methods like `with_retry()` on language models.


## [0.2.0b2] - 2024-12-15

### Added
- Rate limiting functionality for API requests
  - New `USE_RATE_LIMITER` environment variable to enable/disable rate limiting
  - New `RATE_LIMITER_REQUESTS_PER_SECOND` environment variable to set requests per second
  - New `RATE_LIMITER_CHECK_EVERY_N_SECONDS` environment variable to set check interval
  - New `RATE_LIMITER_MAX_BUCKET_SIZE` environment variable to set max bucket size
- `LLMInMemoryRateLimiter` class for handling rate limiting logic
- `RateLimiterInputsValidator` for validating rate limiter inputs
- Comprehensive test suite updates for environment variable handling
  - Tests for default values when environment variables are not set
  - Tests for overriding defaults with environment variables
  - Tests for priority of direct arguments over environment variables

### Changed
- Updated `BehavioralAssertion` class to incorporate rate limiting functionality
- Improved error handling for rate limiter configuration
- Enhanced test coverage to include edge cases in environment variable handling

### Fixed
- None

### Deprecated
- None

### Removed
- None

### Security
- None

This release focuses on introducing rate limiting capabilities to manage API request frequency and enhancing the robustness of environment variable handling. While no bugs were found in the existing environment variable logic, the new comprehensive test suite ensures the reliability of this critical functionality.


## [0.2.0b1] - 2024-11-29

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
1. Custom Prompt Configuration:
- New capability to override SystemMessage and HumanMessage
- Extra friction implemented through required `AsserterPrompts` object
- Marked as dangerous action in documentation

#### Configuration Updates
1. Added `LLM_TIMEOUT` environment variable:
- Sets `request_timeout` in default ChatOpenAI object
- Sets `default_request_timeout` in default ChatAnthropic object
- Can be passed directly to asserter as `timeout` argument
- Recommended to use environment variable instead of direct parameter
- Default is set to 60.0

### Summary
This release focuses on:
1. Better terminology (Semantic → Behavioral)
2. New configuration options
3. Custom prompt capabilities
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