---
domain: system-design
subdomain: dependency-management
concept: capability-conflicts
title: Understanding Gradle #11 – Capability Conflicts
sources:
  - title: "Understanding Gradle #11 – Capability Conflicts"
    url: "https://www.youtube.com/watch?v=5g20kbbqBFk"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-11-01T17:58:03+00:00"
---

# Understanding Gradle #11 – Capability Conflicts

The video explains capability conflicts in Gradle dependency resolution. A version conflict occurs when the same module with different versions is requested, which Gradle detects by matching group and name coordinates. Capability conflicts are different: they involve different modules that provide alternative implementations for the same thing, such as SLF4J bindings. Gradle cannot detect these automatically unless modules declare their capabilities in metadata. The traditional POM file format does not support capability declarations, so Gradle 6 introduced the Gradle Module Metadata format to let libraries publish such information.

In the example, adding Dropwizard transitively brought in Logback Classic while the user explicitly declared SLF4J Simple, resulting in two bindings on the runtime classpath. Without capability metadata, Gradle resolved the dependencies without error, and only a runtime warning appeared. After adding capability metadata to the local module versions, Gradle correctly detected the conflict and produced an error. The video emphasizes that understanding capabilities is key to avoiding subtle runtime issues, and that declaring capabilities lets Gradle fail fast and allows users to specify which alternative they prefer.

- Capability conflicts occur when different modules implement the same functionality, unlike version conflicts which share group and name coordinates.
- Gradle requires capability metadata, such as Gradle Module Metadata, to detect these conflicts; POM files do not support capability declarations.
- Without metadata, conflicting bindings (e.g., SLF4J Simple vs Logback Classic) can silently appear on the classpath, leading to runtime warnings or subtle bugs.
- Declaring capabilities allows Gradle to fail resolution with a clear error, and users can express preferences among conflicting alternatives.