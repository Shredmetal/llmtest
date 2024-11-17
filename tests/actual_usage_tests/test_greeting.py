from llm_app_test.semantic_assert.semantic_assert import SemanticAssertion
from tests.test_content_generators.test_greeting_bot import SimpleGreetingBot


def test_greeting_semantic():

    semantic_assert = SemanticAssertion()

    bot = SimpleGreetingBot()

    actual_output = bot.generate_greeting("Alice")

    expected_behavior = """
    A polite greeting that:
    1. Addresses the person by name (Alice)
    2. Asks about their wellbeing
    """

    semantic_assert.assert_semantic_match(
        actual=actual_output,
        expected_behavior=expected_behavior
    )
