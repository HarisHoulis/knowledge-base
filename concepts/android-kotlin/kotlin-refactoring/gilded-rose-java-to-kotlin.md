---
domain: android-kotlin
subdomain: kotlin-refactoring
concept: gilded-rose-java-to-kotlin
title: Java to Kotlin Gilded Rose - Part 1 Refactoring to Objects
sources:
  - title: "Java to Kotlin Gilded Rose - Part 1 Refactoring to Objects"
    url: "https://www.youtube.com/watch?v=rpGGTT7IuCs"
    author: "Pairing with Duncan"
    date: "2021-10-18T20:30:17+00:00"
---

# Java to Kotlin Gilded Rose - Part 1 Refactoring to Objects

This video, presented by Duncan, demonstrates the initial steps of converting a Java project to Kotlin using the Gilded Rose Kata as an example. The focus is on importing an existing Java project into IntelliJ, enabling Kotlin, and incrementally converting code so that Java and Kotlin can coexist within the same codebase. The author also emphasizes the importance of having a solid test harness before refactoring, as the existing procedural code (particularly the updateQuality method) is confusing and error-prone.

- Incremental conversion allows Java and Kotlin to interoperate, making it easier to migrate a project piece by piece.
- The Gilded Rose Kata provides a procedural, hard-to-understand codebase that serves as a good refactoring exercise.
- Before refactoring, the presenter converts a main method into a JUnit test by capturing System.out using ByteArrayOutputStream and PrintStream, then asserting the output.
- The refactoring plan is to first move from procedural to object-oriented style, and later to a more functional style that better suits Kotlin.