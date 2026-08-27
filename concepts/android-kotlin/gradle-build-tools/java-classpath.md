---
domain: android-kotlin
subdomain: gradle-build-tools
concept: java-classpath
title: Understanding Gradle #26: The Classpath
sources:
  - title: "Understanding Gradle #26 – The Classpath"
    url: "https://www.youtube.com/watch?v=HqAp9JBl2_U"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2022-11-21T09:13:48+00:00"
---

# Understanding Gradle #26: The Classpath

This video explains the Java classpath as a fundamental concept for compiling and running Java applications. The classpath is a list of directories and JAR files containing compiled classes that the Java compiler (`javac`) and runtime (`java`) use to locate dependencies. The video demonstrates how manually specifying the classpath works, and then shows how Gradle automates this process through configurations and dependency resolution.

Gradle builds classpaths for different tasks: compile classpath for `JavaCompile`, runtime classpath for `JavaExec`, and test classpaths for test tasks. Dependency resolution transforms declared dependencies (e.g., in Maven Central) into files on the classpath, and Gradle ensures the correct classpath is used for each Task. The video also covers how tests have their own classpath (including the test framework's dependencies) and how Gradle manages distinct classpaths for compilation, runtime, and testing.

By the end, viewers understand that the classpath is a modularity mechanism in Java, and Gradle's value lies in automatically constructing and isolating classpaths for various build and test tasks, avoiding manual JAR management.

- The classpath is a list of directories/JARs containing compiled Java classes, used by both `javac` and `java`.
- Gradle uses configurations (like `implementation` and `testImplementation`) to declare dependencies and resolve them into classpaths.
- Different tasks (compile, run, test) have distinct classpaths in Gradle, with the test classpath including the test framework and additional test dependencies.
- Gradle's dependency resolution fetches artifacts from repositories and constructs the classpath automatically.
- The video demos a full Gradle build (compile, run, test) and shows how to inspect and customize classpath construction.