---
domain: android-kotlin
subdomain: gradle
concept: custom-artifact-aggregation
title: Understanding Gradle #13 – Aggregating Custom Artifacts
sources:
  - title: "Understanding Gradle #13 – Aggregating Custom Artifacts"
    url: "https://www.youtube.com/watch?v=2gPJD0mAres"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-12-06T09:38:42+00:00"
---

# Understanding Gradle #13 – Aggregating Custom Artifacts

The video explains how to aggregate custom artifacts in Gradle, such as sources or Javadoc, for distribution. It demonstrates creating a custom Javadoc task that requires both compiled classes and source code from all subprojects. The runtime classpath resolvable configuration provides the compiled dependencies out of the box, but a custom resolvable configuration is needed for sources. This new configuration extends the implementation configuration to reuse declared dependencies and sets a custom usage attribute to distinguish it from compile and runtime classpaths (Jendrik, 2021).

When using the custom sources configuration, Gradle fails because the source code is not exposed as a consumable variant in other projects. To fix this, each project must define a consumable configuration that provides source code, with the same usage attribute. This illustrates Gradle's variant model, where consumable configurations define what artifacts are available to consumers, and resolvable configurations are used to select and resolve them (Jendrik, 2021).

- Aggregating custom artifacts requires understanding Gradle's configuration and variant model.
- Resolvable configurations like runtimeClasspath provide external dependencies, but custom artifacts need new configurations.
- A resolvable configuration can extend implementation to reuse existing dependency declarations.
- Custom usage attributes distinguish different variants, e.g., java-sources vs. java-api.
- Each project must expose a consumable configuration (variant) so other projects can resolve its source code.