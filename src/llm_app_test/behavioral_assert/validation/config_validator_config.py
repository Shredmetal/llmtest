from dataclasses import dataclass
from typing import Optional, Set


@dataclass
class ConfigValidatorConfig:
    """Configuration data for validation"""
    api_key: Optional[str]
    provider: Optional[str]
    model: Optional[str]
    valid_models: Set[str]
    temperature: Optional[float]
    max_tokens: Optional[int]
    timeout: Optional[float]
