# Testing Patterns

This guide demonstrates common behavioral testing patterns using llm-app-test. For API reference and syntax, see [API Documentation](../api/behavioral-assertion.md).

## Pattern: Basic Behavioral Testing

**Scenario:** Testing simple greeting behaviour

**Implementation:**

```python
actual = "Hello Alice, how are you today?" 
 
expected_behavior = """A polite greeting that:
    Addresses the person by name (Alice)
    Asks about their wellbeing"""

behavioral_assert.assert_behavioral_match(actual, expected_behavior)
```

**Result:** ✅ PASS

- Recognises personal address
- Identifies greeting context
- Validates wellbeing inquiry

## Pattern: Basic Behavioral Matching

**Scenario**: Testing simple factual statements

Implementation:

```python
actual = "The sky is blue"

expected_behavior = "A statement about the color of the sky"

behavioral_assert.assert_behavioral_match(actual, expected_behavior)
```
**Result:** ✅ PASS

- Shows direct behavioral matching
- Clear relationship between statement and expectation
- Passes when meaning aligns

## Pattern: Expected Behavioral Mismatch

**Scenario**: Validating behavioral mismatch detection

Implementation:

```python
actual = "The sky is blue"

expected_behavior = "A statement about the weather forecast"

behavioral_assert.assert_behavioral_match(actual, expected_behavior)
```
Result: ❌ FAIL

- Fails because the actual statement is about sky colour
- Expected behaviour asks for weather forecast information
- Demonstrates how behavioral mismatches are caught
- Shows when assertions will fail in your tests

## Pattern: Multilingual Behavioral Testing

**Scenario**: Testing behavioral understanding across languages

Implementation:

```python
actual = "Bonjour, comment allez-vous?"

expected_behavior = "A polite greeting asking about wellbeing"

behavioral_assert.assert_behavioral_match(actual, expected_behavior)
```
Result: ✅ PASS

- Demonstrates language-agnostic understanding
- Shows cross-language behavioral matching
- Validates international content handling

## Pattern: Technical Documentation Testing

**Scenario**: Testing technical concept explanations

Implementation:

```python
actual = """The TCP handshake is a three-way process where the client 
         sends SYN, server responds with SYN-ACK, and client confirms with ACK"""
         
expected_behavior = "An explanation of the TCP connection establishment process"

behavioral_assert.assert_behavioral_match(actual, expected_behavior)
```
Result: ✅ PASS

- Validates technical accuracy
- Handles specialised terminology
- Maintains precision in behavioral assessment

## Pattern: Contextual Disambiguation

**Scenario**: Testing understanding of ambiguous terms

Implementation:

```python
actual = "The bank was steep and covered in wildflowers"

expected_behavior = "A description of a riverbank or hillside, not a financial institution"

behavioral_assert.assert_behavioral_match(actual, expected_behavior)
```
Result: ✅ PASS

- Shows contextual understanding
- Handles ambiguous terms
- Validates specific meaning exclusions

## Pattern: Sentiment Analysis

**Scenario**: Testing subtle emotional content

Implementation:

```python
actual = "While the presentation wasn't perfect, it showed promise"

expected_behavior = "A constructive criticism with mixed but generally positive sentiment"

behavioral_assert.assert_behavioral_match(actual, expected_behavior)
```
Result: ✅ PASS

- Detects nuanced sentiment
- Understands mixed emotions
- Validates overall tone

## Pattern: Long-Form Content

**Scenario**: Testing comprehension of detailed explanations

Implementation:

```python
actual = """Machine learning is a subset of artificial intelligence 
         that enables systems to learn and improve from experience without 
         explicit programming. It focuses on developing computer programs 
         that can access data and use it to learn for themselves."""
         
expected_behavior = "A comprehensive definition of machine learning emphasizing autonomous learning and data usage"

behavioral_assert.assert_behavioral_match(actual, expected_behavior)
```
Result: ✅ PASS

- Handles longer text
- Maintains context
- Captures key concepts

## Pattern: Subtle Sentiment Mismatch

**Scenario**: Testing detection of subtle sentiment differences

Implementation:

```python
actual = "The project was completed on time, though there were some hiccups"

expected_behavior = "A statement expressing complete satisfaction with project execution"

behavioral_assert.assert_behavioral_match(actual, expected_behavior)
```
Result: ❌ FAIL

- Fails because actual statement indicates mixed satisfaction
- Expected behaviour suggests complete satisfaction
- Shows sensitivity to subtle emotional differences

## Pattern: Technical Context Mismatch

**Scenario**: Testing technical meaning precision

Implementation:

```python
actual = "The function returns a pointer to the memory address"

expected_behavior = "A description of a function that returns the value stored at a memory location"

behavioral_assert.assert_behavioral_match(actual, expected_behavior)
```
Result: ❌ FAIL

- Fails because returning a pointer is different from returning a stored value
- Shows precision in technical context
- Validates technical accuracy

## Pattern: Ambiguous Reference Testing

**Scenario**: Testing handling of context-dependent terms

Implementation:

```python
actual = "The bank processed the transaction after reviewing the account"

expected_behavior = "A description of a riverbank's geological formation process"

behavioral_assert.assert_behavioral_match(actual, expected_behavior)
```
Result: ❌ FAIL

- Fails because contexts are completely different
- Shows strong contextual understanding
- Validates semantic boundaries in behavioral matching

## Pattern: Temporal Context

**Scenario**: Testing time-based behavioral understanding

Implementation:

```python
actual = "I will have completed the task by tomorrow"

expected_behavior = "A statement about a task that was completed in the past"

behavioral_assert.assert_behavioral_match(actual, expected_behavior)
```
Result: ❌ FAIL

- Fails because of tense mismatch
- Shows temporal awareness
- Validates time context

## Pattern: Logical Implication

**Scenario**: Testing logical relationship understanding

Implementation:

```python
actual = "If it rains, the ground will be wet"

expected_behavior = "A statement indicating that wet ground always means it has rained"

behavioral_assert.assert_behavioral_match(actual, expected_behavior)
```
Result: ❌ FAIL

- Fails because of reversed logical implication
- Shows logical relationship understanding
- Validates causality direction

## Pattern: Multi-Step Reasoning

**Scenario**: Testing complex logical chains

Implementation:

```python
actual = """When water freezes, it expands by approximately 9% in volume. 
This expansion creates less dense ice that floats according to Archimedes' principle of displacement. 
Because Arctic sea ice is already floating in the ocean, its melting doesn't significantly affect sea levels - 
it's already displacing its weight in water. However, land-based glaciers in places like Greenland 
aren't currently displacing any ocean water. When these glaciers melt, they add entirely new water volume 
to the oceans, making them a primary contributor to sea level rise."""

expected_behavior = """A multi-step scientific explanation.
Must maintain logical consistency across all steps."""

behavioral_assert.assert_behavioral_match(actual, expected_behavior)
```
Result: ✅ PASS

- Handles complex logical chains
- Maintains consistency across steps
- Validates scientific reasoning

## Pattern: Nonsensical Content

**Scenario**: Testing handling of grammatically correct but meaningless content

Implementation:

```python
actual = "The colorless green ideas sleep furiously"

expected_behavior = "A grammatically correct but semantically nonsensical statement"

behavioral_assert.assert_behavioral_match(actual, expected_behavior)
```
Result: ✅ PASS

- Recognizes grammatical structure
- Identifies semantic nonsense
- Validates meta-understanding

## Pattern: Extended Narrative

**Scenario**: Testing long-form narrative understanding

Implementation:

```python
actual = """
        The Roman Empire's rise began with modest origins in central Italy. What started as a small 
        settlement along the Tiber River would eventually become one of history's most influential 
        civilizations. In the early days, Rome was ruled by kings, but this system was overthrown 
        in 509 BCE, giving birth to the Roman Republic.

        During the Republic, Rome expanded its territory through military conquest and diplomatic 
        alliances. The Roman army became increasingly professional, developing innovative tactics 
        and technologies. This military success brought wealth and power, but also internal 
        challenges. Social tensions grew between patricians and plebeians, leading to significant 
        political reforms.

        By the 1st century BCE, the Republic faced severe internal strife. Military commanders 
        like Marius, Sulla, and eventually Julius Caesar accumulated unprecedented power. Caesar's 
        crossing of the Rubicon in 49 BCE marked a point of no return. His assassination in 44 BCE 
        led to another civil war, ultimately resulting in his adopted heir Octavian becoming 
        Augustus, the first Roman Emperor.

        Augustus transformed Rome into an empire while maintaining a facade of republican 
        institutions. He implemented sweeping reforms in administration, military organization, 
        and public works. The Pax Romana that followed brought unprecedented peace and prosperity 
        across the Mediterranean world. Trade flourished, cities grew, and Roman culture spread 
        throughout the empire.
        """

expected_behavior = """A historical narrative that:
1. Maintains chronological progression
2. Shows cause-and-effect relationships
3. Develops consistent themes (power, governance, military)
4. Connects multiple historical events coherently
5. Demonstrates character development (e.g., Caesar to Augustus)
"""

behavioral_assert.assert_behavioral_match(actual, expected_behavior)

```
Result: ✅ PASS

- Handles extended narratives
- Maintains thematic consistency
- Validates complex relationships
- Shows chronological understanding

## Pattern: Emoji Quantity Testing

**Scenario**: Testing recognition of repeated emojis

Implementation:

```python
actual = "🤖" * 100

expected_behavior = "A lot of emojis"

behavioral_assert.assert_behavioral_match(actual, expected_behavior)
```

Result: ✅ PASS

- Handles repeated Unicode characters
- Recognises quantity concepts
- Validates emoji processing

## Pattern: Emoji Quantity Mismatch

**Scenario**: Testing quantity recognition accuracy

Implementation:

```python
actual = "🤖" * 100

expected_behavior = "Only a few emojis"

behavioral_assert.assert_behavioral_match(actual, expected_behavior)
```
Result: ❌ FAIL

- Fails due to quantity mismatch
- Shows quantity awareness
- Validates numerical understanding

## Pattern: Mixed Unicode Content ⚠️ Known Reliability Issue

**Scenario**: Testing complex Unicode combinations and repetitive patterns

### Observed Behavior

**Test Case 1: Strict Pattern Matching**

```python
actual = "🤖👾" * 50 + "こんにちは" * 20 + "🌈" * 30

expected_behavior = "A mix of emojis and Japanese text"

behavioral_assert.assert_behavioral_match(actual, expected_behavior)
```

**Results**:

- ✅ Success Rate: 96% (48/50 runs)
- ❌ Failure Rate: 4% (2/50 runs)
- 🔍 Failure Analysis:
    - Occurs primarily during increased API latency
    - GPT-4o occasionally interprets sequential patterns as "distinct collections" rather than "mixed content"
    - Failure message example: "This is not a mix as there is a distinct collection of emojis followed by Japanese text and then a collection of rainbows"

### Recommended Implementation

**Test Case 2: Pattern-Agnostic Matching**

```python
actual = "🤖👾" * 50 + "こんにちは" * 20 + "🌈" * 30

expected = "More than one type of emoji and Japanese text regardless of order"

behavioral_assert.assert_behavioral_match(actual, expected_behavior)
```

**Results**:

- ✅ Success Rate: 100% (preliminary)
- ⚠️ Extended testing in progress
- 🔍 Monitoring prompt effectiveness across different test scenarios

### Best Practices
1. Use pattern-agnostic assertions for repetitive Unicode content
2. Consider implementing retry logic for critical tests
3. Monitor API response times during failures
4. Use enhanced prompts for complex Unicode pattern testing

### Ongoing Investigation
- Testing various prompt configurations to improve reliability
- Monitoring performance impact of different prompt strategies
- Collecting data on failure patterns with different prompt versions

## Pattern: Multilingual Emoji Spam

**Scenario**: Testing repeated multilingual content

Implementation:

```python
actual = "Hello你好Bonjour🌈" * 50

expected_behavior = "A repetitive greeting in multiple languages with rainbows"

behavioral_assert.assert_behavioral_match(actual, expected_behavior)
```
Result: ✅ PASS

- Handles multilingual text
- Recognises repetitive patterns
- Validates mixed content types

## Pattern: ASCII Art Recognition

**Scenario**: Testing complex ASCII art patterns

Implementation:

```python
actual = """
(╯°□°)╯︵ ┻━┻
""" * 20

expected_behavior = "Multiple instances of table-flipping ASCII art"

behavioral_assert.assert_behavioral_match(actual, expected_behavior)
```
Result: ✅ PASS

- Recognises ASCII art patterns
- Understands visual representations
- Validates repeated patterns

## Pattern: Extreme Whitespace

**Scenario**: Testing handling of excessive spacing

Implementation:

```python
actual = "hello    " + " " * 1000 + "    world" + "\n" * 500

expected_behavior = "A greeting with excessive spacing"

behavioral_assert.assert_behavioral_match(actual, expected_behavior)
```
Result: ✅ PASS

- Handles extreme whitespace
- Maintains semantic meaning
- Validates text normalisation

## Pattern: Number Pattern Recognition

**Scenario**: Testing numerical pattern understanding

Implementation:

```python
actual = "".join([str(i % 10) for i in range(1000)])

expected_behavior = "A long sequence of repeating numbers"

behavioral_assert.assert_behavioral_match(actual, expected_behavior)
```
Result: ✅ PASS

- Recognises numerical patterns
- Handles long repetitive sequences
- Validates pattern understanding

## Pattern: Patient Education Content Testing

**Scenario**: Testing medical education content for diabetes management

Implementation:

```python
actual = """
Understanding and Managing Type 2 Diabetes

Type 2 diabetes is a chronic condition that affects how your body processes blood sugar (glucose). 
While this condition is serious, it can be effectively managed through lifestyle changes and, 
when necessary, medication. This guide will help you understand the key aspects of diabetes 
management.

Blood Sugar Monitoring:
Regular blood sugar monitoring is essential. Your target blood glucose levels should typically 
be 80-130 mg/dL before meals and less than 180 mg/dL two hours after meals. However, your 
healthcare provider may set different targets based on your individual needs. Keep a log of 
your readings to identify patterns and adjust your management strategy accordingly.

Dietary Considerations:
A balanced diet is crucial for managing type 2 diabetes. Focus on:
- Controlling portion sizes
- Choosing high-fiber, low-glycemic foods
- Limiting refined carbohydrates and processed sugars
- Including lean proteins and healthy fats
- Spacing meals evenly throughout the day

Physical Activity:
Regular exercise helps control blood sugar levels by improving insulin sensitivity. Aim for:
- At least 150 minutes of moderate-intensity aerobic activity weekly
- Resistance training 2-3 times per week
- Daily movement, even if just short walks
Always check your blood sugar before and after exercise, and carry a fast-acting 
carbohydrate source.

Medication Management:
If prescribed, take diabetes medications as directed. Common medications include:
- Metformin (helps reduce glucose production)
- Sulfonylureas (increase insulin production)
- DPP-4 inhibitors (help maintain blood sugar control)
Never adjust or stop medications without consulting your healthcare provider.

Warning Signs:
Learn to recognize and respond to:
- Hypoglycemia (low blood sugar): shakiness, sweating, confusion
- Hyperglycemia (high blood sugar): increased thirst, frequent urination, fatigue
Seek immediate medical attention if you experience severe symptoms or sustained 
high blood sugar levels.

Regular Health Monitoring:
Schedule regular check-ups with your healthcare team, including:
- HbA1c tests every 3-6 months
- Annual eye examinations
- Regular foot checks
- Kidney function tests
- Cholesterol level monitoring

Remember, diabetes management is a journey, not a destination. Small, consistent 
steps in the right direction can lead to significant improvements in your health 
and quality of life.
"""

expected = """A medical education document that must:
1. Contain an overview section explaining the condition
2. List specific numerical guidelines (blood sugar ranges, exercise minutes)
3. Include structured sections for diet, exercise, and medication
4. Provide clear warning signs AND detailed emergency response procedures
5. End with follow-up care instructions"""
        
behavioral_assert.assert_behavioral_match(actual, expected_behavior)       
```
Result: ❌ FAIL

- Fails because emergency response procedures are missing
- Fails because follow-up care instructions are incomplete
- Shows precision in medical content requirements
- Validates structured information presentation

## Pattern: Investment Portfolio Report Testing

**Scenario**: Testing professional investment portfolio report generation

Implementation:

```python
actual = """
Q4 2023 Portfolio Performance Summary

Portfolio Overview:
Your investment portfolio has demonstrated resilient performance during Q4 2023, 
achieving a total return of 8.2% against our benchmark index return of 7.5%. 
Total portfolio value stands at $1,245,000 as of December 31, 2023.

Asset Allocation Analysis:
Current allocation stands at:
- Equities: 65% ($809,250)
  - US Large Cap: 40% ($498,000)
  - International Developed: 15% ($186,750)
  - Emerging Markets: 10% ($124,500)
- Fixed Income: 25% ($311,250)
  - Government Bonds: 15% ($186,750)
  - Corporate Bonds: 10% ($124,500)
- Alternative Investments: 10% ($124,500)
  - Real Estate: 5% ($62,250)
  - Commodities: 5% ($62,250)

Performance Attribution:
Key contributors to performance:
1. US Technology sector outperformance (+12.3%)
2. Emerging Markets recovery (+9.1%)
3. Corporate Bond yield optimization (+4.2%)

Risk Metrics:
- Portfolio Beta: 0.85
- Sharpe Ratio: 1.45
- Maximum Drawdown: -5.2%
- Standard Deviation: 12.3%

Rebalancing Recommendations:
Based on current market conditions and your investment objectives:
1. Consider increasing Fixed Income allocation by 2%
2. Reduce US Large Cap exposure by 3%
3. Increase Emerging Markets exposure by 1%

Market Outlook:
Looking ahead to 2024, we anticipate:
- Continued monetary policy normalization
- Potential emerging markets opportunities
- Heightened focus on quality factors in equity selection

Next Steps:
1. Schedule quarterly review meeting
2. Discuss rebalancing recommendations
3. Update investment policy statement if needed
"""

expected = """A professional investment portfolio report that must:
1. Present portfolio performance with specific metrics
2. Detail current asset allocation with percentages
3. Include risk analysis metrics
4. Provide forward-looking recommendations
5. Maintain formal financial terminology
6. Include clear next steps or action items"""

asserter.assert_behavioral_match(actual, expected)
```

Result: ✅ PASS

- Shows comprehensive financial reporting structure
- Validates precise numerical data presentation
- Confirms professional financial terminology
- Demonstrates clear action items and recommendations
- Verifies complete risk metric inclusion

## Pattern: Personalized Content Recommendation Testing

**Scenario**: Testing personalized content recommendation generation

Implementation:

```python
actual = """
Personalized Content Recommendations - User Profile #A1234
Generated: November 22, 2024

Recommended Content Queue:
1. "Climate Pioneers" (Documentary Series)
- Episode length: 45 minutes
- New episodes available

2. "Global Power Play" (Political Drama)
- Episode length: 55 minutes
- Features actors from previously watched content

3. "Earth's Tipping Points" (Scientific Documentary)
- Episode length: 40 minutes
- Recently added to platform

Engagement Optimization:
- Scheduled new episode alerts
- Downloadable content for offline viewing
- Similar content suggestions refreshed weekly
- Customized language preferences maintained

Content Accessibility:
All recommended content includes your preferred subtitle options and is 
available in HD quality. Downloads are enabled for offline viewing during 
your upcoming travel dates.
"""

expected = """A personalized content recommendation document that must:
1. Include the viewing patterns and preferences of the user
2. List recommended content with clear reasoning
3. Provide matching percentages or relevance metrics
4. Include viewing optimization suggestions
5. Address content accessibility features"""

asserter.assert_behavioral_match(actual, expected)
```

Result: ❌ FAIL

- Fails because relevance metrics (percentages) are missing
- Lacks explicit matching percentages or relevance scores
- Shows content recommendations without quantified relevance
- Demonstrates engagement optimization suggestions
- Validates content accessibility features

## Pattern: Legal Document Summary Testing

**Scenario**: Testing legal document summary generation

Implementation:

```python
actual = """
Contract Summary Analysis
Document Reference: MSA-2024-0892
Date of Analysis: November 22, 2024

Agreement Overview:
Software Development Master Services Agreement between TechCorp Inc. ("Provider") 
and GlobalEnterprises LLC ("Client") for the development and maintenance of 
enterprise software solutions.

Key Terms and Conditions:
1. Service Scope
- Custom software development services
- System integration capabilities
- Ongoing maintenance and support
- Security compliance implementations

2. Financial Terms
- Base development fee: $750,000
- Monthly maintenance: $15,000
- Change request rate: $200/hour
- Payment terms: Net 30

3. Performance Standards
- 99.9% system availability
- 4-hour response time for critical issues
- Monthly performance reporting
- Quarterly service reviews

4. Intellectual Property Rights
- Client owns all custom development
- Provider retains rights to pre-existing IP
- Joint ownership of derivative works
- Limited license for provider tools

5. Term and Termination
- Initial term: 36 months
- Automatic renewal: 12-month periods
- 90-day termination notice required
- Immediate termination for material breach

Risk Assessment:
- Medium risk: Data protection obligations
- Low risk: Service level commitments
- Low risk: IP ownership structure
- Medium risk: Change management process

Next Steps:
1. Legal team review of data protection terms
2. Technical team validation of SLAs
3. Finance approval of payment terms
4. Compliance review of security standards
"""

expected = """A legal document summary that must:
1. Identify key parties and document type
2. List main contractual terms
3. Include specific numerical values (costs, dates, metrics)
4. Provide risk assessment
5. Outline required actions or next steps"""

asserter.assert_behavioral_match(actual, expected)
```

Result: ✅ PASS

- Shows comprehensive legal document structure
- Validates precise contractual terms
- Confirms specific numerical values inclusion
- Demonstrates clear risk assessment
- Verifies actionable next steps

## Pattern: Maintenance Prediction Testing

**Scenario**: Testing maintenance prediction report generation for CNC equipment

Implementation:

```python
actual = """
Equipment Maintenance Analysis
Machine ID: CNC-1234
Analysis Date: November 22, 2024

Current Status Summary:
The CNC machine is showing early indicators of potential bearing wear in the main spindle.
Recommended action is to schedule maintenance within the next 2 weeks.

Operational Parameters:
- Current Runtime: 2,450 hours
- Average Daily Usage: 18 hours
- Last Maintenance: October 15, 2024

Immediate Recommendations:
1. Schedule bearing inspection
2. Monitor vibration levels daily
3. Prepare replacement parts
4. Plan for 4-hour maintenance window

Impact Assessment:
- Production Impact: Minimal if addressed within 2 weeks
- Resource Requirements: Standard maintenance team
- Parts Cost Estimate: $2,500
"""

expected = """A maintenance prediction report that must:
1. Include current machine status
2. Provide historical maintenance patterns
3. Show failure prediction confidence levels
4. List specific maintenance recommendations
5. Include impact assessment and timeline"""

asserter.assert_behavioral_match(actual, expected)
```
Result: ❌ FAIL

- Fails because historical maintenance patterns are incomplete
- Missing failure prediction confidence levels
- Shows current status and recommendations
- Includes basic impact assessment
- Demonstrates timeline considerations

## Pattern: E-commerce Product Description Testing

**Scenario**: Testing product description for a smart home security camera

Implementation:

```python
actual = """
Smart Home Security Camera - Model HC2000

Transform your home security with our latest AI-powered camera system. This next-generation 
device combines advanced motion detection with crystal-clear 4K video quality, perfect for 
both indoor and outdoor monitoring.

Key Features:
- 4K Ultra HD resolution with HDR
- 160° wide-angle view
- Advanced AI motion detection
- Two-way audio communication
- Night vision up to 30 feet
- Weather-resistant (IP66 rated)

Smart Integration:
Works seamlessly with major platforms including:
- Amazon Alexa
- Google Home
- Apple HomeKit
- IFTTT

Technical Specifications:
- Dimensions: 3.2" x 3.2" x 5.1"
- Weight: 12.3 oz
- Power: AC adapter or rechargeable battery
- Storage: Cloud or local SD card (up to 256GB)
- Connectivity: 2.4GHz/5GHz WiFi

What's in the Box:
- HC2000 Camera
- Mounting bracket
- Power adapter
- Quick start guide
- Screws and anchors

Perfect for:
- Home security
- Baby monitoring
- Pet watching
- Front door monitoring

30-day money-back guarantee
2-year manufacturer warranty
Free technical support
"""

expected = """An e-commerce product description that must:
1. Include clear product name and model
2. List key features and specifications
3. Specify technical details and compatibility
4. Describe package contents
5. Include warranty and support information"""

asserter.assert_behavioral_match(actual, expected)
```
Result: ✅ PASS

- Shows comprehensive product information structure
- Validates technical specifications inclusion
- Confirms compatibility details
- Demonstrates complete package contents listing
- Verifies warranty and support information

## Pattern: Assignment Feedback Testing

**Scenario**: Testing student assignment feedback generation

Implementation:

```python
actual = """
Assignment Feedback
Student ID: STU-2024-456
Assignment: Research Paper on Climate Change
Submission Date: November 22, 2024

Overall Assessment:
Your research paper demonstrates good understanding of climate change basics.
The writing is clear and well-structured, with appropriate use of scientific
terminology throughout the document.

Strengths:
- Strong introduction that sets context
- Good use of current scientific data
- Clear paragraph structure
- Proper citation format

Areas Noted:
- Some statistical interpretations could be more precise
- Additional peer-reviewed sources would strengthen arguments
- Conclusion could be more comprehensive

Grade: B+ (88/100)

Additional Comments:
The paper shows promise and indicates solid research skills. Your analysis
of temperature data trends was particularly well-done. Consider expanding
your discussion of potential mitigation strategies in future work.
"""

expected = """An assignment feedback document that must:
1. Include basic assignment and student information
2. Provide specific strengths and weaknesses
3. List concrete steps for improvement
4. Reference specific learning objectives
5. Include grading criteria and score"""

asserter.assert_behavioral_match(actual, expected)
```

Result: ❌ FAIL

- Fails because concrete improvement steps are missing
- Missing specific learning objectives
- Shows basic assignment information
- Includes strengths and weaknesses
- Demonstrates grading information

## Pattern: Real Estate Listing Testing

**Scenario**: Testing real estate property listing generation

Implementation:

```python
actual = """
Stunning Modern Oasis in Prime Location
123 Maple Avenue, Riverside Heights

Discover urban elegance in this meticulously updated contemporary home, where 
modern luxury meets practical living. This 2,400 sq ft residence seamlessly 
blends indoor and outdoor living spaces.

Property Highlights:
- 4 bedrooms, 2.5 bathrooms
- Built: 2018
- Lot size: 0.25 acres
- Two-car attached garage
- Energy-efficient smart home features

Interior Features:
The open-concept main level showcases:
- Chef's kitchen with quartz countertops
- Custom Italian cabinetry
- Premium stainless steel appliances
- Expansive living room with 12-foot ceilings
- Primary suite with spa-inspired bathroom

Outdoor Living:
- Professional landscaping
- Covered patio with built-in BBQ
- Low-maintenance xeriscaping
- Private backyard retreat

Location Benefits:
- Walking distance to Central Park
- Top-rated school district
- 10 minutes to downtown
- Easy access to major highways

Recent Updates:
- New HVAC system (2023)
- Smart home integration
- Updated LED lighting
- Fresh interior paint

Price: $875,000
Available for immediate viewing
Virtual tour link: [URL]
"""

expected = """A real estate listing that must:
1. Include property overview and key features
2. List specific amenities and updates
3. Describe location benefits
4. Use engaging, descriptive language
5. Provide essential details (size, bedrooms, price)"""

asserter.assert_behavioral_match(actual, expected)
```

Result: ✅ PASS

- Shows comprehensive property information
- Validates specific amenities and features
- Confirms location benefits inclusion
- Demonstrates engaging descriptive language
- Verifies essential property details

## Pattern: Interview Feedback Testing

**Scenario**: Testing interview feedback generation for technical position

Implementation:

```python
def test_interview_feedback_missing_criteria(self, asserter):
"""Test semantic matching for interview feedback generation. Should fail due to
missing evaluation criteria and specific examples."""
actual = """
Interview Feedback Summary
Candidate ID: INT-2024-789
Position: Senior Software Engineer
Interview Date: November 22, 2024

Overall Impression:
The candidate demonstrated strong technical knowledge and communicated well
throughout the interview. They showed enthusiasm for the role and our company's
mission.

Discussion Points:
- Previous experience with cloud architecture
- Team collaboration approaches
- Problem-solving methodology
- Career goals and aspirations

Technical Discussion:
Candidate showed familiarity with:
- Microservices architecture
- CI/CD pipelines
- Cloud platforms (AWS, Azure)
- Agile development practices

Cultural Fit:
Appears to align well with our company values and team dynamics.
Demonstrated good communication skills and collaborative mindset.

Next Steps:
Proceed with reference checks if moving forward.
Schedule follow-up with hiring manager.
"""

expected = """An interview feedback document that must:
1. Include candidate and position information
2. List specific evaluation criteria with ratings
3. Provide concrete examples of responses
4. Include technical assessment scores
5. Offer clear hiring recommendation"""

asserter.assert_behavioral_match(actual, expected)
```
Result: ❌ FAIL

- Fails because evaluation criteria lack ratings
- Missing concrete response examples
- Missing technical assessment scores
- Shows basic candidate information
- Lacks clear hiring recommendation

## Pattern: Customer Service Response Testing

**Scenario**: Testing customer service ticket response generation

Implementation:

```python
actual = """
Ticket Analysis and Response
Ticket ID: CS-2024-1122
Priority: Medium
Category: Product Return

Customer Query Summary:
Customer purchased a wireless headphone (Model: WH-1000XM4) three days ago
and is experiencing connectivity issues with their iPhone 13. Initial
troubleshooting steps were attempted without success.

Issue Analysis:
- Product is within return window (3 of 30 days)
- Common compatibility issue identified
- Troubleshooting already attempted
- Customer tone indicates frustration

Recommended Response:
Dear [Customer Name],

Thank you for reaching out about the connectivity issues with your WH-1000XM4
headphones. I understand how frustrating technical issues can be, especially
with a new purchase.

Based on your description, I can offer you two immediate solutions:

1. Advanced Troubleshooting:
- Reset the headphones (detailed steps attached)
- Update iPhone Bluetooth settings
- Install latest firmware

2. Hassle-free Return:
- Generate return label through our portal
- Full refund processed within 3 business days
- Free return shipping

Would you prefer to try the advanced troubleshooting steps, or would you like
to proceed with the return? I'm here to help with either option.

Next Steps:
- Await customer preference
- Prepare return label if requested
- Schedule follow-up within 24 hours

Response Tone: Empathetic and Solution-focused
Support Resources: KB-2345, RT-6789
"""

expected = """A customer service response that must:
1. Include ticket categorization and priority
2. Summarize the customer's issue accurately
3. Provide multiple solution options
4. Include clear next steps
5. Maintain appropriate tone and empathy"""

asserter.assert_behavioral_match(actual, expected)
```

Result: ✅ PASS

- Shows comprehensive ticket information structure
- Validates accurate issue summary
- Confirms multiple solution options
- Demonstrates clear next steps
- Verifies empathetic and professional tone