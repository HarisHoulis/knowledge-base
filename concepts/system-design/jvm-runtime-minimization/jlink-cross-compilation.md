---
domain: system-design
subdomain: jvm-runtime-minimization
concept: jlink-cross-compilation
title: Using jlink to Cross-Compile Minimal JREs
sources:
  - title: "Using jlink to cross-compile minimal JREs"
    url: "https://jakewharton.com/using-jlink-to-cross-compile-minimal-jres/"
    author: "Jake Wharton"
---

# Using jlink to Cross-Compile Minimal JREs

The technique is valuable for scenarios like multi-architecture Docker images, desktop applications with embedded runtimes, and constrained devices. The article encourages exploring `jdeps` and `jlink` options to keep runtimes small and minimize distribution overhead.

- `jlink` creates minimal JREs containing only the Java modules required by the application.
- `jdeps --print-module-deps` determines the exact module dependencies of compiled classes.
- Cross-compiling minimal JREs is possible by pointing `jlink` at a target platform's JDK `jmods` via `--module-path`.
- Size savings are substantial: 28MiB vs 136MiB for a full JRE in the Hello World example.
- Useful for Docker multi-arch builds, desktop clients, and limited-resource devices.