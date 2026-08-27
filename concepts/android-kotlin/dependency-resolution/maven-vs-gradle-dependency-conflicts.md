---
domain: android-kotlin
subdomain: dependency-resolution
concept: maven-vs-gradle-dependency-conflicts
title: Nonsensical Maven is still a Gradle problem
sources:
  - title: "Nonsensical Maven is still a Gradle problem"
    url: "https://jakewharton.com/nonsensical-maven-is-still-a-gradle-problem/"
    author: "Jake Wharton"
---

# Nonsensical Maven is still a Gradle problem

Jake Wharton discusses how Maven's dependency resolution strategy is objectively confusing and can create problems for consumers of libraries built with Gradle. Maven picks the 'nearest definition' in the dependency tree, and if two versions are at the same depth, the first declaration wins. This means that when library B wants version 1.1 of library C and library D wants version 1.0, Maven may choose 1.0 even if 1.1 is newer and safer. This behavior is not user-friendly and can lead to runtime errors like NoSuchMethodException.

For Gradle-built libraries, this becomes a real issue when a directly declared dependency version is older than a transitive dependency version. For example, OkHttp 4.12.0 declares Kotlin stdlib 1.8.21, but Okio 3.6.0 depends on Kotlin stdlib 1.9.10. Maven consumers then face a conflict that can be detected with the Maven Enforcer plugin's dependency convergence rule. Since Gradle resolves to the newest version, tests run with a different version than what is published, creating a time bomb for Maven users.

The article suggests several mitigations: using Gradle's version mapping to publish resolved versions, enabling failOnVersionConflict(), or writing a custom task to verify that declared first-order dependencies are not upgraded transitively. Wharton shares a Groovy-scripted task that checks for such upgrades and calls on the community to turn it into a proper plugin he can apply to his 30 projects.

- Maven's nearest-wins and first-declaration-wins rules can select older versions than available, leading to runtime errors.
- Gradle-built libraries can inadvertently ship POMs with dependency version mismatches that affect Maven consumers.
- Gradle's pure-resolution and publish-declared-versions doesn't catch the issue; solutions include version mapping, failOnVersionConflict, or custom checks.
- A simple Gradle task can flag when a directly declared dependency is upgraded transitively, helping library authors maintain Maven compatibility.