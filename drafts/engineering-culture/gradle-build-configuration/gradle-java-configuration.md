---
domain: engineering-culture
subdomain: gradle-build-configuration
concept: gradle-java-configuration
title: Using Java to configure Gradle builds
sources:
  - title: "Understanding Gradle #25 – Using Java to configure builds"
    url: "https://www.youtube.com/watch?v=XnVZdMROVG8"
    author: "Jendrik Johannes"
    date: "2022-10-17T14:16:10+00:00"
---

# Using Java to configure Gradle builds

This video demonstrates that Gradle builds can be configured entirely in Java, eliminating the need for XML, Groovy, or Kotlin DSLs. The core approach is based on convention plugins, which are used to centralize and reuse build logic. The tutorial shows how to set up convention plugins in Java, including defining plugin IDs and specifying the Java version for plugin code (Johannes, 2022).

With Java-based configuration, developers can apply other plugins, access extensions, set core Gradle properties, configure tasks, define dependencies or constraints, create custom extensions and tasks, and configure repositories and included builds in settings. All of this is done in a type-safe manner, leveraging Gradle's Java API directly (Johannes, 2022).

The video also highlights that other JVM languages such as Scala can be used for build configuration, and provides example projects on GitHub for both Kotlin DSL and Groovy DSL setups. This approach is positioned as a straightforward alternative for Java-centric projects, making Gradle more accessible to Java developers without requiring knowledge of additional DSLs (Johannes, 2022).

- Gradle build logic can be written entirely in Java, avoiding XML, Groovy, or Kotlin DSLs.
- Convention plugins are the recommended way to centralize and reuse build configuration.
- Java plugins provide full type safety and direct access to Gradle APIs for tasks, extensions, dependencies, and settings.
- Other JVM languages like Scala are also supported for writing build logic.
- Example projects demonstrate the setup with both Kotlin DSL and Groovy DSL variants.