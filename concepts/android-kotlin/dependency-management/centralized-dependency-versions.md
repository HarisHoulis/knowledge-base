---
domain: android-kotlin
subdomain: dependency-management
concept: centralized-dependency-versions
title: Understanding Gradle #09 – Centralizing Dependency Versions
sources:
  - title: "Understanding Gradle #09 – Centralizing Dependency Versions"
    url: "https://www.youtube.com/watch?v=8044F5gc1dE"
    author: "Jendrik Johannes"
    date: "2021-10-04"
---

# Understanding Gradle #09 – Centralizing Dependency Versions

The simplest way to define dependency versions in Gradle is to hardcode them in each dependency declaration. However, this approach leads to duplication and eventual inconsistencies in larger builds, as versions scattered across projects can be upgraded independently, resulting in dependency version conflicts. According to the video, conflicts can cause compile-time or runtime problems because Gradle resolves to a single version, so it's best to avoid them by centralizing versions in projects you control (Jendrik Johannes, 2021).

To centralize versions, Gradle offers dependency constraints, which act as additional inputs to the dependency resolution mechanism. These constraints can be defined in convention plugins, making the same versions available to all projects. The video introduces platforms as a dedicated mechanism: a platform is a separate component or build that applies the java-platform plugin and contains only dependency constraints. Projects depend on the platform to inherit those constraints. Platforms can also reference existing BOMs, such as Jackson BOM or Spring Boot BOM, which provide consistent version sets for libraries. A separate platform build can additionally manage Gradle plugin versions, keeping all version information in one focused place (Jendrik Johannes, 2021).

The video highlights three mechanisms for version management: defining constraints directly in convention plugins, using platforms as separate components, and leveraging existing BOMs. It also suggests that because dependency versions change frequently due to security updates or other external factors, extracting them into a dedicated platform build helps establish a regular upgrade process without mixing versions with static build configuration (Jendrik Johannes, 2021).

- Hardcoding versions in dependency declarations leads to duplication and potential version conflicts in larger builds.
- Dependency constraints can be declared in convention plugins to provide consistent versions across all projects.
- Java platforms are separate components that centralize dependency constraints and can be included by projects as a dependency.
- Platforms can pull in existing BOMs like Jackson or Spring Boot to get consistent version combinations.
- A separate platform build can also manage Gradle plugin versions, further centralizing version management.