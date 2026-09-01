---
domain: engineering-culture
subdomain: gradle-build
concept: classpath-modulepath-testing
title: Understanding Gradle #33 – Classpath and Module Path in Testing
sources:
  - title: "Understanding Gradle #33 – Classpath and Module Path in Testing"
    url: "https://www.youtube.com/watch?v=6rFEDcP8Noc"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2023-06-19"
---

# Understanding Gradle #33 – Classpath and Module Path in Testing

In this video, Jendrik Johannes explains how Gradle uses the classpath and module path concepts specifically for testing Java projects. He begins by revisiting that each source set (main, test, etc.) has its own compile and runtime classpaths, and these are configured independently. This means dependencies declared for tests are isolated from the main source set, and conflicts on a classpath are resolved per source set, as Gradle does not automatically unify versions across all classpaths (Johannes, 2023).

The video then contrasts testing on the classpath with testing on the module path. When tests run on the classpath, all code and dependencies are treated as plain JARs, offering no encapsulation, so test code can directly access internal classes of the main source set. In contrast, testing on the module path uses Java's module system (JPMS) to enforce boundaries, enabling blackbox testing where the test module depends on the tested module as a JAR and only sees exported packages. For whitebox testing, the test module patches the tested module to gain access to internals, which is supported by Gradle's Java Module Testing plugin (Johannes, 2023).

- Each Gradle source set (main, test, etc.) has its own dedicated classpath, and dependency conflicts are resolved per source set.
- Classpath testing treats everything as plain JARs, allowing tests to access internal classes of the production code without encapsulation.
- Module path testing enforces Java module boundaries, supporting blackbox testing (module as JAR) and whitebox testing (patching the module).
- The Java Module Testing plugin simplifies setting up module path tests in Gradle, handling blackbox and whitebox configurations.