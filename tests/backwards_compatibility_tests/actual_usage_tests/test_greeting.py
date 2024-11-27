from langchain_core.messages import HumanMessage

from llm_app_test.semantic_assert.semantic_assert import SemanticAssertion
from tests.backwards_compatibility_tests.actual_usage_tests.test_content_generator.test_greeting_bot import SimpleApiCallBot


def test_greeting_semantic():

    semantic_assert = SemanticAssertion()

    bot = SimpleApiCallBot()

    human_message = HumanMessage(
        content=f"Generate a greeting for Alice"
    )

    actual_output = bot.generate_ai_response(human_message)

    print(actual_output)

    expected_behavior = """
    A polite greeting that:
    1. Addresses the person by name (Alice)
    2. Asks about their wellbeing
    """

    semantic_assert.assert_semantic_match(
        actual=actual_output,
        expected_behavior=expected_behavior
    )
