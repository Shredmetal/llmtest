[← Back to Home](../index.md)

# Quick Start

Get up and running with llm-app-test in under 5 minutes.

## 1. Set Up Environment

Create a `.env` file in your project root:

```
# For OpenAI
OPENAI_API_KEY=your-openai-api-key-here

# OR for Anthropic
ANTHROPIC_API_KEY=your-anthropic-key-here
```

## 2. Write Your First Test

```

from llm_app_test.behavioral_assert.behavioral_assert import BehavioralAssertion

def my_first_behavioral_test(): 
    # Initialize asserter 
    behavioral_assert = BehavioralAssertion()
    
    # Your LLM output
    actual_output = "The sky is blue"
    
    # Expected behavior in natural language
    expected_behavior = "A statement about the color of the sky"
    
    # Test behavioral equivalence
    behavioral_assert.assert_behavioral_match(
        actual=actual_output,
        expected_behavior=expected_behavior
    )
    
```

## 3. Run Your Test

```
pytest my_first_behavioral_test.py
```

## Next Steps

- [CI/CD Integration](../guides/ci-cd.md) - Set up automated testing
- [Configuration](../api/configuration.md) - Configure llm_app_test for your needs

## Additional notes:

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

Actual bot response from one run:

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
E           llm_app_test.exceptions.test_exceptions.BehavioralAssertionError: Behavioral assertion failed: 
Behavioral Assertion Failed:  - Reason: The actual output focuses primarily on the European Theater of World War II, 
rather than providing a narrative about the global nature of the war.
```

### What This Example Demonstrates

1. Real Application Testing
    - Tests an actual LLM application

2. Behavioral Testing Power
    - The bot provides a detailed, accurate response
    - However, the test fails because it doesn't meet the expected behavior
    - Shows how behavioral testing catches incorrect behavior from your app

3. Clear Error Messages
    - The error clearly explains why the test failed
    - Points to specific behavioral mismatch
    - Helps developers understand what needs to change

## Next Steps

- [CI/CD Integration](../guides/ci-cd.md) - Set up automated testing
- [Configuration](../api/configuration.md) - Configure llm-app-test for your needs
- [Behavioral Testing Reliability](../reliability_testing/behavioral_testing_reliability.md) - Learn about testing at scale

## Navigation

- [Back to Home](../index.md)
- [Installation Guide](../getting-started/installation.md)
- [Configuration](../api/configuration.md)
- [API Reference](../api/behavioral-assertion.md)