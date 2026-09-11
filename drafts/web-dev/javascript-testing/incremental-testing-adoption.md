---
domain: web-dev
subdomain: javascript-testing
concept: incremental-testing-adoption
title: How to Add Testing to an Existing Project
sources:
  - title: "How to add testing to an existing project"
    url: "https://kentcdodds.com/blog/how-to-add-testing-to-an-existing-project"
    author: "Kent C. Dodds"
    date: "2019-10-28"
---

# How to Add Testing to an Existing Project

The article addresses the overwhelming scenario of adding tests to a large, untested codebase that is already breaking in production. It advises applying the Testing Trophy principles by focusing first on the highest-ROI steps rather than trying to test everything at once (source).

Step 1 is to set up static tools: ESLint for linting, Prettier for formatting, and TypeScript or Flow for type checking. ESLint is the lowest-cost starting point and can be adopted incrementally by disabling broken rules and enabling others as warnings; type checkers are worth the effort but should not be blocked by imperfect types or fear of `any`/`unknown` (source).

Step 2 is to write a single E2E test covering an important user flow on production or a production-like environment, which acts like hiring a manual QA tester for every deploy. Step 3 is to write a single unit test for the simplest pure function to get tools configured. Step 4 expands to more tests, especially integration tests, once tooling is in place (source).

Step 5 is to teach the whole team how to test, ideally with TestingJavaScript.com licenses, to unify the testing strategy and save time deciding on approaches. The conclusion emphasizes that an incremental, confidence-infusing testing strategy helps you ship with less anxiety (source).

- Start with static tools (ESLint, Prettier, TypeScript/Flow); ESLint is the lowest-cost and most incrementally adoptable.
- Add one E2E test for a critical user flow on production or a production-like environment, even if it is long or runs on a cron.
- Add one unit test for the simplest pure function to install and configure testing tools.
- Expand to more tests, especially integration tests, once tooling exists; the first comprehensive E2E test is highly valuable.
- Teach the whole team to test, ideally via TestingJavaScript.com, to unify the testing strategy.