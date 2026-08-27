---
domain: android-kotlin
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

The video explains capability conflicts in Gradle dependency resolution. It demonstrates a scenario where an application directly adds the SLF4J API and the SLF4J Simple runtime binding, but a framework like Dropwizard transitively brings in Logback Classic, another SLF4J binding. This results in two logging bindings on the runtime classpath, which can cause warnings or unpredictable behavior at runtime. By default, Gradle does not detect this conflict because the modules do not declare that they provide the same capability. The POM file format does not support capabilities; only the Gradle Module Metadata format, introduced in Gradle 6, allows modules to declare capabilities. Without this metadata, conflicting dependencies can silently coexist. The video then shows how adding capability metadata to the modules makes Gradle detect the conflict and report an error, making the issue visible and resolvable.

- Capability conflicts occur when different modules provide alternative implementations of the same feature.
- Gradle cannot detect these conflicts without capability metadata because POM files do not support capabilities.
- Gradle Module Metadata, introduced in Gradle 6, enables modules to declare capabilities.
- Without capability metadata, multiple conflicting dependencies can remain on the classpath silently, causing runtime issues.
- Adding capability metadata makes Gradle detect the conflict and report an error, allowing proper resolution.