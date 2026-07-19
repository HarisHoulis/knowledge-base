---
domain: android-kotlin
subdomain: refactoring
concept: gilded-rose-refactoring
title: Java to Kotlin Gilded Rose - Part 1 Refactoring to Objects
sources:
  - title: "Java to Kotlin Gilded Rose - Part 1 Refactoring to Objects"
    url: "https://www.youtube.com/watch?v=rpGGTT7IuCs"
    author: "Duncan (Pairing with Duncan)"
    date: "2021-10-18T20:30:17+00:00"
---

# Java to Kotlin Gilded Rose - Part 1 Refactoring to Objects

This video demonstrates the process of converting a procedural Java implementation of the Gilded Rose kata to a more object-oriented and eventually functional Kotlin style. The author starts by importing a Java project into IntelliJ, enabling Kotlin support via Gradle, and fixing a pre-existing failing test to ensure the codebase is in a known good state. A key technique shown is converting a main method that prints output into a proper automated test using a ByteArrayOutputStream to capture output and assert against expected results, thus creating a regression test for refactoring safety. The video emphasizes incremental refactoring, keeping tests passing throughout, and lays the groundwork for deeper structural changes in subsequent parts.

- Start by importing a Java project and enabling Kotlin support, ensuring all existing tests pass before refactoring.
- Convert a manually verified main method into an automated test by redirecting System.out to a ByteArrayOutputStream and asserting equality with expected output.
- Use the Gilded Rose kata as an example to incrementally transform procedural code into object-oriented and then functional Kotlin code.
- The refactoring approach relies on regression tests to validate each step without breaking existing functionality.