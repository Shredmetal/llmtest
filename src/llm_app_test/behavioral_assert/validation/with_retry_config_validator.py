from typing import Optional, Tuple, Type

from llm_app_test.exceptions.test_exceptions import RetryConfigurationError
from llm_app_test.with_retry.with_retry_config import WithRetryConfig


class WithRetryConfigValidator:

    @staticmethod
    def validate(config: WithRetryConfig):
        WithRetryConfigValidator._validate_retry_if_exception_type(config.retry_if_exception_type)
        WithRetryConfigValidator._validate_wait_exponential_jitter(config.wait_exponential_jitter)
        WithRetryConfigValidator._validate_stop_after_attempt(config.stop_after_attempt)
        return config

    @staticmethod
    def _validate_retry_if_exception_type(retry_if_exception_type: Optional[Tuple[Type[BaseException], ...]]):
        if retry_if_exception_type is not None:
            if not isinstance(retry_if_exception_type, tuple):
                raise RetryConfigurationError(
                    message="retry_if_exception_type must be a tuple of exception types",
                    reason=f"retry_if_exception_type received {retry_if_exception_type}"
                )
            for exc in retry_if_exception_type:
                if not issubclass(exc, BaseException):
                    raise RetryConfigurationError(
                        message="All elements in retry_if_exception_type must be subclasses of BaseException",
                        reason=f"Invalid exception type: {exc}"
                    )

    @staticmethod
    def _validate_wait_exponential_jitter(wait_exponential_jitter: Optional[bool]):
        if wait_exponential_jitter is not None and not isinstance(wait_exponential_jitter, bool):
            raise RetryConfigurationError(
                message="wait_exponential_jitter must be a boolean",
                reason=f"wait_exponential_jitter received {wait_exponential_jitter}"
            )

    @staticmethod
    def _validate_stop_after_attempt(stop_after_attempt: Optional[int]):
        if stop_after_attempt is not None and (not isinstance(stop_after_attempt, int) or stop_after_attempt <= 0):
            raise RetryConfigurationError(
                message="stop_after_attempt must be an integer",
                reason=f"stop_after_attempt received {stop_after_attempt}"
            )