import os
from typing import Optional
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from llmtest.exceptions.test_exceptions import (
    SemanticAssertionError,
    catch_llm_errors,
    LLMConfigurationError
)


class SemanticAssertion:
    """Core class for semantic testing using LLMs"""

    def __init__(
            self,
            api_key: Optional[str] = None,
            llm=None,
            model: Optional[str] = None,
            temperature: Optional[float] = None
    ):
        """
        Initialize the semantic assertion tester.

        Args:
            api_key: OpenAI API key (optional if set in environment)
            llm: Optional pre-configured LLM
            model: Model to use (optional if set in environment)
            temperature: Temperature setting (optional if set in environment)

        Raises:
            LLMConfigurationError: If api_key cannot be found
        """
        # Load environment variables
        load_dotenv()

        # Get configuration from environment or parameters
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        self.model = model or os.getenv('OPENAI_MODEL', 'gpt-4o')
        self.temperature = float(temperature if temperature is not None
                                 else os.getenv('OPENAI_TEMPERATURE', '0.0'))

        if not self.api_key:
            raise LLMConfigurationError(
                "API key must be provided either through environment or constructor",
                reason="No API key specified"
            )

        self.llm = llm or ChatOpenAI(
            temperature=self.temperature,
            model=self.model,
            api_key=self.api_key,
            max_retries=2
        )

    @catch_llm_errors
    def assert_semantic_match(
            self,
            actual: str,
            expected_behavior: str
    ) -> None:
        """
            Assert that actual output semantically matches expected behavior

            Args:
                actual: The actual output to test
                expected_behavior: The expected behavior description

            Raises:
                TypeError: If inputs are None
                SemanticAssertionError: If outputs don't match semantically
                LLMConnectionError: If LLM service fails
                LLMConfigurationError: If LLM is not properly configured
            """
        if actual is None or expected_behavior is None:
            raise TypeError("Inputs cannot be None")

        system_prompt = """You are a testing system. Your job is to determine if an actual output matches the expected behavior.
        Respond with EXACTLY 'PASS' if it matches, or 'FAIL: <reason>' if it doesn't match.
        Be strict but consider semantic meaning rather than exact wording."""

        human_prompt = f"""
        Expected Behavior: {expected_behavior}

        Actual Output: {actual}

        Does the actual output match the expected behavior? Remember to respond with EXACTLY 'PASS' or 'FAIL: <reason>'."""

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=human_prompt)
        ]

        result = self.llm.invoke(messages).content

        if result.startswith("FAIL"):
            raise SemanticAssertionError(
                "Semantic assertion failed",
                reason=result.split("FAIL: ")[1]
            )
