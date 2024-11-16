import pytest
from ..semanticassert.semantic_assert import SemanticAssertion


def pytest_configure(config):
    """Register semantic test markers"""
    config.addinivalue_line(
        "markers",
        "semantic: mark test as semantic comparison test"
    )


@pytest.fixture
def semantic_assert():
    """Fixture to provide semantic assertion capabilities"""
    return SemanticAssertion()


@pytest.fixture
def assert_semantic_match(semantic_assert):
    """Fixture for semantic matching"""
    return semantic_assert.assert_semantic_match
