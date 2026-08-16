---
domain: system-design
subdomain: java-runtime-optimization
concept: jlink-cross-compile
title: Using jlink to cross-compile minimal JREs
sources:
  - title: "Using jlink to cross-compile minimal JREs"
    url: "https://jakewharton.com/using-jlink-to-cross-compile-minimal-jres/"
    author: "Jake Wharton"
---

# Using jlink to cross-compile minimal JREs

The article demonstrates how to use the JDK's `jlink` tool to create minimal JREs, reducing the runtime footprint for Java applications. With a simple "Hello, world!" program, the author uses `jdeps` to identify required modules (just `java.base`) and then `jlink` to build a custom JRE. The resulting JRE is 28MiB on an M1 Mac, compared to 136MiB for the full JRE, an 80% savings.

A key insight is that `jlink` can create JREs for different platforms by pointing `--module-path` to the JDK's `jmods` for the target OS/architecture. The author cross-compiles a Linux x64 JRE from a Mac M1 host by downloading the Linux JDK and using it as a module source. This generated JRE works on a server after transfer, confirming the cross-compilation approach.

The technique is useful for multi-architecture Docker containers, desktop clients, and constrained devices where full JDKs aren't feasible. The article encourages exploring `jdeps` and `jlink` options to keep runtimes minimal.

- `jlink` creates minimal JREs containing only the Java modules an application needs.
- `jdeps --print-module-deps` identifies module dependencies from compiled `.class` files.
- Cross-compilation is achieved by supplying the target platform's JDK `jmods` via `--module-path`.
- The minimal JRE for "Hello, world!" was 28MiB on Mac M1 and 36MiB on Linux x64, down from 136MiB full JRE.
- Useful for multi-architecture Docker images, desktop clients, and resource-constrained deployments.