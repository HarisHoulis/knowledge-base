---
domain: android-kotlin
subdomain: gradle-build
concept: source-sets
title: Understanding Gradle #16 – Source Sets
sources:
  - title: "Understanding Gradle #16 – Source Sets"
    url: "https://www.youtube.com/watch?v=74PDtHkS_w4"
    author: "Jendrik Johannes"
    date: "2022-06-15"
---

# Understanding Gradle #16 – Source Sets

Source sets are a core abstraction in Gradle that bundle information about where source code and resources live, how they are compiled or processed, and where the resulting outputs are placed. The Java plugin automatically creates two source sets by default—main and test—for every JVM project, including Kotlin/JVM. Source sets also feed configuration into tasks: for example, the compileJava and processResources tasks receive their inputs and outputs from the source set model, and the jar task can simply take all outputs of a source set to create an archive (Jendrik Johannes, 2022).

- Source sets provide a rich model that centralizes source locations, task wiring, and output directories.
- The Java plugin adds a sourceSets extension with pre-created main and test source sets.
- A source set is composed of multiple source directory sets, enabling separate configuration for Java, resources, and other languages.
- Methods like setSrcDirs replace directories, while srcDir adds additional source folders.
- Android and Kotlin Multiplatform plugins offer similar source set concepts with language-specific APIs.