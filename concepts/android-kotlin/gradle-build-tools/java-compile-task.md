---
domain: android-kotlin
subdomain: gradle-build-tools
concept: java-compile-task
title: Understanding Gradle #22 – The JavaCompile Task
sources:
  - title: "Understanding Gradle #22 – The JavaCompile Task"
    url: "https://www.youtube.com/watch?v=wFewehz6rW8"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2022-09-05T09:42:06+00:00"
---

# Understanding Gradle #22 – The JavaCompile Task

The video explains the JavaCompile task in Gradle, which is responsible for compiling Java source code. It covers the processes involved in compilation, including running inside the Gradle Daemon or in a separate worker process, and how tasks can be executed in parallel. The configuration of the task is shown through the options available in the Gradle DSL, such as fork, javaHome, executable, release, and compatibility settings, which control whether compilation uses the daemon, an external tool, or a different Java version.

- JavaCompile can run in the Gradle Daemon, in a worker process, or via an external compiler process.
- The fork option controls whether compilation happens in a separate process; javaHome and executable let you specify a different JDK or compiler executable.
- release and compatibility options control the target Java version and source compatibility.
- gradle.properties can be used to configure daemon memory (e.g., org.gradle.jvmargs) and parallel execution (org.gradle.parallel=true).
- Configuration can be applied to all JavaCompile tasks in a project using the tasks.withType<JavaCompile>() or tasks.withType(JavaCompile) DSL.