---
domain: android-kotlin
subdomain: gradle
concept: custom-tasks-and-extensions
title: Understanding Gradle #07 – Implementing Tasks and Extensions
sources:
  - title: "Understanding Gradle #07 – Implementing Tasks and Extensions"
    url: "https://www.youtube.com/watch?v=wrgyUKC7vOY"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-09-13T15:17:30+00:00"
---

# Understanding Gradle #07 – Implementing Tasks and Extensions

The video demonstrates how to implement custom build logic in Gradle by creating a task class with typed input and output properties, annotated with Gradle's incremental build annotations (@Input, @OutputFile, etc.) to enable incremental builds and build caching. The task action generates a script based on the configured inputs. The presenter then shows how to register the task using tasks.register(), configure it in the build script, and use its output as an input to another task—emphasizing that wiring tasks through outputs is key for Gradle to optimize execution (source: https://www.youtube.com/watch?v=wrgyUKC7vOY).

For extensions, the video introduces an extension interface with properties, registers it via a project extension, and wires the extension properties to the task's properties using lazy configuration. This provides a clean DSL block in the build file, allowing users to configure the task without directly referencing task internals. The presenter concludes by summarizing the benefits: incremental builds, cacheability, and a maintainable, user-friendly build customization layer (source: https://www.youtube.com/watch?v=wrgyUKC7vOY).

- Implement tasks as classes with @Input and @OutputFile annotations to make them incremental and cacheable.
- Use tasks.register() and configure tasks in the build file for readability and lazy configuration.
- Pass task outputs as inputs to other tasks to enable Gradle to skip work when inputs are unchanged.
- Create extensions with a simple interface and register them to expose a DSL for configuring tasks.
- Wire extension properties to tasks using lazy properties (e.g., Property<String>) for tight integration and automatic dependency tracking.