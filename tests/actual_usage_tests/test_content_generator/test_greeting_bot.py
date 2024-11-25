import os
from typing import Optional

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI


class SimpleApiCallBot:
    """A greeting bot that uses ChatOpenAI to generate personalized greetings."""

    def __init__(
            self,
            model: str = "gpt-4o",
            temperature: float = 0.0,
            api_key: Optional[str] = None,
            system_message: Optional[SystemMessage] = None
    ):
        """
        Initialize the greeting bot.

        Args:
            model: The OpenAI model to use
            temperature: Controls randomness in the output
            api_key: Optional API key (will use environment variable if not provided)
        """

        load_dotenv()

        self.llm = ChatOpenAI(
            model_name=model,
            temperature=temperature,
            openai_api_key=api_key or os.getenv("OPENAI_API_KEY"),
            max_retries=2
        )

        if not system_message:
            system_message = SystemMessage(
            content="""You are a friendly greeting bot. Your task is to generate 
            warm, personalized greetings. The greeting should:
            1. Use the person's name
            2. Be friendly and welcoming
            3. Include a question about their wellbeing
            4. Keep responses concise (max 2 sentences)"""
        )

        self.system_prompt = system_message

    def generate_ai_response(self, prompt: HumanMessage) -> str:
        """
        Generate a personalized greeting for the given name.

        Args: name: The name of the person to greet
        Returns: A personalized greeting string
        Raises: Exception: If the LLM call fails
        """
        try:

            response = self.llm.invoke([
                self.system_prompt,
                prompt
            ])

            return response.content

        except Exception as e:
            raise Exception(f"Failed to generate greeting: {str(e)}")
