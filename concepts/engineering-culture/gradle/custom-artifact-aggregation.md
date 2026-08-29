---
domain: engineering-culture
subdomain: gradle
concept: custom-artifact-aggregation
title: Aggregating Custom Artifacts in Gradle
sources:
  - title: "Understanding Gradle #13 – Aggregating Custom Artifacts"
    url: "https://www.youtube.com/watch?v=2gPJD0mAres"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-12-06T09:38:42+00:00"
---

# Aggregating Custom Artifacts in Gradle

In this video, Jendrik Johannes explains how to aggregate custom artifacts in Gradle, such as Javadoc or code coverage reports, which are not handled by standard plugins. He demonstrates that while the application plugin packages runtime dependencies out of the box, custom aggregation requires a deeper understanding of Gradle's dependency management and configurations. The example builds an aggregated Javadoc by creating a new resolvable configuration for source code, extending it from the 'implementation' configuration to include both api and implementation dependencies, and setting a custom usage attribute to distinguish it from other classpaths. However, resolving this configuration fails because other projects do not expose a consumable source-code variant. To solve this, a consumable configuration must be added to each project (ideally in a shared plugin) to publish source code as a variant. This illustrates Gradle's variant model and the distinction between resolvable and consumable configurations, which is essential for custom artifact aggregation in multi-project builds.

- Custom artifacts require explicit configuration; standard plugins only cover typical cases like application distributions.
- Use a resolvable configuration to gather dependencies for a custom task, extending existing configurations like 'implementation' to reuse declared dependencies.
- Set attributes (e.g., usage = 'java-sources') on configurations to differentiate them from runtime or compile classpaths.
- To share custom artifacts between projects, define a consumable configuration (variant) that publishes the artifact, enabling cross-project resolution.