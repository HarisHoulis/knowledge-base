---
domain: web-dev
subdomain: frontend-testing
concept: use-case-coverage
title: How to Know What to Test: Use Case Coverage Over Code Coverage
sources:
  - title: "How to know what to test"
    url: "https://kentcdodds.com/blog/how-to-know-what-to-test"
    author: "Kent C. Dodds"
    date: "2019-04-13"
---

# How to Know What to Test: Use Case Coverage Over Code Coverage

Kent C. Dodds argues that tests are written to gain confidence that an application will work when users use it, so what we test should map to enhancing that confidence. Rather than thinking about the code being tested, think about the use cases that code supports; this helps avoid testing implementation details (Dodds, 2019).

Code coverage can identify lines missing tests, but it does not show which use cases matter. In the arrayify example, adding tests for “returns an array if given an array,” “returns an empty array if given a falsy value,” and “returns an array with the given argument if it’s not an array and not falsy” brings coverage and captures intended behavior. Conversely, 100% code coverage can hide missing use-case coverage: if arrayify is implemented with `.filter(Boolean)`, two tests can cover all lines but miss the falsy-value use case, so a later refactor could break behavior without failing tests (Dodds, 2019).

In React, Dodds says not to test lifecycle methods, element event handlers, or internal component state as implementation details. Instead test observable effects for end users and developer users: user interactions via `userEvent`, changing props or context via `rerender`, and subscription changes (Dodds, 2019).

For an app, start by asking what part would make you most upset if broken, prioritize features, and write a single E2E happy-path test covering the most important use cases. Then add integration tests for edge cases and unit tests for complex business logic; do not chase 100% code coverage (Dodds, 2019).

- Tests should provide confidence that the app works for users; focus on use cases, not code or implementation details.
- Code coverage helps find untested lines but can hide missing use-case coverage when 100% line coverage is achieved without covering all intended behaviors.
- In React, test observable user and developer-user effects (userEvent, rerender, subscription changes) rather than lifecycle methods, event handlers, or internal state.
- Prioritize what would be worst to break, start with one E2E happy-path test, then add integration/unit tests for edge cases and complex logic.
- Avoid targeting 100% code coverage.