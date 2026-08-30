---
domain: android-kotlin
subdomain: gradle-build
concept: custom-artifact-aggregation
title: Understanding Gradle #13 – Aggregating Custom Artifacts
sources:
  - title: "Understanding Gradle #13 – Aggregating Custom Artifacts"
    url: "https://www.youtube.com/watch?v=2gPJD0mAres"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2021-12-06T09:38:42+00:00"
---

# Understanding Gradle #13 – Aggregating Custom Artifacts

In this video, Jendrik Johannes explains how to aggregate custom artifacts in Gradle, such as combining Javadoc from multiple subprojects into a single output. The standard Java and Application plugins handle common distribution cases, but custom aggregation requires a deeper understanding of Gradle's dependency management and configuration model.

The example demonstrates creating a new resolvable configuration to collect source code from all dependencies by extending the existing implementation configuration. A custom usage attribute is set to distinguish this sources configuration from compile and runtime classpaths. This allows Gradle to resolve the right variants from other projects.

However, simply creating a resolvable configuration is insufficient; the subprojects themselves must expose their source code as a consumable configuration (a variant). The video shows how to add this consumable configuration in a shared plugin, attaching the appropriate usage attribute so that the parent project can consume the sources.

The key takeaway is that Gradle variants and configurations are central to custom artifact aggregation. Understanding how consumable and resolvable configurations interact enables developers to tailor distribution and documentation outputs for multi-project builds.

- Standard plugins provide basic packaging, but custom artifact aggregation requires custom configurations.
- Create a resolvable configuration and extend existing dependency declarations to collect sources or other artifacts.
- Use attributes like usage to distinguish configurations and select the appropriate variant.
- Subprojects must expose custom artifacts via consumable configurations for downstream aggregation.
- Gradle's variant model is key to making custom artifacts visible to consumers.