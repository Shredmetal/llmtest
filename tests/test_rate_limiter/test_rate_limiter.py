import os
from unittest.mock import patch, MagicMock

import pytest
from langchain_core.rate_limiters import InMemoryRateLimiter

from llm_app_test.behavioral_assert.behavioral_assert import BehavioralAssertion
from llm_app_test.behavioral_assert.behavioral_assert_config.behavioral_assert_constants import RateLimiterConstants
from llm_app_test.behavioral_assert.validation.rate_limiter_input_validator import RateLimiterInputsValidator
from llm_app_test.rate_limiter.rate_limiter_handler import LLMInMemoryRateLimiter

class TestRateLimiter:

    @pytest.fixture
    def mock_env_variables(self):
        with patch.dict(os.environ, {
            'RATE_LIMITER_REQUESTS_PER_SECOND': '5',
            'RATE_LIMITER_CHECK_EVERY_N_SECONDS': '2',
            'RATE_LIMITER_MAX_BUCKET_SIZE': '10'
        }):
            yield

    def test_initialization_with_env_variables(self, mock_env_variables):
        with patch.object(RateLimiterInputsValidator, 'validate_requests_per_second', return_value=5.0) as mock_rps, \
                patch.object(RateLimiterInputsValidator, 'validate_check_every_n_seconds',
                             return_value=2.0) as mock_check, \
                patch.object(RateLimiterInputsValidator, 'validate_max_bucket_size', return_value=10.0) as mock_max:

            rate_limiter = LLMInMemoryRateLimiter()

            assert rate_limiter.requests_per_second == 5.0
            assert rate_limiter.check_every_n_seconds == 2.0
            assert rate_limiter.max_bucket_size == 10.0

            mock_rps.assert_called_once_with(5.0)
            mock_check.assert_called_once_with(2.0)
            mock_max.assert_called_once_with(10.0)

    def test_default_values_when_env_variables_missing(self):

        with patch.object(RateLimiterInputsValidator, 'validate_requests_per_second',
                          return_value=RateLimiterConstants.REQUESTS_PER_SECOND) as mock_rps, \
                patch.object(RateLimiterInputsValidator, 'validate_check_every_n_seconds',
                             return_value=RateLimiterConstants.CHECK_EVERY_N_SECONDS) as mock_check, \
                patch.object(RateLimiterInputsValidator, 'validate_max_bucket_size',
                             return_value=RateLimiterConstants.MAX_BUCKET_SIZE) as mock_max:
            rate_limiter = LLMInMemoryRateLimiter()

            assert rate_limiter.requests_per_second == RateLimiterConstants.REQUESTS_PER_SECOND
            assert rate_limiter.check_every_n_seconds == RateLimiterConstants.CHECK_EVERY_N_SECONDS
            assert rate_limiter.max_bucket_size == RateLimiterConstants.MAX_BUCKET_SIZE

            mock_rps.assert_called_once_with(RateLimiterConstants.REQUESTS_PER_SECOND)
            mock_check.assert_called_once_with(RateLimiterConstants.CHECK_EVERY_N_SECONDS)
            mock_max.assert_called_once_with(RateLimiterConstants.MAX_BUCKET_SIZE)

    def test_get_rate_limiter_with_limiter_enabled(self, mock_env_variables):
        rate_limiter = LLMInMemoryRateLimiter()
        with patch('llm_app_test.rate_limiter.rate_limiter_handler.InMemoryRateLimiter', return_value=MagicMock()) as mock_rate_limiter:
            limiter = rate_limiter.get_rate_limiter
            mock_rate_limiter.assert_called_once_with(
                requests_per_second=rate_limiter.requests_per_second,
                check_every_n_seconds=rate_limiter.check_every_n_seconds,
                max_bucket_size=rate_limiter.max_bucket_size
            )
            assert limiter is not None


    def test_rate_limiter_disabled_by_default(self):
        asserter = BehavioralAssertion()

        assert asserter.llm.rate_limiter is None

    def test_rate_limiter_disabled_by_default_in_anthropic(self):
        asserter = BehavioralAssertion(provider="anthropic")

        assert asserter.llm.rate_limiter is None

    def test_rate_limiter_env_override_openai(self, mock_env_variables):
        asserter = BehavioralAssertion(use_rate_limiter=True)
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
        asserter = BehavioralAssertion(provider="anthropic", use_rate_limiter=True)

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
        asserter = BehavioralAssertion(use_rate_limiter=True,
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
        asserter = BehavioralAssertion(provider="anthropic",
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
