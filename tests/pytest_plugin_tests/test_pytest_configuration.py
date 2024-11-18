import pytest
from src.llm_app_test.semantic_assert.semantic_assert import SemanticAssertion


class TestPytestConfiguration:
    """Test suite for pytest configuration and fixtures"""

    def test_semantic_assert_fixture_type(self, semantic_assert):
        """Test that semantic_assert fixture returns correct instance"""
        assert isinstance(semantic_assert, SemanticAssertion)

    def test_assert_semantic_match_fixture_callable(self, assert_semantic_match):
        """Test that assert_semantic_match fixture returns callable"""
        assert callable(assert_semantic_match)

    def test_fixtures_relationship(self, semantic_assert, assert_semantic_match):
        """Test that assert_semantic_match fixture uses semantic_assert correctly"""
        # Verify the fixtures are properly linked
        assert assert_semantic_match == semantic_assert.assert_semantic_match

    def test_semantic_marker_usage(self):
        """Test semantic marker can be used on a test"""

        @pytest.mark.semantic
        def sample_test():
            pass

        assert hasattr(sample_test, 'pytestmark')
        assert any(mark.name == 'semantic' for mark in sample_test.pytestmark)

    def test_fixtures_basic_functionality(self, semantic_assert, assert_semantic_match):
        """Test basic functionality of both fixtures"""
        actual = "The sky is blue"
        expected = "A statement about the color of the sky"

        try:
            semantic_assert.assert_semantic_match(actual, expected)
            assert_semantic_match(actual, expected)
        except Exception as e:
            pytest.fail(f"Fixtures failed basic functionality test: {str(e)}")

    @pytest.mark.semantic
    def test_semantic_marker_integration(self, assert_semantic_match):
        """Test semantic marker works with fixture"""
        actual = "Hello, world!"
        expected = "A greeting message"
        assert_semantic_match(actual, expected)
