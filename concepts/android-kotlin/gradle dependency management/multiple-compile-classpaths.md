---
domain: android-kotlin
subdomain: gradle dependency management
concept: multiple-compile-classpaths
title: Understanding Gradle #27 – Multiple Compile Classpaths
sources:
  - title: "Understanding Gradle #27 – Multiple Compile Classpaths"
    url: "https://www.youtube.com/watch?v=Z5n9VK3sOnI"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2022-12-05"
---

# Understanding Gradle #27 – Multiple Compile Classpaths

In this video, Jendrik Johannes explains how Gradle manages multiple compile classpaths in a multi-module Java project. The example with two components demonstrates that each component has its own compile classpath, and dependencies are not automatically exposed to consumers. This is a key part of Java modularity and helps keep builds manageable (Johannes, 2022).

The video clarifies the difference between `implementation` and `api` dependency scopes. Using `implementation` keeps transitive dependencies off the compile classpath of downstream components, reducing coupling and unnecessary recompilation. On the other hand, `api` exposes those dependencies, which is needed when types from the dependency appear in public APIs. Gradle provides ways to inspect these classpaths to understand what is visible at compile time versus runtime (Johannes, 2022).

- Gradle creates separate compile classpaths per component, avoiding a single monolithic classpath.
- The `implementation` configuration hides transitive dependencies from consumers' compile classpath.
- The `api` configuration explicitly exposes dependencies to consumers.
- Inspecting compile classpaths helps developers understand the true visibility of dependencies.
- This approach reduces coupling and improves build performance by limiting recompilation.