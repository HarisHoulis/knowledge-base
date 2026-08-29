---
domain: android-kotlin
subdomain: gradle-build-tool
concept: source-sets
title: Understanding Gradle #16 – Source Sets
sources:
  - title: "Understanding Gradle #16 – Source Sets"
    url: "https://www.youtube.com/watch?v=74PDtHkS_w4"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2022-06-15T16:25:12+00:00"
---

# Understanding Gradle #16 – Source Sets

In this video, Jendrik Johannes explains the concept of source sets in Gradle, building on fundamental Gradle concepts from previous videos. Source sets are a rich data model that centralize information about where source code and resources are located, how they are compiled or processed, and where the resulting outputs are stored. This model is used by Gradle to configure tasks automatically and by IDEs to provide navigation and other tooling features.

The Java plugin adds source sets by default, creating 'main' and 'test' source sets for JVM projects. Each source set is composed of multiple source directory sets (e.g., Java and resources) which can be configured individually. Source sets also carry associated configuration like compile classpath, making them a central point for customizing build logic or adding new tasks. Other Gradle plugins, such as Android or Kotlin Multiplatform, provide similar source set APIs tailored to their respective domains.

- Source sets group source code, resources, task configurations, and outputs into a single model.
- The Java plugin automatically creates 'main' and 'test' source sets for JVM projects.
- Source sets are composed of source directory sets (e.g., java, resources) that can be configured separately.
- IDEs use source set information to enable code navigation and other features.
- Source sets centralize access to classpaths and other build information for custom tasks.