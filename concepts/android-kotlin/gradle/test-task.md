---
domain: android-kotlin
subdomain: gradle
concept: test-task
title: Understanding Gradle #19 – The Test Task
sources:
  - title: "Understanding Gradle #19 – The Test Task"
    url: "https://www.youtube.com/watch?v=YJjNQJSaFww"
    author: "Jendrik Johannes"
    date: "2022-07-19T14:40:54+00:00"
---

# Understanding Gradle #19 – The Test Task

Gradle runs on the JVM, using a lightweight client process that communicates with the Gradle daemon. The daemon caches build information and executes tasks, but heavy or parallel work is delegated to isolated worker processes. The test task leverages this pattern by running test frameworks (e.g., JUnit 5) inside worker processes, which communicate logs and results back to the daemon (Johannes, 2022).

Tests are sent to workers as complete test classes, not individual methods. This means that parallelization depends on the number of test classes; having many small classes improves throughput because each worker can process a class independently. The test task also needs to understand the test framework's annotations to identify tests, and the most important configuration option for parallel execution is `maxParallelForks`, which should be set to enable concurrent test classes across multiple workers (Johannes, 2022).

- Gradle uses a client process and daemon; the daemon executes tasks and can spawn worker processes for isolated, parallel work.
- The test task runs test engines (like JUnit 5) in worker processes, sending complete test classes to each worker.
- To maximize parallel test execution, split tests into many classes rather than few classes with many methods.
- Set `maxParallelForks` to enable parallel forking of test workers.
- Gradle must understand each test framework's annotations to discover and send tests to workers.