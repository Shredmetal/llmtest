import os
from unittest.mock import patch
from langchain_openai import ChatOpenAI
from llm_app_test.semantic_assert.semantic_assert import SemanticAssertion


class TestSemanticAssertionLLMInjection:
    """Test suite for SemanticAssertion LLM injection"""

    @patch.dict(os.environ, {"OPENAI_API_KEY": "test_key"})
    def test_direct_llm_injection(self):
        """Test that directly injected LLM is used correctly"""
        # Create a real ChatOpenAI instance with test configs
        direct_llm = ChatOpenAI(
            model_name="gpt-4o",
            temperature=0.7,
            max_tokens=2000,
            max_retries=5,
            request_timeout=15.0
        )

        # Create asserter with the direct LLM
        asserter = SemanticAssertion(llm=direct_llm)

        # Verify the LLM instance is the same
        assert asserter.llm == direct_llm

        # Verify configurations match using the correct attribute names
        assert asserter.llm.model_name == "gpt-4o"
        assert asserter.llm.temperature == 0.7
        assert asserter.llm.max_tokens == 2000
        assert asserter.llm.max_retries == 5
        assert asserter.llm.request_timeout == 15.0

    @patch.dict(os.environ, {"OPENAI_API_KEY": "test_key"})
    def test_llm_injection_bypasses_config(self):
        """Test that injected LLM bypasses normal configuration"""
        direct_llm = ChatOpenAI()

        asserter = SemanticAssertion(
            llm=direct_llm,
            api_key="different_key",
            model="different_model",
            temperature=0.9
        )

        assert asserter.llm == direct_llm
