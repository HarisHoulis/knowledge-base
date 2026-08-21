---
domain: engineering-culture
subdomain: jvm-tooling
concept: jlink-cross-compilation
title: Using jlink to Cross-Compile Minimal JREs
sources:
  - title: "Using jlink to cross-compile minimal JREs"
    url: "https://jakewharton.com/using-jlink-to-cross-compile-minimal-jres/"
---

# Using jlink to Cross-Compile Minimal JREs

The article demonstrates how to use jlink to create a minimal JRE for a Java application, reducing the runtime size from 136MiB to 28MiB for a "Hello, world!" program. It explains that jdeps can determine the required Java modules, and jlink then builds an image containing only those modules with options like --compress 2, --strip-debug, --no-header-files, and --no-man-pages to further shrink the footprint.

A key insight is that jlink can cross-compile JREs for other platforms by pointing --module-path at a JDK of the target platform (e.g., Linux x64) while running jlink on the host machine. This enables developers to generate platform-specific minimal JREs without needing to install a full JDK for each target platform. The resulting Linux x64 JRE was slightly larger (36MiB) but still small and worked as expected on a remote server.

The article highlights use cases such as multi-architecture Docker containers, desktop applications like JetBrains Compose UI, and resource-constrained devices, and encourages exploring jdeps and jlink options to keep runtimes small.

- jlink creates application-specific JREs that are much smaller than the standard JRE (28MiB vs 136MiB for a simple program).
- jdeps identifies required modules from compiled classes, which can be fed directly to jlink with --add-modules.
- jlink can cross-compile for any platform by specifying --module-path pointing to the target JDK's jmods directory.
- Compression and stripping options (--compress, --strip-debug, --no-header-files, --no-man-pages) reduce size further.
- This technique is valuable for Docker images, desktop apps, and embedded deployments.