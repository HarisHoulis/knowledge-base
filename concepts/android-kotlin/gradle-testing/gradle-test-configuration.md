---
domain: android-kotlin
subdomain: gradle-testing
concept: gradle-test-configuration
title: Configuring Testing in Gradle
sources:
  - title: "Understanding Gradle #18 – Configuring Testing"
    url: "https://www.youtube.com/watch?v=7f_gBvGQN_0"
    author: "Jendrik Johannes"
    date: "2022-07-11T14:37:15+00:00"
---

# Configuring Testing in Gradle

This video from the 'Understanding Gradle' series explains how Gradle's Java plugin sets up testing by default. The plugin creates a 'test' source set, along with 'compileTestJava' and 'processTestResources' tasks, and registers a 'test' task that uses Gradle's built-in Test implementation. The test task is configured with the classpath and compiled test code locations derived from the source set. To write tests, a test framework like JUnit must be added as a dependency, because Gradle itself does not include test annotations [1].

The default test engine is JUnit 4, as it was the standard when Gradle's test task was created. To use JUnit 5, the test task must be configured with `useJUnitPlatform()` and the appropriate JUnit 5 API dependency must be added to `testImplementation`. JUnit 5 is modular: the Jupiter engine executes JUnit 5 tests, while the Vintage engine allows running legacy JUnit 4 tests. The video demonstrates adding the Vintage engine as a `testRuntimeOnly` dependency to run JUnit 4 tests under JUnit 5, and then migrating a test to JUnit 5 by updating imports and dependencies. The newer JVM Test Suites concept simplifies this setup, but understanding the manual configuration is useful for working with older Gradle versions or for deeper insight [1].

- Gradle's Java plugin automatically creates a test source set, compile task, and test task.
- Test dependencies are managed via configurations like testImplementation and testRuntimeOnly.
- By default, Gradle's test task uses JUnit 4; switching to JUnit 5 requires `useJUnitPlatform()` and adding the JUnit 5 Jupiter API dependency.
- JUnit 5's Vintage engine enables running JUnit 4 tests in a JUnit 5 setup.
- JVM Test Suites is a newer feature that simplifies test configuration, but manual setup is still relevant for older Gradle versions.