---
domain: engineering-culture
subdomain: build-systems
concept: maven-dependency-resolution
title: Nonsensical Maven is still a Gradle problem
sources:
  - title: "Nonsensical Maven is still a Gradle problem"
    url: "https://jakewharton.com/nonsensical-maven-is-still-a-gradle-problem/"
    author: "Jake Wharton"
---

# Nonsensical Maven is still a Gradle problem

Jake Wharton explores the tension between Gradle and Maven dependency resolution strategies, highlighting how Maven's 'nearest definition' rule can select older transitive dependency versions than Gradle's default 'highest version' approach. He demonstrates that a Gradle-built library can publish a POM with conflicting transitive versions, creating a 'time bomb' for Maven consumers that may only surface at runtime as NoSuchMethodError or similar failures. The article uses OkHttp 4.12 as a real-world example, where Okio 3.6 depends on Kotlin stdlib 1.9.10 while OkHttp declares 1.8.21, causing Maven to resolve to the older 1.8.21 despite the newer dependency.

Wharton suggests several mitigation strategies: using Gradle's version mapping to publish resolved versions instead of declared ones, which prevents Maven from making an incompatible choice; enabling `failOnVersionConflict()` to catch mismatches during builds; or writing a custom task that checks whether first-order dependencies are upgraded transitively. He notes that each approach has tradeoffs—version mapping undermines declared versions, and `failOnVersionConflict` cannot easily reject upgrades without breaking checks. He ultimately provides a quick Groovy script that flags such upgrades and calls on the community to turn it into a reusable plugin. The article underscores that even pure-Gradle library authors must consider Maven consumers, as the JVM ecosystem remains heterogeneous.

- Maven's dependency resolution chooses the nearest definition, which can override newer versions with older ones based on dependency graph depth, unlike Gradle's highest-version policy.
- Gradle library authors can inadvertently publish POMs with conflicting transitive versions, creating latent runtime failures for Maven consumers.
- Publishing resolved versions via Gradle's version mapping prevents Maven from resolving to an older version, but it undermines the declared versions in the project.
- Using `failOnVersionConflict()` in Gradle catches dependency conflicts at build time, but it cannot distinguish upgrades from other conflicts and may require forcing versions.
- A custom task (or future plugin) can verify that direct dependencies are not upgraded transitively, preserving declared versions while keeping Maven consumers safe.