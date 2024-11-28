# llm_app_test

[![Discord](https://img.shields.io/discord/1307634517766443058?logo=discord&logoColor=white)](https://discord.gg/awy83bZsKf)
[![PyPI Version](https://img.shields.io/pypi/v/llm-app-test?label=pypi%20package)](https://pypi.org/project/llm-app-test/)
![PyPI Downloads](https://img.shields.io/pypi/dm/llm-app-test)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)
[![Documentation](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://Shredmetal.github.io/llmtest/)

> TL;DR: A Python library that lets you test LLM applications by describing expected behavior in plain English.

## Overview

A behavioral testing framework for applications using large language models (LLMs). It leverages LLMs to validate the behavior of applications containing LLMs against natural language test specifications (reliability validated through 30,000 test executions), providing a powerful tool for unit/integration testing of applications containing an LLM (not for testing LLMs themselves). 

We made this because we were unsatisfied with existing approaches to testing our apps that someone else told us to stick a non-deterministic black box into:

1. String/regex matching and embeddings are too brittle - this is obvious for the former. Embeddings allow slightly more flexibility, but you still need to roughly guess what your LLM-powered app is going to say, and set things like thresholds while having an understanding of vector spaces.
2. Academic metrics are of little help to API consumers like us with no ability to change the model. However, we still believe this tool is useful for the software engineering side of things. Please refer to the [Testing Philosophy](#testing-philosophy) section below on when to send things back to the data scientists.
3. We just wanted to define a behavior and assert on it.

⚠️ Note on Reliability: While we cannot guarantee 100% reliability (due to the fundamental nature of LLMs), we validated the library with 30,000 test executions with zero format violations and non-determinism only occurring in one case containing a genuine semantic boundary. 

We stress that  past success doesn't guarantee future determinism - this is an unsolvable problem in LLM testing, but we've implemented extensive mitigations to make it as reliable as possible. We will continue to validate reliability through brute force testing and will report if issues are detected. In this regard, please refer to the reliability testing section of the documentation.

You can go straight to the [documentation](https://Shredmetal.github.io/llmtest/) if you wish ⚠️ This is where you will find the most up-to-date information about the library.

## The Cool Stuff:

✨ Test your LLM apps in minutes, not hours

🚀 CI/CD ready out of the box (Tested in GitHub Actions CI - Please let us know if it just works(tm) in other CI systems)

💰 Cost-effective testing solution

🔧 No infrastructure needed (Unless if you want to inject a custom LLM, please refer to the configuration page of the documentation for details)
## Installation - Reading the rest of the readme first is strongly recommended before use

```
pip install llm-app-test
```

Please refer to the [documentation](https://shredmetal.github.io/llmtest/getting-started/installation/) for full instructions.

## Testing Philosophy

When integrating LLMs into your application, treat them as you would any closed-source third-party library (because there's a pretty good chance you can't actually change the LLM itself):

1. Write tests for expected behaviour
2. Focus on interface boundaries
3. Test application-level functionality
4. Maintain clear separation of concerns

### ⚠️ Important Information on Understanding Responsibilities

llm-app-test is built by engineers for engineers so that all of us have a tool to validate the behaviour of applications that have had an LLM stuffed into them. It is **NOT** a Data Science tool nor a replacement for model metrics used by Data Science teams to validate model suitability.

#### Software Engineer's Role

- Write tests for expected application behaviour (in the same way you would for any piece of production code)
- Validate inputs and outputs
- Ensure proper integration
- Monitor system performance (if all of your llm_app_test tests were passing before, and they suddenly start failing, you might have a problem)
- Escalate consistent failures to DS team (as this might indicate a fundamental problem with the model, or perhaps it might be worth seeking assistance with the `expected_behavior` prompt in the `assert_behavioral_match` function)

#### Data Science Team's Role

- Handle model-level issues
- Address consistent test failures
- Evaluate model suitability
- Optimise model performance
- Adjust prompts when needed

### When to Escalate

Escalate to your Data Science team when:

1. Tests consistently fail despite correct implementation
2. Model responses are consistently inappropriate
3. Performance degradation is observed
4. Pattern of failures indicates model-level issues

### 🔍 What Makes This Different?

This is an ENGINEERING tool, not a data science tool. The difference is crucial:

Data Science Tools:
- Test model performance
- Evaluate model accuracy
- Measure model metrics

llm_app_test (Engineering Tool):
- Tests your APPLICATION code
- Validates integration points
- Ensures system behaviour
- Maintains production reliability

Think of it this way: You don't test Redis itself, you test your application's use of Redis. 
Similarly, llm_app_test helps you test your application's use of LLMs.

## In summary:

### What llm_app_test Does

- Tests LLM applications (not the LLMs themselves)
- Validates system message + prompt template outputs
- Ensures correct behavior of your application
- Tests the parts YOU control in your LLM application

### What llm_app_test Doesn't Do

- Test LLM model performance (that's the provider's responsibility)
- Validate base model capabilities
- Test model reliability
- Handle model safety features

### When to Use llm_app_test

- Testing application-level LLM integration
- Validating prompt engineering
- Testing system message effectiveness
- Ensuring consistent response patterns (just stick the test in a loop if you have to)

### When Not to Use llm_app_test

- Testing base LLM performance
- Evaluating model capabilities
- Testing model safety features

## Why llm_app_test?

Testing LLM applications is challenging because:
- Outputs are non-deterministic
- Application behavior meaning matters more than exact matches
- Traditional testing approaches don't work well
- Integration into CI/CD pipelines is complex

llm_app_test solves these challenges by:
- Using LLMs to evaluate the correct behavior
- Providing a clean, maintainable testing framework
- Offering simple CI/CD integration
- Supporting multiple LLM providers

## Example of Behavioral Testing:

### Real World Example

Here's a powerful example showing behavioral testing in action:

```
from langchain_core.messages import SystemMessage, HumanMessage
from llm_app_test.behavioral_assert.behavioral_assert import BehavioralAssertion
from your_bot_module import SimpleApiCallBot  # Your LLM wrapper

def test_ww2_narrative():
    behavioral_assert = BehavioralAssertion()

    # Define the bot's behavior with a system message
    system_message = SystemMessage(
        """
        You are a historian bot and you will respond to specific requests 
        for information about history. Be detailed but do not go beyond 
        what was asked for.
        """
    )

    # Initialize the bot
    # This is a simple API call to openAI - you can find this in our tests/actual_usage_tests directory in the repo
    bot = SimpleApiCallBot(system_message=system_message) 
    
    # Create the user's request
    human_message = HumanMessage(
        content="Tell me about the European Theater of World War 2, the major battles, and how the European war ended"
    )

    # Get the bot's response
    actual_output = bot.generate_ai_response(human_message)

    # Define expected behavior
    expected_behavior = """
    A narrative about World War 2 and the global nature of the war
    """

    # This will fail because the bot's response focuses only on Europe
    behavioral_assert.assert_behavioral_match(actual_output, expected_behavior)
```

Note: Claude is a little too helpful and will say stuff about the other theaters so when calling the generation bot with Claude, use this:

```
"Tell me about the European Theater of World War 2, the major battles, and how the European war ended. Only mention the European theater and do not mention the other theaters."
```

Actual bot response from one run (GPT-4o):

```
The European Theater of World War II was a significant front in the global conflict that lasted from 1939 to 1945. It involved most of the countries of Europe and was marked by numerous major battles and campaigns. Here is an overview of some of the key events and battles:

1. **Invasion of Poland (1939):** The war in Europe began with Germany's invasion of Poland on September 1, 1939. This prompted Britain and France to declare war on Germany. The swift German victory was achieved through the use of Blitzkrieg tactics.

2. **Battle of France (1940):** In May 1940, Germany launched an invasion of France and the Low Countries. The German forces bypassed the heavily fortified Maginot Line and quickly advanced through the Ardennes, leading to the fall of France in June 1940.

3. **Battle of Britain (1940):** Following the fall of France, Germany attempted to gain air superiority over Britain in preparation for an invasion. The Royal Air Force successfully defended the UK, marking the first major defeat for Hitler's military forces.

4. **Operation Barbarossa (1941):** On June 22, 1941, Germany launched a massive invasion of the Soviet Union. This campaign opened the Eastern Front, which became the largest and bloodiest theater of war in World War II.

5. **Battle of Stalingrad (1942-1943):** One of the deadliest battles in history, the Battle of Stalingrad was a turning point on the Eastern Front. The Soviet victory marked the beginning of a major offensive push against German forces.

6. **North African Campaign (1940-1943):** This series of battles involved the Allies and Axis powers fighting for control of North Africa. The decisive Allied victory at the Second Battle of El Alamein in 1942 marked the beginning of the end for Axis forces in Africa.

7. **Invasion of Italy (1943):** After the successful North African Campaign, the Allies invaded Sicily in July 1943 and then mainland Italy. This led to the fall of Mussolini's regime and Italy's eventual surrender, although fighting continued in Italy until 1945.

8. **D-Day and the Battle of Normandy (1944):** On June 6, 1944, Allied forces launched Operation Overlord, the largest amphibious invasion in history, landing on the beaches of Normandy, France. This marked the beginning of the liberation of Western Europe from Nazi occupation.

9. **Battle of the Bulge (1944-1945):** Germany's last major offensive on the Western Front took place in the Ardennes Forest. Despite initial successes, the Allies eventually repelled the German forces, leading to a rapid advance into Germany.

10. **Fall of Berlin (1945):** The final major offensive in Europe was the Soviet assault on Berlin in April 1945. The city fell on May 2, 1945, leading to the suicide of Adolf Hitler and the unconditional surrender of German forces.

The European war officially ended with Germany's unconditional surrender on May 7, 1945, which was ratified on May 8, known as Victory in Europe (VE) Day. This marked the end of World War II in Europe, although the war continued in the Pacific until Japan's surrender in September 1945.

Error message thrown by `assert_behavioral_match`:
```

```
E           llm_app_test.exceptions.test_exceptions.BehavioralAssertionError: Behavioral assertion failed: 
Behavioral Assertion Failed:  - Reason: The actual output focuses primarily on the European Theater of World War II, 
rather than providing a narrative about the global nature of the war.
```

### What This Example Demonstrates

1. Real Application Testing
    - Tests an actual LLM-based application

2. Behavioral Testing Power
    - The bot provides a detailed, accurate response
    - However, the test fails because it doesn't meet the expected behavior
    - Shows how behavioral testing catches incorrect behavior from your app

3. Clear Error Messages
    - The error clearly explains why the test failed
    - Points to specific behavioral mismatch
    - Helps developers understand what needs to change

## Documentation

Full documentation available at: [https://Shredmetal.github.io/llmtest/](https://Shredmetal.github.io/llmtest/)

- Installation Guide
- Quick Start Guide
- API Reference
- Best Practices
- CI/CD Integration
- Configuration Options

## License

MIT

## Reporting Issues
If you encounter issues:
1. Create an issue on our GitHub repository
2. Include your Python version and environment details
3. Describe the problem you encountered with version 0.1.0b4

## 🆘 Support
- Discord: [Join our community](https://discord.gg/awy83bZsKf)
- Issues: [GitHub Issues](https://github.com/Shredmetal/llmtest/issues)
- Documentation: [Full Docs](https://shredmetal.github.io/llmtest/)
- Email: morganj.lee01@gmail.com

## Due to the number of downloads I am seeing on pypistats.org, I am including these instructions in case a beta update breaks something on your end:

### Emergency Rollback Instructions

If you experience issues with version 0.2.0b1, you can roll back to the previous stable version (0.1.0b4) using one of these methods:

#### Method 1: Direct Installation of Previous Version

```
pip uninstall llm-app-test 
pip install llm-app-test==0.1.0b4
```
#### Method 2: Force Reinstall (if Method 1 fails)

```
pip install --force-reinstall llm-app-test==0.1.0b4
```
#### Verification
After rolling back, verify the installation:
```
import llm_app_test 
print(llm_app_test.version) # Should show 0.1.0b4
```

## ⚠️ Important Note About Rate Limits - If Running Large Numbers of Tests:

### Anthropic Rate limits:

Tier 1:

| Model                        | Maximum Requests per minute (RPM) | Maximum Tokens per minute (TPM) | Maximum Tokens per day (TPD) |
|------------------------------|-----------------------------------|---------------------------------|------------------------------|
| Claude 3.5 Sonnet 2024-10-22 | 50                                | 40,000                          | 1,000,000                    |
| Claude 3.5 Sonnet 2024-06-20 | 50                                | 40,000                          | 1,000,000                    |
| Claude 3 Opus                | 50                                | 20,000                          | 1,000,000                    |


Tier 2:

| Model                        | Maximum Requests per minute (RPM) | Maximum Tokens per minute (TPM) | Maximum Tokens per day (TPD) |
|------------------------------|-----------------------------------|---------------------------------|------------------------------|
| Claude 3.5 Sonnet 2024-10-22 | 1,000                             | 80,000                          | 2,500,000                    |
| Claude 3.5 Sonnet 2024-06-20 | 1,000                             | 80,000                          | 2,500,000                    |
| Claude 3 Opus                | 1,000                             | 40,000                          | 2,500,000                    |

### OpenAI Rate Limits

Tier 1

| Model                   | RPM | RPD    | TPM     | Batch Queue Limit |
|-------------------------|-----|--------|---------|-------------------|
| gpt-4o                  | 500 | -      | 30,000  | 90,000            |
| gpt-4o-mini             | 500 | 10,000 | 200,000 | 2,000,000         |
| gpt-4o-realtime-preview | 100 | 100    | 20,000  | -                 |
| gpt-4-turbo             | 500 | -      | 30,000  | 90,000            |


Tier 2:

| Model                   | RPM   | TPM       | Batch Queue Limit |
|-------------------------|-------|-----------|-------------------|
| gpt-4o                  | 5,000 | 450,000   | 1,350,000         |
| gpt-4o-mini             | 5,000 | 2,000,000 | 20,000,000        |
| gpt-4o-realtime-preview | 200   | 40,000    | -                 |
| gpt-4-turbo             | 5,000 | 450,000   | 1,350,000         |