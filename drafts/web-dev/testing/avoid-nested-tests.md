---
domain: web-dev
subdomain: testing
concept: avoid-nested-tests
title: Avoid Nesting when you're Testing
sources:
  - title: "Avoid Nesting when you're Testing"
    url: "https://kentcdodds.com/blog/avoid-nesting-when-youre-testing"
    author: "Kent C. Dodds"
    date: "2019-07-29"
---

# Avoid Nesting when you're Testing

In "Avoid Nesting when you're Testing," Kent C. Dodds argues that nested `describe` blocks with `beforeEach` hooks encourage using test hooks as a mechanism for code reuse, which leads to unmaintainable tests. He demonstrates this with a React `Login` component test suite where variables like `handleSubmit`, `user`, and `errorMessage` are defined and reassigned across nested scopes, forcing readers to trace variable values over time (Dodds, 2019).

To avoid this, Dodds recommends inlining test setup and actions so each test is self-contained. He shows a rewritten suite using separate `test` calls without `describe` nesting, noting that duplication is acceptable for simple tests and that removing abstraction improves readability (Dodds, 2019).

For cases needing shared setup, he applies the AHA (Avoid Hasty Abstractions) principle: prefer duplication over the wrong abstraction and optimize for change first. He suggests using composable setup functions that return values instead of mutable `beforeEach` variables, and grouping tests by file rather than `describe` blocks. He also cautions that cleanup utilities like `afterEach` may still be needed when tests modify global state, though the example predates automatic cleanup in @testing-library/react@9 (Dodds, 2019).

- Nested `describe`/`beforeEach` tests with mutable variables force readers to trace variable definitions and reassignments across multiple scopes, increasing cognitive load.
- Prefer inlining test setup and actions in each test to keep tests self-contained and readable; avoid unnecessary abstraction for small suites.
- Apply AHA (Avoid Hasty Abstractions): prefer duplication over the wrong abstraction and optimize for change first.
- When sharing is needed, use composable setup functions that return values instead of mutable `beforeEach` variables.
- Group tests by file rather than `describe` blocks, and use `afterEach`/cleanup when tests modify global state; note example predates automatic RTL cleanup.