---
domain: android-kotlin
subdomain: gradle
concept: java-build-config
title: Using Java to configure Gradle builds
sources:
  - title: "Understanding Gradle #25 – Using Java to configure builds"
    url: "https://www.youtube.com/watch?v=XnVZdMROVG8"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2022-10-17T14:16:10+00:00"
---

# Using Java to configure Gradle builds

This video demonstrates that Gradle builds can be configured entirely in Java, without XML, Groovy, or Kotlin DSL. It builds on a convention plugins setup and shows how to write convention plugins as Java classes that implement `Plugin<Project>`. Plugin IDs are defined as static constants, and the Java version for plugins is specified in the build configuration. (source: https://www.youtube.com/watch?v=XnVZdMROVG8)

Inside the plugin's apply method, you can programmatically configure the build: apply other plugins, access and configure extensions, set core Gradle properties, configure tasks, define dependencies and constraints, and create custom extensions and tasks. Settings plugins can similarly configure repositories, included builds, and subprojects through the `Settings` API. This approach gives full access to Gradle's Java APIs and is a supported alternative to using DSLs. (source: https://www.youtube.com/watch?v=XnVZdMROVG8)

Gradle is JVM-based, so you can also use other JVM languages like Scala for build configuration. The video references example projects on GitHub and official Gradle documentation for writing plugins in Java, making it practical to adopt this style in real projects. (source: https://www.youtube.com/watch?v=XnVZdMROVG8)

- Gradle builds can be configured with plain Java via convention plugins, eliminating the need for XML, Groovy, or Kotlin DSL.
- A convention plugin class implements `Plugin<Project>`, and its plugin ID is defined as a string constant.
- The Java API allows applying plugins, configuring extensions and tasks, setting properties, and defining dependencies programmatically.
- Settings files can also be configured in Java using the `Settings` API to manage repositories, included builds, and subprojects.
- Because Gradle is JVM-based, other JVM languages like Scala can be used for build configuration.