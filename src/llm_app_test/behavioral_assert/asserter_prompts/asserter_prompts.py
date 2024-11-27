from dataclasses import dataclass

@dataclass(frozen=True)
class AsserterPrompts:
    """Holds the prompts used for semantic assertion testing"""
    system_prompt: str
    human_prompt: str
