---
domain: android-kotlin
subdomain: dependency-management
concept: gradle-capability-conflicts
title: Understanding Gradle #11 – Capability Conflicts
sources:
  - title: "Understanding Gradle #11 – Capability Conflicts"
    url: "https://www.youtube.com/watch?v=5g20kbbqBFk"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-11-01T17:58:03+00:00"
---

# Understanding Gradle #11 – Capability Conflicts

This video explains capability conflicts in Gradle dependency resolution, which occur when different modules provide alternative implementations of the same capability. Unlike version conflicts, where Gradle can detect conflicts because the group and name coordinates are identical, capability conflicts are not automatically detected unless modules explicitly declare their capabilities. In the example, adding Dropwizard transitively brings in Logback Classic, causing two SLF4J bindings on the runtime classpath without Gradle raising an error, leading to runtime warnings or subtle issues (Jendrik Johannes, 2021).

Gradle introduced the Gradle Module Metadata format in Gradle 6 to support declaring capabilities, as the traditional POM format cannot represent this concept. By adding capability metadata to the conflicting modules, Gradle can detect and report a capability conflict error. The video demonstrates this by using local copies with added metadata. It also emphasizes that many libraries still lack this metadata, so conflicts may go unnoticed, and suggests that developers need to understand how to manage preferences when multiple capabilities are available (Jendrik Johannes, 2021).

- Capability conflicts arise when different modules provide alternative implementations of the same capability.
- Gradle cannot detect capability conflicts without explicit capability metadata; POM files do not support this concept.
- Gradle Module Metadata, introduced in Gradle 6, enables modules to declare capabilities.
- Missing capability metadata can lead to runtime warnings or subtle bugs that are hard to debug.
- Declaring capabilities helps Gradle identify conflicts and allows developers to resolve them.