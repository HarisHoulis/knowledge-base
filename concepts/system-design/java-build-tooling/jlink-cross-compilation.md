---
domain: system-design
subdomain: java-build-tooling
concept: jlink-cross-compilation
title: Using jlink to Cross-Compile Minimal JREs
sources:
  - title: "Using jlink to cross-compile minimal JREs"
    url: "https://jakewharton.com/using-jlink-to-cross-compile-minimal-jres/"
---

# Using jlink to Cross-Compile Minimal JREs

The article demonstrates how to use the JDK's jlink tool to create minimal, application-specific JREs. Starting with a simple Hello World program, the author shows that a full JDK (329M) or even a full JRE (136M) is overkill. By running jdeps on the compiled class, only the java.base module is required, and jlink with options --compress 2, --strip-debug, --no-header-files, --no-man-pages produces a 28MiB JRE on an M1 Mac.

- jlink creates custom minimal JREs by including only the Java modules your application needs.
- jdeps identifies required modules; for Hello World, only java.base is needed.
- JREs are platform-specific, so a JRE built on macOS won't run on Linux.
- jlink can cross-compile for other platforms by using --module-path pointing to that platform's JDK jmods.
- The cross-compiled Linux x64 JRE was 36M and successfully ran on a Linux server, enabling multi-architecture distribution.