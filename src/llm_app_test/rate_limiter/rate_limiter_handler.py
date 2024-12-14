import os
from typing import Optional

from dotenv import load_dotenv
from langchain_core.rate_limiters import InMemoryRateLimiter

from llm_app_test.behavioral_assert.behavioral_assert_config.behavioral_assert_constants import RateLimiterConstants
from llm_app_test.behavioral_assert.validation.rate_limiter_input_validator import RateLimiterInputsValidator


class LLMInMemoryRateLimiter:
    """
    Represents an in-memory rate limiter with configurable properties.

    This class provides the functionality to initialize an in-memory rate
    limiter with specific rate-limiting parameters. The parameters can be
    overridden manually or taken from environment variables if not specified.
    It supports validation of the input values and provides a property to
    retrieve an instance of the rate limiter.

    Attributes:
        requests_per_second: The number of allowed requests per second.
        check_every_n_seconds: The interval in seconds to check for request limits.
        max_bucket_size: The maximum capacity of the token bucket for requests.

    Methods:
        get_rate_limiter: Returns an initialized InMemoryRateLimiter instance with
                          the specified configuration.
    """
    def __init__(self,
                 requests_per_second: Optional[float] = None,
                 check_every_n_seconds: Optional[float] = None,
                 max_bucket_size: Optional[float] = None
    ):
        """
        Initializes the rate limiter with the specified or default parameters, validating the provided or
        retrieved configurations using the `RateLimiterInputsValidator`.

        Attributes:
        requests_per_second: Configures the number of requests allowed per second, either set explicitly,
                              retrieved from the environment variable `RATE_LIMITER_REQUESTS_PER_SECOND`
                              or defaults to `RateLimiterConstants.REQUESTS_PER_SECOND`.
        check_every_n_seconds: Configures the interval in seconds for checking the request bucket state,
                                set explicitly, via the `RATE_LIMITER_CHECK_EVERY_N_SECONDS` environment variable,
                                or defaults to `RateLimiterConstants.CHECK_EVERY_N_SECONDS`.
        max_bucket_size: Configures the maximum size of the request bucket, either explicitly set, retrieved
                         from the `RATE_LIMITER_MAX_BUCKET_SIZE` environment variable or defaults to
                         `RateLimiterConstants.MAX_BUCKET_SIZE`.

        Parameters:
        requests_per_second: Optional[float]
            The desired allowed rate of requests per second. If not specified, attempts to retrieve this
            value from environmental variables or fallbacks to constants.
        check_every_n_seconds: Optional[float]
            The time duration to check the bucket status. If not provided, tries retrieving this
            from environmental variables or uses a default constant.
        max_bucket_size: Optional[float]
            Designated size of maximum bucket item slots. If undefined, loads it as priority via env else
            its constant-source if newly absent-used.
        """
        load_dotenv()
        requests_per_second_override = requests_per_second if requests_per_second is not None else float(
            os.getenv('RATE_LIMITER_REQUESTS_PER_SECOND', RateLimiterConstants.REQUESTS_PER_SECOND))
        check_every_n_seconds_override = check_every_n_seconds if check_every_n_seconds is not None else float(
            os.getenv('RATE_LIMITER_CHECK_EVERY_N_SECONDS', RateLimiterConstants.CHECK_EVERY_N_SECONDS))
        max_bucket_size_env = max_bucket_size if max_bucket_size is not None else float(
            os.getenv('RATE_LIMITER_MAX_BUCKET_SIZE', RateLimiterConstants.MAX_BUCKET_SIZE))

        self.requests_per_second = RateLimiterInputsValidator.validate_requests_per_second(requests_per_second_override)
        self.check_every_n_seconds = RateLimiterInputsValidator.validate_check_every_n_seconds(
            check_every_n_seconds_override)
        self.max_bucket_size = RateLimiterInputsValidator.validate_max_bucket_size(max_bucket_size_env)

    @property
    def get_rate_limiter(self) -> InMemoryRateLimiter:
        """
            Returns an instance of InMemoryRateLimiter configured with the rate
            limiting parameters defined for the current instance.

            @return: An instance of InMemoryRateLimiter configured with the
            specified rate limiting settings.
            @rtype: InMemoryRateLimiter
        """
        return InMemoryRateLimiter(
            requests_per_second=self.requests_per_second,
            check_every_n_seconds=self.check_every_n_seconds,
            max_bucket_size=self.max_bucket_size
        )