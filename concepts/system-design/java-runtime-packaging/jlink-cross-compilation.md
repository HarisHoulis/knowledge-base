---
domain: system-design
subdomain: java-runtime-packaging
concept: jlink-cross-compilation
title: Using jlink to Cross-Compile Minimal JREs
sources:
  - title: "Using jlink to cross-compile minimal JREs"
    url: "https://jakewharton.com/using-jlink-to-cross-compile-minimal-jres/"
---

# Using jlink to Cross-Compile Minimal JREs

The article demonstrates how to use jlink, a JDK tool, to create minimal JREs for Java applications. Starting with a simple Hello, world program, the author shows that while a full JDK is 329MB and a full JRE is 136MB, jlink can produce a 28MB runtime containing only the java.base module. The author then addresses cross-platform deployment: the resulting JRE is host-specific, so to ship to a different architecture, you can use jlink from your host with a --module-path pointing to the target platform's JDK jmods, effectively cross-compiling. This approach works for Linux x64, enabling a 36MB runtime that runs on the server. The technique is useful for Docker images, desktop apps, and constrained devices.

- jlink creates minimal JREs by including only required modules.
- jdeps identifies required modules from compiled classes.
- The minimal JRE is platform-specific; to cross-compile, use jlink with --module-path to a JDK for the target platform.
- This yields huge size savings (e.g., 136MB JRE reduced to 28MB for hello world).
- Enables multi-architecture deployment for containers, desktop, and IoT.