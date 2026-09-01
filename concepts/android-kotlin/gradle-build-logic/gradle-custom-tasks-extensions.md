---
domain: android-kotlin
subdomain: gradle-build-logic
concept: gradle-custom-tasks-extensions
title: Understanding Gradle #07 – Implementing Tasks and Extensions
sources:
  - title: "Understanding Gradle #07 – Implementing Tasks and Extensions"
    url: "https://www.youtube.com/watch?v=wrgyUKC7vOY"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-09-13T15:17:30+00:00"
---

# Understanding Gradle #07 – Implementing Tasks and Extensions

The video explains how to implement custom Gradle logic by creating a task class and an extension. It demonstrates a task that generates a script, starting with defining input/output properties using Gradle's annotations to make the task incremental and cacheable. The task action is implemented in a class method, and the task is registered and configured in the build file. It also shows how to use the task's output as input to another task and how to further configure the task in the build file, followed by running an incremental build to verify that inputs are tracked. (Source: https://www.youtube.com/watch?v=wrgyUKC7vOY)

The second part covers implementing extensions, which allow users to configure build logic from the build script. An extension interface is created with property definitions, then registered and configured in the build file. The extension is wired to the task so that the task can use the configured values. Finally, the extension is used in the build file to provide a clean DSL-like API. The video emphasizes the importance of using Gradle's lazy configuration and annotations to benefit from incremental builds and build caching. (Source: https://www.youtube.com/watch?v=wrgyUKC7vOY)

- Define custom tasks by creating a class with annotated input/output properties and an action method.
- Use Gradle's input/output annotations to make tasks incremental and cacheable via the build cache.
- Register tasks using the Gradle API and configure them in the build file, allowing outputs to feed into other tasks.
- Create extensions as interfaces with properties to expose a DSL-like configuration in the build script.
- Wire extensions to tasks to consume configuration values, enabling reusable and configurable build logic.