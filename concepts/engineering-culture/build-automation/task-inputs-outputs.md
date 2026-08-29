---
domain: engineering-culture
subdomain: build-automation
concept: task-inputs-outputs
title: Understanding Gradle #06 – Configuring Task Inputs and Outputs
sources:
  - title: "Understanding Gradle #06 – Configuring Task Inputs and Outputs"
    url: "https://www.youtube.com/watch?v=Pj9hSRauiQM"
    author: "Jendrik Johannes"
    date: "2021-09-06T12:27:35+00:00"
---

# Understanding Gradle #06 – Configuring Task Inputs and Outputs

In Gradle, every actionable task must declare its inputs and outputs. These declarations are essential for Gradle's incremental build support: if the inputs and outputs are unchanged since the last run, Gradle can skip the task entirely, saving time and resources. Without proper input/output configuration, Gradle cannot determine whether a task is up-to-date, forcing it to rerun unnecessarily.

The video demonstrates how to configure a custom task from scratch for packaging an application. The instructor registers a task and then explicitly sets its inputs (the start script, compiled classes, and dependency files) and its output (the resulting archive). By doing so, running the build again correctly recognizes the task as up-to-date when nothing has changed, showcasing the practical benefits of incremental builds.

Finally, the tutorial explains how to wire the custom task into the build lifecycle, ensuring it executes at the appropriate phase. The core takeaway is that correctly specifying task inputs and outputs is a fundamental practice for efficient Gradle builds, as it enables caching and avoids redundant work.

- Task inputs and outputs are mandatory declarations for actionable tasks to enable Gradle's incremental build feature.
- Configuring inputs/outputs allows Gradle to skip tasks that are already up-to-date, reducing build times.
- The video shows a practical example of packaging an app by defining inputs like start scripts, classes, and dependencies, and the output archive.
- Wiring custom tasks into the build lifecycle ensures they run at the right time, complementing the input/output setup.