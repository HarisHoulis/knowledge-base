---
domain: web-dev
subdomain: react-testing
concept: test-isolation
title: Test Isolation with React
sources:
  - title: "Test Isolation with React"
    url: "https://kentcdodds.com/blog/test-isolation-with-react"
    author: "Kent C. Dodds"
    date: "2018-07-02"
---

# Test Isolation with React

Kent C. Dodds argues that React tests sharing a single rendered component across multiple test cases create shared mutable state, making tests depend on each other and unreliable when run individually or refactored ([source](https://kentcdodds.com/blog/test-isolation-with-react)). In the opening example, tests rely on previous clicks to pass; skipping the click test breaks all following tests.

The first improvement is to render the component in `beforeEach` so each test gets its own instance, and React Testing Library automatically unmounts after each test. This makes tests isolated and lets any test be deleted or skipped without affecting others, at the cost of rendering per test—a tradeoff Dodds defends because of improved confidence and maintainability.

Next, Dodds prefers avoiding `beforeEach` and shared variables by using a custom render helper (e.g., `renderCounter`) that returns the needed queries per test, making each test visually and technically isolated. Finally, he recommends testing use cases rather than individual functionality: one test can make multiple assertions that follow the user's journey, such as allowing clicks until `maxClicks` is reached and then requiring a reset. Better error output and code frames make multi-assertion tests easier to debug.

Conclusion: keep tests isolated from one another and focus on use cases rather than functionality to improve reliability and confidence.

- Sharing a rendered component across tests creates mutable state and inter-test dependencies, so tests can't reliably run or be refactored in isolation.
- Render a fresh component per test via `beforeEach` or a custom helper, relying on React Testing Library to automatically unmount after each test.
- Avoid `beforeEach` and shared variables when possible; use a custom render helper that returns queries for each test.
- Prefer testing use cases (e.g., allows clicks until `maxClicks` is reached, then requires a reset) over isolated functionality; multiple assertions are acceptable with good error output.
- Isolated tests improve reliability, simplify test code, and increase confidence and maintainability.