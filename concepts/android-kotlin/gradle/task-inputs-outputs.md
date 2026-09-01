---
domain: android-kotlin
subdomain: gradle
concept: task-inputs-outputs
title: Understanding Gradle #06 – Configuring Task Inputs and Outputs
sources:
  - title: "Understanding Gradle #06 – Configuring Task Inputs and Outputs"
    url: "https://www.youtube.com/watch?v=Pj9hSRauiQM"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-09-06T12:27:35+00:00"
---

# Understanding Gradle #06 – Configuring Task Inputs and Outputs

The video explains how to configure a Gradle task from scratch, focusing on the concept of task inputs and outputs. Actionable tasks in Gradle must declare their inputs and outputs, which is essential for enabling incremental builds. When inputs and outputs are properly configured, Gradle can skip tasks that are already up-to-date, dramatically improving build performance.

The presenter walks through a practical example of packaging an application. He registers a custom task and then configures inputs and outputs step by step to package a start script, compiled classes, and dependencies. After each configuration, the incremental build is run to show how Gradle detects unchanged inputs and skips the task execution when nothing has changed.

Finally, the task is wired into the build lifecycle, making it part of the standard build process. The key takeaway is that declaring task inputs and outputs is not just a best practice, but a fundamental requirement for scalable, efficient Gradle builds. The video cites official Gradle documentation for further reading on task configuration and inputs/outputs.

- Actionable tasks must declare inputs and outputs for Gradle's incremental build to work.
- Configuring inputs and outputs allows Gradle to skip tasks when their inputs haven't changed.
- Packaging tasks can be broken down into start script, classes, and dependencies as separate inputs.
- Wiring custom tasks into the build lifecycle integrates them with standard build phases.
- Properly configured inputs/outputs are essential for fast, repeatable builds.