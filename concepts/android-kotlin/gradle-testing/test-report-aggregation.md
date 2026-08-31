---
domain: android-kotlin
subdomain: gradle-testing
concept: test-report-aggregation
title: Understanding Gradle Test and Code Coverage Reporting
sources:
  - title: "Understanding Gradle #21 – Test and Code Coverage Reporting"
    url: "https://www.youtube.com/watch?v=uZvzWlP9BYE"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2022-08-22T14:47:38+00:00"
---

# Understanding Gradle Test and Code Coverage Reporting

This video from the 'Understanding Gradle' series explains how to activate and customize test and code coverage reports in Gradle. It starts by showing that each component (e.g., subproject) automatically produces test reports when its `test` task runs, while JaCoCo code coverage reports require explicit enablement through the `jacoco` plugin. The focus then shifts to generating reports for the complete code base in a multi-project build.

- Test tasks generate per-component test reports by default; JaCoCo reports require the `jacoco` plugin.
- Use `test-report-aggregation` and `jacoco-report-aggregation` plugins to produce combined reports across all projects.
- Report aggregation uses variant-aware dependency management to discover and combine individual component results.
- Aggregated report tasks can be wired into lifecycle tasks (e.g., `check`) for convenient access.
- The `outgoingVariants` help task helps understand how variants are shared between projects for aggregation.