---
domain: android-kotlin
subdomain: dependency-management
concept: capability-conflicts
title: Understanding Gradle #11 – Capability Conflicts
sources:
  - title: "Understanding Gradle #11 – Capability Conflicts"
    url: "https://www.youtube.com/watch?v=5g20kbbqBFk"
    author: "Jendrik Johannes"
    date: "2021-11-01"
---

# Understanding Gradle #11 – Capability Conflicts

Jendrik Johannes explains capability conflicts in Gradle dependency resolution. Capability conflicts occur when different modules provide alternative implementations of the same thing, such as multiple SLF4J bindings. Unlike version conflicts, Gradle cannot automatically detect capability conflicts because Maven POM files lack a capability concept. To enable detection, modules must publish Gradle Module Metadata that declares their capabilities (Johannes, 2021). Without this metadata, conflicts may go unnoticed and only appear as runtime warnings or subtle errors. Gradle can only resolve a capability conflict if it knows the conflicting modules share a capability, so libraries need to provide this information. In practice, you may need to add the metadata manually or use dependency resolution strategies to handle conflicts.

- Capability conflicts arise when different modules provide the same API or implementation.
- Gradle requires Gradle Module Metadata to detect capability conflicts; Maven POM files do not support capabilities.
- Without metadata, conflicts go undetected and can lead to runtime warnings or unpredictable behavior.
- Libraries must declare capabilities for Gradle to fail or resolve conflicts automatically.