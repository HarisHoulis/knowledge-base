---
domain: system-design
subdomain: dependency-management
concept: classpath-collision-detection
title: Detect and Resolve Classpath Collisions in Gradle
sources:
  - title: "Understanding Gradle #29 – Detect and Resolve Collisions on a Classpath"
    url: "https://www.youtube.com/watch?v=KocTqF0hO_8"
    author: "Jendrik Johannes"
    date: "2023-01-23"
---

# Detect and Resolve Classpath Collisions in Gradle

Classpath collisions occur when multiple JARs on the Java classpath contain the same fully qualified class. The JVM silently picks the first one it encounters, which can lead to subtle runtime errors such as NoSuchMethodError or unexpected behavior. The video demonstrates this with a simple example where two different libraries provide the same class, and the classpath order affects which version gets loaded. This is particularly dangerous because the error may not appear during compilation but only at runtime when the wrong implementation is used (Johannes, 2023, https://www.youtube.com/watch?v=KocTqF0hO_8).

Gradle's built-in dependency version conflict resolution handles collisions only when the same component (same group and module) appears in multiple versions. It automatically selects the highest version. However, collisions between different components—for instance, when two independent libraries bundle or shade the same third-party package—are not automatically resolved. These collisions are undetected by default, which can cause hard-to-debug issues that vary depending on classpath order and environment (Johannes, 2023, https://www.youtube.com/watch?v=KocTqF0hO_8).

To address this, the video introduces two plugins. The Classpath Collision Detector plugin scans all classpath configurations and reports any class that appears in more than one JAR, making the problem visible. The Java Ecosystem Capabilities plugin goes a step further by allowing you to declare 'capabilities' for components. When two different components provide the same capability (e.g., they both contain the same API package), Gradle treats them as conflicting and applies standard version conflict resolution, effectively turning a classpath collision into a resolvable version conflict (Johannes, 2023, https://www.youtube.com/watch?v=KocTqF0hO_8).

In practice, developers should first run the collision detector to identify all collisions, then use the capabilities plugin to declare the relevant capabilities or use component metadata rules. After that, Gradle can resolve the conflict by selecting the highest version or through explicit dependency constraints. The recommended workflow is to integrate both plugins into the build and regularly check for collisions, especially when adding new dependencies or upgrading existing ones. This approach brings classpath collisions under control and keeps JVM applications reliable (Johannes, 2023, https://www.youtube.com/watch?v=KocTqF0hO_8).

- Classpath collisions happen when multiple dependencies contain the same fully qualified class, and JVM picks the first one without any warning.
- Gradle's version conflict resolution only handles collisions between different versions of the same component; collisions between different components remain undetected.
- The classpath-collision-detector plugin scans all classpaths and reports every class that appears more than once, making collisions visible.
- The java-ecosystem-capabilities plugin lets you declare capabilities so that distinct components providing the same API are treated as conflicting, enabling Gradle to resolve them via standard conflict resolution.
- Use both plugins together to automatically detect and then resolve classpath collisions in your Gradle build.