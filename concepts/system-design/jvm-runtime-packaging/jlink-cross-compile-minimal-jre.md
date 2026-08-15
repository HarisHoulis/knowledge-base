---
domain: system-design
subdomain: jvm-runtime-packaging
concept: jlink-cross-compile-minimal-jre
title: Using jlink to Cross-Compile Minimal JREs
sources:
  - title: "Using jlink to cross-compile minimal JREs"
    url: "https://jakewharton.com/using-jlink-to-cross-compile-minimal-jres/"
    author: "Jake Wharton"
---

# Using jlink to Cross-Compile Minimal JREs

The article explains how to use `jlink`, a JDK tool, to create bespoke minimal JREs for an application. Starting with a simple 'Hello, world' program, the author demonstrates that while a full JDK is 329MB and a pre-built JRE is 136MB, using `jdeps` to list required modules and `jlink` with options like `--compress 2`, `--strip-debug`, `--no-header-files`, and `--no-man-pages` can produce a 28MB JRE containing only the `java.base` module, an 80% reduction in size.

- `jlink` creates minimal JREs by including only the modules your application requires, as identified by `jdeps`.
- Cross-compiling is possible by pointing `jlink` at a JDK for a different platform via `--module-path` and specifying the target's jmods directory.
- A minimal JRE for a simple program can be as small as 28MiB on ARM Mac and 36MiB on Linux x64, compared to 136MiB for a full JRE.
- This approach is valuable for multi-architecture Docker containers, desktop apps, and resource-constrained devices.