---
domain: engineering-culture
subdomain: build-tools
concept: maven-dependency-resolution-conflicts
title: Nonsensical Maven is still a Gradle problem
sources:
  - title: "Nonsensical Maven is still a Gradle problem"
    url: "https://jakewharton.com/nonsensical-maven-is-still-a-gradle-problem/"
    author: "Jake Wharton"
---

# Nonsensical Maven is still a Gradle problem

Jake Wharton argues that Maven's dependency resolution strategy is objectively nonsensical, as it selects the 'nearest definition' and, at equal depth, the 'first declaration wins'. This can cause Gradle-published libraries to break Maven consumers when transitive dependency versions conflict, because Maven may downgrade a dependency to an older version that lacks APIs required by a newer transitive dependency. For example, OkHttp 4.12 declares Kotlin stdlib 1.8.21, while its transitive Okio 3.6 depends on 1.9.10, creating a conflict that Maven resolves to the older version, risking runtime errors like NoSuchMethodException (https://jakewharton.com/nonsensical-maven-is-still-a-gradle-problem/).

Wharton suggests several mitigations for Gradle library authors: use Gradle's versionMapping publishing with 'fromResolutionOf' to publish resolved versions instead of declared ones; use failOnVersionConflict() to detect conflicts; or write a custom task that fails if a directly declared dependency is upgraded transitively. He provides a Groovy script that checks first-order dependencies and invites the community to turn it into a reusable plugin. The underlying tension is that Gradle's default conflict resolution picks the newest version, hiding problems that only Maven consumers will experience.

- Maven's dependency resolution uses 'nearest definition' and 'first declaration wins', which can downgrade transitive dependencies and cause runtime failures.
- Gradle libraries can unknowingly publish POMs that conflict for Maven consumers when direct dependencies are older than transitive ones, as shown by OkHttp's Kotlin stdlib mismatch.
- Gradle's versionMapping can replace declared versions with resolved versions in published metadata, preventing the problem but altering intended versions.
- failOnVersionConflict() detects conflicts but cannot reject upgrades to newer versions, leading to a need for custom dependency graph checks.
- A practical solution is a custom task that verifies direct dependencies are not upgraded transitively, which Wharton implemented and invites the community to productize.