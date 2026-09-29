---
domain: web-dev
subdomain: javascript-testing
concept: common-testing-mistakes
title: Common Testing Mistakes
sources:
  - title: "Common Testing Mistakes"
    url: "https://kentcdodds.com/blog/common-testing-mistakes"
    author: "Kent C. Dodds"
    date: "2018-11-12"
---

# Common Testing Mistakes

Kent C. Dodds outlines three common testing mistakes: testing implementation details, chasing 100% code coverage, and repeat testing in E2E suites. He argues the purpose of testing is confidence, so any practice that does not increase confidence should be reconsidered (Common Testing Mistakes).

Testing implementation details is harmful because it allows the code to break without failing the test—e.g., a typo in an onClick handler—and causes tests to fail during refactors such as renaming a method. Such tests are high-maintenance and low-confidence (Common Testing Mistakes).

For code coverage, Dodds says 100% coverage is a mistake for applications. Coverage only tells you that code ran; it does not prove business requirements, integration correctness, or that the app cannot enter a bad state. It also weights every covered line equally, so testing an About page can boost coverage as much as testing checkout. He recommends identifying critical parts first, then using coverage to find missing edge cases; 100% is appropriate for small, isolated open-source modules (Common Testing Mistakes).

On E2E tests, Dodds warns against repeating registration/login flows for every test. Since tests should be isolated, each test needs a new user, but only one test needs to exercise the actual happy-path registration flow to gain confidence. Other tests should make the same HTTP calls the app makes during registration/login, which is faster and less brittle (Common Testing Mistakes).

- Testing implementation details can let real bugs pass and cause false failures during refactoring, so tests should focus on behavior that gives confidence.
- 100% code coverage is a poor goal for applications because coverage only shows code was executed, not that requirements, integration, or bad states are handled.
- Prioritize coverage of critical paths like checkout over trivial pages, and use coverage reports after identifying critical areas.
- In E2E tests, avoid repeating registration/login flows; use direct HTTP calls for setup and keep one test that actually exercises the flow.
- Testing is about confidence—if a test action does not add confidence, consider stopping it.