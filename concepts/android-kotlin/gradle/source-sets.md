---
domain: android-kotlin
subdomain: gradle
concept: source-sets
title: Understanding Gradle #16 – Source Sets
sources:
  - title: "Understanding Gradle #16 – Source Sets"
    url: "https://www.youtube.com/watch?v=74PDtHkS_w4"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2022-06-15T16:25:12+00:00"
---

# Understanding Gradle #16 – Source Sets

In the 16th episode of the Understanding Gradle series, Jendrik Johannes explains the concept of source sets, which are a fundamental abstraction introduced by the Java Gradle plugin. A source set is more than just a folder; it is a data structure that centralizes information about where source code and resources live, which tasks compile or process them, and where the output files are placed. This allows Gradle to automatically wire task dependencies (e.g., compileJava, processResources) and makes the build setup more comprehensible and better supported by IDEs like IntelliJ. The transcript contrasts this with a naive setup where source paths would be hidden inside task configurations, showing how source sets provide a richer model ([source](https://www.youtube.com/watch?v=74PDtHkS_w4)).

Source sets are composed of multiple source directory sets, such as `java` and `resources`, which are combined into a single source set (e.g., `main`). Each source directory set can be configured independently, allowing you to change the source folder or add additional directories. The default `main` and `test` source sets are created automatically by the Java plugin, and other JVM plugins (Groovy, Scala, Kotlin) follow a similar pattern. Android projects and Kotlin Multiplatform projects also use source sets, though with slightly different APIs tailored to their respective build environments. The video emphasizes that source sets act as a central point to modify conventions and gather information for custom tasks, making them essential for any non-trivial Gradle build ([source](https://www.youtube.com/watch?v=74PDtHkS_w4)).

- Source sets are a rich model introduced by the Java plugin that group source directories, build tasks, outputs, and classpath information.
- The default `main` and `test` source sets are created automatically, and IDEs use them to recognize source folders and enable navigation.
- Each source set combines multiple source directory sets (e.g., java, resources), which can be individually configured to change or add source folders.
- Custom source sets and modifications to existing ones allow adapting the build to non-standard layouts and integrating extra tasks.
- Android and Kotlin Multiplatform projects also have source sets, but with different APIs specific to their ecosystems.