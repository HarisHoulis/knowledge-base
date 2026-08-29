---
domain: android-kotlin
subdomain: gradle-dependency-management
concept: declaring-dependencies
title: Understanding Gradle #08 – Declaring Dependencies
sources:
  - title: "Understanding Gradle #08 – Declaring Dependencies"
    url: "https://www.youtube.com/watch?v=igug9tbl4J4"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-09-20T14:02:26+00:00"
---

# Understanding Gradle #08 – Declaring Dependencies

This video explains how to declare dependencies in Gradle using group and artifact coordinates, and introduces the concept of configurations as scopes or buckets for organizing dependencies. Configurations like `implementation`, `api`, `compileOnly`, and `runtimeOnly` are provided by the Java Library plugin, each serving a specific purpose in the build. The video demonstrates how these configurations affect dependency resolution and consumer visibility, using an included build project as an example.

Gradle's dependency management relies on configurations to determine how dependencies are used during compilation, runtime, and publication. The `implementation` configuration keeps dependencies internal to the module, while `api` exposes them to consumers. Other configurations like `compileOnly` and `runtimeOnly` handle compile-time-only and runtime-only dependencies respectively. The video also shows how to inspect dependency resolution results and emphasizes that Gradle uses this configuration information to know what to do with each dependency, including whether to include it in the published metadata.

Finally, the video touches on dependency versions, noting that they can be declared directly or managed through constraints and centralization. It sets the stage for further topics like version conflicts and dependency constraints, which are covered in subsequent videos in the series.

- Gradle dependencies are declared using group and artifact coordinates, creating a unique identifier for each dependency.
- Configurations (e.g., `implementation`, `api`, `compileOnly`, `runtimeOnly`) define the scope and visibility of dependencies in the build.
- The Java Library plugin provides standard configurations for declaring and consuming dependencies, affecting how they appear in published metadata.
- Dependency resolution results can be inspected to understand what Gradle resolves and why.
- Dependency versions can be declared explicitly or managed via constraints and centralization strategies.