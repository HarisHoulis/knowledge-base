---
domain: android-kotlin
subdomain: gradle
concept: capability-conflicts
title: Understanding Gradle #11 – Capability Conflicts
sources:
  - title: "Understanding Gradle #11 – Capability Conflicts"
    url: "https://www.youtube.com/watch?v=5g20kbbqBFk"
    author: "Jendrik Johannes"
    date: "2021-11-01"
---

# Understanding Gradle #11 – Capability Conflicts

To let Gradle detect such conflicts, modules need to publish capability metadata. The Maven POM format does not support this, so Gradle introduced Gradle Module Metadata in Gradle 6. In the video, the author manually adds capability metadata to local copies of slf4j-simple and logback-classic, after which Gradle raises a capability conflict error instead of silently accepting both bindings. This highlights the importance of capability metadata for conflict detection and the need for explicit resolution when conflicts exist. (Jendrik Johannes, 2021)

- Capability conflicts arise when different modules provide alternative implementations of the same API or feature.
- Gradle cannot detect capability conflicts unless modules declare their capabilities via Gradle Module Metadata.
- Maven POM format does not support capabilities; Gradle 6 introduced module metadata to fill this gap.
- In the SLF4J example, adding capability metadata to the local copies enabled Gradle to detect the conflict and fail, rather than allowing both bindings on the runtime classpath.
- Without capability metadata, conflicts often surface only as runtime warnings or hard-to-debug issues.