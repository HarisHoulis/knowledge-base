---
domain: android-kotlin
subdomain: build-dependency-management
concept: gradle-dependency-declaration
title: Understanding Gradle #08 – Declaring Dependencies
sources:
  - title: "Understanding Gradle #08 – Declaring Dependencies"
    url: "https://www.youtube.com/watch?v=igug9tbl4J4"
    author: "Jendrik Johannes"
    date: "2021-09-20T14:02:26+00:00"
---

# Understanding Gradle #08 – Declaring Dependencies

Finally, the video discusses dependency versions, notes that Gradle knows what to do through dependencies, and highlights that versions can be managed centrally. The example project is available on GitHub (timestamp 11:38, 12:59).

- Configurations act as scopes/buckets for dependencies; the Java Library plugin provides implementation, api, compileOnly, compileOnlyApi, and runtimeOnly.
- Dependencies are declared using group and artifact name (GA) coordinates, optionally with a version.
- Gradle uses configurations to determine dependency visibility and behavior during compilation and runtime.
- Understanding configurations is essential for correct dependency management in Gradle.
- Dependency versions can be omitted and centralised, as covered in related videos.