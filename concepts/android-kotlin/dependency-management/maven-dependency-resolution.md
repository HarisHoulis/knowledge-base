---
domain: android-kotlin
subdomain: dependency-management
concept: maven-dependency-resolution
title: Nonsensical Maven is still a Gradle problem
sources:
  - title: "Nonsensical Maven is still a Gradle problem"
    url: "https://jakewharton.com/nonsensical-maven-is-still-a-gradle-problem/"
    author: "Jake Wharton"
---

# Nonsensical Maven is still a Gradle problem

To mitigate this, library maintainers can use Gradle's version mapping to publish the resolved versions, or fail on version conflicts. Jake also sketches a custom task that checks whether declared direct dependencies are upgraded transitively, which would catch mismatches before publication. He calls for a community plugin to automate this, since Maven's popularity means such issues remain real and need addressing (jakewharton.com).

- Maven's default dependency resolution chooses the nearest version to the project, and at equal depth the first declaration wins, potentially preferring older versions.
- This behavior can break Maven consumers when a Gradle-built library declares an older dependency than its own transitive dependencies require.
- Gradle users can publish resolved versions using versionMapping, but this undermines explicit version declarations.
- enable failOnVersionConflict or write a Gradle task to ensure declared versions match the resolved graph, preventing accidental mismatches.
- The issue is infrequent but real, and maintainers should consider Maven consumers when publishing libraries.