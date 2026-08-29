---
domain: android-kotlin
subdomain: build-tooling
concept: test-fixtures
title: Understanding Gradle #20 – Test Fixtures
sources:
  - title: "Understanding Gradle #20 – Test Fixtures"
    url: "https://www.youtube.com/watch?v=fSRN6YKa5B0"
    author: "Jendrik Johannes"
    date: "2022-08-08T07:04:07+00:00"
---

# Understanding Gradle #20 – Test Fixtures

In this video, Jendrik Johannes (2022) explains how to share code among tests in different projects or builds using Gradle's test fixtures feature. The example demonstrates code for creating test data and the alternatives of sharing test code versus using explicit test fixtures. The video highlights that test fixtures are exposed as a feature variant, enabling a clean dependency mechanism.

The core of the solution is the `java-test-fixtures` plugin. As Johannes (2022) shows, applying this plugin automatically creates a special `testFixtures` source set and a corresponding feature variant. This allows other projects to depend on the test fixtures through a dedicated `testFixtures` configuration, making the shared code explicit and manageable. The approach avoids the pitfalls of simply sharing the entire test source set, such as pulling in unwanted dependencies or mixing concerns.

The video also references related concepts like source sets, feature variants, and testing configuration, indicating that test fixtures are built upon these existing Gradle mechanisms. The summary emphasizes that this is the recommended way to share test utilities, builders, and sample data across projects, providing clear separation and reusability.

- The `java-test-fixtures` plugin creates a dedicated `testFixtures` source set for reusable test code.
- Test fixtures are exposed as a feature variant, allowing other projects to consume them via a `testFixtures` dependency configuration.
- Using explicit test fixtures is preferable to sharing the whole test source set, as it avoids unnecessary coupling.
- The feature enables clean sharing of test data builders, helpers, and mock objects across multiple Gradle projects.