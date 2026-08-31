---
domain: android-kotlin
subdomain: gradle
concept: custom-gradle-tasks-extensions
title: Understanding Gradle #07 – Implementing Tasks and Extensions
sources:
  - title: "Understanding Gradle #07 – Implementing Tasks and Extensions"
    url: "https://www.youtube.com/watch?v=wrgyUKC7vOY"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-09-13T15:17:30+00:00"
---

# Understanding Gradle #07 – Implementing Tasks and Extensions

This video from Jendrik Johannes (onepiece.Software) demonstrates how to implement custom build logic in Gradle, specifically by creating a custom Task class that generates a script. The process involves defining input and output properties with annotations, which enables Gradle to treat the task as incremental and cacheable. The task action is implemented in the class, and then the task is registered and configured in the build file. Additionally, the video shows how the task's output can be used as input to another task, and how further configuration can be done in the build script (Jendrik Johannes, 2021).

The second part of the video focuses on implementing Gradle extensions. An extension interface is created to define properties, and then the extension is registered and configured. This extension is wired to the custom task, allowing users to configure the task from the build file in a DSL-like manner. The video concludes with a summary of the benefits: using input/output annotations enables incremental builds and build caching, while extensions provide a clean, user-friendly configuration API (Jendrik Johannes, 2021).

- Create custom Gradle tasks by extending DefaultTask and annotating input/output properties for incremental builds and caching.
- Implement the task action in the task class, then register and configure the task in the build file.
- Task outputs can be consumed as inputs by other tasks, enabling task dependency and efficient build pipelines.
- Define a Gradle extension interface to expose DSL-like configuration options and wire it to the task for easy setup.
- Using annotations and lazy properties ensures optimal performance and compatibility with Gradle's build cache.