import pytest
from llm_app_test.semantic_assert.semantic_assert import SemanticAssertion
from llm_app_test.exceptions.test_exceptions import (
    SemanticAssertionError
)


class TestRealWorldSemanticAssertion:
    """Test suite for semantic matching across diverse industry-specific LLM applications.

    This test class is specifically designed to validate semantic matching capabilities
    across a wide range of real-world LLM application outputs. It contains both positive
    and negative test cases that represent actual use cases where LLMs are being used
    in production environments.

    Industries Covered:
        - Healthcare (Patient Education)
        - Financial Services (Portfolio Reporting)
        - Media/Entertainment (Content Recommendations)
        - Legal (Document Summarization)
        - Manufacturing (Maintenance Prediction)
        - E-commerce (Product Descriptions)
        - Education (Assignment Feedback)
        - Real Estate (Property Listings)
        - Human Resources (Interview Feedback)
        - Customer Service (Ticket Response)

    Test Structure:
        - Each test validates specific industry requirements
        - Mix of positive and negative test cases
        - Focus on realistic content length and complexity
        - Industry-specific terminology and formatting
        - Comprehensive coverage of common LLM outputs

    Purpose:
        This test suite is designed for brute force reliability testing of the semantic
        matcher. It ensures the library can handle diverse, real-world content while
        maintaining consistent behavior across multiple test runs.

    Usage:
        These tests are intended to be run multiple times (1000+) to validate the
        consistency and reliability of the semantic matching functionality across
        different contexts and content types.
    """
    @pytest.fixture
    def asserter(self):
        return SemanticAssertion()


    def test_patient_education_diabetes_management(self, asserter):
        """Test semantic matching for patient education content about diabetes management. Failure is expected because
        this does not contain emergency response steps."""
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
        4. Provide clear warning signs and emergency response steps
        5. End with follow-up care instructions"""

        with pytest.raises(SemanticAssertionError) as excinfo:
            asserter.assert_semantic_match(actual, expected)
        assert "Semantic assertion failed" in str(excinfo.value)

    def test_investment_portfolio_report_generation(self, asserter):
        """Test semantic matching for investment portfolio report generation. Tests that the report
        contains all required sections and maintains professional financial terminology."""
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

        asserter.assert_semantic_match(actual, expected)

    def test_content_recommendation_missing_viewing_patterns(self, asserter):
        """Test semantic matching for content recommendations. Should fail due to missing viewing patterns
        and user preferences section."""
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

        with pytest.raises(SemanticAssertionError) as excinfo:
            asserter.assert_semantic_match(actual, expected)
        assert "Semantic assertion failed" in str(excinfo.value)

    def test_legal_document_summary_generation(self, asserter):
        """Test semantic matching for legal document summary generation. Tests that the summary
        maintains legal accuracy while being accessible to non-legal readers."""
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

        asserter.assert_semantic_match(actual, expected)

    def test_maintenance_prediction_missing_historical_context(self, asserter):
        """Test semantic matching for maintenance prediction report. Should fail due to
        missing historical maintenance context and pattern analysis."""
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

        with pytest.raises(SemanticAssertionError) as excinfo:
            asserter.assert_semantic_match(actual, expected)
        assert "Semantic assertion failed" in str(excinfo.value)

    def test_product_description_generation(self, asserter):
        """Test semantic matching for e-commerce product description generation. Tests that the description
        includes all required elements of an effective product listing."""
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

        asserter.assert_semantic_match(actual, expected)

    def test_assignment_feedback_missing_improvement_steps(self, asserter):
        """Test semantic matching for student assignment feedback. Should fail due to
        missing specific improvement steps and learning objectives."""
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

        with pytest.raises(SemanticAssertionError) as excinfo:
            asserter.assert_semantic_match(actual, expected)
        assert "Semantic assertion failed" in str(excinfo.value)

    def test_real_estate_listing_generation(self, asserter):
        """Test semantic matching for real estate listing generation. Tests that the listing
        includes all essential elements of an effective property description."""
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

        asserter.assert_semantic_match(actual, expected)

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

        with pytest.raises(SemanticAssertionError) as excinfo:
            asserter.assert_semantic_match(actual, expected)
        assert "Semantic assertion failed" in str(excinfo.value)

    def test_customer_service_ticket_response(self, asserter):
        """Test semantic matching for customer service ticket analysis and response generation."""
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

        asserter.assert_semantic_match(actual, expected)



