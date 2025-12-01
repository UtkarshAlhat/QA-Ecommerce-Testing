📄 TEST SUMMARY REPORT — Mini E-Commerce Testing

Project: QA — Mini E-Commerce Testing
AUT: https://automationexercise.com

Tester: Utkarsh Alhat
Test Cycle: Round 1 (Manual Testing)
Date: 25th nov 2025

1. Objective

To validate core e-commerce functionalities such as Registration, Login, Search, Cart, and Checkout on AutomationExercise and ensure the major flows work correctly.

2. Test Scope

Included:

Signup & Login
Search
Product listing & detail
Add to cart & cart updates
Checkout & Order confirmation
Cross-browser (Chrome, Firefox)

Excluded:

Payment integration
Security & performance tests

3. Test Execution Summary

Execution Item	Count
Total Test Cases	20
Passed	10
Failed	10
Blocked	0
Not Executed	0
4. Defect Summary
Severity	Count
Critical	3
Major	5
Medium	2
Low	0

Total Bugs: 10
(Refer to Bug_Reports.xlsx for full info)

5. Major Defects Found

Checkout accepts empty mandatory fields (Critical)
Cart total does not update after quantity change (Critical)
Order ID missing on confirmation page (Major)
Login accepts invalid email formats (Major)

6. Overall Product Quality

The application has multiple major defects in critical flows like login validation, cart calculations, and checkout validation.

Stability Rating: Moderate
Reliability: Medium
User Impact: High (due to cart & checkout issues)

7. Recommendations

Fix critical cart and checkout validation issues immediately.
Add proper input validation for email and address fields.
Improve search relevancy.
Test responsiveness and mobile layout fixes.

8. Conclusion

Round 1 testing is completed.
Critical bugs exist → the product is not ready for production but suitable as a QA testing practice environment.
