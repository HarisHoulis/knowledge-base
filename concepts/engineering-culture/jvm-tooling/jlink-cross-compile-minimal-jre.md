---
domain: engineering-culture
subdomain: jvm-tooling
concept: jlink-cross-compile-minimal-jre
title: Using jlink to Cross-Compile Minimal JREs
sources:
  - title: "Using jlink to cross-compile minimal JREs"
    url: "https://jakewharton.com/using-jlink-to-cross-compile-minimal-jres/"
    author: "Jake Wharton"
---

# Using jlink to Cross-Compile Minimal JREs

The article demonstrates how to use the JDK's jlink tool to create minimal JREs tailored to a specific application. Starting with a simple "Hello, world!" program, it shows that a full JDK occupies 329 MB and the corresponding full JRE 136 MB. Using jdeps to analyze the compiled class, the program only requires the java.base module. Running jlink with --add-modules java.base produces a minimal JRE of just 28 MB on macOS ARM, an 80% reduction from the full JRE, while still running the application correctly.

However, attempting to run this JRE on a Linux x64 server fails with "Exec format error" because JREs contain platform-specific binaries. The solution is to cross-compile by downloading the target platform's JDK (Linux x64, 338 MB) and pointing the host jlink at its jmods directory via --module-path. This produces a Linux x64 minimal JRE of 36 MB that successfully runs on the server. The technique enables small, platform-specific runtimes for multi-architecture Docker containers, desktop clients, and resource-constrained devices, and the article encourages exploring jdeps and jlink options for further size optimization.

- jlink creates custom minimal JREs that include only the Java modules required by the application.
- jdeps identifies the module dependencies from compiled .class files, enabling precise module selection.
- JREs are platform-specific; cross-compilation requires using the target platform's JDK jmods via --module-path.
- The minimal JRE can be dramatically smaller (e.g., 28 MB vs 136 MB for a full JRE), easing distribution.
- This approach is valuable for multi-architecture Docker builds, desktop apps, and computing environments with tight storage constraints.