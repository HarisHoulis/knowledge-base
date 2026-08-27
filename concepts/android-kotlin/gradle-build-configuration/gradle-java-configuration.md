---
domain: android-kotlin
subdomain: gradle-build-configuration
concept: gradle-java-configuration
title: Using Java to configure Gradle builds
sources:
  - title: "Understanding Gradle #25 – Using Java to configure builds"
    url: "https://www.youtube.com/watch?v=XnVZdMROVG8"
    author: "Jendrik Johannes"
    date: "2022-10-17"
---

# Using Java to configure Gradle builds

This video demonstrates how to configure Gradle builds entirely in Java, without relying on XML, Groovy, or Kotlin DSL. It builds on a convention plugins setup, showing how to write convention plugins in Java. The process involves defining plugin IDs, setting the Java version for plugins, and creating a plugin implementation class that implements the 'Plugin<Project>' interface (Jendrik Johannes, 2022).

- Convention plugins can be implemented in plain Java using the Plugin<Project> interface.
- Access all Gradle DSL features through the Project and Settings APIs.
- Configure tasks, dependencies, extensions, and settings programmatically in Java.
- Java-based configuration is a viable alternative to Groovy or Kotlin DSL, with support for other JVM languages.
- Includes practical examples for repositories, included builds, and custom tasks.