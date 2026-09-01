---
domain: engineering-culture
subdomain: gradle-testing
concept: junit-test-configuration
title: Understanding Gradle #18 – Configuring Testing
sources:
  - title: "Understanding Gradle #18 – Configuring Testing"
    url: "https://www.youtube.com/watch?v=7f_gBvGQN_0"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2022-07-11"
---

# Understanding Gradle #18 – Configuring Testing

The test task is wired to the test source set's classpath and outputs, and additional configurations like testRuntimeOnly are used for engines. The example shows how to replace JUnit 4 dependencies with the JUnit 5 API and adjust imports. The JVM Test Suites concept provides a more structured way to declare custom test suites, reducing boilerplate compared to manual source set and task configuration.

- The Java plugin creates a test source set and a test task by default, with dependencies like testImplementation and testRuntimeOnly.
- The default test engine is JUnit 4; to use JUnit 5, call useJUnitPlatform() and add the Jupiter engine (and Vintage for JUnit 4 compatibility).
- JUnit 5's modular design allows running both JUnit 4 and JUnit 5 tests in the same run, facilitating migration.
- JVM Test Suites simplify test configuration by providing a higher-level DSL compared to manually configuring source sets and tasks.