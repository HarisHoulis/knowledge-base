---
domain: engineering-culture
subdomain: build-tools
concept: java-module-path
title: Understanding Gradle #31 – The Module Path
sources:
  - title: "Understanding Gradle #31 – The Module Path"
    url: "https://www.youtube.com/watch?v=X9u1taDwLSA"
    author: "Jendrik Johannes (onepiece.Software)"
    date: "2023-03-07T19:15:01+00:00"
---

# Understanding Gradle #31 – The Module Path

This video by Jendrik Johannes explains the Java Module System (JPMS, also called Jigsaw) and the module path, contrasting it with the traditional classpath. It highlights how the classpath is a flat list of JARs where all packages are visible and conflicts can go undetected, while the module path introduces explicit module declarations. A minimal module-info.java specifies the module name, and 'require' directives declare dependencies, while 'exports' directives control package visibility. Unlike classpath conflicts, module path conflicts are detected by Java, providing stronger encapsulation.

The video demonstrates using javac and java with the module path, emphasizing the need for module-info.java in modular projects. It then shows how Gradle integrates with the Java Module System: Gradle continues to handle dependency resolution, but for modular projects, it places dependencies on the module path rather than the classpath. This can lead to redundancy because dependencies must be declared both in Gradle (e.g., as implementation dependencies) and in module-info.java via 'require'.

To eliminate redundancy, the author introduces the java-module-dependencies plugin, which maps module names to Gradle coordinates (Group:Artifact). This allows developers to declare dependencies using module names directly, aligning with JPMS and simplifying version management. The video also discusses using module names in version management to centralize dependency versions.

Overall, the content bridges the gap between Gradle's dependency management and Java's module system, offering practical advice for building modular Java applications with Gradle.

- The module path is a JPMS concept that provides stronger encapsulation than the classpath by requiring explicit module declarations and dependencies.
- Java can detect conflicts on the module path (e.g., split packages), while classpath collisions are often silent.
- Gradle resolves dependencies for modular projects onto the module path, but developers must declare them both in Gradle and in module-info.java, leading to redundancy.
- The java-module-dependencies plugin reduces redundancy by mapping module names to Gradle coordinates, allowing dependencies to be declared with module names.
- Module names can be used in Gradle version management, centralizing version declarations.