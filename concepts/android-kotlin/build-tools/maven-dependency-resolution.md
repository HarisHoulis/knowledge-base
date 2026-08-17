---
domain: android-kotlin
subdomain: build-tools
concept: maven-dependency-resolution
title: Nonsensical Maven is still a Gradle problem
sources:
  - title: "Nonsensical Maven is still a Gradle problem"
    url: "https://jakewharton.com/nonsensical-maven-is-still-a-gradle-problem/"
    author: "Jake Wharton"
---

# Nonsensical Maven is still a Gradle problem

The article by Jake Wharton discusses the conflict between Maven's and Gradle's dependency resolution strategies, and how this affects library authors. Maven resolves transitive dependency versions using the 'nearest definition', meaning it picks the version closest to the project in the dependency graph; if two versions are at the same depth, the first declared wins. Gradle, on the other hand, resolves to the newest version. This difference creates a trap for library developers using Gradle: they may unintentionally publish a project where a direct dependency is older than a transitive dependency, causing Maven consumers to select the older version. For example, OkHttp 4.12 declares Kotlin stdlib 1.8.21 while its dependency Okio 3.6 requires 1.9.10, so Maven consumers get 1.8.21. The article suggests several solutions: using Gradle's version mapping to publish the resolved versions, enabling failOnVersionConflict in library builds to detect conflicts, or writing a custom Gradle task to verify that declared dependencies are not upgraded transitively. The author acknowledges that failOnVersionConflict cannot reject upgrades and recommends building a plugin to check for this issue.

- Maven's 'nearest definition' strategy can select an older transitive dependency version over a newer one, leading to runtime errors.
- Gradle-built libraries can inadvertently create dependency graphs that break Maven consumers because Gradle resolves to the newest version but publishes the declared version.
- The Maven Enforcer Plugin's dependency convergence rule can detect such mismatches in consumer projects.
- Gradle's version mapping feature can publish resolved versions to prevent the problem, but it undermines the declared versions.
- A custom Gradle task can check whether declared direct dependencies are upgraded transitively, offering a more targeted solution.