---
domain: engineering-culture
subdomain: build-tooling
concept: centralizing-dependency-versions
title: Understanding Gradle #09 – Centralizing Dependency Versions
sources:
  - title: "Understanding Gradle #09 – Centralizing Dependency Versions"
    url: "https://www.youtube.com/watch?v=8044F5gc1dE"
    author: "Jendrik Johannes (onepiece.Software)"
    date: "2021-10-04T11:44:19+00:00"
---

# Understanding Gradle #09 – Centralizing Dependency Versions

Platforms can also include existing BOMs (like Jackson BOM or Spring Boot BOM) to provide consistent versions for widely used libraries, and they can even manage Gradle plugin versions. This setup allows teams to regularly upgrade dependencies in a controlled way without mixing version management with other build logic.

- Hardcoding dependency versions in each build script leads to duplication and potential version conflicts.
- Dependency constraints in convention plugins centralize versions across all projects.
- Platforms (Java Platform plugin) provide a separate, reusable component for version management.
- Platforms can import existing BOMs (e.g., Jackson BOM) and manage Gradle plugin versions.
- Separating versions from other build configuration makes regular upgrades easier and safer.