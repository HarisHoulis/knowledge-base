---
domain: engineering-culture
subdomain: dependency-management
concept: maven-dependency-resolution-conflicts
title: Nonsensical Maven is still a Gradle problem
sources:
  - title: "Nonsensical Maven is still a Gradle problem"
    url: "https://jakewharton.com/nonsensical-maven-is-still-a-gradle-problem/"
---

# Nonsensical Maven is still a Gradle problem

The article argues that Maven's dependency resolution strategy is objectively problematic and creates pitfalls for library authors publishing with Gradle. Maven picks the 'nearest definition' in the dependency tree, and if multiple versions are at the same depth, the first declaration wins. This can result in older transitive versions being selected even when a newer version is present, potentially causing runtime failures like NoSuchMethodException. Gradle, by contrast, resolves to the newest version by default, but when publishing Maven metadata, it often declares the originally declared versions, not the resolved ones, creating a mismatch for Maven consumers. The article uses OkHttp as a real example: OkHttp 4.12 declares Kotlin stdlib 1.8.21 while Okio 3.6 depends on 1.9.10, leading to a dependency conflict that Maven would resolve to the older version.

- Maven's default resolution strategy (nearest definition, first declaration wins) can select older versions than intended, unlike Gradle's newest-version policy.
- Gradle library publishers can unintentionally create dependency conflicts for Maven consumers when their declared versions differ from transitively resolved versions.
- Using Gradle's versionMapping with fromResolutionOf or fromResolutionResult can publish resolved versions, but it undermines declared versions.
- Gradle's failOnVersionConflict detects conflicts but cannot reject upgrades without forcing versions, making it an incomplete solution.
- A custom task can check if first-order dependencies' requested versions match selected versions, alerting authors to transitive upgrades.