from typing import Optional

from llm_app_test.behavioral_assert.asserter_prompts.asserter_prompts import AsserterPrompts


class AsserterPromptConfigurator:
    """Manages prompts for behavioral assertion testing"""

    DEFAULT_SYSTEM_PROMPT = """You are a testing system. Your job is to determine if an actual output matches the expected behavior.

    Important: You can only respond with EXACTLY: 
    1. 'PASS' if it matches, or 
    2. 'FAIL: <reason>' if it doesn't match.

    Any other type of response will mean disaster which as a testing system, you are meant to prevent.

    Be strict but consider semantic meaning rather than exact wording."""

    DEFAULT_HUMAN_PROMPT = """
    Expected Behavior: {expected_behavior}

    Actual Output: {actual}

    Does the actual output match the expected behavior? Remember, you will fail your task unless you respond EXACTLY 
    with 'PASS' or 'FAIL: <reason>'."""

    def __init__(
            self,
            system_prompt: Optional[str] = None,
            human_prompt: Optional[str] = None
    ) -> None:
        """
        Initialise the prompt configurator with optional custom prompts.

        Args:
            system_prompt: Optional custom system prompt
            human_prompt: Optional custom human prompt. Must contain {expected_behavior} and {actual} placeholders

        Raises:
            ValueError: If human_prompt doesn't contain required placeholders
        """
        if human_prompt and ('{expected_behavior}' not in human_prompt or '{actual}' not in human_prompt):
            raise ValueError("Human prompt must contain {expected_behavior} and {actual} placeholders")

        self._prompts = AsserterPrompts(
            system_prompt=system_prompt or self.DEFAULT_SYSTEM_PROMPT,
            human_prompt=human_prompt or self.DEFAULT_HUMAN_PROMPT
        )

    @property
    def prompts(self) -> AsserterPrompts:
        """
        Returns the configured prompts.

        Returns:
            AsserterPrompts: Immutable dataclass containing the configured prompts
        """
        return self._prompts