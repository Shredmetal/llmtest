import pytest


class TestFixtureIsolation:
    """Test suite for fixture isolation and reusability"""

    def test_fixture_state_isolation(self, behavioral_assert):
        """Test that fixture state doesn't persist between tests"""
        behavioral_assert._previous_result = "test"

        assert hasattr(behavioral_assert, '_previous_result')
        assert behavioral_assert._previous_result == "test"

    def test_fixture_clean_state(self, behavioral_assert):
        """Test that fixture starts with clean state"""
        assert not hasattr(behavioral_assert, '_previous_result')

    def test_fixture_functionality(self, behavioral_assert):
        """Test that fixture provides working instance"""
        try:
            behavioral_assert.assert_behavioral_match(
                "Hello", "A greeting message"
            )
        except Exception as e:
            pytest.fail(f"Fixture failed to provide working instance: {str(e)}")

    def test_fixture_reusability(self, assert_behavioral_match):
        """Test that fixture can be reused multiple times"""
        test_cases = [
            ("The sky is blue", "A statement about the sky's color"),
            ("Hello world", "A greeting message"),
            ("Python is great", "A statement about Python programming")
        ]

        for actual, expected in test_cases:
            try:
                assert_behavioral_match(actual, expected)
            except Exception as e:
                pytest.fail(f"Fixture reuse failed on case {actual}: {str(e)}")
