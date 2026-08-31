---
domain: android-kotlin
subdomain: gradle-build
concept: java-test-fixtures
title: Understanding Gradle #20 – Test Fixtures
sources:
  - title: "Understanding Gradle #20 – Test Fixtures"
    url: "https://www.youtube.com/watch?v=fSRN6YKa5B0"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2022-08-08T07:04:07+00:00"
---

# Understanding Gradle #20 – Test Fixtures

The video by Jendrik Johannes explains how to share code among tests in different Gradle projects or builds. It highlights the problem of duplicating test data creation code and introduces test fixtures as a clean solution. The java-test-fixtures plugin is presented as the tool to create a separate testFixtures source set, which is automatically exposed as a feature variant to consuming projects' test code only. This avoids the pitfalls of sharing test code through the main source set or by depending on another project's test source set, which can pollute production or cause coupling. The explanation includes a practical example available in both Kotlin and Groovy DSL on GitHub, showing how to set up and consume test fixtures. The video also touches on how tests act as a feature variant, enabling proper dependency management for test utilities.

- Test fixtures allow sharing test helpers and test data across modules without exposing them to production code.
- The java-test-fixtures plugin adds a testFixtures source set and creates a corresponding feature variant.
- Using test fixtures is preferable to depending on another module's test source set because it is explicit and avoids coupling issues.
- Consuming modules can access test fixtures only in their test compilation and runtime classpaths.
- The example repository demonstrates the setup using both Kotlin and Groovy DSL.