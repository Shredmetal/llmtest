import pytest
from llm_app_test.exceptions.test_exceptions import RetryConfigurationError
from llm_app_test.behavioral_assert.validation.with_retry_config_validator import WithRetryConfigValidator
from llm_app_test.with_retry.with_retry_config import WithRetryConfig


class TestWithRetryConfigValidator:
    """Tests for WithRetryConfigValidator class."""

    @pytest.mark.parametrize("retry_if_exception_type, wait_exponential_jitter, stop_after_attempt, expected", [
        ((ValueError, TypeError), "true", "3", WithRetryConfig((ValueError, TypeError), True, 3)),
        ((Exception,), "false", "5", WithRetryConfig((Exception,), False, 5)),
        ((), "true", "1", WithRetryConfig((), True, 1)),
    ])
    def test_validate_valid_inputs(self, retry_if_exception_type, wait_exponential_jitter, stop_after_attempt,
                                   expected):
        result = WithRetryConfigValidator.validate(retry_if_exception_type, wait_exponential_jitter, stop_after_attempt)
        assert isinstance(result, WithRetryConfig)
        assert result.retry_if_exception_type == expected.retry_if_exception_type
        assert result.wait_exponential_jitter == expected.wait_exponential_jitter
        assert result.stop_after_attempt == expected.stop_after_attempt

    @pytest.mark.parametrize("retry_if_exception_type, wait_exponential_jitter, stop_after_attempt", [
        ("not a tuple", "true", "3"),
        ((ValueError, "not an exception"), "true", "3"),
        ((ValueError,), "not a boolean", "3"),
        ((ValueError,), "true", "not an integer"),
        ((ValueError,), "true", "0"),
    ])
    def test_validate_invalid_inputs(self, retry_if_exception_type, wait_exponential_jitter, stop_after_attempt):
        with pytest.raises(RetryConfigurationError):
            WithRetryConfigValidator.validate(retry_if_exception_type, wait_exponential_jitter, stop_after_attempt)

    @pytest.mark.parametrize("retry_if_exception_type, expected", [
        ((ValueError, TypeError), (ValueError, TypeError)),
        ((), ()),
    ])
    def test_validate_retry_if_exception_type_valid(self, retry_if_exception_type, expected):
        """Test valid retry_if_exception_type inputs."""
        result = WithRetryConfigValidator._validate_retry_if_exception_type(retry_if_exception_type)
        assert result == expected

    @pytest.mark.parametrize("retry_if_exception_type", [
        1,
        (1, "not a type"),
        ((int, str), "not exception types"),
    ])
    def test_validate_retry_if_exception_type_invalid(self, retry_if_exception_type):
        """Test invalid retry_if_exception_type inputs."""
        with pytest.raises(RetryConfigurationError):
            WithRetryConfigValidator._validate_retry_if_exception_type(retry_if_exception_type)

    @pytest.mark.parametrize("wait_exponential_jitter, expected", [
        ("true", True),
        ("false", False),
        (True, True),
        (False, False),
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
        (1, 1),
        (10, 10),
    ])
    def test_validate_stop_after_attempt_valid(self, stop_after_attempt, expected):
        """Test valid stop_after_attempt inputs."""
        result = WithRetryConfigValidator._validate_stop_after_attempt(stop_after_attempt)
        assert result == expected

    @pytest.mark.parametrize("stop_after_attempt", [
        "string",
        0,
        -1,
        0.2
    ])
    def test_validate_stop_after_attempt_invalid(self, stop_after_attempt):
        """Test invalid stop_after_attempt inputs."""
        with pytest.raises(RetryConfigurationError):
            WithRetryConfigValidator._validate_stop_after_attempt(stop_after_attempt)
