---
domain: engineering-culture
subdomain: jvm-tooling
concept: jlink-cross-compile
title: Using jlink to cross-compile minimal JREs
sources:
  - title: "Using jlink to cross-compile minimal JREs"
    url: "https://jakewharton.com/using-jlink-to-cross-compile-minimal-jres/"
---

# Using jlink to cross-compile minimal JREs

The article demonstrates how to use jlink, a JDK tool, to create minimal JREs for Java applications. By running jdeps on a simple 'Hello, world!' program, it identifies the required Java modules (java.base) and then uses jlink to produce a custom runtime. This reduces the JRE size from 136MiB to just 28MiB on the host platform [source]. 

Beyond the host platform, jlink can cross-compile JREs for different architectures by using the --module-path flag to point at a JDK of the target platform. The article shows creating a Linux x64 JRE from a macOS ARM JDK, resulting in a 36MiB runtime that successfully runs on a Linux server. This technique is valuable for multi-architecture Docker containers, desktop apps, and resource-constrained devices, where smaller runtimes are critical.

- Use jdeps to list required Java modules for an application.
- jlink creates a minimal runtime by including only needed modules.
- jlink's --module-path can reference JDKs for other platforms, enabling cross-compilation of JREs.
- Minimal JREs significantly reduce binary size (e.g., 136MB to 28MB).
- Cross-compiled JREs solve multi-architecture deployment needs.