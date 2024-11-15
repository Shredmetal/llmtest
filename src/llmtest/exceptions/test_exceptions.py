from functools import wraps
from typing import Callable, Any, Optional, Dict
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
            )
        except TypeError as e:
            raise
        except Exception as e:
            if isinstance(e, LLMTestError):
                raise
            raise LLMConnectionError(
                f"LLM operation failed in {func.__name__}",
                reason=str(e)
            )
    return wrapper


class LLMTestError(Exception):
    """Base exception class for all llmtest errors."""
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


class SemanticAssertionError(LLMTestError):
    """Raised when semantic assertion fails."""
    def __init__(self, message: str, reason: Optional[str] = None, details: Optional[Dict] = None):
        super().__init__(
            message=f"Semantic assertion failed: {message}",
            reason=reason,
            details=details
        )


class LLMConfigurationError(LLMTestError):
    """Raised when there are issues with LLM configuration."""
    def __init__(self, message: str, reason: Optional[str] = None, details: Optional[Dict] = None):
        super().__init__(
            message=f"LLM configuration error: {message}",
            reason=reason,
            details=details
        )


class LLMConnectionError(LLMTestError):
    """Raised when there are issues connecting to the LLM service."""
    def __init__(self, message: str, reason: Optional[str] = None, details: Optional[Dict] = None):
        super().__init__(
            message=f"LLM connection error: {message}",
            reason=reason,
            details=details
        )


class InvalidPromptError(LLMTestError):
    """Raised when prompt construction fails or is invalid."""
    def __init__(self, message: str, reason: Optional[str] = None, details: Optional[Dict] = None):
        super().__init__(
            message=f"Invalid prompt error: {message}",
            reason=reason,
            details=details
        )



