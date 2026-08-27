---
domain: android-kotlin
subdomain: gradle-testing
concept: configuring-testing
title: Understanding Gradle #18 – Configuring Testing
sources:
  - title: "Understanding Gradle #18 – Configuring Testing"
    url: "https://www.youtube.com/watch?v=7f_gBvGQN_0"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2022-07-11"
---

# Understanding Gradle #18 – Configuring Testing

The video explains how Gradle's Java plugin provides a default testing setup: test code goes into the `src/test` source set, and the plugin registers a `test` task linked to that source set. To write and run tests, you must explicitly add a test framework as a dependency. By default, the test task is preconfigured for JUnit 4. To use JUnit 5, you configure the task with `useJUnitPlatform()` and add the appropriate engine dependencies — for example, the vintage engine to run existing JUnit 4 tests, and the Jupiter API to write JUnit 5 tests. The video also introduces the newer JVM test suites concept, which simplifies applying modern testing conventions.

- Gradle's Java plugin automatically creates a `test` source set and a `test` task, but you must add a test framework dependency.
- The default test task is configured for JUnit 4; switch to JUnit 5 with `useJUnitPlatform()`.
- Test dependencies use dedicated configurations like `testImplementation` and `testRuntimeOnly`.
- JUnit 5 is modular: you need the Jupiter API for JUnit 5 tests and can add the vintage engine for JUnit 4 compatibility.
- The new JVM test suites feature provides a simpler way to configure test setups compared to manually tweaking the `test` task.