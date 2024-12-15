import pytest
import sys
from pathlib import Path
from dotenv import load_dotenv


def get_test_files():
    """Get all test files"""
    test_dir = Path(__file__).parent
    backwards_dir = test_dir / "backwards_compatibility_tests"

    behavioral_test_files = [
        str(test_dir / "test_llm_setup" / "test_llm_provider.py"),
        str(test_dir / "test_llm_setup" / "test_llm_factory.py"),
        str(test_dir / "test_config_validator" / "test_config_validator.py"),
        str(test_dir / "pytest_plugin_tests" / "test_fixture_isolation.py"),
        str(test_dir / "pytest_plugin_tests" / "test_pytest_configuration.py"),
        str(test_dir / "test_behavioral_assert" / "test_assert_behavioral_match_input_validator.py"),
        str(test_dir / "test_behavioral_assert" / "test_behavioral_assert_validations.py"),
        str(test_dir / "test_behavioral_assert" / "test_behavioral_assert_configuration.py"),
        str(test_dir / "test_behavioral_assert" / "test_behavioral_assert_prompt_configurator.py"),
        str(test_dir / "test_behavioral_assert" / "test_behavioral_assert_llm_injection.py"),
        str(test_dir / "test_behavioral_assert" / "test_behavioral_assert_env_configuration.py"),
        str(test_dir / "actual_usage_tests" / "test_greeting.py"),
        str(test_dir / "actual_usage_tests" / "test_ww2_narrative.py"),
        str(test_dir / "test_behavioral_assert" / "test_behavioral_assert_basic.py"),
        str(test_dir / "test_behavioral_assert" / "test_behavioral_assert_complex.py"),
        str(test_dir / "test_behavioral_assert" / "test_behavioral_assert_ridiculous.py"),
        str(test_dir / "test_behavioral_assert" / "test_behavioral_assert_real_world.py"),
        str(test_dir / "test_rate_limiter" / "test_rate_limiter.py"),
        str(test_dir / "test_rate_limiter" / "test_rate_limiter_scoped.py"),
        str(test_dir / "test_rate_limiter_validator" / "test_rate_limiter_input_validator.py")
    ]

    semantic_test_files = [
        str(backwards_dir / "test_llm_setup" / "test_llm_provider.py"),
        str(backwards_dir / "test_llm_setup" / "test_llm_factory.py"),
        str(backwards_dir / "test_rate_limiter" / "test_rate_limiter_backwards_compatibility.py"),
        str(backwards_dir / "test_rate_limiter" / "test_rate_limiter_scoped_backwards_compatibility.py"),
        str(backwards_dir / "test_config_validator" / "test_config_validator.py"),
        str(backwards_dir / "pytest_plugin_tests" / "test_fixture_isolation.py"),
        str(backwards_dir / "pytest_plugin_tests" / "test_pytest_configuration.py"),
        str(backwards_dir / "test_semantic_assert" / "test_assert_semantic_match_input_validator.py"),
        str(backwards_dir / "test_semantic_assert" / "test_semantic_assert_validations.py"),
        str(backwards_dir / "test_semantic_assert" / "test_semantic_assert_configuration.py"),
        str(backwards_dir / "test_semantic_assert" / "test_semantic_assert_prompt_configurator.py"),
        str(backwards_dir / "test_semantic_assert" / "test_semantic_assert_llm_injection.py"),
        str(backwards_dir / "test_semantic_assert" / "test_semantic_assert_env_configuration.py"),
        str(backwards_dir / "actual_usage_tests" / "test_greeting.py"),
        str(backwards_dir / "actual_usage_tests" / "test_ww2_narrative.py"),
        str(backwards_dir / "test_semantic_assert" / "test_semantic_assert_basic.py"),
        str(backwards_dir / "test_semantic_assert" / "test_semantic_assert_complex.py"),
        str(backwards_dir / "test_semantic_assert" / "test_semantic_assert_ridiculous.py"),
        str(backwards_dir / "test_semantic_assert" / "test_semantic_assert_real_world.py")
    ]

    return behavioral_test_files + semantic_test_files


def test_run_all():
    """Run all tests as a pytest test"""
    load_dotenv()
    test_files = get_test_files()

    args = [
        "-vv",
        "--capture=no",
        "--showlocals",
        *test_files
    ]

    result = pytest.main(args)

    assert result == 0

if __name__ == "__main__":
    # For direct running
    load_dotenv()
    test_files = get_test_files()
    exit_code = pytest.main(["-v"] + test_files)
    sys.exit(exit_code)