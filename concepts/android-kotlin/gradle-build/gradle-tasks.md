---
domain: android-kotlin
subdomain: gradle-build
concept: gradle-tasks
title: Understanding Gradle #04 – Tasks
sources:
  - title: "Understanding Gradle #04 – Tasks"
    url: "https://www.youtube.com/watch?v=9tY4MFEgmgM"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-08-23T10:29:46+00:00"
---

# Understanding Gradle #04 – Tasks

This video introduces the Gradle task concept, explaining that tasks are the fundamental building blocks of any Gradle build. It walks through the tasks available in a plain/empty project, then shows how applying the Base plugin and Java Library plugin adds more tasks. A key distinction is made between lifecycle tasks (like 'build' or 'clean') that orchestrate the build and actionable tasks (like 'compile' or 'test') that actually perform work (source: Understanding Gradle #04 – Tasks).

The video emphasizes that Gradle tasks are incremental: Gradle can reuse results from a previous build run if task inputs and outputs are unchanged, and can even pull results from a build cache for even faster builds (source: Understanding Gradle #04 – Tasks). Dependencies between tasks are also covered, since tasks form a graph that determines execution order. Examples from the Application plugin illustrate how task dependencies and lifecycle tasks work in practice, and the summary ties these concepts together (source: Understanding Gradle #04 – Tasks).

- Tasks are the core unit of work in Gradle, and different plugins contribute different sets of tasks.
- Lifecycle tasks orchestrate builds, while actionable tasks do the actual work.
- Gradle supports incremental builds and build cache to avoid redundant work and speed up builds.
- Task dependencies define the execution order and form a directed graph.