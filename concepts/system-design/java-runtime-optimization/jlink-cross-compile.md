---
domain: system-design
subdomain: java-runtime-optimization
concept: jlink-cross-compile
title: Using jlink to Cross-Compile Minimal JREs
sources:
  - title: "Using jlink to cross-compile minimal JREs"
    url: "https://jakewharton.com/using-jlink-to-cross-compile-minimal-jres/"
    author: "Jake Wharton"
---

# Using jlink to Cross-Compile Minimal JREs

jlink is a JDK tool that creates bespoke, minimal JREs tailored to an application. For a simple "Hello, world!" program, jdeps reports that only the java.base module is required. Using jlink with flags like --compress 2, --strip-debug, --no-header-files, and --no-man-pages produces a 28MiB runtime on Apple Silicon—an 80% reduction from the full 136MiB JRE. The author demonstrates that jlink can also cross-compile by pointing --module-path at a different platform's JDK, such as producing a Linux x64 JRE from an M1 Mac. This minimal JRE is then successfully transferred and executed on a Linux server, proving the approach works for multi-architecture deployments. The article highlights applications in Docker containers, desktop clients like JetBrains Compose UI, and resource-constrained devices, while encouraging exploration of jdeps and jlink options to keep runtimes small.

- Use jdeps --print-module-deps to determine which Java modules your application actually needs.
- jlink can generate a minimal JRE by specifying --add-modules with the required modules and enabling compression/debug-stripping flags.
- Cross-compilation is achieved by setting --module-path to a target platform's JDK jmods on the host machine.
- The article achieved a 28MiB JRE for a simple program on Apple Silicon and a 36MiB JRE for Linux x64, compared to a 136MiB standard JRE.
- This technique is valuable for multi-architecture Docker images, desktop apps, and devices with limited storage.