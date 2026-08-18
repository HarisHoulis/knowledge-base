---
domain: system-design
subdomain: jvm-runtime
concept: jlink-cross-compilation
title: Using jlink to Cross-Compile Minimal JREs
sources:
  - title: "Using jlink to cross-compile minimal JREs"
    url: "https://jakewharton.com/using-jlink-to-cross-compile-minimal-jres/"
---

# Using jlink to Cross-Compile Minimal JREs

The article demonstrates how to use `jlink` to create minimal, platform-specific JREs for Java applications. Starting with a simple "Hello, world!" program, the author shows that while a full JDK is 329MB and a standard JRE is 136MB, `jlink` can produce a runtime of only 28MB by including only the required Java modules. The `jdeps` tool identifies module dependencies (`java.base` in this example), which are then passed to `jlink` via `--add-modules`.

The key insight is that `jlink` can operate on JDKs for different platforms by using the `--module-path` flag to point to the target platform's JMOD files. This allows cross-compilation of minimal JREs on a developer's machine. For instance, the author builds a Linux x64 JRE from an M1 Mac, which works on a remote Linux server after transferring the tar archive. This approach is beneficial for multi-architecture Docker containers, desktop applications like JetBrains Compose UI, and resource-constrained devices.

- jlink creates custom minimal JREs, reducing runtime size dramatically (e.g., 136MB to 28MB for Hello World).
- jdeps can list required Java modules for a program, which are then added via --add-modules.
- jlink supports cross-compilation by specifying --module-path to a target platform's JDK jmods directory.
- The resulting minimal JRE is platform-specific and must be built for each target architecture.
- This technique is useful for Docker images, desktop apps, and IoT/device deployments.