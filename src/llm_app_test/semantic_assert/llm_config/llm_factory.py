from langchain_anthropic import ChatAnthropic
from langchain_core.language_models import BaseLanguageModel
from langchain_openai import ChatOpenAI

from llm_app_test.semantic_assert.llm_config.llm_config import LLMConfig
from llm_app_test.semantic_assert.llm_config.llm_provider_enum import LLMProvider


class LLMFactory:
    """Factory class for creating LLM instances"""

    @staticmethod
    def create_llm(config: LLMConfig) -> BaseLanguageModel:
        """Create an LLM instance based on the provided configuration"""
        if config.provider == LLMProvider.OPENAI:
            return LLMFactory._create_openai_llm(config)
        return LLMFactory._create_anthropic_llm(config)

    @staticmethod
    def _create_openai_llm(config: LLMConfig) -> ChatOpenAI:
        """Create and configure OpenAI LLM instance"""
        return ChatOpenAI(
            temperature=config.temperature,
            model=config.model,
            api_key=config.api_key,
            max_retries=config.max_retries,
            max_tokens=config.max_tokens,
            request_timeout=config.timeout
        )

    @staticmethod
    def _create_anthropic_llm(config: LLMConfig) -> ChatAnthropic:
        """Create and configure Anthropic LLM instance"""
        return ChatAnthropic(
            temperature=config.temperature,
            model=config.model,
            anthropic_api_key=config.api_key,
            max_retries=config.max_retries,
            max_tokens=config.max_tokens,
            request_timeout=config.timeout
        )
