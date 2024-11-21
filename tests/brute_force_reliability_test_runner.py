import pytest
import time
from collections import defaultdict
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='../reliability_testing/2024-11-21_test_runs_5.log'
)


class TestRunner:
    def __init__(self, iterations=100):
        self.iterations = iterations
        self.stats = defaultdict(int)
        self.total_duration = 0

    def run_tests(self):
        logging.info(f"Starting test suite execution for {self.iterations} iterations")
        start_time = time.time()

        for iteration in range(self.iterations):
            logging.info(f"Starting iteration {iteration + 1}")

            try:
                pytest_args = [
                    "test_semantic_assert/test_semantic_assert_complex.py",
                    "-v",
                    "--no-header",
                    "--tb=short"
                ]

                result = pytest.main(pytest_args)

                if result == pytest.ExitCode.OK:
                    self.stats['passed'] += 1
                elif result == pytest.ExitCode.TESTS_FAILED:
                    self.stats['failed'] += 1
                else:
                    self.stats['error'] += 1

            except Exception as e:
                logging.error(f"Error in iteration {iteration + 1}: {str(e)}")
                self.stats['error'] += 1

        self.total_duration = time.time() - start_time
        self._log_final_results()

    def _log_final_results(self):
        logging.info("\n=== Final Test Results ===")
        logging.info(f"Total Iterations: {self.iterations}")
        logging.info(f"Passed: {self.stats['passed']}")
        logging.info(f"Failed: {self.stats['failed']}")
        logging.info(f"Errors: {self.stats['error']}")
        logging.info(f"Total Duration: {self.total_duration:.2f} seconds")
        logging.info("=====================")


if __name__ == "__main__":
    runner = TestRunner(iterations=100)
    runner.run_tests()
