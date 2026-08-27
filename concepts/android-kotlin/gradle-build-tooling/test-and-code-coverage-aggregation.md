---
domain: android-kotlin
subdomain: gradle-build-tooling
concept: test-and-code-coverage-aggregation
title: Understanding Gradle #21 – Test and Code Coverage Reporting
sources:
  - title: "Understanding Gradle #21 – Test and Code Coverage Reporting"
    url: "https://www.youtube.com/watch?v=uZvzWlP9BYE"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2022-08-22T14:47:38+00:00"
---

# Understanding Gradle #21 – Test and Code Coverage Reporting

This video explains how to enable code coverage (JaCoCo) reports in Gradle and how to aggregate test and coverage reports for a multi-project code base. By default, each component (subproject) produces its own test report and JaCoCo coverage report when the relevant plugins are applied. The video demonstrates that these per-component reports are useful for individual modules but do not give an overview of the entire code base (source).

- Each component generates its own test and JaCoCo coverage report by default.
- Apply the `test-report-aggregation` and `jacoco-report-aggregation` plugins to create unified reports across the whole code base.
- Wire the aggregation tasks into lifecycle tasks like `check` for one-command report generation.
- Report aggregation uses variant-aware dependency management to automatically include reports from all relevant subprojects.
- Use the `outgoingVariants` help task to inspect and understand which variants participate in aggregation.