---
domain: system-design
subdomain: jvm-packaging
concept: jlink-cross-compile-minimal-jres
title: Using jlink to cross-compile minimal JREs
sources:
  - title: "Using jlink to cross-compile minimal JREs"
    url: "https://jakewharton.com/using-jlink-to-cross-compile-minimal-jres/"
    author: "Jake Wharton"
---

# Using jlink to cross-compile minimal JREs

The article further demonstrates that jlink can cross-compile minimal JREs for other platforms by using the --module-path option to point to jmods from a different JDK (e.g., Linux x64). This allows developers to generate platform-specific runtimes from a single host machine, as shown by producing a Linux x64 JRE from an M1 Mac and successfully running it on a Linux server. This makes jlink valuable for multi-architecture Docker images, desktop applications like JetBrains Compose UI, and devices with limited storage. The key is to combine jdeps for module discovery and jlink with appropriate flags such as --compress, --strip-debug, --no-header-files, and --no-man-pages.

- jlink creates minimal JREs by including only required Java modules.
- jdeps identifies the modules needed by a program; 'Hello, world!' only requires java.base.
- Cross-compiling is possible by pointing jlink's --module-path to a target platform's JDK jmods.
- The minimal JRE for 'Hello, world!' was 28MB (M1) and 36MB (Linux x64), versus 136MB full JRE.
- This approach benefits multi-arch Docker, desktop apps, and resource-constrained devices.