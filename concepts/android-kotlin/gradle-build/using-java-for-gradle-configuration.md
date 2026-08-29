---
domain: android-kotlin
subdomain: gradle-build
concept: using-java-for-gradle-configuration
title: Understanding Gradle #25 – Using Java to configure builds
sources:
  - title: "Understanding Gradle #25 – Using Java to configure builds"
    url: "https://www.youtube.com/watch?v=XnVZdMROVG8"
    author: "Jendrik Johannes"
    date: "2022-10-17T14:16:10+00:00"
---

# Understanding Gradle #25 – Using Java to configure builds

This video demonstrates how to configure Gradle builds using Java directly, eliminating the need for XML, Groovy, or Kotlin DSLs. It builds on a convention plugins setup and shows how to implement convention plugins in Java, define plugin IDs, and specify the Java version for plugin compilation. The approach uses standard Java classes to implement Gradle plugins, which are then applied to projects (https://www.youtube.com/watch?v=XnVZdMROVG8).

The video walks through the practical configuration steps: applying plugins, accessing Gradle extensions, setting core properties like repositories, configuring tasks, defining dependencies and constraints, and creating custom extensions and tasks. It also covers configuring Settings, including repositories, included builds, and subprojects, all through Java code. The examples are available on GitHub for both Kotlin DSL and Groovy DSL variants (https://github.com/jjohannes/understanding-gradle/tree/main/25_Using_Java_to_configure_builds).

Finally, the video notes that other JVM languages, such as Scala, can also be used for Gradle configuration. It references the Gradle documentation and sample for writing plugins in Java, and concludes with a summary of the benefits of using Java for build configuration, such as better IDE support and explicit typing.

- Use Java to write Gradle convention plugins, avoiding Groovy or Kotlin DSL syntax.
- Define plugin IDs and Java version directly in the plugin implementation.
- Configure tasks, extensions, dependencies, and custom plugins through the Gradle Java API.
- Settings files (repositories, included builds, subprojects) are also configurable in Java.
- The approach is compatible with other JVM languages like Scala.