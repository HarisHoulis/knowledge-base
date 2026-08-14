---
domain: android-kotlin
subdomain: dependency-resolution
concept: maven-dependency-resolution
title: Nonsensical Maven is still a Gradle problem
sources:
  - title: "Nonsensical Maven is still a Gradle problem"
    url: "https://jakewharton.com/nonsensical-maven-is-still-a-gradle-problem/"
    author: "Jake Wharton"
---

# Nonsensical Maven is still a Gradle problem

The article explains a critical difference between Gradle and Maven dependency resolution: Maven picks the 'nearest definition' and, at equal depth, the first declaration wins. This can cause older transitive versions to override newer ones, leading to runtime errors. The author illustrates with a simple graph where Maven chooses version 1.0 over 1.1, which is unintuitive and unsafe (source: https://jakewharton.com/nonsensical-maven-is-still-a-gradle-problem/).

- Maven's dependency resolution uses 'nearest definition' and 'first declaration wins' at equal depth, which can select older versions over newer ones.
- Gradle-built libraries can unintentionally create dependency graphs that cause Maven consumers to resolve conflicting versions.
- Use Gradle's `versionMapping` to publish resolved versions instead of declared versions to avoid Maven conflicts.
- `failOnVersionConflict()` is a blunt instrument that rejects all version conflicts, including upgrades, and requires manual forcing to fix.
- A custom Gradle task can detect when first-order dependencies are upgraded transitively and fail the build, protecting Maven consumers.