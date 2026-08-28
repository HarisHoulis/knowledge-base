---
domain: engineering-culture
subdomain: build-systems
concept: maven-gradle-dependency-resolution
title: Nonsensical Maven is still a Gradle problem
sources:
  - title: "Nonsensical Maven is still a Gradle problem"
    url: "https://jakewharton.com/nonsensical-maven-is-still-a-gradle-problem/"
    author: "Jake Wharton"
---

# Nonsensical Maven is still a Gradle problem

Jake Wharton argues that Maven's dependency resolution strategy is 'objectively bonkers' because it uses 'nearest definition' and 'first declaration wins' rules, which can pick older versions of transitive dependencies over newer ones, leading to runtime failures. He illustrates this with examples showing how a project can end up using C v1.0 even when a transitive dependency explicitly wants C v1.1 (https://jakewharton.com/nonsensical-maven-is-still-a-gradle-problem/). This behavior, while common in Maven, is not user-friendly and forces consumers to manually declare and monitor versions.

Wharton then highlights that Gradle's default behavior of choosing the newest version is safer, but library authors publishing to Maven can still create 'time bombs' by declaring a dependency that is older than a transitive dependency, as seen in OkHttp 4.12 depending on Kotlin stdlib 1.8.21 while Okio 3.6 depends on 1.9.10. He proposes several mitigations: using Gradle's version mapping to publish resolved dependency versions, enabling 'failOnVersionConflict' to catch mismatches at build time, or writing a custom task that checks whether first-order declared dependencies are upgraded transitively. He ultimately calls for a community plugin to automate this check (https://jakewharton.com/nonsensical-maven-is-still-a-gradle-problem/).

- Maven's dependency resolution uses 'nearest definition' and 'first declaration wins', which can select older versions than what transitive dependencies request, causing runtime errors.
- Gradle's default 'newest wins' strategy is safer, but library authors can still silently publish dependency graphs with version mismatches that only affect Maven consumers.
- Gradle's version mapping (fromResolutionOf/fromResolutionResult) can align published POMs with resolved versions, preventing downstream Maven conflicts.
- Using 'resolutionStrategy.failOnVersionConflict()' in library builds catches mismatches, but it cannot reject upgrades and requires manual version alignment.
- A custom Gradle task can detect when declared first-order dependencies are upgraded transitively, offering a practical solution for library maintainers.