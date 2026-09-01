---
domain: android-kotlin
subdomain: gradle
concept: test-task-internals
title: Understanding Gradle #19 – The Test Task
sources:
  - title: "Understanding Gradle #19 – The Test Task"
    url: "https://www.youtube.com/watch?v=YJjNQJSaFww"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2022-07-19T14:40:54+00:00"
---

# Understanding Gradle #19 – The Test Task

This video explains how Gradle's Test task works under the hood. Gradle runs on Java virtual machines. When you run a build, a lightweight client process communicates with the Gradle daemon, which configures the build, builds a task graph, and executes tasks. The daemon caches information in memory for better performance. Task actions can execute directly in the daemon, but for heavy work like running tests, Gradle uses worker processes to isolate the work and avoid harming the daemon (e.g., memory leaks). The Test task uses these worker processes: it spawns one or more test workers, and the test framework's engine runs tests inside them without awareness of Gradle. Gradle identifies test classes and sends entire classes to workers, so parallelization is improved by having many small test classes rather than a few large ones. The video also stresses configuring maxParallelForks to enable parallel test execution, since tests are not parallel by default.

- Gradle runs on a JVM and uses a daemon process to cache build state; the client process just reports feedback.
- Heavy tasks like tests run in isolated worker processes to protect the daemon from resource issues.
- The Test task sends complete test classes to worker processes, where the test framework engine (e.g., JUnit 5) executes them.
- Set maxParallelForks to run tests in parallel; by default tests are not executed in parallel.
- For high parallelization, split tests into many small test classes rather than a few classes with many methods.