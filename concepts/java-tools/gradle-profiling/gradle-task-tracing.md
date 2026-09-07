---
domain: java-tools
subdomain: gradle-profiling
concept: gradle-task-tracing
title: Tracing Gradle task execution
sources:
  - title: "Tracing Gradle task execution"
    url: "https://jakewharton.com/tracing-gradle-task-execution/"
---

# Tracing Gradle task execution

Gradle's built-in `--profile` and `--scan` provide task execution timings, but `--profile` gives only a rough picture while `--scan` sends details to remote servers. The author seeks a middle ground: granularity without offloading data externally. They explore the Gradle profiler's integrations, which are designed for deterministic build performance measurements but aren't ideal for direct CI use.

For CI builds, Java Flight Recorder can be attached to individual Gradle builds using `jcmd` and JVM flags, and a plugin can automate recording. The resulting flamegraph shows where time is spent globally, but stacks are not tied to specific tasks and daemonized tasks like the Kotlin compiler are missed. The author notes this output's utility is limited unless paired with a strong `jcmd` integration.

An alternative is the Chrome trace output from the Gradle profiler, which requires building its `chrome-trace.jar` and applying a plugin via an init script. This produces a visual timeline of concurrent task execution, including CPU load, heap size, and GC events—context absent from `--profile`—but offers almost no per-task or worker-level visibility. The author integrated this into SDK Search's CI and finds it useful, while wishing for future additions like worker-level detail and merging with JFR data.

- Gradle's --profile is too coarse, while --scan requires sending build details remotely.
- Java Flight Recorder can profile a single build but lacks task correlation and misses daemonized tasks.
- The Gradle profiler's chrome-trace.jar enables Chrome trace generation via an init script, giving a timeline with CPU and heap metrics.
- Neither tracing approach is perfect; Chrome traces are suitable for CI, while JFR is better for deeper task analysis.
- Desired future improvements include worker visibility in Chrome traces and merging JFR data with Chrome trace output.