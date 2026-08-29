---
domain: android-kotlin
subdomain: gradle-build
concept: lifecycle-tasks
title: Understanding Gradle #05 – Lifecycle Tasks
sources:
  - title: "Understanding Gradle #05 – Lifecycle Tasks"
    url: "https://www.youtube.com/watch?v=sOo0p4Gpjcc"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-08-30T13:26:18+00:00"
---

# Understanding Gradle #05 – Lifecycle Tasks

Lifecycle tasks are tasks without actions that serve as entry points to group and execute other tasks. The video explains how to make builds accessible by using the built-in `tasks` task, which lists available tasks, and how to restrict the list to a specific group via the `group` property. It also shows how to attach existing lifecycle tasks like `check` to a custom group and why custom lifecycle tasks, such as `qualityCheck`, are useful for combining multiple verification tasks into a single convenient command.

Beyond single-project builds, the video discusses lifecycle tasks in the root build of multi-project builds, which is particularly helpful for CI pipelines. It covers how lifecycle tasks can span multiple subprojects and even multiple builds, allowing a single task name to trigger a coordinated set of operations. Finally, it gives notes on invoking tasks from the command line, emphasizing the use of fully qualified task paths (e.g., `:project:task`) to avoid ambiguities in multi-project setups.

- Lifecycle tasks are task containers that group other tasks; they have no action of their own.
- Run `gradlew tasks` to see available tasks; organize them with the `group` and `description` properties.
- Create custom lifecycle tasks (e.g., `qualityCheck`) to trigger multiple verification tasks with one command.
- For multi-project builds, define lifecycle tasks in the root build to orchestrate tasks across subprojects and builds.
- From the command line, use fully qualified task paths (e.g., `:project:task`) to avoid ambiguity.