---
domain: android-kotlin
subdomain: gradle-dependency-management
concept: centralizing-dependency-versions
title: Centralizing Dependency Versions in Gradle
sources:
  - title: "Understanding Gradle #09 – Centralizing Dependency Versions"
    url: "https://www.youtube.com/watch?v=8044F5gc1dE"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-10-04"
---

# Centralizing Dependency Versions in Gradle

The video explains the pitfalls of hardcoding dependency versions directly in Gradle build scripts, which can lead to duplication and version conflicts across projects. To address this, it recommends centralizing version management using Gradle's built-in mechanisms, specifically dependency constraints defined in convention plugins, so that a single constraint is applied to all projects consistently.

The video then introduces platforms as a more focused and flexible solution. A platform is a separate component created with the java-platform plugin that contains only dependency constraints. It can be defined as a subproject or in a separate build, and it can import existing BOMs (e.g., Jackson BOM or Spring Boot BOM) to leverage community-maintained version sets. This separation of dependency versions from other build configuration makes regular updates and security fixes easier to manage, as the versions are kept in one dedicated place.

- Hardcoding versions in build scripts causes duplication and potential dependency conflicts.
- Dependency constraints in convention plugins centralize versions and apply them to every project.
- Platforms are dedicated components for dependency constraints, created via the java-platform plugin.
- Platforms can import existing BOMs to reuse consistent version sets from the community.
- Centralizing dependency versions simplifies regular upgrades and reduces inconsistency risks.