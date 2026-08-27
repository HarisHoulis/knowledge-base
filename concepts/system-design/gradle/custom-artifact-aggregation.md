---
domain: system-design
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

On the producer side, each project must expose a consumable configuration as a variant, otherwise resolution fails. The video illustrates adding such a configuration in a shared parent/plugin, setting the same attribute, and attaching the project's source directories. Once both sides are configured, Gradle can resolve the custom configuration and the aggregation task (e.g., fullJavadoc) receives all sources. This demonstrates Gradle's variant-aware dependency resolution as a key mechanism for custom artifact aggregation.

- Understand resolvable vs consumable configurations.
- Use attributes to differentiate configurations.
- Extend existing configurations to reuse the dependency set.
- Expose project artifacts as consumable configurations (variants) for cross-project aggregation.
- Aggregating custom artifacts requires both consumer and producer configurations.