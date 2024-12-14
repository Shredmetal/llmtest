import pytest

from llm_app_test.behavioral_assert.validation.rate_limiter_input_validator import RateLimiterInputsValidator


def generate_invalid_float_value_error(field_name: str, value: str):
    return f"Invalid {field_name} value for float conversion: {value}. Must be a valid non-negative float."

def generate_minimum_float_value_error_for_check_every_n_seconds(field_name: str, value: str):
    return f"Invalid value for {field_name}: {value}. Value for {field_name} must be at least 1.0."

def generate_negative_float_value_error(field_name: str, value: str):
    return f"Negative float value passed for {field_name}: {value}. Must be a valid non-negative float."

def generate_invalid_int_value_error(field_name: str, value: str):
    return f"Invalid {field_name} value for integer conversion: {value}. Must be a valid non-negative integer."

def generate_negative_int_value_error(field_name: str, value: str):
    return f"Negative integer value passed for {field_name}: {value}. Must be a valid non-negative integer."

def test_validate_requests_per_second_valid_values():
    assert RateLimiterInputsValidator.validate_requests_per_second("1e3") == 1000.0
    assert RateLimiterInputsValidator.validate_requests_per_second("3.14") == 3.14
    assert RateLimiterInputsValidator.validate_requests_per_second("1.4875") == 1.4875
    assert RateLimiterInputsValidator.validate_requests_per_second("1.0") == 1.0

def test_validate_requests_per_second_invalid_format():
    with pytest.raises(ValueError, match=generate_invalid_float_value_error("requests_per_second", "abc")):
        RateLimiterInputsValidator.validate_requests_per_second("abc")

    with pytest.raises(ValueError, match=generate_invalid_float_value_error("requests_per_second", "1..3")):
        RateLimiterInputsValidator.validate_requests_per_second("1..3")

    with pytest.raises(ValueError, match=generate_invalid_float_value_error("requests_per_second", "1e3.1")):
        RateLimiterInputsValidator.validate_requests_per_second("1e3.1")


def test_validate_requests_per_second_negative_value():
    with pytest.raises(ValueError, match=generate_minimum_float_value_error_for_check_every_n_seconds("requests_per_second", "-0.5")):
        RateLimiterInputsValidator.validate_requests_per_second("-0.5")
    with pytest.raises(ValueError, match=generate_minimum_float_value_error_for_check_every_n_seconds("requests_per_second", "0.99")):
        RateLimiterInputsValidator.validate_requests_per_second("0.99")


def test_validate_check_every_n_seconds_valid_values():
    assert RateLimiterInputsValidator.validate_check_every_n_seconds("1e-3") == 0.001
    assert RateLimiterInputsValidator.validate_check_every_n_seconds("2.5") == 2.5
    assert RateLimiterInputsValidator.validate_check_every_n_seconds("0") == 0.0


def test_validate_check_every_n_seconds_invalid_format():
    with pytest.raises(ValueError, match=generate_invalid_float_value_error("check_every_n_seconds", "abc")):
        RateLimiterInputsValidator.validate_check_every_n_seconds("abc")

    with pytest.raises(ValueError, match=generate_invalid_float_value_error("check_every_n_seconds", "1e--3")):
        RateLimiterInputsValidator.validate_check_every_n_seconds("1e--3")

    with pytest.raises(ValueError, match=generate_invalid_float_value_error("check_every_n_seconds", "1.2.3")):
        RateLimiterInputsValidator.validate_check_every_n_seconds("1.2.3")


def test_validate_check_every_n_seconds_value_less_than_1():
    with pytest.raises(ValueError, match=generate_negative_float_value_error("check_every_n_seconds", "-1.2")):
        RateLimiterInputsValidator.validate_check_every_n_seconds("-1.2")
    with pytest.raises(ValueError, match=generate_negative_float_value_error("check_every_n_seconds", "-0.99")):
        RateLimiterInputsValidator.validate_check_every_n_seconds("-0.99")
    with pytest.raises(ValueError, match=generate_negative_float_value_error("check_every_n_seconds", "-945.58")):
        RateLimiterInputsValidator.validate_check_every_n_seconds("-945.58")


def test_validate_max_bucket_size_valid_values():
    assert RateLimiterInputsValidator.validate_max_bucket_size("10") == 10
    assert RateLimiterInputsValidator.validate_max_bucket_size("0") == 0
    assert RateLimiterInputsValidator.validate_max_bucket_size("123456") == 123456


def test_validate_max_bucket_size_invalid_format():
    with pytest.raises(ValueError, match=generate_invalid_int_value_error("max_bucket_size", "abc")):
        RateLimiterInputsValidator.validate_max_bucket_size("abc")

    with pytest.raises(ValueError, match=generate_invalid_int_value_error("max_bucket_size", "1.5")):
        RateLimiterInputsValidator.validate_max_bucket_size("1.5")

    with pytest.raises(ValueError, match=generate_invalid_int_value_error("max_bucket_size", "1e3")):
        RateLimiterInputsValidator.validate_max_bucket_size("1e3")

    with pytest.raises(ValueError, match=generate_invalid_int_value_error("max_bucket_size", "123,456")):
        RateLimiterInputsValidator.validate_max_bucket_size("123,456")


def test_validate_max_bucket_size_negative_value():
    with pytest.raises(ValueError, match=generate_negative_int_value_error("max_bucket_size", "-10")):
        RateLimiterInputsValidator.validate_max_bucket_size("-10")