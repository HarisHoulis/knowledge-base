---
domain: system-design
subdomain: gradle-build-tooling
concept: classpath-module-path-testing
title: Understanding Gradle #33 – Classpath and Module Path in Testing
sources:
  - title: "Understanding Gradle #33 – Classpath and Module Path in Testing"
    url: "https://www.youtube.com/watch?v=6rFEDcP8Noc"
    author: "Jendrik Johannes (onepiece.Software)"
    date: "2023-06-19"
---

# Understanding Gradle #33 – Classpath and Module Path in Testing

This video explains how Gradle uses the Java classpath and module path concepts specifically for testing. When testing with the classpath, each source set (main, test, etc.) has its own classpath, which can lead to dependency conflicts if not managed carefully. Gradle runs tests on the classpath in a straightforward manner, but the module system introduces stricter encapsulation that changes how tests are structured and executed. The video contrasts 'blackbox' testing (testing a module from outside, requiring the module to be packaged as a JAR) with 'whitebox' testing (testing internals by placing test classes on the module path), and demonstrates how the java-module-testing plugin simplifies whitebox testing by adding the module to the test module path.

- In Gradle, each source set has its own classpath for both compilation and test execution, and conflicts on these classpaths must be resolved explicitly.
- When using the Java Module System, testing can be performed as blackbox (against a module JAR) or whitebox (with test classes on the module path to access internals).
- The java-module-testing plugin automates the wiring needed for reliable whitebox testing with modules, handling module path and required module resolution.
- The video provides practical examples in Kotlin and Groovy DSL, showcasing how to set up both classpath-based and module-path-based testing in Gradle.