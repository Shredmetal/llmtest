class LLMConstants:
    """Constants for LLM configuration"""
    DEFAULT_TEMPERATURE = 0.0
    DEFAULT_MAX_TOKENS = 4096
    DEFAULT_MAX_RETRIES = 2


class ModelConstants:
    """Constants for model configuration"""
    DEFAULT_OPENAI_MODEL = "gpt-4o"
    DEFAULT_ANTHROPIC_MODEL = "claude-3-5-sonnet-latest"

    OPENAI_MODELS = {"gpt-4o", "gpt-4-turbo"}
    ANTHROPIC_MODELS = {"claude-3-5-sonnet-latest", "claude-3-opus-latest"}