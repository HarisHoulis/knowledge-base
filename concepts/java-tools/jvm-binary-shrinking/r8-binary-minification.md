---
domain: java-tools
subdomain: jvm-binary-shrinking
concept: r8-binary-minification
title: Shrinking a Kotlin Binary by 99.2%
sources:
  - title: "Shrinking a Kotlin binary by 99.2%"
    url: "https://jakewharton.com/shrinking-a-kotlin-binary/"
    author: "Jake Wharton"
---

# Shrinking a Kotlin Binary by 99.2%

Jake Wharton describes how he reduced a Kotlin JVM binary from roughly 1.62 MiB to 13,643 bytes (99.2% smaller). The tool, dependency-tree-diff, was originally built to show dependency tree changes in pull requests. The first version used Kotlin script, but CI lacked kotlinc, so he switched to a Kotlin Gradle project and produced a fat JAR with kotlin-stdlib included [1].

Initial reductions came from filtering unused files such as .kotlin_metadata, module-info.class, and Maven metadata, yielding an 11% smaller binary. Then R8, normally used for Android, was applied to the JAR for code shrinking, dropping the binary to about 37 KiB after adding -allowaccessmodification. Further manual code changes replaced kotlin.io.File.readText with java.nio.file.Paths.readString and Kotlin's lineSequence with Java 11's String.lines, cutting the binary to 13,643 bytes [1].

The remaining size is dominated by Kotlin's empty collection implementations and redundant Intrinsics null checks, some of which stem from an R8 bug caused by Kotlin's method renaming. The article concludes by recommending R8, ProGuard, or Graal native image for anyone building JVM binaries or shaded libraries [1].

- Measuring and reconsidering standard library usage can drastically reduce JVM binary size.
- R8 can optimize Java classfiles, not just Android DEX, when given the right ProGuard configuration.
- Filtering unused metadata and module files gives an initial easy size reduction.
- Using Java 11's built-in String.lines() and java.nio readString methods avoided pulling in Kotlin's sequence and file utilities.
- Kotlin's empty collections and intrinsic null checks still contribute significantly to the final binary size.