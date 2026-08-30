---
domain: engineering-culture
subdomain: gradle-testing
concept: classpath-modulepath-testing
title: Understanding Gradle #33: Classpath and Module Path in Testing
sources:
  - title: "Understanding Gradle #33 – Classpath and Module Path in Testing"
    url: "https://www.youtube.com/watch?v=6rFEDcP8Noc"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2023-06-19T13:38:43+00:00"
---

# Understanding Gradle #33: Classpath and Module Path in Testing

In Gradle, each source set has its own compile and runtime classpaths, and tests are typically executed on the classpath alongside regular dependencies. The video explains how this works and how conflicts on classpaths can be resolved (1:35–4:40). When testing Java modules, Gradle supports two approaches: blackbox testing, where the test code is itself a module and the system under test is on the module path, and whitebox testing, where test code is placed on the classpath and uses module patching to access internals (8:24–14:08).

The video also introduces the java-module-testing plugin, which simplifies setting up modular tests, especially for whitebox scenarios (12:43). It emphasizes that while classpath-based testing is simpler and works for most projects, modular projects require careful consideration of the module path to avoid runtime errors. The examples are shown using Kotlin DSL and are available on GitHub (0:00–8:00, 14:08–18:00).

- In Gradle, every source set has its own compile and runtime classpaths for testing.
- Classpath-based testing is the default and works by putting all dependencies on the classpath, but conflicts can arise.
- For Java modules, tests can be run as blackbox (test is a module) or whitebox (test patches the module via classpath).
- The java-module-testing plugin automates the configuration needed for module-path tests.
- Understanding the difference between classpath and module path is crucial for modular Java projects.