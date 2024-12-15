import pytest
from llm_app_test.behavioral_assert.behavioral_assert import BehavioralAssertion

class TestRateLimiterScoped:

    @pytest.fixture(scope="class")
    def shared_asserter(self):
        return BehavioralAssertion(use_rate_limiter=True,
                                   rate_limiter_requests_per_second=2,
                                   rate_limiter_check_every_n_seconds=1,
                                   rate_limiter_max_bucket_size=2)

    def test_rate_limiter_first_call(self, shared_asserter):
        rate_limiter_id = id(shared_asserter.llm.rate_limiter)
        assert rate_limiter_id is not None

    def test_rate_limiter_second_call(self, shared_asserter):
        rate_limiter_id = id(shared_asserter.llm.rate_limiter)
        assert rate_limiter_id is not None

    def test_shared_rate_limiter(self, shared_asserter):
        rate_limiter_id = id(shared_asserter.llm.rate_limiter)
        assert rate_limiter_id is not None
        assert hasattr(self, 'first_rate_limiter_id'), "First test didn't run"
        assert rate_limiter_id == self.first_rate_limiter_id, "Rate limiter instance changed"

    @pytest.fixture(autouse=True)
    def store_first_rate_limiter_id(self, shared_asserter):
        if not hasattr(self, 'first_rate_limiter_id'):
            self.first_rate_limiter_id = id(shared_asserter.llm.rate_limiter)
