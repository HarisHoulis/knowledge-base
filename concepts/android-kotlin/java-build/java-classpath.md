---
domain: android-kotlin
subdomain: java-build
concept: java-classpath
title: Understanding Gradle #26 – The Classpath
sources:
  - title: "Understanding Gradle #26 – The Classpath"
    url: "https://www.youtube.com/watch?v=HqAp9JBl2_U"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2022-11-21T09:13:48+00:00"
---

# Understanding Gradle #26 – The Classpath

In this video (Johannes, 2022), the concept of the Java classpath is introduced as part of a series on Java modularity. The classpath is the fundamental mechanism Java uses to locate compiled classes and resources during compilation and execution. The video demonstrates how to manually pass the classpath to the `javac` compiler and the `java` runtime, showing the pitfalls of managing it by hand and how changing the runtime classpath affects program behavior.

The video then shifts to Gradle, explaining how Gradle automates classpath construction through dependency resolution. It shows how to compile and run Java code with Gradle, and how Gradle distinguishes between compile-time and runtime classpaths. It also explains that testing uses its own set of classpaths, which can include additional dependencies such as testing libraries. The overall message is that Gradle simplifies classpath management by resolving dependencies and constructing the correct classpaths for each task (Johannes, 2022).

- The classpath is a critical concept in Java for locating classes at compile time and runtime.
- Manually managing the classpath with `javac` and `java` is error-prone and hard to scale.
- Gradle automatically constructs classpaths based on declared dependencies.
- Gradle uses separate classpaths for compiling, running, and testing Java code.
- Understanding classpaths helps developers debug and optimize Gradle builds.