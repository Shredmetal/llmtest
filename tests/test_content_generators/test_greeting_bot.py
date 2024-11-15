import os
from typing import Optional

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI


class SimpleGreetingBot:
    """A greeting bot that uses ChatOpenAI to generate personalized greetings."""

    def __init__(
            self,
            model: str = "gpt-3.5-turbo",
            temperature: float = 0.0,
            api_key: Optional[str] = None
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
            model=model,
            temperature=temperature,
            api_key=api_key or os.getenv("OPENAI_API_KEY"),
            max_retries=2
        )

        self.system_prompt = SystemMessage(
            content="""You are a friendly greeting bot. Your task is to generate 
            warm, personalized greetings. The greeting should:
            1. Use the person's name
            2. Be friendly and welcoming
            3. Include a question about their wellbeing
            4. Keep responses concise (max 2 sentences)"""
        )

    def generate_greeting(self, name: str) -> str:
        """
        Generate a personalized greeting for the given name.

        Args: name: The name of the person to greet
        Returns: A personalized greeting string
        Raises: Exception: If the LLM call fails
        """
        try:
            human_message = HumanMessage(
                content=f"Generate a greeting for {name}"
            )

            response = self.llm.invoke([
                self.system_prompt,
                human_message
            ])

            return response.content

        except Exception as e:
            raise Exception(f"Failed to generate greeting: {str(e)}")
