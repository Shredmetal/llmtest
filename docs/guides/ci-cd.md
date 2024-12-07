[← Back to Home](../index.md)

# CI/CD Guide for llm-application Test Library

This guide provides a detailed explanation of setting up Continuous Integration (CI) using GitHub Actions for the `llm-application` test library. It includes a step-by-step example of a CI workflow, environment variable setup, and best practices for CI integration.

---

## 1. CI Integration

### GitHub Actions Example
Below is an example of a GitHub Actions workflow file (`ci.yml`) configured for the `llm-application` test library. It runs necessary tests in parallel for changes pushed to the `main` branch or submitted as pull requests to `main`.

```yaml
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  test:
    name: Run basic tests and ensure all pass
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python 3.10
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install GPG
        run: sudo apt-get install -y gpg

      - name: Decrypt API key
        env:
          GPG_PASSPHRASE: ${{ secrets.GPG_PASSPHRASE }}
        run: |
          gpg --batch --yes --passphrase "$GPG_PASSPHRASE" \
              -o openai-api-key.txt -d openai-api-key.txt.gpg

      - name: Set API Key Environment Variable
        run: |
            export OPENAI_API_KEY=$(cat openai-api-key.txt)
            echo "OPENAI_API_KEY=$OPENAI_API_KEY" >> $GITHUB_ENV

      - name: Install dependencies
        run: |
          pip install .

      - name: Make test script executable
        run: chmod +x ci-necessary-tests.sh

      - name: Run tests
        run: ./ci-necessary-tests.sh
        env:
          OPENAI_API_KEY: ${{ env.OPENAI_API_KEY }}
```

## Environment Variable Setup Guide
	1.	Create Encrypted Secrets:
       •	Navigate to your repository on GitHub.
       •	Go to Settings > Secrets and variables > Actions.
       •	Add a secret named GPG_PASSPHRASE containing the passphrase for your encrypted API key.
	2.	Encrypt API Keys:
	  •	Use gpg to encrypt the API key file locally:
```
gpg --batch --yes --passphrase "your-passphrase" -c openai-api-key.txt
```
	  •	Add the resulting openai-api-key.txt.gpg file to your repository.

	3.	Environment Variable Usage:
	  •	The workflow uses the decrypted key as an environment variable (OPENAI_API_KEY) during the test run.

## Best Practices for CI Integration
	•	Keep Secrets Secure:
	•	Never commit plain-text API keys or sensitive credentials.
	•	Use GitHub Secrets to securely manage sensitive data.
	•	Parallelize Tests:
	•	Leverage parallel execution to reduce CI runtime, especially for large test suites.
	•	Fail Fast:
	•	Configure the CI to exit immediately upon test failure to save time and resources.
	•	Keep Workflows Modular:
	•	Separate workflows for testing, deployment, and other stages to enhance clarity and maintainability.

## 2. Workflow Example
```yaml
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python 3.10
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: pip install .

      - name: Run Tests
        run: pytest
```

## Explaining ci-necessary-tests.sh
### How It Works
	1.	Test File List:
	  •	Specify the test files to be run in the test_files array.
	2.	Parallel Execution:
	  •	Each test file runs as a background process, improving efficiency.
	3.	Error Tracking:
	  •	The script tracks process IDs and exit statuses to determine if any test failed.
	4.	Final Status:
	  •	If all tests pass, the script exits with a status of 0. Otherwise, it exits with an error status of 1.
---
---

## Customizing the CI Workflow

### Tailoring to Your Needs

The provided workflow is modular and can be easily customized:

1. **Triggering on Specific Events**:
   - Modify the `on` section to run workflows for specific branches or events.
     ```yaml
     on:
       push:
         branches:
           - dev
       pull_request:
         branches:
           - dev
     ```

2. **Adding Additional Steps**:
   - Include additional steps like linting, type checking, or deployment.
     ```yaml
     - name: Lint code
       run: pylint my_library/
     ```

3. **Changing Python Versions**:
   - Update the `python-version` field to test across multiple Python versions.
     ```yaml
     - name: Set up Python
       uses: actions/setup-python@v4
       with:
         python-version: ['3.9', '3.10', '3.11']
     ```

4. **Conditional Execution**:
   - Use `if` conditions to execute specific steps only when required.
     ```yaml
     - name: Deploy to production
       if: github.ref == 'refs/heads/main'
       run: ./deploy.sh
     ```

---

## Troubleshooting

Here are common issues and solutions for setting up CI workflows:

1. **`OPENAI_API_KEY` Not Found**:
   - Ensure the `OPENAI_API_KEY` env variable is correctly configured in the .env file.

3. **`ci-necessary-tests.sh` Permissions Denied**:
   - Ensure the script is executable:
     ```bash
     chmod +x ci-necessary-tests.sh
     ```

4. **Workflow Doesn’t Trigger**:
   - Verify the `on` section matches the desired branch and event settings.

5. **Long Runtime**:
   - Cache dependencies using the `actions/cache` action to speed up workflows:
     ```yaml
     - name: Cache Python dependencies
       uses: actions/cache@v3
       with:
         path: ~/.cache/pip
         key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
         restore-keys: |
           ${{ runner.os }}-pip-
     ```

---

## Conclusion

With this guide, you can confidently set up a CI/CD pipeline for testing your LLM application using our test library. 
The examples and best practices here are flexible enough to adapt to various CI needs, ensuring efficient, reliable, 
and secure integration into your development workflow.

For further enhancements or specific use cases, feel free to extend the scripts and workflows to meet your project’s requirements.

## Navigation

- [Back to Home](../index.md)
- [Installation Guide](../getting-started/installation.md)
- [Quick Start Guide](../getting-started/quickstart.md)
- [API Reference](../api/behavioral-assertion.md)
