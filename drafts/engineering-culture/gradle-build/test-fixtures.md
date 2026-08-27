---
domain: engineering-culture
subdomain: gradle-build
concept: test-fixtures
title: Understanding Gradle #20 – Test Fixtures
sources:
  - title: "Understanding Gradle #20 – Test Fixtures"
    url: "https://www.youtube.com/watch?v=fSRN6YKa5B0"
    author: "Jendrik Johannes"
    date: "2022-08-08"
---

# Understanding Gradle #20 – Test Fixtures

This video from the 'Understanding Gradle' series explains how to share code among tests in different projects or builds using Gradle's test fixtures. The presenter, Jendrik Johannes, starts with a common scenario: code that creates test data is needed in multiple test suites. Instead of duplicating this code, Gradle allows it to be packaged as test fixtures. The video clarifies the difference between simply sharing test code and using explicit test fixtures, emphasizing that test fixtures are a dedicated part of the project's structure (Johannes, 2022).

Test fixtures are implemented as a feature variant of the project, similar to how main code and test code are variants. This means that other projects or subprojects can depend on the test fixtures of a project without pulling in the tests themselves. The `java-test-fixtures` plugin is introduced as the way to enable this mechanism in Gradle. With this plugin, a separate `testFixtures` source set is created, and dependencies can be declared on that source set from other projects. The video summarizes that test fixtures provide a clean and explicit way to share test-related code across builds, improving maintainability and reducing duplication (Johannes, 2022).

- Test fixtures allow sharing test data creation code across projects or builds.
- Test fixtures are implemented as a feature variant, distinct from main and test source sets.
- The `java-test-fixtures` plugin creates a dedicated `testFixtures` source set.
- Other projects can depend on test fixtures explicitly, without including actual tests.