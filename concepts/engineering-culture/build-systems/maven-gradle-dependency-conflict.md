---
domain: engineering-culture
subdomain: build-systems
concept: maven-gradle-dependency-conflict
title: Nonsensical Maven is still a Gradle problem
sources:
  - title: "Nonsensical Maven is still a Gradle problem"
    url: "https://jakewharton.com/nonsensical-maven-is-still-a-gradle-problem/"
    author: "Jake Wharton"
---

# Nonsensical Maven is still a Gradle problem

This article argues that Maven's dependency resolution strategy is objectively nonsensical, and that Gradle library authors must account for it when publishing. Unlike Gradle's default of selecting the newest version, Maven uses "nearest definition" and "first declaration wins" policies, which can arbitrarily select older versions of transitive dependencies. This can cause runtime errors like NoSuchMethodException when a library expects APIs from a newer version. The article uses a concrete example: OkHttp 4.12 depends on Okio 3.6 and Kotlin stdlib 1.8.21, but Okio 3.6 requires Kotlin stdlib 1.9.10, so Maven consumers of OkHttp may end up with the older 1.8.21.

The article suggests several mitigation strategies. The Maven Enforcer plugin's dependencyConvergence rule can detect these conflicts from the consumer side, but it's a reactive measure. For Gradle publishers, versionMapping with fromResolutionOf can publish the resolved versions instead of the declared ones, preventing the Maven conflict entirely. However, the author notes this undermines declared versions and prefers to have declarations match resolutions. Another option is failOnVersionConflict(), which fails the build on any conflict, but it rejects both upgrades and downgrades, and forcing specific versions ironically disables future detection.

As a result, the author wrote a custom Gradle task that checks first-order dependencies against their resolved versions, ensuring that declared versions are not silently upgraded by transitive resolution. The task is a quick hack and is offered as a starting point for a cleaner plugin. The article emphasizes that library authors should take responsibility for the dependency graphs they publish, even though the problem originates from Maven's flawed resolution logic.

- Maven's nearest-wins and first-declaration-wins dependency resolution can silently select older versions, causing runtime failures.
- Gradle-built libraries may publish dependency graphs with mismatched versions that are only problematic for Maven consumers.
- Maven Enforcer's dependencyConvergence rule can catch conflicts, but it's a consumer-side mitigation.
- Gradle's versionMapping can publish resolved versions, but it compromises the clarity of declared versions.
- failOnVersionConflict() is too blunt; it rejects both upgrades and downgrades, and forcing versions disables future conflict detection.
- A custom verification task can enforce that declared first-order dependency versions match the resolved versions, preventing Maven-related issues.