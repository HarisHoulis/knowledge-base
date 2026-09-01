---
domain: engineering-culture
subdomain: jvm-tooling
concept: jlink-cross-compile
title: Using jlink to Cross-Compile Minimal JREs
sources:
  - title: "Using jlink to cross-compile minimal JREs"
    url: "https://jakewharton.com/using-jlink-to-cross-compile-minimal-jres/"
    author: "Jake Wharton"
---

# Using jlink to Cross-Compile Minimal JREs

The article demonstrates how to use jlink, a JDK tool, to create minimal JREs tailored to an application's specific needs. Starting with a simple "Hello, world!" program, the author uses jdeps to identify the required Java module (java.base) and then invokes jlink with options like --compress 2, --strip-debug, and --no-header-files to produce a JRE that is only 28 MiB, compared to 136 MiB for a standard JRE and 329 MiB for a full JDK. This significant size reduction is achieved by including only the necessary modules and stripping non-essential files (Jake Wharton, "Using jlink to cross-compile minimal JREs").

The article goes on to illustrate a key capability: cross-compiling minimal JREs for different platforms from a single host. After discovering that a JRE built for an M1 Mac cannot run on a Linux x64 server, the author downloads a Linux x64 JDK and points jlink's --module-path to that JDK's jmods directory. This yields a Linux x64 JRE that works correctly on the server, proving that jlink can effectively cross-compile JREs for multiple architectures and platforms (Jake Wharton, "Using jlink to cross-compile minimal JREs").

The technique is particularly valuable for multi-architecture Docker containers, desktop applications using frameworks like JetBrains Compose UI, and resource-constrained devices where a full JDK is impractical. The article encourages exploring additional jdeps and jlink options to further minimize runtime footprint (Jake Wharton, "Using jlink to cross-compile minimal JREs").

- jdeps helps determine which Java modules an application requires, enabling minimal JRE construction.
- jlink can create a custom JRE that is significantly smaller than a full JRE or JDK.
- Using jlink's --module-path with a JDK for another platform allows cross-compilation of JREs from any host.
- Minimal JREs are useful for multi-architecture Docker images, desktop apps, and embedded devices.
- jlink options like --compress, --strip-debug, --no-header-files, and --no-man-pages help reduce JRE size.