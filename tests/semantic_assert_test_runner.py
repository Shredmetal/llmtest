import pytest
import sys
from pathlib import Path


def run_semantic_tests():
    """Run all semantic assertion tests"""
    test_dir = Path(__file__).parent / "test_semantic_assert"
    test_files = [
        str(test_dir / "test_semantic_assert_basic.py"),
        str(test_dir / "test_semantic_assert_validations.py"),
        str(test_dir / "test_semantic_assert_complex.py"),
        str(test_dir / "test_semantic_assert_ridiculous.py")
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