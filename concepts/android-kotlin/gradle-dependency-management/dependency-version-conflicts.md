---
domain: android-kotlin
subdomain: gradle-dependency-management
concept: dependency-version-conflicts
title: Understanding Gradle #10 – Dependency Version Conflicts
sources:
  - title: "Understanding Gradle #10 – Dependency Version Conflicts"
    url: "https://www.youtube.com/watch?v=YYWhfy6c2YQ"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-10-18T20:49:08+00:00"
---

# Understanding Gradle #10 – Dependency Version Conflicts

Gradle resolves dependency version conflicts by picking the highest required version. When a project depends on multiple libraries that require different versions of the same library, Gradle uses this 'highest version wins' rule, assuming newer versions are backward-compatible. However, this can lead to unexpected behavior, as demonstrated with a project using commons-lang 3.6 while a transitive dependency commons-text brings in 3.7, causing Gradle to select 3.7 (source). 

The issue becomes more serious when a transitive dependency update introduces a version whose behavior differs from the one used in isolated modules. For instance, upgrading commons-text from 1.4 to 1.5 pulls in commons-lang 3.8.1, which includes a bug fix that changes number handling—breaking the application while tests still pass. This happens because the business logic module's test classpath had no conflict and used the older 3.6, whereas the final application classpath resolved to the higher 3.8.1. Such discrepancies often go unnoticed until a dependency update surfaces them. Gradle's consistent resolution feature helps avoid these surprises by ensuring all projects and configurations use a unified set of versions (source).

- Gradle automatically resolves dependency conflicts by selecting the highest required version among conflicting libraries.
- Transitive dependency updates can silently change behavior in the final application, even if module tests pass with a different version.
- Consistent resolution helps prevent classpath mismatches by aligning versions across all projects and configurations.