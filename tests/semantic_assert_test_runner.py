import pytest
import sys
import coverage
from pathlib import Path


def run_semantic_tests():
    """Run all semantic assertion tests"""
    test_dir = Path(__file__).parent
    test_files = [
        str(test_dir / "test_semantic_assert" / "test_semantic_assert_validations.py"),
        str(test_dir / "test_semantic_assert" / "test_semantic_assert_basic.py"),
        str(test_dir / "test_semantic_assert" / "test_semantic_assert_complex.py"),
        str(test_dir / "test_semantic_assert" / "test_semantic_assert_ridiculous.py"),
        str(test_dir / "actual_usage_tests" / "test_greeting.py"),
        str(test_dir / "test_llm_setup" / "test_llm_provider.py"),
        str(test_dir / "test_llm_setup" / "test_llm_factory.py"),
        str(test_dir / "test_config_validator" / "test_config_validator.py"),
        str(test_dir / "pytest_plugin_tests" / "test_fixture_isolation.py"),
        str(test_dir / "pytest_plugin_tests" / "test_pytest_configuration.py")
    ]

    cov = coverage.Coverage(source=['src.llm_app_test'])
    cov.start()

    args = [
        *test_files,
        "-v",
    ]
    result = pytest.main(args)

    cov.stop()
    cov.save()
    cov.report()
    cov.html_report()

    return result


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    exit_code = run_semantic_tests()
    sys.exit(exit_code)