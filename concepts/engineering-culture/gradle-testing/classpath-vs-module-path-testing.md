---
domain: engineering-culture
subdomain: gradle-testing
concept: classpath-vs-module-path-testing
title: Understanding Gradle #33 – Classpath and Module Path in Testing
sources:
  - title: "Understanding Gradle #33 – Classpath and Module Path in Testing"
    url: "https://www.youtube.com/watch?v=6rFEDcP8Noc"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2023-06-19"
---

# Understanding Gradle #33 – Classpath and Module Path in Testing

This video, part of the 'Understanding Gradle' series, explains how the concepts of classpath and module path apply to testing Java projects. It starts by showing how Gradle sets up distinct classpaths for each source set—main and test—and how the test runtime classpath naturally includes the main output plus test dependencies. This setup can lead to dependency conflicts, which the video addresses by walking through typical conflict scenarios and how Gradle resolves them, while noting that collisions can still occur and need explicit handling (source: https://www.youtube.com/watch?v=6rFEDcP8Noc).

- Gradle creates separate classpaths for each source set; the test source set's runtime classpath includes main outputs and test dependencies, which can lead to conflicts.
- Classpath conflicts are resolved by Gradle's dependency resolution, but collisions can still cause issues and need explicit investigation.
- Tests can run on the classpath (non-modular) or the module path (modular), with the latter requiring module-aware configurations.
- Blackbox testing treats the module under test as a jar and tests it via its public API, while whitebox testing uses patching to access internal parts.
- The java-module-testing plugin (gradlex-org) simplifies modular testing in Gradle by handling module-path and patch configurations automatically.