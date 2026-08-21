---
domain: engineering-culture
subdomain: dependency-management
concept: maven-gradle-dependency-conflicts
title: Nonsensical Maven is still a Gradle problem
sources:
  - title: "Nonsensical Maven is still a Gradle problem"
    url: "https://jakewharton.com/nonsensical-maven-is-still-a-gradle-problem/"
    author: "Jake Wharton"
---

# Nonsensical Maven is still a Gradle problem

Maven's dependency resolution strategy is described as nonsensical: it picks the 'nearest definition' and, on ties, the first declaration wins. This can result in older versions of transitive dependencies being selected over newer ones, potentially causing runtime errors. The author illustrates this with a pop quiz where Maven chooses version 1.0 over 1.1, while Gradle would choose the newer version (Jake Wharton, https://jakewharton.com/nonsensical-maven-is-still-a-gradle-problem/).

This becomes a problem for libraries built with Gradle because Gradle resolves conflicts to the newest version, so library authors may not notice that their declared dependency versions are lower than those resolved transitively. When published, Maven consumers may end up with the older declared version, leading to failures. The article uses OkHttp 4.12 as an example: it declares Kotlin stdlib 1.8.21, but Okio 3.6 depends on 1.9.10, creating a conflict that Maven would resolve incorrectly (Jake Wharton, same source).

The article explores solutions: using Gradle's versionMapping to publish resolved versions, the Maven enforcer plugin's dependency convergence rule, and Gradle's failOnVersionConflict(). Each has tradeoffs. The author ultimately proposes a custom Gradle task that fails if a declared first-order dependency is upgraded transitively, and invites the community to turn it into a proper plugin (Jake Wharton, same source).

- Maven's nearest-definition and first-declaration-wins strategy can select older versions than Gradle's newest-wins approach.
- Gradle-built libraries can inadvertently publish dependency graphs with version mismatches that break Maven consumers.
- Possible mitigations include publishing resolved versions via versionMapping, using Maven enforcer dependency convergence, or enabling failOnVersionConflict.
- The author shares a custom Gradle task to detect when direct dependencies are upgraded transitively, but notes it needs polishing.