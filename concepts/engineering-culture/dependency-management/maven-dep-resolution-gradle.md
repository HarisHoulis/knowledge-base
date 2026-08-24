---
domain: engineering-culture
subdomain: dependency-management
concept: maven-dep-resolution-gradle
title: Nonsensical Maven is still a Gradle problem
sources:
  - title: "Nonsensical Maven is still a Gradle problem"
    url: "https://jakewharton.com/nonsensical-maven-is-still-a-gradle-problem/"
---

# Nonsensical Maven is still a Gradle problem

Jake Wharton discusses how Maven's dependency resolution strategy, which picks the nearest definition or first declaration at the same depth, can select older versions over newer ones, causing runtime errors. This is particularly problematic for library authors who build with Gradle but have Maven consumers, because Gradle resolves to the newest version by default, which may not match what Maven resolves to.

The article uses OkHttp 4.12 as an example: it depends on Okio 3.6 and Kotlin stdlib 1.8.21, while Okio 3.6 depends on Kotlin stdlib 1.9.10. A Maven consumer would get Kotlin stdlib 1.8.21 due to nearest definition, potentially causing issues. Wharton suggests using the Maven Enforcer plugin's dependency convergence rule for Maven consumers, and for Gradle library authors, publishing resolved versions via Gradle's versionMapping or using failOnVersionConflict.

Wharton notes that failOnVersionConflict cannot handle upgrades cleanly, so he wrote a custom task to detect when declared dependencies are upgraded transitively. He concludes by hoping someone will turn this into a reusable plugin.

- Maven's dependency resolution uses "nearest definition" and first declaration wins, which can select older versions over newer ones.
- Gradle's default resolution selects the newest version, creating a mismatch with Maven consumers that can lead to runtime failures.
- Gradle library authors can use versionMapping to publish resolved versions or failOnVersionConflict to detect conflicts.
- failOnVersionConflict cannot handle upgrades, so a custom task is needed to check that declared dependency versions are not changed by transitive resolution.