---
domain: android-kotlin
subdomain: gradle-build-tools
concept: lifecycle-tasks
title: Understanding Gradle #05 – Lifecycle Tasks
sources:
  - title: "Understanding Gradle #05 – Lifecycle Tasks"
    url: "https://www.youtube.com/watch?v=sOo0p4Gpjcc"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-08-30T13:26:18+00:00"
---

# Understanding Gradle #05 – Lifecycle Tasks

Lifecycle tasks in Gradle are tasks without actions that serve as organizational entry points, grouping related tasks to make builds more accessible and easier to run from the command line. The video demonstrates using `./gradlew tasks` to discover available tasks and how to narrow the listing to a custom group by configuring the task's group property, which helps users understand what a build offers without reading scripts (source: Understanding Gradle #05 – Lifecycle Tasks).

- Lifecycle tasks are empty tasks that depend on other tasks, providing convenient grouping and naming for build actions.
- Run `./gradlew tasks` to see all tasks; limit output to a specific group (e.g., `./gradlew tasks --group verification`) for clarity.
- Custom lifecycle tasks like `qualityCheck` can combine multiple existing tasks (e.g., lint, test) into a single target, useful for CI pipelines.
- Root build lifecycle tasks can trigger tasks across all subprojects, enabling whole-project checks with one command.
- Task names can be invoked by simple name from subprojects or by fully qualified path (`:subproject:tasks`) for fine-grained execution control.