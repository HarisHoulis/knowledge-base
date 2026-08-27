---
domain: android-kotlin
subdomain: gradle
concept: gradle-tasks
title: Understanding Gradle #04 – Tasks
sources:
  - title: "Understanding Gradle #04 – Tasks"
    url: "https://www.youtube.com/watch?v=9tY4MFEgmgM"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-08-23T10:29:46+00:00"
---

# Understanding Gradle #04 – Tasks

This video explains the core concept of tasks in Gradle, using a plain/empty project as a starting point. It shows how the Base plugin adds lifecycle tasks (like `build`) and how the Java Library plugin introduces additional actionable tasks. The key distinction is between lifecycle tasks, which orchestrate other tasks but perform no direct work, and actionable tasks that actually execute actions. Gradle tasks are incremental: they can reuse outputs from previous build runs or from the build cache, making builds faster by skipping unnecessary work. The video also demonstrates task dependencies, showing how Gradle constructs a task graph to determine execution order, and covers tasks added by the Application plugin for running applications.

- Gradle builds are organized around tasks, which are contributed by plugins.
- Lifecycle tasks (e.g., `build`) do not perform work themselves but depend on actionable tasks.
- Incremental builds and the build cache allow Gradle to reuse previous task outputs.
- Tasks can have dependencies, forming a graph that Gradle executes in order.
- Plugins like Base, Java Library, and Application provide pre-defined tasks for common workflows.