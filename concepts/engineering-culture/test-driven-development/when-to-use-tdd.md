---
domain: engineering-culture
subdomain: test-driven-development
concept: when-to-use-tdd
title: When I Follow TDD
sources:
  - title: "When I follow TDD"
    url: "https://kentcdodds.com/blog/when-i-follow-tdd"
    author: "Kent C. Dodds"
    date: "2020-06-29"
---

# When I Follow TDD

Kent C. Dodds explains his pragmatic approach to test-driven development (TDD), which he frames as the red-green-refactor cycle. He does not apply TDD universally but rather in situations where it brings clear benefits, such as fixing bugs, writing pure utility functions, and building well-defined user interfaces. For bug fixes, he reproduces the bug with a failing test first, which gives confidence that the fix actually addresses the issue. For pure functions with complex input/output logic, TDD helps ensure correctness against well-understood requirements.

- TDD is the red-green-refactor cycle: write a failing test, make it pass, then refactor with safety.
- Follow TDD for bug fixes to reproduce the bug and verify the fix with a test.
- Use TDD for pure utility functions when they are complex enough to need isolated unit tests.
- TDD works for well-defined UIs when tests focus on user behavior, not implementation details (e.g., with Testing Library).
- Avoid TDD in exploratory coding or when uncertain about the project's direction; the same applies to adding types and abstractions.