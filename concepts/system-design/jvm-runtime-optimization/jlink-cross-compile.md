---
domain: system-design
subdomain: jvm-runtime-optimization
concept: jlink-cross-compile
title: Using jlink to cross-compile minimal JREs
sources:
  - title: "Using jlink to cross-compile minimal JREs"
    url: "https://jakewharton.com/using-jlink-to-cross-compile-minimal-jres/"
---

# Using jlink to cross-compile minimal JREs

jlink is a JDK tool for creating bespoke, minimal JREs by including only the Java modules an application actually needs. The article demonstrates this with a simple 'Hello, world!' program, showing that a full JDK consumes 329MiB and a full JRE 136MiB, but a jlink-generated JRE drops to just 28MiB for a basic application (source: https://jakewharton.com/using-jlink-to-cross-compile-minimal-jres/).

A sibling tool, jdeps, analyzes class dependencies and lists required modules—for 'Hello, world!' this is only java.base. Using jlink with flags like --compress, --strip-debug, --no-header-files, and --no-man-pages yields a significantly smaller runtime that still executes the program correctly.

A key capability highlighted is that jlink can operate on JDKs for different platforms by pointing --module-path to another platform's jmods. This enables cross-compiling minimal JREs from a single host, as demonstrated by producing a Linux x64 JRE from an M1 Mac. The resulting 36MiB runtime runs successfully on a Linux server, making the approach valuable for multi-architecture Docker containers, desktop clients like JetBrains Compose UI, and resource-constrained devices.

- jlink creates minimal JREs by including only required modules, reducing a 136MiB JRE to 28MiB for a trivial program.
- jdeps identifies module dependencies; 'Hello, world!' only needs java.base.
- jlink can cross-compile by using --module-path to point at another platform's JDK modules, enabling multi-platform JRE generation from a single host.
- The technique is useful for multi-architecture Docker containers, desktop applications, and devices where a full JDK is impractical.