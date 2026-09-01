---
domain: engineering-culture
subdomain: dependency-management
concept: maven-dependency-resolution-conflict
title: Nonsensical Maven is still a Gradle problem
sources:
  - title: "Nonsensical Maven is still a Gradle problem"
    url: "https://jakewharton.com/nonsensical-maven-is-still-a-gradle-problem/"
    author: "Jake Wharton"
---

# Nonsensical Maven is still a Gradle problem

Jake Wharton argues that Maven's dependency resolution strategy is objectively nonsensical. Maven selects the "nearest definition" in the dependency tree, and if two versions are at the same depth, the first declaration wins. This means a transitive dependency can silently downgrade a library to an older version, causing runtime errors such as NoSuchMethodException. In contrast, Gradle automatically picks the highest version, which is safer for consumers. This difference becomes critical for library authors who publish with Gradle but have Maven users—their tests may pass with the newer transitive version while Maven users get the older one, leading to breakage. The article uses OkHttp's dependency graph as an example, where OkHttp declares Kotlin stdlib 1.8.21 but Okio 3.6 transitively requires 1.9.10, and Maven would resolve to 1.8.21. The author emphasizes that this is a real problem even if rarely triggered, and offers several mitigation strategies: Maven's dependencyConvergence enforcer rule, Gradle's version mapping for publications, failOnVersionConflict in Gradle, and a custom task to detect when declared dependencies are upgraded transitively. The author concludes by hoping for a community plugin to generalize this check.

- Maven resolves dependencies by nearest definition and first declaration wins, which can select older versions than Gradle's highest-version strategy.
- Gradle-built libraries may ship POMs where the declared dependency version differs from the resolved transitive version, creating time bombs for Maven consumers.
- The Maven enforcer plugin's dependencyConvergence rule can eagerly detect such conflicts for Maven users.
- Gradle can avoid this by publishing with resolved version mapping or failOnVersionConflict(), but failOnVersionConflict does not allow rejecting upgrades.
- A custom Gradle task can verify that first-order dependencies resolve to their declared versions, helping library authors maintain consistency.