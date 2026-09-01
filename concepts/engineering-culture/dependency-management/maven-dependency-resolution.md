---
domain: engineering-culture
subdomain: dependency-management
concept: maven-dependency-resolution
title: Nonsensical Maven is still a Gradle problem
sources:
  - title: "Nonsensical Maven is still a Gradle problem"
    url: "https://jakewharton.com/nonsensical-maven-is-still-a-gradle-problem/"
---

# Nonsensical Maven is still a Gradle problem

The article discusses how Maven's dependency resolution strategy can cause problems for Maven consumers of libraries built with Gradle. Maven picks the nearest definition in the dependency tree, and if two versions are at the same depth, the first declaration wins. This can result in selecting an older version of a transitive dependency, potentially causing runtime errors. The author illustrates this with a scenario where one library depdends on version 1.1 of C and another on 1.0, but Maven selects 1.0. This behavior is unintuitive and user-unfriendly, even for Gradle users who may unknowingly create such graphs when publishing libraries.

- Maven's dependency resolution uses nearest-definition and first-declaration-wins, which can select older versions over newer ones, risking runtime failures.
- Gradle users publishing libraries can create dependency graphs with version mismatches that only affect Maven consumers, even though Gradle itself resolves to the newest version.
- Using Gradle's versionMapping publishing feature can publish resolved versions instead of declared ones, preventing Maven consumer issues.
- Setting `failOnVersionConflict()` in Gradle fails the build on conflicts, but it cannot reject upgrades to newer transitive versions without also forcing versions, which undermines future checks.
- A simple task can be written to detect when declared direct dependencies are upgraded transitively, and the author hopes for a plugin to standardize this check.