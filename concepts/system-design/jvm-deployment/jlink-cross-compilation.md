---
domain: system-design
subdomain: jvm-deployment
concept: jlink-cross-compilation
title: Using jlink to cross-compile minimal JREs
sources:
  - title: "Using jlink to cross-compile minimal JREs"
    url: "https://jakewharton.com/using-jlink-to-cross-compile-minimal-jres/"
---

# Using jlink to cross-compile minimal JREs

The article demonstrates using `jlink` to create minimal, application-specific JREs from a JDK. Starting with a simple "Hello, world!" program, the author shows how `jdeps` can determine required Java modules, and then `jlink` can build a runtime image containing only those modules. The resulting minimal JRE is significantly smaller than a full JRE—28 MiB vs 136 MiB for the example—making it suitable for distribution and embedded use (Jake Wharton, jakewharton.com).

- `jlink` builds minimal JREs by including only the Java modules your application requires, determined via `jdeps --print-module-deps`.
- Using options like `--compress 2`, `--strip-debug`, `--no-header-files`, and `--no-man-pages` further reduces the JRE size.
- `jlink` can cross-compile for other platforms by pointing `--module-path` at the target platform's JDK `jmods` directory.
- This approach enables efficient multi-architecture Docker containers, desktop apps, and constrained device deployments (Jake Wharton, jakewharton.com).