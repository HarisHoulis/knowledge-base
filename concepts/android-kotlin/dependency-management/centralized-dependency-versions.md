---
domain: android-kotlin
subdomain: dependency-management
concept: centralized-dependency-versions
title: Understanding Gradle #09 – Centralizing Dependency Versions
sources:
  - title: "Understanding Gradle #09 – Centralizing Dependency Versions"
    url: "https://www.youtube.com/watch?v=8044F5gc1dE"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-10-04"
---

# Understanding Gradle #09 – Centralizing Dependency Versions

In this video, Jendrik Johannes discusses the problem of hardcoding dependency versions directly in build scripts, which can lead to duplication and inconsistency across multi-project builds. He emphasizes that when the same dependency version is repeated in multiple places, upgrading one occurrence and forgetting the others creates version conflicts that Gradle must resolve, potentially causing issues at compile or runtime. The best approach is to centralize versions to avoid such conflicts in projects you control.

The solution introduced is using dependency constraints declared in a convention plugin, which provides a central place for build information. By defining constraints once, Gradle applies them to all projects that apply the plugin, ensuring consistent versions. However, for regularly updated external dependencies, separating version information into a dedicated mechanism is beneficial. Gradle offers platforms, which are components that contain only dependency constraints, defined via the `java-platform` plugin. A platform can be a separate subproject or build, and can also pull in existing BOMs like the Jackson BOM or Spring Boot BOM, which provide curated version sets for widely used libraries.

Overall, the video outlines three mechanisms for version management: dependency constraints, platforms, and BOMs, which can be combined. Using a separate build for the platform also allows managing Gradle plugin versions centrally. This approach helps teams maintain a regular upgrade process and keeps build configuration clean and focused (onepiece.Software, 2021).

- Hardcoding versions in each build script causes duplication and risks dependency conflicts when upgrades are applied inconsistently.
- Dependency constraints in a convention plugin centralize versions for all projects that apply the plugin.
- Platforms (using the java-platform plugin) are separate components that aggregate dependency constraints and can be reused across builds.
- Existing BOMs like Jackson or Spring Boot can be imported into a platform to provide consistent version combinations.
- A separate build for the platform can also manage Gradle plugin versions centrally.