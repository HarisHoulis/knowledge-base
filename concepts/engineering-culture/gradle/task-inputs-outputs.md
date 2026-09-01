---
domain: engineering-culture
subdomain: gradle
concept: task-inputs-outputs
title: Understanding Gradle #06 – Configuring Task Inputs and Outputs
sources:
  - title: "Understanding Gradle #06 – Configuring Task Inputs and Outputs"
    url: "https://www.youtube.com/watch?v=Pj9hSRauiQM"
    author: "Jendrik Johannes"
    date: "2021-09-06T12:27:35+00:00"
---

# Understanding Gradle #06 – Configuring Task Inputs and Outputs

This video explains the concept of task inputs and outputs in Gradle and why they are critical for incremental builds. Actionable tasks need explicit declarations of what they consume (inputs) and what they produce (outputs), enabling Gradle to skip tasks when nothing relevant has changed, thereby speeding up builds [0:00, 1:00]. The presenter demonstrates this by configuring a custom task from scratch, starting with registering it [1:43, 2:19]. He then shows how to set inputs and outputs for packaging a start script, the application's classes, and its dependencies, running incremental builds after each step to observe when the task is considered up-to-date [2:52, 3:43, 4:01, 4:33, 4:54, 5:34]. Finally, he illustrates wiring the task into the build lifecycle so it executes at the appropriate phase [5:49]. The key takeaway is that properly declaring inputs and outputs makes builds more efficient and reliable, a fundamental practice for any Gradle-based project.

- Actionable tasks must declare inputs and outputs to support incremental builds.
- Inputs and outputs allow Gradle to skip tasks when nothing has changed, reducing build time.
- You can configure a task to package different artifacts (start scripts, classes, dependencies) by specifying the corresponding inputs.
- Wiring a custom task into the build lifecycle ensures it runs at the correct stage.
- Running incremental builds verifies that the task is correctly configured and up-to-date detection works.