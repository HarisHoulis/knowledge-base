---
domain: android-kotlin
subdomain: dependency-management
concept: maven-gradle-dependency-resolution
title: Nonsensical Maven is still a Gradle problem
sources:
  - title: "Nonsensical Maven is still a Gradle problem"
    url: "https://jakewharton.com/nonsensical-maven-is-still-a-gradle-problem/"
    author: "Jake Wharton"
---

# Nonsensical Maven is still a Gradle problem

Maven's default dependency resolution strategy uses the 'nearest definition' and first-declaration-wins, which can select older versions of transitive dependencies over newer ones requested elsewhere in the graph. This can cause runtime failures like NoSuchMethodError for consumers. Gradle, by contrast, resolves to the newest version, which is generally safer. The article highlights how this difference creates a hidden trap for library authors publishing with Gradle: a library may declare an older version of a dependency while a transitive dependency requests a newer one, and Maven consumers will then use the older version.

- Maven's nearest-wins and first-declaration-wins resolution can pick older dependency versions, unlike Gradle's newest-wins.
- Gradle library authors can unintentionally publish POMs that conflict for Maven users, e.g., OkHttp 4.12 declaring Kotlin stdlib 1.8.21 while Okio 3.6 requires 1.9.10.
- Maven users can detect these conflicts with the dependency convergence rule in the Maven Enforcer Plugin.
- Gradle's failOnVersionConflict() detects conflicts but cannot reject transitive upgrades without permanently forcing versions.
- A custom Gradle task can check that first-order dependencies resolve to the exact requested version, ensuring Maven compatibility.