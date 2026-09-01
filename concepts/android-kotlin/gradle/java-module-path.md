---
domain: android-kotlin
subdomain: gradle
concept: java-module-path
title: Understanding Gradle #31 – The Module Path
sources:
  - title: "Understanding Gradle #31 – The Module Path"
    url: "https://www.youtube.com/watch?v=X9u1taDwLSA"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2023-03-07T19:15:01+00:00"
---

# Understanding Gradle #31 – The Module Path

This video explains the Java Module System (JPMS/Jigsaw) and the module path, contrasting it with the traditional classpath. The classpath is a flat list of JARs where packages can conflict and encapsulation is weak. The module path, used for modular Java applications, enforces module boundaries via module-info.java, which declares module names, required modules, and exported packages. This provides more reliable configuration and strong encapsulation (Jendrik Johannes, 2023).

The video demonstrates how to use javac and java with the --module-path option and how to write a minimal module-info.java. It covers 'requires' directives for dependencies and 'exports' directives for package visibility. A key advantage of the module path is that Java itself detects conflicts, such as two modules providing the same package, whereas the classpath silently allows duplicate classes (Jendrik Johannes, 2023).

In the context of Gradle, dependency management remains Gradle's responsibility, but modular applications also require module-info.java to declare dependencies, leading to redundancy. The video introduces the java-module-dependencies plugin, which maps module names to Maven coordinates, reducing duplication and simplifying version management in Gradle builds (Jendrik Johannes, 2023).

- Module path is a more disciplined alternative to classpath, enforcing module boundaries and allowing Java to detect conflicts.
- module-info.java is central to JPMS, using 'requires' for dependencies and 'exports' for package visibility.
- Gradle still manages dependency coordinates, but modular applications need both Gradle dependencies and module-info declarations, causing redundancy.
- The java-module-dependencies plugin helps avoid duplication by mapping module names to Maven coordinates.
- Examples are provided in both Kotlin DSL and Groovy DSL for Gradle builds.