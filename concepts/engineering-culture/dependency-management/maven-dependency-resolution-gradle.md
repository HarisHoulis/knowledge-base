---
domain: engineering-culture
subdomain: dependency-management
concept: maven-dependency-resolution-gradle
title: Nonsensical Maven is still a Gradle problem
sources:
  - title: "Nonsensical Maven is still a Gradle problem"
    url: "https://jakewharton.com/nonsensical-maven-is-still-a-gradle-problem/"
---

# Nonsensical Maven is still a Gradle problem

The article, by Jake Wharton, highlights how Maven's dependency resolution strategy is objectively problematic for Gradle-published libraries. Maven uses the 'nearest definition' rule, meaning the closest dependency version in the graph wins, and if two versions are at the same depth, the first declaration wins. This can result in an older transitive dependency being selected over a newer one, causing runtime errors. The article demonstrates this with a graph where library B wants C v1.1 and D wants C v1.0; Maven selects 1.0, while Gradle would select 1.1.

- Maven's dependency resolution uses 'nearest definition' and 'first declaration wins', which can select an older version over a newer one, unlike Gradle's newest-version policy.
- Library authors using Gradle can publish POMs that contain conflicting transitive versions, creating time bombs for Maven consumers.
- Gradle's versionMapping with fromResolutionOf can publish resolved versions, but it undermines declared versions and is not ideal for all projects.
- failOnVersionConflict() is a blunt tool that fails builds on any conflict, including upgrades, making it hard to use in practice.
- A custom Gradle task can detect when directly declared dependencies are upgraded transitively, helping library authors align their declarations and avoid Maven resolution issues.