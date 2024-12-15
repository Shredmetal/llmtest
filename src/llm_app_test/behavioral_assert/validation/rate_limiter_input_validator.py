from llm_app_test.exceptions.test_exceptions import RateLimiterConfigurationError


class RateLimiterInputsValidator:
    """Validator for rate_limiter parameters"""

    @classmethod
    def validate_non_negative_float(cls, value: float, field_name: str) -> float:
        """
        Generic validator for non-negative floats.
        """
        if field_name == "requests_per_second" and value < 1.0:
            raise RateLimiterConfigurationError(
                message=f"Invalid value for requests_per_second: {value}.",
                reason="Value for requests_per_second must be at least 1.0.")
        if value < 0:
            raise RateLimiterConfigurationError(
                message=f"Negative float value passed for {field_name}: {value}. ",
                reason=f"{field_name} Must be a valid non-negative float.")

        return value

    @classmethod
    def validate_requests_per_second(cls, value: float) -> float:
        return cls.validate_non_negative_float(value, "requests_per_second")

    @classmethod
    def validate_check_every_n_seconds(cls, value: float) -> float:
        return cls.validate_non_negative_float(value, "check_every_n_seconds")

    @classmethod
    def validate_max_bucket_size(cls, value: float) -> float:
        return cls.validate_non_negative_float(value, "max_bucket_size")
