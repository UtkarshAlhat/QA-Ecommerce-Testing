
📄 TEST PLAN — Mini E-Commerce Testing

Project: QA — Mini E-Commerce Testing
AUT: https://automationexercise.com

Author: Utkarsh Alhat
Date: 25th Nov 2025

1. Introduction

This Test Plan defines the scope, approach, resources, schedule, and deliverables for testing the e-commerce demo website AutomationExercise.

2. Objectives

Validate key functional flows of the application.

Ensure major modules work as expected (login, search, cart, checkout).

Identify defects, log them, and ensure critical defects are addressed.

Provide confidence in the stability and usability of the AUT.

3. Scope of Testing
In Scope

Registration & Login

Product search

Product listing & product detail

Add to cart, update quantity, remove from cart

Checkout flow

Order confirmation

Cross-browser check on Chrome & Firefox

Out of Scope

Payment processing (no real payments)

Performance testing

Security testing

Database testing

Non-user-facing API testing

Accessibility testing

4. Test Approach
Manual Testing

Functional testing

UI/UX testing

Positive & negative testing

Boundary value testing

Regression testing

Cross-browser testing

Automation Testing (Optional)

Automate smoke test cases using Selenium + Python / Playwright.

Generate HTML reports.

5. Testing Types

Functional Testing

Smoke Testing

Regression Testing

Negative Testing

Boundary Value Analysis (BVA)

Equivalence Partitioning (EP)

Usability Testing

Cross-browser Testing

6. Test Deliverables

Requirement Analysis document

Test Plan

Test Scenarios

Test Cases

Bug Reports

RTM (Traceability Matrix)

Test Summary Report

Automation scripts (if applicable)

HTML automation report (optional)

7. Entry Criteria

AUT is accessible and stable

Requirement Analysis completed

Test Plan finalized

Test Scenarios prepared

Test data prepared

Test environment ready (browser installed)

8. Exit Criteria

All critical test cases executed

All critical and high-severity bugs fixed or closed

Test Summary Report submitted

No major open risks

RTM updated and complete

9. Risks & Mitigations
Risk	Mitigation
Demo site downtime	Retry later, adjust test execution timeline
Flaky UI elements	Re-run test case, record behavior carefully
Multiple users creating test data	Use timestamp emails
Browser compatibility issues	Retest on latest versions
10. Test Environment

OS: Windows 10 / Linux / macOS

Browsers: Chrome (latest), Firefox (latest)

Tools: VS Code, Excel/Google Sheets, Lightshot, GitHub

Automation: Python, Selenium, PyTest (optional)

11. Tools & Resources

Manual testing: Excel/Google Sheets

Bug tracking: GitHub Issues (or Notion/Trello)

Automation: Selenium + Python (optional)

Code editor: VS Code

Version control: Git & GitHub

12. Roles & Responsibilities
Role	Responsibility
QA Engineer (You)	Prepare documents, execute tests, log defects, write automation scripts
13. Schedule (Tentative)
Task	Duration
Requirement Analysis	1 day
Test Plan	1 day
Scenarios & Test Cases	2–3 days
Manual execution	2–3 days
Bug reporting	Parallel
Automation (optional)	3–5 days
Final summary	1 day
14. Approval

Test Plan reviewed and approved for execution by the QA Engineer (self-approved for portfolio).