---
domain: system-design
subdomain: jvm-runtime-images
concept: jlink-cross-compile-minimal-jres
title: Using jlink to Cross-Compile Minimal JREs
sources:
  - title: "Using jlink to cross-compile minimal JREs"
    url: "https://jakewharton.com/using-jlink-to-cross-compile-minimal-jres/"
---

# Using jlink to Cross-Compile Minimal JREs

The article demonstrates how to use `jlink` to create minimal JREs tailored to an application. A simple "Hello, world!" program is used as an example: the full JDK is 329MiB and the full JRE is 136MiB, but running `jdeps --print-module-deps` shows that only the `java.base` module is required. Using `jlink` with `--add-modules java.base` and options like `--compress 2` and `--strip-debug` produces a 28MiB JRE on the author's M1 Mac, an 80% reduction from the full JRE (Using jlink to cross-compile minimal JREs, https://jakewharton.com/using-jlink-to-cross-compile-minimal-jres/).

The key insight is that `jlink` can operate on JDK builds for other platforms by pointing `--module-path` at the target platform's `jmods` directory. The author downloads a Linux x64 JDK and, from the M1 Mac host, generates a Linux x64 minimal JRE that is 36MiB. This JRE successfully runs the same compiled Java class on a Linux server, proving that JREs can be effectively cross-compiled from a single host machine (Using jlink to cross-compile minimal JREs, https://jakewharton.com/using-jlink-to-cross-compile-minimal-jres/).

This approach is useful for multi-architecture Docker containers, desktop applications, and constrained devices where full JDKs cannot be shipped. The article encourages exploring all `jdeps` and `jlink` options to keep runtimes as small as possible (Using jlink to cross-compile minimal JREs, https://jakewharton.com/using-jlink-to-cross-compile-minimal-jres/).

- `jdeps --print-module-deps` identifies the Java modules an application actually requires.
- `jlink` builds a minimal JRE containing only those modules; a Hello World class needs just `java.base`.
- Use `--module-path` to point `jlink` at a target platform's JDK `jmods` to cross-compile JREs for other OS/architectures.
- The resulting JREs are platform-specific but dramatically smaller: 28MiB for Mac ARM and 36MiB for Linux x64, versus 136MiB full JRE.
- This technique supports multi-architecture containers, desktop apps, and resource-constrained devices.