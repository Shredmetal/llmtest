import pytest
from langchain_core.messages import HumanMessage, SystemMessage

from llm_app_test.exceptions.test_exceptions import BehavioralAssertionError
from llm_app_test.behavioral_assert.behavioral_assert import BehavioralAssertion
from tests.actual_usage_tests.test_content_generator.test_greeting_bot import SimpleApiCallBot


def test_ww2_narrative():

    behavioral_assert = BehavioralAssertion()

    system_message = SystemMessage(
        """
        You are a historian bot and you will respond to specific requests for information about history.
        Be detailed but do not go beyond what was asked for.
        """
    )

    bot = SimpleApiCallBot(system_message=system_message)

    human_message = HumanMessage(
        content=f"Tell me about the European Theater of World War 2, the major battles, and how the European war ended"
    )

    actual_output = bot.generate_ai_response(human_message)

    print(actual_output)

    expected_behavior = """
    A narrative about World War 2 and the global nature of the war
    """

    with pytest.raises(BehavioralAssertionError) as excinfo:
        behavioral_assert.assert_behavioral_match(actual_output, expected_behavior)
    assert "Behavioral assertion failed" in str(excinfo.value)