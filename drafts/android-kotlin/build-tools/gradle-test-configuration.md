---
domain: android-kotlin
subdomain: build-tools
concept: gradle-test-configuration
title: Understanding Gradle #18 – Configuring Testing
sources:
  - title: "Understanding Gradle #18 – Configuring Testing"
    url: "https://www.youtube.com/watch?v=7f_gBvGQN_0"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2022-07-11"
---

# Understanding Gradle #18 – Configuring Testing

This video explains how to configure testing in Gradle, starting with the default setup provided by the Java plugin. The plugin creates a test source set and a test task by default, and the test task is initially configured to use JUnit 4. To write and run tests, you need to add a test framework as a dependency using configurations like testImplementation and testRuntimeOnly. The video demonstrates adding JUnit 4 and then switching to JUnit 5 by configuring the test task with `useJUnitPlatform()` and adding the Jupiter API, along with the Vintage engine to run legacy JUnit 4 tests. The modular nature of JUnit 5 is highlighted, and the video mentions the newer JVM Test Suites concept as a way to simplify modern testing conventions in Gradle.

- The Java plugin automatically sets up a test source set and a test task, with JUnit 4 as the default test framework.
- To use JUnit 5, configure the test task with `useJUnitPlatform()` and add the Jupiter API as a testImplementation dependency.
- JUnit 5's modular design allows mixing JUnit 4 and JUnit 5 tests via the Vintage engine.
- Test dependencies are managed through dedicated configurations like testImplementation and testRuntimeOnly.
- Gradle's newer JVM Test Suites feature aims to simplify testing configuration, but the manual approach is still useful for older versions.