---
domain: android-kotlin
subdomain: gradle-dependencies
concept: dependency-configurations
title: Understanding Gradle #08 – Declaring Dependencies
sources:
  - title: "Understanding Gradle #08 – Declaring Dependencies"
    url: "https://www.youtube.com/watch?v=igug9tbl4J4"
    author: "Jendrik Johannes"
    date: "2021-09-20"
---

# Understanding Gradle #08 – Declaring Dependencies

Gradle organizes dependencies into configurations, which act as buckets or scopes that define how dependencies are used and exposed. The Java Library plugin provides configurations such as implementation, api, compileOnly, compileOnlyApi, and runtimeOnly. implementation keeps dependencies internal to a module, while api exposes them to consumers; compileOnly and compileOnlyApi are for compile-time-only dependencies, and runtimeOnly is for runtime-only dependencies. This separation lets Gradle understand what is needed at compile time versus runtime and what should be visible downstream [Jendrik Johannes, 2021].

To declare a dependency, Gradle uses group/name coordinates (GA), optionally with a version. The video demonstrates preparing a group and an included build project, then declaring dependencies in different configurations and inspecting dependency resolution results. Gradle distinguishes between configurations for declaring dependencies, for resolving them, and for consuming them, which is key to knowing what tasks can do with dependencies. Dependency versions can be specified directly or managed centrally through constraints and platforms [Jendrik Johannes, 2021].

- Configurations are scopes/buckets for dependencies; the Java Library plugin provides implementation, api, compileOnly, compileOnlyApi, and runtimeOnly.
- Dependencies are declared by group/artifact (GA) coordinates plus an optional version.
- implementation hides dependencies from consumers, while api exposes them.
- compileOnly/compileOnlyApi and runtimeOnly separate compile-time and runtime-only dependencies.
- Gradle configurations serve distinct purposes: declaring, resolving, and consuming dependencies.