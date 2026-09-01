---
domain: android-kotlin
subdomain: gradle-dependency-management
concept: declaring-dependencies
title: Understanding Gradle #08 – Declaring Dependencies
sources:
  - title: "Understanding Gradle #08 – Declaring Dependencies"
    url: "https://www.youtube.com/watch?v=igug9tbl4J4"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-09-20"
---

# Understanding Gradle #08 – Declaring Dependencies

In this video, Jendrik Johannes explains how to declare dependencies in Gradle using group and artifact name coordinates, and introduces the concept of configurations—scopes or buckets that organize dependencies for different purposes. The Java Library plugin provides several standard configurations, including implementation, api, compileOnly, compileOnlyApi, and runtimeOnly, each controlling when a dependency is used: at compile time, runtime, or both, and whether it is exposed to consumers of the library (Jendrik Johannes, 2021).

The video demonstrates declaring dependencies in a Gradle build file, covering the syntax and meaning of each configuration. For example, implementation keeps a dependency internal to the module, while api makes it part of the public API surface. compileOnly and compileOnlyApi are for dependencies needed only at compile time, and runtimeOnly for dependencies needed only at runtime. It also explores how Gradle's configurations serve distinct roles: declaring dependencies, resolving them, and consuming them from other projects (Jendrik Johannes, 2021).

Additionally, the video discusses dependency versions, noting that Gradle can manage versions separately and that dependencies can be declared without a fixed version when using version catalogs or constraints. The overall message is that Gradle's dependency model relies on configurations to give precise control over the build classpath and runtime behavior, making it essential to choose the right configuration for each dependency (Jendrik Johannes, 2021).

- Configurations are scopes or buckets for dependencies; the Java Library plugin defines implementation, api, compileOnly, compileOnlyApi, and runtimeOnly.
- Dependencies are declared using group and artifact name (GA) coordinates, with versions managed separately.
- api vs implementation determines whether a dependency is exposed transitively to consumers.
- compileOnly/compileOnlyApi are for compile-time-only dependencies; runtimeOnly is for runtime-only dependencies.
- Gradle configurations are used for declaring, resolving, and consuming dependencies, enabling precise build behavior.