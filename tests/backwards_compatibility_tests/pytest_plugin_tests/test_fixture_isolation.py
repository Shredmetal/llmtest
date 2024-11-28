import pytest


class TestFixtureIsolation:
    """Test suite for fixture isolation and reusability"""

    def test_fixture_state_isolation(self, semantic_assert):
        """Test that fixture state doesn't persist between tests"""
        semantic_assert._previous_result = "test"

        assert hasattr(semantic_assert, '_previous_result')
        assert semantic_assert._previous_result == "test"

    def test_fixture_clean_state(self, semantic_assert):
        """Test that fixture starts with clean state"""
        assert not hasattr(semantic_assert, '_previous_result')

    def test_fixture_functionality(self, semantic_assert):
        """Test that fixture provides working instance"""
        try:
            semantic_assert.assert_semantic_match(
                "Hello", "A greeting message"
            )
        except Exception as e:
            pytest.fail(f"Fixture failed to provide working instance: {str(e)}")

    def test_fixture_reusability(self, assert_semantic_match):
        """Test that fixture can be reused multiple times"""
        test_cases = [
            ("The sky is blue", "A statement about the sky's color"),
            ("Hello world", "A greeting message"),
            ("Python is great", "A statement about Python programming")
        ]

        for actual, expected in test_cases:
            try:
                assert_semantic_match(actual, expected)
            except Exception as e:
                pytest.fail(f"Fixture reuse failed on case {actual}: {str(e)}")
