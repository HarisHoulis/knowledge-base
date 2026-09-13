---
domain: engineering-culture
subdomain: automated-testing
concept: testing-trophy
title: Write tests. Not too many. Mostly integration.
sources:
  - title: "Write tests. Not too many. Mostly integration."
    url: "https://kentcdodds.com/blog/write-tests"
    author: "Kent C. Dodds"
    date: "2019-07-13"
---

# Write tests. Not too many. Mostly integration.

Kent C. Dodds expands on Guillermo Rauch's tweet "Write tests. Not too many. Mostly integration." He argues that automated tests are worth writing because they save maintenance time and catch bugs before production, though static typing and linting also provide confidence. However, even strongly typed languages need tests because typing cannot verify business logic. Dodds warns against mandating 100% code coverage: returns diminish beyond roughly 70% coverage, and chasing full coverage leads to testing trivial code or implementation details, which slows teams down and makes refactoring harder. Tests should rarely need to change when code is refactored.

- Write automated tests because they save time and catch bugs early, but do not mandate 100% coverage.
- Diminishing returns set in beyond roughly 70% coverage; avoid testing implementation details or trivial code.
- The Testing Trophy favors integration tests as the best trade-off between confidence and speed/expense.
- To write more integration tests, mock less; mocking removes confidence in the integration being tested.
- In React, avoid shallow rendering as part of favoring integration-level tests.