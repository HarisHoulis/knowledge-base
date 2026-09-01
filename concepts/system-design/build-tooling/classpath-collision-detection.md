---
domain: system-design
subdomain: build-tooling
concept: classpath-collision-detection
title: Detect and Resolve Classpath Collisions in Gradle
sources:
  - title: "Understanding Gradle #29 – Detect and Resolve Collisions on a Classpath"
    url: "https://www.youtube.com/watch?v=KocTqF0hO_8"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2023-01-23T14:48:52+00:00"
---

# Detect and Resolve Classpath Collisions in Gradle

This video explains how classpath collisions occur in Java applications and how Gradle can help detect and resolve them. A collision happens when the same fully qualified class appears more than once on the classpath. The JVM then silently picks the first class it finds, which can lead to subtle runtime errors such as wrong method behavior or NoSuchMethodError. The video demonstrates this with an example that shows how the location of a class can be looked up and how running java with a colliding classpath can produce unknown behavior (0:45–1:20).

Gradle's default dependency version conflict resolution resolves collisions that come from different versions of the same component by selecting the highest version and evicting the lower ones. However, collisions between different components that provide the same class are not automatically detected. These are called capability conflicts, and they often occur when libraries repackage third-party code or split APIs across multiple artifacts. The video highlights that such collisions can go unnoticed until they cause problems at runtime (2:42–5:11).

To address this, two Gradle plugins are presented. The Classpath Collisions Detector plugin scans a classpath for duplicate classes and reports them, making hidden collisions visible (6:53). The Java Ecosystem Capabilities plugin allows you to declare capabilities for external modules so Gradle can treat them as conflicting components. This lets you configure the build to fail on known capability conflicts or align the versions of all modules that share a capability (8:06). The video concludes with a summary of how these tools improve dependency hygiene and build reliability (11:01).

- Classpath collisions occur when multiple dependencies contain the same fully qualified class, and the JVM picks one arbitrarily, causing hard-to-debug runtime errors.
- Gradle's version conflict resolution only handles collisions between different versions of the same component; collisions between different components are not caught automatically.
- The Classpath Collisions Detector plugin identifies duplicate classes on a classpath, making potential issues visible.
- The Java Ecosystem Capabilities plugin lets you declare component capabilities so Gradle can detect and fail on capability conflicts, enabling proper resolution via version alignment or exclusion.
- Explicit detection and resolution of classpath collisions is essential for reliable, reproducible Java builds.