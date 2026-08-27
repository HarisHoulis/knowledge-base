---
domain: android-kotlin
subdomain: dependency-management
concept: centralized-dependency-versions
title: Understanding Gradle #09 – Centralizing Dependency Versions
sources:
  - title: "Understanding Gradle #09 – Centralizing Dependency Versions"
    url: "https://www.youtube.com/watch?v=8044F5gc1dE"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-10-04T11:44:19+00:00"
---

# Understanding Gradle #09 – Centralizing Dependency Versions

The video discusses the pitfalls of defining dependency versions directly in Gradle build scripts, which can lead to duplication and version conflicts in multi-project builds. It recommends using dependency constraints in convention plugins to centralize versions, ensuring consistency across projects (Jendrik Johannes, 2021). 

It then introduces platforms (or BOMs) as a more flexible mechanism for managing versions. Platforms are separate components that publish dependency constraints and can be imported via the java-platform plugin. They can also consume existing BOMs like Jackson or Spring Boot, and can be isolated in separate builds to manage plugin versions as well (Jendrik Johannes, 2021).

- Inline version declarations cause duplication and potential conflicts; centralizing avoids these issues.
- Dependency constraints in convention plugins enforce versions across all projects.
- Platforms (BOMs) allow publishing constraints and reusing existing BOMs like Jackson and Spring Boot.
- Platforms can be placed in separate builds to manage both library and plugin versions.