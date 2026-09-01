---
domain: android-kotlin
subdomain: dependency-management
concept: dependency-version-conflicts
title: Understanding Gradle #10 – Dependency Version Conflicts
sources:
  - title: "Understanding Gradle #10 – Dependency Version Conflicts"
    url: "https://www.youtube.com/watch?v=YYWhfy6c2YQ"
    author: "Jendrik Johannes"
    date: "2021-10-18"
---

# Understanding Gradle #10 – Dependency Version Conflicts

Dependency version conflicts arise when multiple components in a dependency graph require different versions of the same library. Gradle treats versions declared in metadata or constraints as 'required versions' and resolves conflicts by a simple rule: the higher version wins. This heuristic assumes backward compatibility but can introduce subtle runtime issues. For example, in the video, increasing commons-text from 1.4 to 1.5 triggered a transitive dependency on commons-lang 3.8.1, whose version was higher than the explicitly constrained 3.6. Although the unit tests for the business logic library still passed (because they used the older 3.6), the final application runtime selected 3.8.1. This changed the behavior of NumberUtils.isCreatable (a bug fix) and broke the application's expectation that leading-zero numbers are not recognized (Johannes, 2021). The issue highlights a common pitfall: library code is compiled and tested against one version, but at runtime the application's full dependency graph may resolve a different version, leading to unexplained behavior changes.

To mitigate such surprises, Gradle introduced 'consistent resolution', which aims to align dependency versions across the whole build (e.g., for both the library and the application) so that the same version is used everywhere. This ensures that what you test is what you run. The video thus recommends using consistent resolution to make dependency conflict resolution more predictable and to reduce the risk of hidden version mismatches.

- Gradle's default conflict resolution is 'highest version wins'.
- A transitive dependency can raise a library's version unexpectedly, changing behavior.
- Unit tests may not catch version conflicts because they run against a different classpath than the final application.
- Consistent resolution aligns dependency versions across projects to prevent such mismatches.