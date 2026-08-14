---
domain: system-design
subdomain: java-runtime-optimization
concept: jlink-minimal-jre
title: Using jlink to Cross-Compile Minimal JREs
sources:
  - title: "Using jlink to cross-compile minimal JREs"
    url: "https://jakewharton.com/using-jlink-to-cross-compile-minimal-jres/"
    author: "Jake Wharton"
---

# Using jlink to Cross-Compile Minimal JREs

jlink is a JDK tool that creates bespoke, minimal JREs containing only the Java modules required by an application. The article demonstrates this with a simple 'Hello, world!' program, showing how jdeps can list the necessary modules (in this case, just java.base) and how jlink can produce a runtime that is 28MiB versus 136MiB for the full JRE—an 80% size reduction (Jake Wharton, https://jakewharton.com/using-jlink-to-cross-compile-minimal-jres/).

The same jlink command can target a different platform by pointing --module-path at the jmods directory of a JDK for the desired OS and architecture. This allows cross-compiling minimal JREs from a single host machine, as demonstrated by building a Linux x64 runtime on an M1 Mac and successfully running it on a Linux server. This technique is useful for multi-architecture Docker images, desktop applications, and resource-constrained devices where a full JDK is impractical.

- Use jdeps to determine required modules for an application, then jlink to create a minimal JRE.
- jlink produces an 80% smaller runtime compared to the standard JRE for simple applications.
- Cross-compile JREs for other platforms by using --module-path to point to the target platform's JDK jmods.
- The approach is beneficial for Docker multi-arch images, desktop clients, and devices with limited storage.