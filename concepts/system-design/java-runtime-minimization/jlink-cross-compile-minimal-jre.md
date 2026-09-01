---
domain: system-design
subdomain: java-runtime-minimization
concept: jlink-cross-compile-minimal-jre
title: Using jlink to cross-compile minimal JREs
sources:
  - title: "Using jlink to cross-compile minimal JREs"
    url: "https://jakewharton.com/using-jlink-to-cross-compile-minimal-jres/"
---

# Using jlink to cross-compile minimal JREs

The article demonstrates how to use `jlink`, a JDK tool, to generate a minimal JRE tailored to a specific Java application. For a simple "Hello, world!" program, `jdeps --print-module-deps` identifies that only `java.base` is required. Running `jlink` with `--add-modules java.base` and options like `--compress 2`, `--strip-debug`, `--no-header-files`, and `--no-man-pages` produces a runtime of approximately 28MiB on macOS ARM, compared to 136MiB for a standard JRE and 329MiB for the full JDK (source: "Using jlink to cross-compile minimal JREs", jakewharton.com).

The article also explains that although the generated JRE is platform-specific, `jlink` can cross-compile by downloading a JDK for a different target platform and setting `--module-path` to that JDK's `jmods` directory. Using a macOS ARM host, the author successfully creates a Linux x64 minimal JRE and runs it on a remote server. This technique is useful for multi-architecture Docker images, desktop clients like JetBrains Compose UI, and embedded or constrained devices where a full JDK or JRE is too large (source: "Using jlink to cross-compile minimal JREs", jakewharton.com).

- `jdeps --print-module-deps` tells you which Java modules your application needs.
- `jlink` builds a minimal JRE with only the required modules, drastically reducing binary size.
- Flags such as `--compress 2`, `--strip-debug`, `--no-header-files`, and `--no-man-pages` help shrink the runtime.
- Cross-compile by pointing host `jlink` to a target platform's `jmods` via `--module-path`.
- This approach is ideal for multi-arch Docker, desktop apps, and resource-constrained devices.