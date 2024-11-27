# Step-by-Step Release Process

1. Release Branch Validation

Ensure the release/version branch has been reviewed and approved
All tests must pass on the release branch before proceeding - 100% coverage is required because this is a testing library. The core functionality **MUST** be covered by tests.

2. Version Management

- Update version number in two locations:
  - src/llm_app_test/__init__.py
  - pyproject.toml
- Use format: `version.devX` where X is incremented if issues arise with PyPI test deployment
- Example: `0.1.0.dev0`, `0.1.0.dev1`, etc.

3. Build Process

```
# Build wheel
python -m build
```

4. Test Repository Deployment

```
# Upload to PyPI test
twine upload --repository testpypi dist/*
```

5. Test Installation Verification

```
# Create clean virtual environment (OR JUST USE PYCHARM LIKE A NORMAL HUMAN)
python -m venv test_env
source test_env/bin/activate  # or `test_env\Scripts\activate` on Windows

# Install from test PyPI with main index fallback
pip install --index-url https://test.pypi.org/simple/ \
    --extra-index-url https://pypi.org/simple \
    llm-app-test
```

6. Testing Procedure

- Copy test directory from working project to new installation
- Create .env file with required API keys:

```
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
```

- Execute test suite in both modes:

```
# OpenAI mode
LLM_PROVIDER=openai

# Anthropic mode
LLM_PROVIDER=anthropic
```

7. Quality Gates

- If any tests fail:
  - Fix identified issues
  - Increment X in version.devX
  - Return to step 2
- If all tests pass:
  - Proceed to production deployment

8. Production Deployment

```
# Upload to production PyPI
twine upload dist/*
```

9. Production Verification

```
# Install from production PyPI
pip install llm-app-test

# Run full test suite again following steps in Testing Procedure
```

10. Post-Deployment Monitoring

- If issues are found, **immediately** yank the release:

```
pip install twine-yank
twine yank llm-app-test==<version>

# Or just go to PyPI and yank it 
# Doesn't matter how it gets done as long as it gets yanked before too many people are affected
```

- Monitor for 12 hours after release
- If no issues arise, proceed to final step

11. Branch Management

- Create pull request to merge release branch into main
- Ensure CI passes on the PR
- Obtain necessary approvals
- Complete the merge


