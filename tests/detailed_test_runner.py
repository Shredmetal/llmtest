import pytest
import time
from collections import defaultdict
import logging
from _pytest.reports import TestReport

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='../reliability_testing_real_world_2/2024-11-23_semantic_reliability_test_medical_only_2.log'
)

class DetailedTestRunner:
    def __init__(self, iterations=200):
        self.iterations = iterations
        self.stats = defaultdict(int)
        self.total_duration = 0
        self.test_results = defaultdict(lambda: {'passed': 0, 'failed': 0})

    def pytest_runtest_logreport(self, report: TestReport):
        if report.when == 'call':
            test_name = report.nodeid.split("::")[-1]
            if report.passed:
                self.test_results[test_name]['passed'] += 1
            elif report.failed:
                self.test_results[test_name]['failed'] += 1
                logging.error(f"Test failed: {test_name}")
                if hasattr(report, 'longrepr'):
                    logging.error(f"Failure reason: {str(report.longrepr)}")

    def run_tests(self):
        logging.info(f"Starting medical test suite execution for {self.iterations} iterations")
        start_time = time.time()

        for iteration in range(self.iterations):
            logging.info(f"Starting iteration {iteration + 1}")

            try:
                pytest_args = [
                    "test_semantic_assert/test_semantic_assert_real_world.py::TestRealWorldSemanticAssertion::test_patient_education_diabetes_management",
                    "-v",
                    "--no-header",
                    "--tb=short"
                ]
                plugin = self
                pytest.main(pytest_args, plugins=[plugin])

            except Exception as e:
                logging.error(f"Error in iteration {iteration + 1}: {str(e)}")
                self.stats['error'] += 1

        self.total_duration = time.time() - start_time
        self._log_final_results()

    def _log_final_results(self):
        logging.info("\n=== Final Test Results ===")
        logging.info(f"Total Iterations: {self.iterations}")

        for test_name, results in self.test_results.items():
            logging.info(f"\nTest: {test_name}")
            logging.info(f"Passed: {results['passed']}")
            logging.info(f"Failed: {results['failed']}")
            success_rate = (results['passed'] / self.iterations) * 100
            logging.info(f"Success Rate: {success_rate:.2f}%")

        logging.info(f"\nTotal Duration: {self.total_duration:.2f} seconds")
        logging.info("=====================")

if __name__ == "__main__":
    runner = DetailedTestRunner(iterations=200)
    runner.run_tests()
