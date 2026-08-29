---
domain: android-kotlin
subdomain: gradle-build-tools
concept: test-coverage-aggregation
title: Understanding Gradle #21 – Test and Code Coverage Reporting
sources:
  - title: "Understanding Gradle #21 – Test and Code Coverage Reporting"
    url: "https://www.youtube.com/watch?v=uZvzWlP9BYE"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2022-08-22T14:47:38+00:00"
---

# Understanding Gradle #21 – Test and Code Coverage Reporting

Gradle automatically generates test reports for each subproject after running tests, but these reports are isolated per component. To get a unified view of test results and code coverage across a multi-project build, Gradle provides dedicated aggregation plugins: `test-report-aggregation` and `jacoco-report-aggregation`. These plugins collect results from all subprojects and produce a single aggregated report, which is especially useful for understanding the health of the entire codebase.

The aggregation mechanism leverages Gradle's variant-aware dependency management. When applied, the aggregation plugins create configurations (such as `testReportAggregation` and `jacocoAggregation`) that are resolved across all projects. Each subproject exposes its test results or coverage data as outgoing variants, and the aggregation project consumes these variants to generate the combined report. The `outgoingVariants` help task can be used to inspect what variants each project exposes, helping developers debug and understand the dependency resolution.

To integrate aggregated reporting into the build lifecycle, the aggregation tasks can be wired into a lifecycle task like `check`. The plugins also support aggregating reports for multiple source sets, not just the standard `test` source set, providing flexibility for projects with custom test setups. This approach simplifies reporting and makes it easier to track quality metrics across the entire build.

- Test and JaCoCo reports are generated per subproject by default; use aggregation plugins to combine them into a single report.
- Apply `test-report-aggregation` and `jacoco-report-aggregation` plugins in an aggregation project to collect results from all subprojects.
- Aggregation relies on variant-aware dependency management and configurations like `testReportAggregation` and `jacocoAggregation`.
- Use the `outgoingVariants` help task to debug and understand how variants are exposed for aggregation.
- Wire aggregation tasks into lifecycle tasks like `check` to produce reports automatically.