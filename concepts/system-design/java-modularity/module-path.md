---
domain: system-design
subdomain: java-modularity
concept: module-path
title: Understanding Gradle #31 – The Module Path
sources:
  - title: "Understanding Gradle #31 – The Module Path"
    url: "https://www.youtube.com/watch?v=X9u1taDwLSA"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2023-03-07T19:15:01+00:00"
---

# Understanding Gradle #31 – The Module Path

The video explains the Java Module System (JPMS, Jigsaw) and focuses on the role of the module path as opposed to the classpath. It demonstrates using javac and java with the module path, creating a minimal module-info.java, and using 'require' and 'exports' directives to define module dependencies and expose packages. It also highlights that Java can detect conflicts on the module path, something the classpath does not offer.

The video then shows how to build Java modules with Gradle, emphasizing that Gradle handles dependency management via configurations while module-info.java declares the module-level dependencies. The author points out redundant dependency definitions and introduces the 'java-module-dependencies' plugin to mitigate this. Finally, it covers how module names map to Gradle (GA) coordinates and how that mapping can be used in version management.

- The module path is a distinct mechanism from the classpath, providing stronger encapsulation and conflict detection at runtime.
- A minimal module-info.java requires 'require' directives for dependencies and 'exports' directives to make packages accessible.
- Gradle builds modular applications by combining its own dependency management (configurations) with module-info.java declarations.
- The 'java-module-dependencies' plugin helps reduce redundancy when declaring dependencies in both Gradle and module-info.
- Mapping module names to Maven coordinates enables more integrated version management in Gradle.