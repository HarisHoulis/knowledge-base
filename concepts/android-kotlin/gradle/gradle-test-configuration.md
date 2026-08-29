---
domain: android-kotlin
subdomain: gradle
concept: gradle-test-configuration
title: Understanding Gradle #18 – Configuring Testing
sources:
  - title: "Understanding Gradle #18 – Configuring Testing"
    url: "https://www.youtube.com/watch?v=7f_gBvGQN_0"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2022-07-11T14:37:15+00:00"
---

# Understanding Gradle #18 – Configuring Testing

The video explains how Gradle handles testing, starting with the default setup from the Java plugin. The plugin creates a test source set, which adds tasks like compileTestJava and resource copying, and registers a test task using Gradle's core Test implementation. This task is configured from the source set with the classpath and compiled test code locations. Historically, additional configuration is often needed; Gradle now offers JVM test suites to simplify this setup, but understanding the underlying configuration is useful for older versions or special cases.

To write and run tests, developers need a test framework and engine. By default, the test task is configured to use JUnit 4, so a JUnit 4 test works with just a testImplementation dependency. For JUnit 5, you must call useJUnitPlatform() on the test task and add the appropriate engine dependencies. JUnit 5 is modular, with a Jupiter engine for JUnit 5 tests and a Vintage engine for running JUnit 4 tests. The demo shows adding Veterans as testRuntimeOnly to run JUnit 4 tests under the JUnit 5 platform, then migrating fully to JUnit 5 by replacing dependencies and adjusting imports to Jupiter annotations.

- The Java plugin automatically sets up a test source set and a test task configured for JUnit 4 by default.
- To use JUnit 5, call useJUnitPlatform() on the test task and add the Jupiter engine; optionally add Vintage for JUnit 4 support.
- JUnit 5's modular design requires explicit engine dependencies, often as testRuntimeOnly.
- Gradle's JVM test suites provide a simpler, more modern way to configure tests, but manual configuration is still needed for older Gradle versions.