---
domain: android-kotlin
subdomain: dependency-management
concept: maven-dependency-resolution-vs-gradle
title: Nonsensical Maven is still a Gradle problem
sources:
  - title: "Nonsensical Maven is still a Gradle problem"
    url: "https://jakewharton.com/nonsensical-maven-is-still-a-gradle-problem/"
    author: "Jake Wharton"
---

# Nonsensical Maven is still a Gradle problem

The article emphasizes that even though Maven's behavior is problematic, library authors using Gradle should take responsibility for ensuring their published POMs do not contain dependency conflicts that would affect Maven users. The proposed solutions range from simple configuration changes to a custom verification task, highlighting the need for a standardized plugin to detect such issues.

- Maven resolves transitive dependency conflicts by picking the 'nearest definition' and, at equal depth, the first declared, which can result in older versions being selected.
- Gradle's default conflict resolution picks the newest version, so Gradle-built libraries may publish POMs with dependency mismatches that only cause problems for Maven consumers.
- OkHttp 4.12 serves as a real-world example: it declares Kotlin stdlib 1.8.21 but its transitive dependency Okio requires 1.9.10, creating a conflict for Maven users.
- Mitigation strategies include using Gradle's version mapping for publications, enabling failOnVersionConflict(), or writing a custom task that verifies first-order dependencies are not upgraded transitively.
- A community plugin is needed to help library authors easily apply this verification across projects.