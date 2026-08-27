---
domain: android-kotlin
subdomain: build-tools
concept: jlink-cross-compile
title: Using jlink to cross-compile minimal JREs
sources:
  - title: "Using jlink to cross-compile minimal JREs"
    url: "https://jakewharton.com/using-jlink-to-cross-compile-minimal-jres/"
---

# Using jlink to cross-compile minimal JREs

The article demonstrates using JDK's jlink tool to create minimal, platform-specific JREs. It starts with a simple Hello World program and shows how jdeps can determine required Java modules (java.base). Using jlink with options like --compress, --strip-debug, --no-header-files, and --no-man-pages reduces the JRE from 136MiB to 28MiB on an Apple Silicon Mac. The author then explains that a JRE built on macOS won't run on Linux due to platform-specific binaries. By downloading a Linux x64 JDK and using --module-path to point jlink at that JDK's jmods, you can cross-compile a minimal JRE for Linux from a Mac, resulting in a 36MiB runtime that runs successfully on a Linux server. This technique is useful for multi-architecture Docker containers, desktop clients, or constrained devices.

- jlink creates minimal JREs by including only required Java modules
- jdeps lists the modules an application depends on
- JREs are platform-specific; use --module-path to point to a target platform's JDK
- jlink flags like --compress, --strip-debug reduce size significantly (80% savings)
- This enables cross-compiling minimal JREs for different architectures from a single host