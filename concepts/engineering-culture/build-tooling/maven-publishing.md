---
domain: engineering-culture
subdomain: build-tooling
concept: maven-publishing
title: Understanding Gradle #12 – Publishing Libraries
sources:
  - title: "Understanding Gradle #12 – Publishing Libraries"
    url: "https://www.youtube.com/watch?v=8z5KFCLZDd0"
    author: "Jendrik Johannes"
    date: "2021-11-22T13:42:02+00:00"
---

# Understanding Gradle #12 – Publishing Libraries

In this video, Jendrik Johannes explains the fundamentals of publishing libraries with Gradle. He starts by describing the Maven repository structure, which organizes artifacts by group, artifact, and version coordinates, and shows how Gradle creates and uploads these artifacts. The video emphasizes that a Maven repository is not just a folder but a standardized layout that clients can consume.

A key concept introduced is Gradle Module Metadata, a JSON-based file that accompanies the POM and carries richer dependency information, including variant-aware details and capabilities. This metadata allows Gradle to resolve dependencies more accurately than POM alone. The video demonstrates how to configure publishing for library subprojects using Gradle's DSL, focusing on the concepts of components and publications.

It then covers declaring repositories to publish to, whether remote or local, and running the associated publish tasks. Finally, it shows how to consume the published versions in another project as dependencies. The talk concludes with a summary and pointers to related videos and documentation.

- Maven repository layout uses group, artifact, and version coordinates.
- Gradle Module Metadata provides richer dependency and variant information than POM.
- Publishing is configured via the `publishing` block with `publications` and `repositories`.
- The `publish` tasks upload artifacts to the configured repositories.
- Published libraries can be consumed as regular dependencies from another project.