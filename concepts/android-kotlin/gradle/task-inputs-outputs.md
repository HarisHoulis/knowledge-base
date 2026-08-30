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

Gradle tasks that perform work are 'actionable' tasks, and they should declare explicit inputs and outputs. This is the foundation for Gradle's incremental build support: when inputs and outputs are declared, Gradle can check whether they have changed and skip the task if they haven't (Jendrik Johannes, 2021). The video walks through configuring a custom packaging task from scratch, first by registering the task and then by adding inputs and outputs to package the start script, the classes, and the dependencies.

Each configuration step is followed by an incremental build run, showing that the task is skipped when nothing has changed. The video also demonstrates how to wire the task into the build lifecycle so it runs automatically during the build. The key takeaway is that declaring inputs and outputs is not just a formality—it is essential for making builds fast and correct: without them, Gradle cannot determine whether a task is up-to-date.

- Actionable tasks require explicit inputs and outputs to support incremental builds.
- Use `inputs.file()`/`inputs.dir()` and `outputs.file()`/`outputs.dir()` to declare task inputs and outputs.
- Configure your task in a `tasks.register` block or via a custom task class.
- Run an incremental build after configuration to see the up-to-date behavior.
- Wire custom tasks into the build lifecycle (e.g., with `dependsOn`) to include them in the build process.