import pytest
import sys
from pathlib import Path


def run_semantic_tests():
    """Run all semantic assertion tests"""
    test_dir = Path(__file__).parent
    test_files = [

        str(test_dir / "test_llm_setup" / "test_llm_provider.py"),
        str(test_dir / "test_llm_setup" / "test_llm_factory.py"),
        str(test_dir / "test_config_validator" / "test_config_validator.py"),
        str(test_dir / "pytest_plugin_tests" / "test_fixture_isolation.py"),
        str(test_dir / "pytest_plugin_tests" / "test_pytest_configuration.py"),
        str(test_dir / "test_semantic_assert" / "test_semantic_assert_validations.py"),
        str(test_dir / "test_semantic_assert" / "test_semantic_assert_configuration.py"),
        str(test_dir / "test_semantic_assert" / "test_semantic_assert_prompt_configurator.py"),
        str(test_dir / "test_semantic_assert" / "test_semantic_assert_llm_injection.py"),
        str(test_dir / "test_semantic_assert" / "test_semantic_assert_env_configuration.py"),
        str(test_dir / "actual_usage_tests" / "test_greeting.py"),
        str(test_dir / "actual_usage_tests" / "test_ww2_narrative.py"),
        str(test_dir / "test_semantic_assert" / "test_semantic_assert_basic.py"),
        str(test_dir / "test_semantic_assert" / "test_semantic_assert_complex.py"),
        str(test_dir / "test_semantic_assert" / "test_semantic_assert_ridiculous.py"),
        str(test_dir / "test_semantic_assert" / "test_semantic_assert_real_world.py")
    ]

    args = [
        *test_files,
        "-v",
    ]

    return pytest.main(args)


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()

    exit_code = run_semantic_tests()
    sys.exit(exit_code)