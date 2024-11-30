import pytest
from llm_app_test.behavioral_assert.asserter_prompts.asserter_prompt_configurator import AsserterPromptConfigurator
from llm_app_test.behavioral_assert.behavioral_assert import BehavioralAssertion
from llm_app_test.exceptions.test_exceptions import InvalidPromptError


class TestAsserterPromptConfigurator:
    """Test suite for AsserterPromptConfigurator"""

    def test_default_prompts(self):
        """Test that default prompts are set correctly"""
        configurator = AsserterPromptConfigurator()

        # Check system prompt
        assert configurator.prompts.system_prompt == AsserterPromptConfigurator.DEFAULT_SYSTEM_PROMPT

        # Check human prompt
        assert configurator.prompts.human_prompt == AsserterPromptConfigurator.DEFAULT_HUMAN_PROMPT

    def test_custom_prompts(self):
        """Test that custom prompts are set correctly"""
        custom_system = "Custom system prompt"
        custom_human = "Custom human prompt with {expected_behavior} and {actual}"

        configurator = AsserterPromptConfigurator(
            system_prompt=custom_system,
            human_prompt=custom_human
        )

        assert configurator.prompts.system_prompt == custom_system
        assert configurator.prompts.human_prompt == custom_human

    def test_invalid_human_prompt(self):
        """Test that invalid human prompt raises ValueError"""
        with pytest.raises(InvalidPromptError) as excinfo:
            AsserterPromptConfigurator(
                human_prompt="Invalid prompt without placeholders"
            )
        assert "must contain {expected_behavior} and {actual} placeholders" in str(excinfo.value)

    def test_prompt_configuration_in_behavioral_assertion(self):
        """Test that prompts are properly configured in BehavioralAssertion"""
        custom_system = "Custom system prompt"
        custom_human = "Custom human prompt with {expected_behavior} and {actual}"

        custom_prompts = AsserterPromptConfigurator(
            system_prompt=custom_system,
            human_prompt=custom_human
        )

        asserter = BehavioralAssertion(
            api_key="test_key",
            custom_prompts=custom_prompts
        )

        assert asserter.custom_prompts.prompts.system_prompt == custom_system
        assert asserter.custom_prompts.prompts.human_prompt == custom_human
