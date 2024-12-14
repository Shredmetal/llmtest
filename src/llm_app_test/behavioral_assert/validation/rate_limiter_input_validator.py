import re


class RateLimiterInputsValidator:
    """Validator for rate_limiter parameters"""

    @classmethod
    def validate_non_negative_float(cls, value: str, field_name: str) -> float:
        """
        Generic validator for non-negative floats, including scientific notation.
        """
        try:
            if isinstance(value, str):
            # Ensure the value is purely a float (no non-digit characters except - and .)
                if not re.match(r"^-?\d+(\.\d+)?([eE][+-]?\d+)?$", value.strip()):
                    raise ValueError(
                        f"Invalid {field_name} value for float conversion: {value}. Must be a valid non-negative float.")

            parsed_to_float_value = float(value)
            if field_name == "requests_per_second" and parsed_to_float_value < 1.0:
                raise ValueError(
                    f"Invalid value for requests_per_second: {value}. Value for requests_per_second must be at least 1.0.")
            if parsed_to_float_value < 0:
                raise ValueError(
                    f"Negative float value passed for {field_name}: {value}. Must be a valid non-negative float.")

            return parsed_to_float_value
        except ValueError as e:
            raise ValueError(str(e))

    @classmethod
    def validate_requests_per_second(cls, value: str) -> float:
        return cls.validate_non_negative_float(value, "requests_per_second")

    @classmethod
    def validate_check_every_n_seconds(cls, value: str) -> float:
        return cls.validate_non_negative_float(value, "check_every_n_seconds")

    @classmethod
    def validate_max_bucket_size(cls, value: str) -> int:
        try:
            if isinstance(value, str):
                # Ensure the value is purely an integer (no decimal points, e/E, or other non-digit characters except -)
                if not re.match(r"^-?\d+$", value.strip()):
                    raise ValueError(f"Invalid max_bucket_size value for integer conversion: {value}. Must be a valid non-negative integer.")

            parsed_to_int_value = int(value)
            if parsed_to_int_value < 0:
                raise ValueError(f"Negative integer value passed for max_bucket_size: {value}. Must be a valid non-negative integer.")

            return int(parsed_to_int_value)
        except ValueError as e:
            raise ValueError(str(e))