---
domain: android-kotlin
subdomain: jvm-tooling
concept: jlink-cross-compile-minimal-jres
title: Using jlink to Cross-Compile Minimal JREs
sources:
  - title: "Using jlink to cross-compile minimal JREs"
    url: "https://jakewharton.com/using-jlink-to-cross-compile-minimal-jres/"
---

# Using jlink to Cross-Compile Minimal JREs

The article demonstrates how to use the JDK's `jlink` tool to create minimal, bespoke JREs tailored to a specific application. Starting with a simple "Hello, world!" program, the author shows that while a full JDK (329MiB) or standard JRE (136MiB) is large, `jdeps` can identify the required Java modules—in this case, only `java.base`. Running `jlink` with options like `--compress 2`, `--strip-debug`, and `--add-modules java.base` produces a JRE of just 28MiB for the host platform (M1 Mac), an 80% size reduction from the full JRE.

- `jdeps --print-module-deps` lists the minimal set of Java modules required by an application.
- `jlink` creates a custom JRE containing only those modules, drastically reducing binary size.
- By supplying `--module-path` pointing to a JDK for another platform (e.g., Linux x64), `jlink` can cross-compile minimal JREs for multiple architectures from a single host.
- This approach is useful for multi-architecture Docker containers, desktop apps like JetBrains Compose UI, and devices with limited storage.
- The resulting JRE is still platform-specific, so a separate image must be produced for each target OS/architecture.