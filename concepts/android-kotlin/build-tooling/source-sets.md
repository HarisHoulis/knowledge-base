---
domain: android-kotlin
subdomain: build-tooling
concept: source-sets
title: Understanding Gradle #16 – Source Sets
sources:
  - title: "Understanding Gradle #16 – Source Sets"
    url: "https://www.youtube.com/watch?v=74PDtHkS_w4"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2022-06-15T16:25:12+00:00"
---

# Understanding Gradle #16 – Source Sets

Source sets in Gradle are a rich model that encapsulate where source files and resources live, how they are compiled or processed by tasks, and where the resulting outputs are placed. While Gradle tasks can directly reference sources and outputs, source sets provide a structured, IDE-friendly abstraction that groups related configuration and feeds it into task setups automatically. This makes builds more maintainable and enables tooling like IDEs to offer navigation and other conveniences based on known source locations.

By default, the Java plugin introduces two source sets: `main` and `test`. Each source set is a combination of multiple source directory sets (e.g., `java`, `resources`), allowing fine-grained configuration, such as changing or adding source directories. The Java plugin registers a `sourceSets` extension, and similar concepts exist in Android and Kotlin Multiplatform projects, though with different APIs. Source sets serve as a central point to modify conventions or access information for additional custom tasks.

- Source sets aggregate source locations, build tasks, and outputs into a coherent model.
- IDE integration relies on source sets to understand project structure and provide navigation.
- The Java plugin creates default `main` and `test` source sets.
- Each source set contains multiple source directory sets (e.g., Java vs. resources).
- Source sets can be customized to change or add source directories.