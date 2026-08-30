---
domain: android-kotlin
subdomain: dependency-management
concept: compile-classpath
title: Understanding Gradle #27 – Multiple Compile Classpaths
sources:
  - title: "Understanding Gradle #27 – Multiple Compile Classpaths"
    url: "https://www.youtube.com/watch?v=Z5n9VK3sOnI"
    author: "Jendrik Johannes"
    date: "2022-12-05"
---

# Understanding Gradle #27 – Multiple Compile Classpaths

This video explains how Gradle manages multiple compile classpaths in modular Java projects, building on Part 1 about classpaths. It demonstrates with an example of two independent components, showing how they are compiled separately and how dependencies between them are handled. The key insight is that compile classpaths are intentionally reduced: even if a component has transitive dependencies, they are not necessarily visible at compile time unless explicitly declared as 'api'.

The video covers the distinction between compile and runtime classpaths. Dependencies that are only needed internally should use the 'implementation' scope, while dependencies that are exposed through a library's public API must use the 'api' scope. Using 'api' has a side effect: those dependencies become visible to consumers at compile time, which increases the compile classpath but ensures correctness. The example on GitHub (Kotlin DSL and Groovy DSL) illustrates these concepts in practice.

Overall, the video emphasizes that understanding dependency scopes is crucial for creating modular, maintainable builds. By keeping compile classpaths minimal, you avoid leaking internal implementation details and reduce the risk of conflicts, while 'api' dependencies explicitly define the contract for consumers.

- Compile classpaths should be reduced to only what is necessary for compilation, not the full transitive dependency set.
- Use 'implementation' for internal dependencies and 'api' for dependencies exposed in the public API of a component.
- 'api' dependencies become visible on the compile classpath of downstream consumers, which is a side effect to consider.
- Components can be compiled independently, and Gradle's configurations (e.g., compileClasspath, runtimeClasspath) manage these scopes automatically.
- The example demonstrates a modular project with two components and how to export artifacts for both compilation and runtime.