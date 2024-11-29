import pytest
from llm_app_test.behavioral_assert.asserter_prompts.asserter_prompt_configurator import AsserterPromptConfigurator
from llm_app_test.semantic_assert.semantic_assert import SemanticAssertion


class TestAsserterPromptInjector:
    """Test suite for AsserterPromptConfigurator"""

    def test_default_prompts(self):
        """Test that default prompts are set correctly"""
        injector = AsserterPromptConfigurator()

        # Check system prompt
        assert injector.prompts.system_prompt == AsserterPromptConfigurator.DEFAULT_SYSTEM_PROMPT

        # Check human prompt
        assert injector.prompts.human_prompt == AsserterPromptConfigurator.DEFAULT_HUMAN_PROMPT

    def test_custom_prompts(self):
        """Test that custom prompts are set correctly"""
        custom_system = "Custom system prompt"
        custom_human = "Custom human prompt with {expected_behavior} and {actual}"

        injector = AsserterPromptConfigurator(
            system_prompt=custom_system,
            human_prompt=custom_human
        )

        assert injector.prompts.system_prompt == custom_system
        assert injector.prompts.human_prompt == custom_human

    def test_invalid_human_prompt(self):
        """Test that invalid human prompt raises ValueError"""
        with pytest.raises(ValueError) as excinfo:
            AsserterPromptConfigurator(
                human_prompt="Invalid prompt without placeholders"
            )
        assert "must contain {expected_behavior} and {actual} placeholders" in str(excinfo.value)

    def test_prompt_configuration_in_semantic_assertion(self):
        """Test that prompts are properly injected into SemanticAssertion"""
        custom_system = "Custom system prompt"
        custom_human = "Custom human prompt with {expected_behavior} and {actual}"

        custom_prompts = AsserterPromptConfigurator(
            system_prompt=custom_system,
            human_prompt=custom_human
        )

        asserter = SemanticAssertion(
            api_key="test_key",
            prompt_injector=custom_prompts
        )

        assert asserter.prompt_injector.prompts.system_prompt == custom_system
        assert asserter.prompt_injector.prompts.human_prompt == custom_human
