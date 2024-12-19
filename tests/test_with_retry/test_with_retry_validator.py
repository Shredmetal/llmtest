import pytest
from llm_app_test.exceptions.test_exceptions import RetryConfigurationError
from llm_app_test.behavioral_assert.validation.with_retry_config_validator import WithRetryConfigValidator


class TestWithRetryConfigValidator:
    """Tests for WithRetryConfigValidator class."""

    @pytest.mark.parametrize("retry_if_exception_type, expected", [
        ((ValueError, TypeError), (ValueError, TypeError)),
        ((), ()),
    ])
    def test_validate_retry_if_exception_type_valid(self, retry_if_exception_type, expected):
        """Test valid retry_if_exception_type inputs."""
        result = WithRetryConfigValidator._validate_retry_if_exception_type(retry_if_exception_type)
        assert result == expected

    @pytest.mark.parametrize("retry_if_exception_type", [
        (1, "not a tuple"),
        ((int, str), "not exception types"),
    ])
    def test_validate_retry_if_exception_type_invalid(self, retry_if_exception_type):
        """Test invalid retry_if_exception_type inputs."""
        with pytest.raises(RetryConfigurationError):
            WithRetryConfigValidator._validate_retry_if_exception_type(retry_if_exception_type)

    @pytest.mark.parametrize("wait_exponential_jitter, expected", [
        ("true", True),
        ("false", False),
    ])
    def test_validate_wait_exponential_jitter_valid(self, wait_exponential_jitter, expected):
        """Test valid wait_exponential_jitter inputs."""
        result = WithRetryConfigValidator._validate_wait_exponential_jitter(wait_exponential_jitter)
        assert result == expected

    @pytest.mark.parametrize("wait_exponential_jitter", [
        ("yes", "invalid string"),
        ("no", "invalid string"),
    ])
    def test_validate_wait_exponential_jitter_invalid(self, wait_exponential_jitter):
        """Test invalid wait_exponential_jitter inputs."""
        with pytest.raises(RetryConfigurationError):
            WithRetryConfigValidator._validate_wait_exponential_jitter(wait_exponential_jitter)

    @pytest.mark.parametrize("stop_after_attempt, expected", [
        ("1", 1),
        ("10", 10),
    ])
    def test_validate_stop_after_attempt_valid(self, stop_after_attempt, expected):
        """Test valid stop_after_attempt inputs."""
        result = WithRetryConfigValidator._validate_stop_after_attempt(stop_after_attempt)
        assert result == expected

    @pytest.mark.parametrize("stop_after_attempt", [
        ("0", "non-positive integer"),
        ("-1", "negative integer"),
        ("abc", "non-integer string"),
    ])
    def test_validate_stop_after_attempt_invalid(self, stop_after_attempt):
        """Test invalid stop_after_attempt inputs."""
        with pytest.raises(RetryConfigurationError):
            WithRetryConfigValidator._validate_stop_after_attempt(stop_after_attempt)
