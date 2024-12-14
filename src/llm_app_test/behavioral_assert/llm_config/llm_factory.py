from typing import Optional

from langchain_anthropic import ChatAnthropic
from langchain_core.language_models import BaseLanguageModel
from langchain_core.rate_limiters import InMemoryRateLimiter
from langchain_openai import ChatOpenAI

from llm_app_test.behavioral_assert.llm_config.llm_config import LLMConfig
from llm_app_test.behavioral_assert.llm_config.llm_provider_enum import LLMProvider


class LLMFactory:
    """Factory class for creating LLM instances"""

    @staticmethod
    def create_llm(config: LLMConfig, rate_limiter: Optional[InMemoryRateLimiter] = None) -> BaseLanguageModel:
        """Create an LLM instance based on the provided configuration"""
        if config.provider == LLMProvider.OPENAI:
            return LLMFactory._create_openai_llm(config, rate_limiter)
        return LLMFactory._create_anthropic_llm(config, rate_limiter)

    @staticmethod
    def _create_openai_llm(config: LLMConfig, rate_limiter: Optional[InMemoryRateLimiter] = None) -> ChatOpenAI:
        """Create and configure OpenAI LLM instance"""
        return ChatOpenAI(
            temperature=config.temperature,
            model_name=config.model,
            openai_api_key=config.api_key,
            max_retries=config.max_retries,
            max_tokens=config.max_tokens,
            request_timeout=config.timeout,
            rate_limiter=rate_limiter
        )

    @staticmethod
    def _create_anthropic_llm(config: LLMConfig, rate_limiter: Optional[InMemoryRateLimiter] = None) -> ChatAnthropic:
        """Create and configure Anthropic LLM instance"""
        return ChatAnthropic(
            temperature=config.temperature,
            model=config.model,
            anthropic_api_key=config.api_key,
            max_retries=config.max_retries,
            max_tokens=config.max_tokens,
            default_request_timeout=config.timeout,
            rate_limiter=rate_limiter
        )
