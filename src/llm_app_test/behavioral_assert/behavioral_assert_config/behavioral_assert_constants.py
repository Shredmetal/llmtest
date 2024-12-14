class LLMConstants:
    """Constants for LLM configuration"""
    DEFAULT_TEMPERATURE = 0.0
    DEFAULT_MAX_TOKENS = 4096
    DEFAULT_MAX_RETRIES = 2
    DEFAULT_TIMEOUT = 60.0


class ModelConstants:
    """Constants for model configuration"""
    DEFAULT_OPENAI_MODEL = "gpt-4o"
    DEFAULT_ANTHROPIC_MODEL = "claude-3-5-sonnet-latest"

    OPENAI_MODELS = {"gpt-4o", "gpt-4-turbo"}
    ANTHROPIC_MODELS = {"claude-3-5-sonnet-latest", "claude-3-opus-latest"}

class RateLimiterConstants:
    """Constants for rate limiter configuration"""
    REQUESTS_PER_SECOND = 1.0
    CHECK_EVERY_N_SECONDS = 0.1
    MAX_BUCKET_SIZE = 1