---
domain: android-kotlin
subdomain: gradle-dependency-management
concept: classpath-collision-detection
title: Detect and Resolve Collisions on a Classpath
sources:
  - title: "Understanding Gradle #29 – Detect and Resolve Collisions on a Classpath"
    url: "https://www.youtube.com/watch?v=KocTqF0hO_8"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2023-01-23T14:48:52+00:00"
---

# Detect and Resolve Collisions on a Classpath

In this video, Jendrik Johannes explains how classpath collisions occur in Java projects and how to handle them with Gradle. When multiple dependencies on the classpath contain classes with the same fully qualified name, the JVM loads the first one it encounters, potentially causing subtle runtime errors. For example, running a simple Java command with a colliding classpath demonstrates that the class loaded is determined by the order of the classpath entries, not by the programmer's intent. Gradle's built-in version conflict resolution only helps when the same component is declared with different versions, but it does not detect collisions between different components that provide the same class or package. This gap can lead to undetected issues in production. To address this, Johannes introduces two plugin solutions. The Classpath Collisions Detector plugin scans the classpath and reports any overlapping classes, making the problem visible. The Java Ecosystem Capabilities plugin assigns capabilities to components, allowing Gradle to apply proper conflict resolution when multiple components provide the same feature. By declaring capabilities, teams can either fail the build or consistently select the correct provider, ensuring predictable behavior. The video emphasizes that these tools integrate naturally into Gradle's existing dependency resolution model and help maintain a clean and reliable classpath.

- Classpath collisions happen when multiple dependencies contain the same fully qualified class; the JVM loads the first in classpath order, leading to unpredictable behavior.
- Gradle's version conflict resolution handles same-component versions but not collisions across different components providing the same class.
- The classpath-collision-detector plugin identifies overlapping classes on the classpath.
- The java-ecosystem-capabilities plugin lets you declare capabilities so Gradle can resolve conflicts by choosing one provider consistently or failing the build.