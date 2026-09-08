---
domain: java-tools
subdomain: unit-testing
concept: enum-parameterized-tests
title: Better Parameterized Tests with Burst
sources:
  - title: "Better Parameterized Tests with Burst"
    url: "https://developer.squareup.com/blog/better-parameterized-tests-with-burst"
    author: "Daniel Lubarov, Jake Wharton, and D. Koutsogiorgas"
---

# Better Parameterized Tests with Burst

The article introduces Burst, a Square library that provides an alternate data variation mechanism for JUnit tests. Unlike JUnit 4's Parameterized runner, which requires cumbersome object-array declarations for each parameter combination, Burst uses enums to generate test variations automatically from constructor or method parameters. This approach is type-safe and reduces boilerplate, making test failures easier to diagnose because the generated test hierarchy clearly shows which parameter combination failed.

- Burst automatically generates a test for each combination of enum parameters declared in a test constructor or method, eliminating the need for explicit arrays.
- It supports both class-level and method-level parameterization, unlike JUnit's Parameterized which only handles whole classes.
- A BurstAndroid runner is provided for JUnit 3-based Android tests, where built-in parameterization is unavailable.
- BurstAndroid can skip tests based on environment via isClassApplicable/isMethodApplicable, enabling annotations like @PhoneOnly or @TabletOnly.