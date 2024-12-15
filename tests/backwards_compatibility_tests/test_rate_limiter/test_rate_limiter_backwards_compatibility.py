import os
from unittest.mock import patch

import pytest
from langchain_core.rate_limiters import InMemoryRateLimiter

from llm_app_test.semantic_assert.semantic_assert import SemanticAssertion

class TestRateLimiterBackwardsCompatibility:

    @pytest.fixture
    def mock_env_variables(self):
        with patch.dict(os.environ, {
            'RATE_LIMITER_REQUESTS_PER_SECOND': '5',
            'RATE_LIMITER_CHECK_EVERY_N_SECONDS': '2',
            'RATE_LIMITER_MAX_BUCKET_SIZE': '10',
            'OPENAI_API_KEY': 'test_openai_api_key',
            'ANTHROPIC_API_KEY': 'test_anthropic_api_key'
        }):
            yield


    def test_rate_limiter_disabled_by_default(self):
        asserter = SemanticAssertion()

        assert asserter.llm.rate_limiter is None

    def test_rate_limiter_disabled_by_default_in_anthropic(self):
        asserter = SemanticAssertion(provider="anthropic")

        assert asserter.llm.rate_limiter is None

    def test_rate_limiter_env_override_openai(self, mock_env_variables):
        asserter = SemanticAssertion(use_rate_limiter=True)
        expected_limiter = InMemoryRateLimiter(
            requests_per_second=5.0,
            check_every_n_seconds=2.0,
            max_bucket_size=10.0
        )

        actual_limiter = asserter.llm.rate_limiter
        assert actual_limiter.requests_per_second == expected_limiter.requests_per_second
        assert actual_limiter.check_every_n_seconds == expected_limiter.check_every_n_seconds
        assert actual_limiter.max_bucket_size == expected_limiter.max_bucket_size

    def test_rate_limiter_env_override_anthropic(self, mock_env_variables):
        asserter = SemanticAssertion(provider="anthropic", use_rate_limiter=True)

        expected_limiter = InMemoryRateLimiter(
            requests_per_second=5.0,
            check_every_n_seconds=2.0,
            max_bucket_size=10.0
        )

        actual_limiter = asserter.llm.rate_limiter
        assert actual_limiter.requests_per_second == expected_limiter.requests_per_second
        assert actual_limiter.check_every_n_seconds == expected_limiter.check_every_n_seconds
        assert actual_limiter.max_bucket_size == expected_limiter.max_bucket_size

    def test_rate_limiter_direct_override_openai(self, mock_env_variables):
        asserter = SemanticAssertion(use_rate_limiter=True,
                                     rate_limiter_requests_per_second=2.0,
                                     rate_limiter_check_every_n_seconds=4.0,
                                     rate_limiter_max_bucket_size=9.0)
        expected_limiter = InMemoryRateLimiter(
            requests_per_second=2.0,
            check_every_n_seconds=4.0,
            max_bucket_size=9.0
        )

        actual_limiter = asserter.llm.rate_limiter
        assert actual_limiter.requests_per_second == expected_limiter.requests_per_second
        assert actual_limiter.check_every_n_seconds == expected_limiter.check_every_n_seconds
        assert actual_limiter.max_bucket_size == expected_limiter.max_bucket_size

    def test_rate_limiter_direct_override_anthropic(self, mock_env_variables):

        asserter = SemanticAssertion(provider="anthropic",
                                     use_rate_limiter=True,
                                     rate_limiter_requests_per_second=2.0,
                                     rate_limiter_check_every_n_seconds=4.0,
                                     rate_limiter_max_bucket_size=9.0)

        expected_limiter = InMemoryRateLimiter(
            requests_per_second=2.0,
            check_every_n_seconds=4.0,
            max_bucket_size=9.0
        )

        actual_limiter = asserter.llm.rate_limiter
        assert actual_limiter.requests_per_second == expected_limiter.requests_per_second
        assert actual_limiter.check_every_n_seconds == expected_limiter.check_every_n_seconds
        assert actual_limiter.max_bucket_size == expected_limiter.max_bucket_size
