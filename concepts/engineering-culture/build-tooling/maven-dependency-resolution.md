---
domain: engineering-culture
subdomain: build-tooling
concept: maven-dependency-resolution
title: Nonsensical Maven is still a Gradle problem
sources:
  - title: "Nonsensical Maven is still a Gradle problem"
    url: "https://jakewharton.com/nonsensical-maven-is-still-a-gradle-problem/"
    author: "Jake Wharton"
---

# Nonsensical Maven is still a Gradle problem

Jake Wharton's article discusses how Maven's dependency resolution semantics are counterintuitive, particularly the 'nearest definition' rule and first-declaration-wins at the same depth. This can lead to Maven consumers silently using older transitive versions than what a library author declared, causing runtime failures. Gradle, by default, resolves to the newest version, which masks these issues for library authors testing with Gradle.

While building with Gradle, authors may unknowingly create dependency graphs that are problematic for Maven consumers. The article uses OkHttp 4.12 as an example, where the declared Kotlin stdlib 1.8.21 conflicts with Okio 3.6's transitive 1.9.10. Maven would pick 1.8.21 due to nearest definition, potentially breaking Okio's expectations.

Solutions discussed include using Gradle's version mapping to publish resolved versions, enabling failOnVersionConflict to detect mismatches early, and a custom task called 'sympathyForMrMaven' that checks whether first-order dependencies are upgraded transitively. The task is a quick Groovy hack, but the author invites the community to productionize it into a plugin.

- Maven resolves dependency conflicts by 'nearest definition', picking the closest version in the tree; at equal depth, the first declared wins.
- These semantics can select older versions than library authors declared, causing runtime errors for Maven consumers.
- Gradle's newest-version resolution can hide such conflicts during a library's own builds and tests.
- Gradle version mapping can publish resolved versions, but it undermines declared versions; failOnVersionConflict catches conflicts but rejects upgrades too.
- A custom task can verify that declared direct dependency versions are not upgraded transitively, offering a practical workaround.