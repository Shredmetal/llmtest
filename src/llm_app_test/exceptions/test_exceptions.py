from functools import wraps
from typing import Callable, Any, Optional, Dict
from anthropic import APIError
from openai import OpenAIError


def catch_llm_errors(func: Callable) -> Callable:
    """Decorator to catch and handle LLM-related errors."""
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        try:
            return func(*args, **kwargs)
        except OpenAIError as e:
            raise LLMConnectionError(
                "OpenAI API error occurred",
                reason=str(e)
            ) from e
        except APIError as e:
            raise LLMConnectionError(
                "Anthropic API error occurred",
                reason=str(e)
            ) from e
        except TypeError as e:
            raise
        except Exception as e:
            if isinstance(e, LLMAppTestError):
                raise
            raise LLMConnectionError(
                f"LLM operation failed in {func.__name__}",
                reason=str(e)
            ) from e
    return wrapper


class LLMAppTestError(Exception):
    """Base exception class for all llm_app_test errors."""
    def __init__(
        self,
        message: str,
        reason: Optional[str] = None,
        details: Optional[dict] = None  # Added details
    ):
        self.message = message
        self.reason = reason
        self.details = details or {}
        super().__init__(self.message)

    def __str__(self) -> str:
        base_message = self.message
        if self.reason:
            base_message += f" - Reason: {self.reason}"
        if self.details:
            base_message += f" - Details: {self.details}"
        return base_message


class BehavioralAssertionError(LLMAppTestError):
    """Raised when semantic assertion fails."""
    def __init__(self, message: str, reason: Optional[str] = None, details: Optional[Dict] = None):
        super().__init__(
            message=f"Behavioral assertion failed: {message}",
            reason=reason,
            details=details
        )


class LLMConfigurationError(LLMAppTestError):
    """Raised when there are issues with LLM configuration."""
    def __init__(self, message: str, reason: Optional[str] = None, details: Optional[Dict] = None):
        super().__init__(
            message=f"LLM configuration error: {message}",
            reason=reason,
            details=details
        )


class LLMConnectionError(LLMAppTestError):
    """Raised when there are issues connecting to the LLM service."""
    def __init__(self, message: str, reason: Optional[str] = None, details: Optional[Dict] = None):
        super().__init__(
            message=f"LLM connection error: {message}",
            reason=reason,
            details=details
        )


class InvalidPromptError(LLMAppTestError):
    """Raised when prompt construction fails or is invalid."""
    def __init__(self, message: str, reason: Optional[str] = None, details: Optional[Dict] = None):
        super().__init__(
            message=f"Invalid prompt error: {message}",
            reason=reason,
            details=details
        )



