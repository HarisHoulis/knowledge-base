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

The article discusses how Maven's dependency resolution strategy, which picks the 'nearest definition' rather than the highest version, is objectively problematic for JVM library consumers. Gradle resolves to the newest version, which is usually safer, but when Gradle-built libraries publish POM files, they can accidentally embed dependency version mismatches (e.g., OkHttp 4.12 depends on Kotlin stdlib 1.8.21 while Okio 3.6 depends on 1.9.10). Maven users then risk runtime failures due to missing APIs.

The author suggests several mitigations for Gradle library authors. One option is to use Gradle's `versionMapping` to publish the resolved dependency versions instead of declared ones, which prevents Maven consumers from seeing mismatched trees but undermines declared versions. Another is to enable `failOnVersionConflict()`, which forces the build to fail on any conflict in the transitive graph, but this is too strict and can fail on upgrades that are actually safe. The author ultimately proposes a custom task that checks whether first-order dependencies resolve to the requested version, failing if a direct dependency was upgraded transitively. This 'sympathy for Maven' task helps library maintainers avoid shipping mismatched POMs.

- Maven's dependency resolution picks the nearest definition, not the highest version, leading to potential runtime errors when transitive dependencies conflict.
- Gradle-built libraries can inadvertently create Maven-incompatible POMs when direct dependency versions differ from transitive resolutions.
- Using `versionMapping` with `fromResolutionOf` can align published POMs with resolved versions, but may not suit all projects.
- Gradle's `failOnVersionConflict()` is too strict for many projects, but a custom task can detect undesired transitive upgrades of first-order dependencies.
- The author calls for a reusable plugin to automate this 'Maven sympathy' check across many library projects.