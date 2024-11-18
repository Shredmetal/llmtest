from llm_app_test.semantic_assert.llm_config.llm_provider_enum import LLMProvider


class TestLLMProvider:
    def test_provider_values(self):
        """Test LLMProvider enum values"""
        assert LLMProvider.OPENAI.value == "openai"
        assert LLMProvider.ANTHROPIC.value == "anthropic"

    def test_provider_comparison(self):
        """Test LLMProvider comparison"""
        assert LLMProvider.OPENAI == LLMProvider.OPENAI
        assert LLMProvider.ANTHROPIC == LLMProvider.ANTHROPIC
        assert LLMProvider.OPENAI != LLMProvider.ANTHROPIC