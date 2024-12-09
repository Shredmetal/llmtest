[← Back to Home](../index.md)

# CI/CD Integration

llm_app_test is designed for seamless integration with CI/CD pipelines.

## Setting Up CI/CD

### 1. Environment Setup
Add your API keys as secrets in your CI/CD environment:

```
env:
  OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}

# OR
env:
  ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

### 2. Test Configuration

```
from llm_app_test.behavioral_assert.behavioral_assert import BehavioralAssertion

def test_llm_output():
    behavioral_assert = BehavioralAssertion() # Your tests here
```


### 3. CI/CD Pipeline Configuration

#### GitHub Actions Example

```
name: LLM Application Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'
          
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install llm-app-test
          
      - name: Run tests
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: pytest tests/
```


## Best Practices

1. **API Key Management**:

    - Never commit API keys
    - Use CI/CD environment secrets
    - Rotate keys regularly

2. **Cost Control**:

    - Run behavioral tests only on critical paths
    - Consider test result caching

3. **Pipeline Optimization**:

    - Run traditional tests first
    - Run behavioral tests in parallel
    - Set appropriate timeouts

4. **Error Handling**:

    - Implement retry logic for API failures (though Langchain should have this covered)
    - Log detailed error information
    - Set up alerts for repeated failures

## Common Issues

1. **API Rate Limits**:
    - Implement exponential backoff (configuration and integration of Langchain implementation planned for future version)
    - Use test result caching
    - Consider parallel test execution

2. **Cost Management**:
    - Monitor API usage
    - Set budget alerts
    - Use test filtering

---
## Navigation

- [Back to Home](../index.md)
- [Installation Guide](../getting-started/installation.md)
- [Quick Start Guide](../getting-started/quickstart.md)
- [API Reference](../api/behavioral-assertion.md)
