---
domain: engineering-culture
subdomain: jlink cross-compilation
concept: jlink-cross-compile-minimal-jres
title: Using jlink to Cross-Compile Minimal JREs
sources:
  - title: "Using jlink to cross-compile minimal JREs"
    url: "https://jakewharton.com/using-jlink-to-cross-compile-minimal-jres/"
    author: "Jake Wharton"
---

# Using jlink to Cross-Compile Minimal JREs

The article demonstrates how to use the JDK tool jlink to create minimal JREs tailored to an application, dramatically reducing the runtime size compared to a standard JRE. Starting with a simple Hello World program, the author uses jdeps to determine that only the java.base module is required, then runs jlink to produce a 28MiB JRE from a 136MiB full JRE, achieving an 80% size reduction while retaining functionality.

Cross-compilation is then explored by downloading a JDK for a different platform (Linux x64) and using jlink's --module-path to point at that JDK's jmods. This allows the host machine (an M1 Mac) to produce a minimal JRE for a different operating system and architecture, which is verified to run successfully on a Linux server. The technique is presented as ideal for multi-architecture Docker images, desktop applications, and constrained devices, with a note to explore jdeps and jlink options for further optimization.

- jdeps --print-module-deps identifies exactly which Java modules an application requires.
- jlink with --add-modules, --compress, --strip-debug, and no header/man pages creates a minimal JRE, shrinking a 136MiB JRE to 28MiB for a simple program.
- Using --module-path with a target platform's JDK jmods enables cross-compiling minimal JREs from any host architecture.
- Cross-compiled JREs work on the target platform, verified via scp/ssh execution on a Linux x64 server.
- This approach is beneficial for multi-arch Docker containers, desktop clients, and small devices.