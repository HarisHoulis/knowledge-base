---
domain: engineering-culture
subdomain: build-tooling
concept: maven-publishing
title: Understanding Gradle #12 – Publishing Libraries
sources:
  - title: "Understanding Gradle #12 – Publishing Libraries"
    url: "https://www.youtube.com/watch?v=8z5KFCLZDd0"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-11-22T13:42:02+00:00"
---

# Understanding Gradle #12 – Publishing Libraries

In this video, Jendrik Johannes explains what a Maven repository is and how to publish libraries or components to it using Gradle. He starts by breaking down the Maven repository structure, which organizes artifacts by group, artifact ID, and version. He also introduces Gradle Module Metadata, a feature that enhances dependency resolution by publishing additional information about variants and dependencies beyond what Maven POM files provide (Jendrik, 2021).

The core of the video demonstrates how to configure publishing for library subprojects using Gradle's `maven-publish` plugin. Johannes walks through the DSL concepts of 'components' and 'publications'—where a publication is tied to a software component (like `java` or `java-library`) and describes how that component should be exposed. He then shows how to configure repositories to publish to, run the generated `publish` tasks, and consume the published versions from another project. The example also covers using timestamped versions for snapshot-like publication (Jendrik, 2021).

A key takeaway is that Gradle's publishing setup is flexible and designed for multi-project builds, making it straightforward to share libraries both internally and publicly. The video points to further resources on customizing publishing, managing credentials, and understanding consumable configurations for variant-aware dependency resolution (Jendrik, 2021).

- Maven repositories store artifacts under group, artifact ID, and version coordinates.
- Gradle publishes Module Metadata alongside POM files for richer dependency resolution.
- Use the `maven-publish` plugin to define publications and repositories.
- Publications are linked to Gradle components, allowing variant-aware publishing.
- After running `publish`, the library can be consumed by other projects as a normal dependency.