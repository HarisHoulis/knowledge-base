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

In this video, Jendrik Johannes explains the nature of dependency version conflicts in Gradle, how they arise, and how Gradle resolves them by default. He demonstrates that when multiple dependencies require different versions of the same library, Gradle's default conflict resolution is to select the highest required version, operating on a "higher version wins" rule (Jendrik Johannes, 2021). This approach is a best guess that assumes higher versions are backward compatible, but it can lead to unexpected behavior when a transitive dependency pulls in a higher version without the developer actively changing anything.

The video illustrates a real-world scenario: upgrading commons-text from 1.4 to 1.5 causes commons-lang to jump from 3.6 to 3.8.1 because the new commons-text depends on a newer commons-lang. This fix changes the behavior of a method (NumberUtils.isCreatable) that the developer's code relied upon, breaking the application even though the library's unit tests still pass. The problem is that the dependency conflict only appears at the application runtime classpath, not in the library's isolated test classpath, so the issue goes unnoticed during development (Jendrik Johannes, 2021).

To address such surprises, Gradle introduced a feature called consistent resolution, which helps ensure that the same dependency versions are used across all projects and configurations, reducing the gap between compilation/test time and runtime behavior. The video emphasizes that understanding conflict resolution is crucial for any developer working with external libraries and transitive dependencies (Jendrik Johannes, 2021).

- Dependency version conflicts arise when different modules in the dependency graph declare different required versions of the same library.
- Gradle's default conflict resolution rule is 'higher version wins', assuming backward compatibility, but this can lead to unintended runtime behavior.
- Upgrading a direct dependency can pull a newer transitive dependency that changes behavior in your code, even if your tests still pass.
- The inconsistency between a library's test classpath and the application's runtime classpath is a common root cause of subtle issues.
- Gradle's consistent resolution feature helps avoid surprises by aligning dependency versions across projects and configurations.