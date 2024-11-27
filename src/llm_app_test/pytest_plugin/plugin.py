import pytest
from llm_app_test.behavioral_assert.behavioral_assert import BehavioralAssertion
from llm_app_test.semantic_assert.semantic_assert import deprecated, SemanticAssertion


def pytest_configure(config):
    """Register test markers"""
    # Add new marker
    config.addinivalue_line(
        "markers",
        "behavioral: mark test as behavioral comparison test"
    )

    # Deprecate old marker
    config.addinivalue_line(
        "markers",
        "semantic: (deprecated) mark test as semantic comparison test. Use 'behavioral' marker instead. Will be removed in version 1.0.0 or first update after 1 June 2025"
    )


@pytest.fixture
def behavioral_assert():
    """Fixture to provide semantic assertion capabilities"""
    return BehavioralAssertion()


@pytest.fixture
def assert_behavioral_match(behavioral_assert):
    """Fixture for semantic matching"""
    return behavioral_assert.assert_behavioral_match

@pytest.fixture
@deprecated
def semantic_assert():
    """Deprecated: Use behavioral_assert instead"""
    return SemanticAssertion()

@pytest.fixture
@deprecated
def assert_semantic_match(semantic_assert):
    """Deprecated: Use assert_behavioral_match instead"""
    return semantic_assert.assert_semantic_match
