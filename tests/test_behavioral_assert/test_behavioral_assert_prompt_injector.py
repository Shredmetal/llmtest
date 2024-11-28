import pytest
from llm_app_test.behavioral_assert.asserter_prompts.asserter_prompt_injector import AsserterPromptInjector
from llm_app_test.behavioral_assert.behavioral_assert import BehavioralAssertion


class TestAsserterPromptInjector:
    """Test suite for AsserterPromptInjector"""

    def test_default_prompts(self):
        """Test that default prompts are set correctly"""
        injector = AsserterPromptInjector()

        # Check system prompt
        assert injector.prompts.system_prompt == AsserterPromptInjector.DEFAULT_SYSTEM_PROMPT

        # Check human prompt
        assert injector.prompts.human_prompt == AsserterPromptInjector.DEFAULT_HUMAN_PROMPT

    def test_custom_prompts(self):
        """Test that custom prompts are set correctly"""
        custom_system = "Custom system prompt"
        custom_human = "Custom human prompt with {expected_behavior} and {actual}"

        injector = AsserterPromptInjector(
            system_prompt=custom_system,
            human_prompt=custom_human
        )

        assert injector.prompts.system_prompt == custom_system
        assert injector.prompts.human_prompt == custom_human

    def test_invalid_human_prompt(self):
        """Test that invalid human prompt raises ValueError"""
        with pytest.raises(ValueError) as excinfo:
            AsserterPromptInjector(
                human_prompt="Invalid prompt without placeholders"
            )
        assert "must contain {expected_behavior} and {actual} placeholders" in str(excinfo.value)

    def test_prompt_injection_in_semantic_assertion(self):
        """Test that prompts are properly injected into BehavioralAssertion"""
        custom_system = "Custom system prompt"
        custom_human = "Custom human prompt with {expected_behavior} and {actual}"

        custom_prompts = AsserterPromptInjector(
            system_prompt=custom_system,
            human_prompt=custom_human
        )

        asserter = BehavioralAssertion(
            api_key="test_key",
            prompt_injector=custom_prompts
        )

        assert asserter.prompt_injector.prompts.system_prompt == custom_system
        assert asserter.prompt_injector.prompts.human_prompt == custom_human
