import pytest
from llm_app_test.exceptions.test_exceptions import RateLimiterConfigurationError
from llm_app_test.behavioral_assert.validation.rate_limiter_input_validator import RateLimiterInputsValidator


class TestRateLimiterInputsValidator:
    """Tests for RateLimiterInputsValidator class."""

    @pytest.mark.parametrize("value, expected", [
        (1.0, 1.0),
        (5.0, 5.0),
        (100.0, 100.0),
        (1.5, 1.5)
    ])
    def test_validate_requests_per_second_valid_values(self, value: float, expected: float):
        """Test that valid requests_per_second values are accepted and returned unchanged."""
        result = RateLimiterInputsValidator.validate_requests_per_second(value)
        assert result == expected

    @pytest.mark.parametrize("invalid_value", [
        -1.0,
        -100.0
    ])
    def test_validate_requests_per_second_invalid_values(self, invalid_value: float):
        """Test that invalid requests_per_second values raise appropriate errors."""
        with pytest.raises(RateLimiterConfigurationError) as exc_info:
            RateLimiterInputsValidator.validate_requests_per_second(invalid_value)

        if invalid_value < 1.0:
            assert "must be a valid non-negative float" in str(exc_info.value)

    @pytest.mark.parametrize("value, expected", [
        (0.0, 0.0),
        (1.0, 1.0),
        (5.0, 5.0),
        (0.001, 0.001)
    ])
    def test_validate_check_every_n_seconds_valid_values(self, value: float, expected: float):
        """Test that valid check_every_n_seconds values are accepted and returned unchanged."""
        result = RateLimiterInputsValidator.validate_check_every_n_seconds(value)
        assert result == expected

    @pytest.mark.parametrize("invalid_value", [
        -0.1,
        -1.0,
        -100.0
    ])
    def test_validate_check_every_n_seconds_invalid_values(self, invalid_value: float):
        """Test that invalid check_every_n_seconds values raise appropriate errors."""
        with pytest.raises(RateLimiterConfigurationError) as exc_info:
            RateLimiterInputsValidator.validate_check_every_n_seconds(invalid_value)
        assert "must be a valid non-negative float" in str(exc_info.value)

    @pytest.mark.parametrize("value, expected", [
        (0.0, 0.0),
        (1.0, 1.0),
        (10.0, 10.0),
        (100.0, 100.0)
    ])
    def test_validate_max_bucket_size_valid_values(self, value: float, expected: float):
        """Test that valid max_bucket_size values are accepted and returned unchanged."""
        result = RateLimiterInputsValidator.validate_max_bucket_size(value)
        assert result == expected

    @pytest.mark.parametrize("invalid_value", [
        -0.1,
        -1.0,
        -100.0
    ])
    def test_validate_max_bucket_size_invalid_values(self, invalid_value: float):
        """Test that invalid max_bucket_size values raise appropriate errors."""
        with pytest.raises(RateLimiterConfigurationError) as exc_info:
            RateLimiterInputsValidator.validate_max_bucket_size(invalid_value)
        assert "must be a valid non-negative float" in str(exc_info.value)

    @pytest.mark.parametrize("string", [
        "hello",
        "zero point five",
        "float(1.0)"
    ])
    def test_validate_alphabetical_strings_always_fail(self, string: float):
        """Test that invalid alphabetical values always raise appropriate errors."""

        with pytest.raises(RateLimiterConfigurationError) as exc_info:
            RateLimiterInputsValidator.validate_max_bucket_size(string)
        assert "Conversion to float failed" in str(exc_info.value)

        with pytest.raises(RateLimiterConfigurationError) as exc_info:
            RateLimiterInputsValidator.validate_check_every_n_seconds(string)
        assert "Conversion to float failed" in str(exc_info.value)

        with pytest.raises(RateLimiterConfigurationError) as exc_info:
            RateLimiterInputsValidator.validate_requests_per_second(string)
        assert "Conversion to float failed" in str(exc_info.value)

    @pytest.mark.parametrize("data", [
        [0.1, 0.2, 0.3],
        ["zero point five"],
        {"one": 1, "two": 2, "three": 3}
    ])
    def test_validate_complex_types_always_fail(self, data: float):
        """Test that invalid data structures always raise appropriate errors."""

        with pytest.raises(RateLimiterConfigurationError) as exc_info:
            RateLimiterInputsValidator.validate_max_bucket_size(data)
        assert "Conversion to float failed" in str(exc_info.value)

        with pytest.raises(RateLimiterConfigurationError) as exc_info:
            RateLimiterInputsValidator.validate_check_every_n_seconds(data)
        assert "Conversion to float failed" in str(exc_info.value)

        with pytest.raises(RateLimiterConfigurationError) as exc_info:
            RateLimiterInputsValidator.validate_requests_per_second(data)
        assert "Conversion to float failed" in str(exc_info.value)