---
domain: android-kotlin
subdomain: gradle
concept: lifecycle-tasks
title: Understanding Gradle #05 – Lifecycle Tasks
sources:
  - title: "Understanding Gradle #05 – Lifecycle Tasks"
    url: "https://www.youtube.com/watch?v=sOo0p4Gpjcc"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-08-30"
---

# Understanding Gradle #05 – Lifecycle Tasks

Lifecycle tasks in Gradle are special tasks that contain no action themselves but serve as grouping nodes for other tasks, making builds more accessible and easier to run. The video explains how to view available tasks using `gradle tasks`, filter tasks by group, and create custom lifecycle tasks such as `qualityCheck` by wiring dependencies with `dependsOn` (onepiece.Software, 2021). This approach helps structure build logic and provides simple entry points for common operations.

The tutorial also demonstrates lifecycle tasks in the root project, especially useful for CI pipelines because they can aggregate tasks from multiple subprojects or even multiple builds. By placing lifecycle tasks centrally, you can run a full build with a single command, such as `build` or a custom `ci` task. Additionally, the video covers command-line invocation nuances, like using fully qualified task paths (`:subproject:task`) to target specific tasks, and emphasizes that keeping lifecycle tasks in the root build simplifies orchestration (onepiece.Software, 2021).

- Lifecycle tasks are task groups with no actions that depend on other tasks, enabling cleaner build entry points.
- Run `gradle tasks` to discover tasks and use groups to organize your custom lifecycle tasks.
- Custom lifecycle tasks like `qualityCheck` can be created with `dependsOn` to bundle multiple checks.
- Place lifecycle tasks in the root project for CI to trigger multi-subproject or multi-build workflows with one command.
- Use fully qualified task paths on the command line to execute tasks in specific subprojects when needed.