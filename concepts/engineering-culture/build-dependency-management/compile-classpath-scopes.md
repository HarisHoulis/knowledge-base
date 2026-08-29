---
domain: engineering-culture
subdomain: build-dependency-management
concept: compile-classpath-scopes
title: Understanding Gradle: Multiple Compile Classpaths
sources:
  - title: "Understanding Gradle #27 – Multiple Compile Classpaths"
    url: "https://www.youtube.com/watch?v=Z5n9VK3sOnI"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2022-12-05T16:15:11+00:00"
---

# Understanding Gradle: Multiple Compile Classpaths

In this video, Jendrik Johannes explains how Gradle manages multiple compile classpaths in Java projects, emphasizing the importance of dependency scopes (implementation, api) for modularity. He demonstrates with an example of two independent components and shows how Gradle reduces the compile classpath for each component by only exposing the APIs that are actually needed at compile time, even when transitive dependencies exist.

Gradle distinguishes between dependencies required at compile time (exported to consumers) and those required only at runtime. By using the 'api' scope, a library can expose its transitive dependencies to consumers' compile classpaths, while 'implementation' keeps them hidden, promoting encapsulation and faster builds. The video also covers how artifacts are exported for both compilation and runtime, and how this impacts the overall build performance and maintainability.

- Multiple compile classpaths allow components to compile independently against reduced dependency sets.
- The 'implementation' dependency scope hides transitive dependencies from consumers' compile classpath, while 'api' exposes them.
- Using 'api' for dependencies that appear in the public API prevents compilation errors in consumers and ensures correct runtime behavior.
- Properly scoping dependencies reduces compilation overhead and enforces encapsulation between modules.
- Gradle configurations map these scopes to different classpaths used during compilation and execution.