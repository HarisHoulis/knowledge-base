---
domain: engineering-culture
subdomain: gradle-build-tooling
concept: test-fixtures
title: Understanding Gradle #20 – Test Fixtures
sources:
  - title: "Understanding Gradle #20 – Test Fixtures"
    url: "https://www.youtube.com/watch?v=fSRN6YKa5B0"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2022-08-08T07:04:07+00:00"
---

# Understanding Gradle #20 – Test Fixtures

This video explains how to share code among tests across different projects or builds using Gradle's test fixtures mechanism. The presenter, Jendrik Johannes, uses a simple example of code that creates test data to illustrate the problem: when multiple projects need the same test setup utilities, copying code or sharing the entire test source set becomes messy. He contrasts 'sharing test code' versus 'explicit test fixtures' as a cleaner, more maintainable approach (Jendrik Johannes, 2022).

The core idea is to treat tests as a feature variant of the project. Gradle's `java-test-fixtures` plugin adds a dedicated `TestFixtures` source set, which can be published and consumed by other projects. This allows a project to declare a dependency on another project's test fixtures using `testImplementation(testFixtures(project(":myproject")))`. By making test fixtures an explicit variant, Gradle ensures that the fixture code is only available to test compilations, not production code, and avoids the anti-pattern of exposing the whole test source set. The video also summarizes how this integrates with Gradle's source sets and feature variants (Jendrik Johannes, 2022).

- Test fixtures provide a clean way to share test setup code across projects without duplicating code or leaking the whole test source set.
- Gradle's `java-test-fixtures` plugin creates a `TestFixtures` source set that is automatically registered as a feature variant.
- Consumers can depend on another project's test fixtures using the syntax `testImplementation(testFixtures(project(":project")))`.
- Test fixtures are compiled separately and used only in the test implementation of the consuming project.
- The approach builds on Gradle's existing source set and feature variant concepts, making it a natural and scalable pattern.