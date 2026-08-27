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

The video explains how to declare dependencies in Gradle using group/name (GA) coordinates and the role of configurations as scopes or buckets. It emphasizes that dependencies are declared with coordinates like group:name:version, and configurations determine the visibility and usage of those dependencies. The video uses the Java Library plugin's configurations as an example, highlighting implementation, api, compileOnly, compileOnlyApi, runtimeOnly, and other configurations (Jendrik Johannes, 2021, 1:03).

Key differences are illustrated: implementation vs api semantics affect transitive dependency exposure—implementation keeps dependencies internal to the module, while api exposes them to consumers. compileOnly/compileOnlyApi are for compile-time only, while runtimeOnly is for runtime-only. The video walks through a sample project and inspects dependency resolution results, then clarifies the terminology of configurations for declaring, resolving, and consuming (Jendrik Johannes, 2021, 8:56, 10:09). It underscores that Gradle's dependency management is based on configurations and that knowing which configuration to use is crucial for correct builds.

The video also touches on version handling, noting that versions can be omitted and managed centrally (as a preview to a related video). Overall, it provides a foundational understanding of dependency declaration in Gradle, setting the stage for more advanced topics like version conflicts and centralizing versions (Jendrik Johannes, 2021, 11:38, 12:59).

- Configurations act as scopes/buckets for dependencies, controlling their visibility and usage.
- Dependencies are declared using group, artifact name, and version coordinates (GA coordinates).
- The `implementation` configuration keeps dependencies internal, while `api` exposes them to consumers.
- `compileOnly` and `runtimeOnly` restrict dependencies to specific lifecycle phases (compile-time only and runtime-only, respectively).
- Gradle distinguishes between configurations for declaring, resolving, and consuming dependencies, which is key to understanding dependency management.