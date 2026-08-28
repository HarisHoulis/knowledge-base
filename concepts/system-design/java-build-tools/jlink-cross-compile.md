---
domain: system-design
subdomain: java-build-tools
concept: jlink-cross-compile
title: Using jlink to Cross-Compile Minimal JREs
sources:
  - title: "Using jlink to cross-compile minimal JREs"
    url: "https://jakewharton.com/using-jlink-to-cross-compile-minimal-jres/"
    author: "Jake Wharton"
---

# Using jlink to Cross-Compile Minimal JREs

The article then addresses the challenge of shipping to different platforms. While Java bytecode is platform-independent, the JRE is not, so the author uses jlink's --module-path option to point to a Linux x64 JDK's jmods from a Mac host, effectively cross-compiling a minimal JRE for Linux x64. The resulting runtime is 36MiB and runs successfully on the target server. This approach enables multi-architecture Docker containers, desktop clients, and constrained devices.

- jdeps lists the Java modules required by an application; for a basic program, only java.base is needed.
- jlink can create a minimal JRE with only the specified modules, reducing size from 136MiB to 28MiB in the example.
- jlink can use a JDK for a different platform via --module-path, enabling cross-compilation of minimal JREs from any host.
- The minimal JRE is still platform-specific, so separate builds are needed for each target architecture.
- jlink options like --compress, --strip-debug, --no-header-files, and --no-man-pages further reduce size.