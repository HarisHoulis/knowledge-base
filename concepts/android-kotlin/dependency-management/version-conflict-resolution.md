---
domain: android-kotlin
subdomain: dependency-management
concept: version-conflict-resolution
title: Understanding Gradle #10 – Dependency Version Conflicts
sources:
  - title: "Understanding Gradle #10 – Dependency Version Conflicts"
    url: "https://www.youtube.com/watch?v=YYWhfy6c2YQ"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-10-18T20:49:08+00:00"
---

# Understanding Gradle #10 – Dependency Version Conflicts

Dependency version conflicts occur when multiple dependencies in a Gradle build require different versions of the same library. In the video, Jendrik Johannes demonstrates how adding commons-text to an application pulls in commons-lang3, leading to versions 3.6 and 3.7 appearing in the runtime classpath. Gradle's default resolution is simply "higher version wins," under the assumption that newer versions are backward compatible (Johannes, 2021).

However, this default strategy can cause subtle problems. When the author upgrades commons-text from 1.4 to 1.5, commons-lang3 is bumped to 3.8.1, which includes a bug fix that changes how numbers with leading zeros are handled. The business logic module's tests still pass because its test runtime classpath has no conflict and picks the older 3.6 from a constraint. But in the full application runtime, the conflicting graph resolves to 3.8.1, causing the application to behave differently from the tests.

Gradle's newer "consistent resolution" feature aims to avoid such surprises by aligning versions across the dependency graph, so the version tested is the version that runs. The video emphasizes that without such alignment, conflicts can go unnoticed for a long time, only surfacing after a dependency update changes behavior unexpectedly (Johannes, 2021).

- Gradle resolves dependency version conflicts by selecting the highest required version.
- Transitive dependencies can introduce version conflicts that override explicit constraints.
- Test classpaths and application runtime classpaths can differ, causing tests to pass while the app fails.
- Consistent resolution helps avoid surprises by aligning dependency versions across the graph.