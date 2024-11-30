import pytest

from llm_app_test.behavioral_assert.behavioral_assert import BehavioralAssertion


class TestPytestConfiguration:
    """Test suite for pytest configuration and fixtures"""

    def test_behavioral_assert_fixture_type(self, behavioral_assert):
        """Test that behavioral_assert fixture returns correct instance"""
        assert isinstance(behavioral_assert, BehavioralAssertion)

    def test_assert_behavioral_match_fixture_callable(self, assert_behavioral_match):
        """Test that assert_behavioral_match fixture returns callable"""
        assert callable(assert_behavioral_match)

    def test_fixtures_relationship(self, behavioral_assert, assert_behavioral_match):
        """Test that assert_behavioral_match fixture uses behavioral_assert correctly"""
        # Verify the fixtures are properly linked
        assert assert_behavioral_match == behavioral_assert.assert_behavioral_match

    def test_behavioral_marker_usage(self):
        """Test semantic marker can be used on a test"""

        @pytest.mark.behavioral
        def sample_test():
            pass

        assert hasattr(sample_test, 'pytestmark')
        assert any(mark.name == 'behavioral' for mark in sample_test.pytestmark)

    def test_fixtures_basic_functionality(self, behavioral_assert, assert_behavioral_match):
        """Test basic functionality of both fixtures"""
        actual = "The sky is blue"
        expected = "A statement about the color of the sky"

        try:
            behavioral_assert.assert_behavioral_match(actual, expected)
            assert_behavioral_match(actual, expected)
        except Exception as e:
            pytest.fail(f"Fixtures failed basic functionality test: {str(e)}")

    @pytest.mark.behavioral
    def test_behavioral_marker_integration(self, assert_behavioral_match):
        """Test behavioral marker works with fixture"""
        actual = "Hello, world!"
        expected = "A greeting message"
        assert_behavioral_match(actual, expected)

    def test_behavioral_marker_registration(self):
        """Test that behavioral marker is properly registered"""

        @pytest.mark.behavioral
        def sample_test():
            pass

        assert 'behavioral' in sample_test.pytestmark[0].name