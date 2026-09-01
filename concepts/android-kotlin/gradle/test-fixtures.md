---
domain: android-kotlin
subdomain: gradle
concept: test-fixtures
title: Understanding Gradle #20 – Test Fixtures
sources:
  - title: "Understanding Gradle #20 – Test Fixtures"
    url: "https://www.youtube.com/watch?v=fSRN6YKa5B0"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2022-08-08T07:04:07+00:00"
---

# Understanding Gradle #20 – Test Fixtures

This video from the 'Understanding Gradle' series explains how to share code among tests in different projects or builds. The presenter, Jendrik Johannes, introduces the concept of test fixtures as a clean way to reuse test data and helper classes, contrasting it with the more ad-hoc approach of sharing test code between modules.

The video demonstrates a common scenario where test data creation code is needed in multiple test suites. Instead of duplicating this code or exposing it as a regular dependency, the 'java-test-fixtures' plugin provides a dedicated mechanism. This plugin creates a special 'test fixtures' feature variant that can be consumed by other modules' test compilation.

It also covers the idea of 'Tests as a Feature Variant', showing how Gradle treats test fixtures as a proper variant with its own dependencies and publication. The example on GitHub is provided in both Kotlin and Groovy DSL for the build scripts, allowing viewers to follow along. The video concludes with a summary of best practices for sharing test code in a maintainable way.

- Test fixtures allow sharing test-specific code (like data builders or utilities) across multiple projects or builds.
- Using the 'java-test-fixtures' plugin is preferable to simply depending on another module's test code, as it creates a dedicated, explicit variant.
- Test fixtures are modeled as a feature variant, making them a first-class citizen in Gradle's dependency management.
- The approach works with both Kotlin DSL and Groovy DSL, with example code available on GitHub.