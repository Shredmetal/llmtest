from llm_app_test.exceptions.test_exceptions import InvalidPromptError


class AssertBehavioralMatchValidator:
    """Validator for assert_behavioral_match inputs"""

    @staticmethod
    def validate(actual, expected_behavior):
        """Validates that both actual and expected_behavior are non-None strings.

            Args:
                actual: The actual output to validate
                expected_behavior: The expected behavior to validate against

            Raises:
                InvalidPromptError: If either input is None or not a string
            """
        AssertBehavioralMatchValidator._validate_actual(actual)
        AssertBehavioralMatchValidator._validate_expected_behavior(expected_behavior)

    @staticmethod
    def _validate_actual(actual):
        if actual is None:
            raise InvalidPromptError(
                f"Invalid actual argument: {actual}'",
                reason="actual must be a string and cannot be None")
        if not isinstance(actual, str):
            raise InvalidPromptError(
                f"Invalid actual argument: {actual}'",
                reason=f"actual must be a string, got {type(actual).__name__}")

    @staticmethod
    def _validate_expected_behavior(expected_behavior):
        if expected_behavior is None:
            raise InvalidPromptError(
                f"Invalid expected_behavior argument: {expected_behavior}'",
                reason="expected_behavior must be a string and cannot be None")
        if not isinstance(expected_behavior, str):
            raise InvalidPromptError(
                f"Invalid expected_behavior argument: {expected_behavior}'",
                reason=f"expected_behavior must be a string, got {type(expected_behavior).__name__}")
