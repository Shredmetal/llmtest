import os
from typing import Optional

from dotenv import load_dotenv
from langchain_core.rate_limiters import InMemoryRateLimiter

from llm_app_test.behavioral_assert.behavioral_assert_config.behavioral_assert_constants import RateLimiterConstants
from llm_app_test.behavioral_assert.validation.rate_limiter_input_validator import RateLimiterInputsValidator


class LLMInMemoryRateLimiter:
    def __init__(self, use_rate_limiter: bool):

        load_dotenv()
        self.use_rate_limiter = use_rate_limiter
        requests_per_second_env = os.getenv('RATE_LIMITER_REQUESTS_PER_SECOND',
                                            RateLimiterConstants.REQUESTS_PER_SECOND)
        check_every_n_seconds_env = os.getenv('RATE_LIMITER_CHECK_EVERY_N_SECONDS',
                                              RateLimiterConstants.CHECK_EVERY_N_SECONDS)
        max_bucket_size_env = os.getenv('RATE_LIMITER_MAX_BUCKET_SIZE', RateLimiterConstants.MAX_BUCKET_SIZE)

        # Validate values
        self.requests_per_second = RateLimiterInputsValidator.validate_requests_per_second(requests_per_second_env)
        self.check_every_n_seconds = RateLimiterInputsValidator.validate_check_every_n_seconds(
            check_every_n_seconds_env)
        self.max_bucket_size = RateLimiterInputsValidator.validate_max_bucket_size(max_bucket_size_env)

    @property
    def get_rate_limiter(self) -> Optional[InMemoryRateLimiter]:
        return InMemoryRateLimiter(
            requests_per_second=self.requests_per_second,
            check_every_n_seconds=self.check_every_n_seconds,
            max_bucket_size=self.max_bucket_size
        ) if self.use_rate_limiter else None