---
domain: android-kotlin
subdomain: gradle
concept: gradle-tasks
title: Understanding Gradle #04 – Tasks
sources:
  - title: "Understanding Gradle #04 – Tasks"
    url: "https://www.youtube.com/watch?v=9tY4MFEgmgM"
    author: "Jendrik Johannes"
    date: "2021-08-23"
---

# Understanding Gradle #04 – Tasks

Gradle tasks are the fundamental units of work in a build. A plain/empty project has only a minimal set of predefined tasks, but plugins like the Base plugin introduce lifecycle tasks such as `assemble` and `check`. The Java Library plugin further adds actionable tasks like `jar`, `test`, and `compileJava`. Lifecycle tasks are typically no-op tasks that orchestrate other tasks, while actionable tasks perform the actual work.

Gradle tasks are incremental: Gradle can reuse outputs from previous build runs (UP-TO-DATE) or from a shared build cache (FROM-CACHE), skipping unnecessary work. Tasks also have dependencies, forming a graph that determines execution order. For example, the `build` task depends on `check` and `assemble`, and the Application plugin adds tasks like `run` for application execution.

Understanding task types, lifecycle tasks, and dependencies is essential for configuring and debugging Gradle builds. The video demonstrates how plugins contribute different sets of tasks and how Gradle's incremental and caching features improve build efficiency.

- Tasks are the core units of Gradle builds; plugins contribute task types and instances.
- Lifecycle tasks (e.g., `build`, `check`) group actionable tasks and often have no work of their own.
- Gradle supports incremental builds and build cache to skip tasks that are already up-to-date or cached.
- Task dependencies define the execution order and overall build graph.
- Different plugins (Base, Java Library, Application) add specific tasks relevant to their purpose.