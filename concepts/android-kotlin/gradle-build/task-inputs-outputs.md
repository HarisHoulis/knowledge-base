---
domain: android-kotlin
subdomain: gradle-build
concept: task-inputs-outputs
title: Understanding Gradle #06 – Configuring Task Inputs and Outputs
sources:
  - title: "Understanding Gradle #06 – Configuring Task Inputs and Outputs"
    url: "https://www.youtube.com/watch?v=Pj9hSRauiQM"
    author: "Jendrik Johannes"
    date: "2021-09-06T12:27:35+00:00"
---

# Understanding Gradle #06 – Configuring Task Inputs and Outputs

This video from onepiece.Software explains Gradle task configuration, focusing on the critical concept of task inputs and outputs. Actionable tasks are defined by their inputs and outputs, which enable Gradle's incremental build feature by determining whether a task is up-to-date or needs to be re-run. The video demonstrates why declaring these correctly is essential for build performance and correctness.

Using a hands-on example, Jendrik Johannes registers a custom task to package an application, then progressively configures its inputs and outputs for the start script, compiled classes, and dependencies. Each step is followed by running an incremental build to show how Gradle skips unnecessary work when inputs and outputs are correctly declared. The task is then wired into the build lifecycle to ensure it runs at the appropriate phase.

The summary ties together how understanding inputs and outputs is fundamental for authoring robust Gradle tasks, and points to further resources on task configuration and creating archives. The example code is available on GitHub, and related videos cover plugins, tasks, lifecycle, and dependency declaration.

- Task inputs and outputs are the basis for Gradle's incremental build support.
- Configuring a task from scratch involves registering it and explicitly declaring inputs and outputs.
- Running incremental builds after each configuration step demonstrates how Gradle uses inputs/outputs to skip up-to-date tasks.
- Wiring custom tasks into the build lifecycle ensures they execute at the right point in the build.
- Refer to the official Gradle docs for more on task inputs/outputs and archive creation.