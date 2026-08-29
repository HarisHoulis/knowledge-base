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

The video explains the basics of tasks in Gradle, comparing tasks found in a plain/empty project, a project with the Base plugin, and a project with the Java Library plugin. It highlights the difference between lifecycle tasks and actionable tasks, and how plugins add tasks to a build.

- Gradle projects have different tasks depending on the plugins applied (e.g., Base, Java Library, Application).
- Tasks are incremental and can reuse results from previous builds (UP-TO-DATE) or from the build cache (FROM-CACHE).
- Dependencies exist between tasks, and the Application plugin adds additional tasks like run.
- The video is part of a series covering Gradle fundamentals, with further episodes on lifecycle tasks and configuring inputs/outputs.