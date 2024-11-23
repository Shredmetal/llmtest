from dataclasses import dataclass
from typing import Optional

from llm_app_test.semantic_assert.llm_config.llm_provider_enum import LLMProvider


@dataclass
class LLMConfig:
    provider: LLMProvider
    api_key: Optional[str] = None
    model: Optional[str] = None
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None
    max_retries: Optional[int] = None
    timeout: Optional[float] = None