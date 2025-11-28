
Requirement Analysis — Mini E-Commerce Testing

Project: QA — Mini E-Commerce Testing
AUT: https://automationexercise.com

Author: Utkarsh Alhat
Date: 25th Nov 2025

1. Purpose

This document lists the functional and non-functional requirements, high-level modules, actors, test data needs, assumptions, and constraints for QA testing of the AutomationExercise demo e-commerce website.

2. Scope

In scope

User registration and login

Product search, listing and product detail

Add to cart, update quantity, remove from cart

Checkout flow (shipping details, order placement)

Order confirmation and (if available) order history

Cross-browser verification (Chrome, Firefox)

Out of scope

Payment gateway integration (do not perform real payments)

Performance, load, and stress testing

Security and penetration testing

Accessibility (can be added later)

3. Actors

Guest user — visits site without logging in

Registered user — user with an account

Admin — (not used; site is demo only)

System — e-commerce application (AUT)

4. High-level Modules

Home / Landing page

Signup / Registration

Login / Logout

Product Search

Product Listing / Filtering (if available)

Product Detail Page (PDP)

Cart / Cart Management

Checkout / Shipping Details

Order Confirmation / Order Summary

Account / Order History (if available)

5. Functional Requirements (FR)

FR-01 — Registration

The system shall allow a user to register with name and unique email.

The system shall validate email format and mandatory fields.

FR-02 — Login

The system shall allow registered users to login using email and password.

The system shall show an error message for invalid credentials.

FR-03 — Search

The system shall allow searching products by name and return relevant results.

FR-04 — Product Detail

The system shall display product name, price, description, and Add to Cart button on PDP.

FR-05 — Cart Management

The system shall allow adding items to cart, updating quantity, and removing items.

The system shall recalculate totals correctly when quantity changes.

FR-06 — Checkout

The system shall collect shipping details (name, address, city, zip, country, phone).

The system shall validate mandatory fields and show inline errors.

On successful checkout, the system shall display an order confirmation with order id/summary.

FR-07 — Order History

The system shall allow users to view past orders (if supported by AUT).

6. Non-Functional Requirements (NFR)

NFR-01: The website should load main pages within 5 seconds on a stable connection.

NFR-02: Core flows (login, add to cart, checkout) should function correctly on Chrome and Firefox latest stable versions.

NFR-03: Error messages should be clear and actionable.

7. Test Data Requirements

Valid email addresses (use testuser+<timestamp>@mail.com pattern).

Valid passwords (min length as required by site).

Sample shipping addresses (name, address, city, zip, country, phone).

Product names to search (e.g., Dress, T-Shirt, Jeans).

Invalid inputs for negative tests (invalid email formats, empty mandatory fields, extremely long strings).

8. Acceptance Criteria (for testing)

All Critical test cases pass (Login, Add to Cart, Checkout success).

No Critical or High severity open defects at time of sign-off.

Test coverage for planned modules completed and RTM updated.

9. Environment & Configuration

AUT URL: https://automationexercise.com

Browsers: Chrome (latest), Firefox (latest)

OS: Windows 10 / Ubuntu 22.04 / macOS (tests may be run on any)

Tools: Manual test cases in Google Sheets / Excel; Selenium (optional); GitHub for repo

10. Constraints & Assumptions

The AUT is a public demo site — availability is not guaranteed.

Do not perform destructive tests that may alter global demo data.

Test accounts can be created but avoid spamming or automated mass account creation.

Payment flows will be mocked or skipped — do not use real payment cards.

11. Risks

Demo site downtime could block testing.

Flaky UI elements due to demo or CDN issues.

Test data conflicts if multiple testers use same test accounts.

12. Next steps (linked to test artifacts)

Create Test Plan (Test scope, tools, entry/exit criteria).

Create Test Scenarios and Test Cases.

Execute manual tests and log defects.

(Optional) Implement automation for smoke flows.