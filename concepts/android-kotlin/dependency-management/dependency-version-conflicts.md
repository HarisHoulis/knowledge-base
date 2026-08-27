---
domain: android-kotlin
subdomain: dependency-management
concept: dependency-version-conflicts
title: Understanding Gradle #10 – Dependency Version Conflicts
sources:
  - title: "Understanding Gradle #10 – Dependency Version Conflicts"
    url: "https://www.youtube.com/watch?v=YYWhfy6c2YQ"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-10-18T20:49:08+00:00"
---

# Understanding Gradle #10 – Dependency Version Conflicts

Dependency version conflicts arise when multiple dependencies in a Gradle build require different versions of the same library. For example, the project's own dependency on commons-lang 3.6 conflicts with the version 3.7 that commons-text 1.4 transitively requires. Gradle's default conflict resolution is a simple "highest version wins" rule, based on the assumption that newer versions are backward compatible (Jendrik Johannes, Understanding Gradle #10, YouTube, 2021).

This heuristic can lead to subtle problems. The author demonstrates a scenario where the business logic module is compiled and tested against commons-lang 3.6, but when assembled into the full application, commons-text 1.5 pulls in commons-lang 3.8.1. This newer version fixes a bug that changes behavior the code relies on—detecting leading zeros—causing an unexpected regression at runtime. Because the unit tests run in isolation, they still pass with the old version, so the breakage goes unnoticed (Jendrik Johannes, Understanding Gradle #10, YouTube, 2021).

The root cause is that dependency resolution happens for the final application graph, not per-module. To address this, Gradle introduced a "consistent resolution" feature that aligns versions across projects, reducing the risk of conflicts and ensuring the versions used for compilation and testing match those used in the final runtime classpath (Jendrik Johannes, Understanding Gradle #10, YouTube, 2021).

- A dependency version conflict occurs when two or more dependencies require different versions of the same library.
- Gradle's default strategy for conflicting required versions is to select the highest version.
- The version chosen for a transitive dependency in a full application can differ from the version used when compiling/testing an individual module in isolation.
- This mismatch can lead to runtime behavior changes that unit tests do not catch.
- Gradle's consistent resolution feature helps avoid such surprises by aligning versions across the whole build.