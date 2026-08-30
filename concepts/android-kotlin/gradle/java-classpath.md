---
domain: android-kotlin
subdomain: gradle
concept: java-classpath
title: Understanding Gradle #26 – The Classpath
sources:
  - title: "Understanding Gradle #26 – The Classpath"
    url: "https://www.youtube.com/watch?v=HqAp9JBl2_U"
    author: "Jendrik Johannes"
    date: "2022-11-21"
---

# Understanding Gradle #26 – The Classpath

The video explains the Java classpath, a fundamental concept for Java modularity. It defines the classpath as a list of locations, such as JAR files and directories, that the Java compiler and runtime use to find classes. The presenter demonstrates using javac and java commands directly with the `-cp` flag, showing how changing the classpath affects compilation and execution. The example highlights the distinction between compile-time and runtime classpaths, and how manually managing them can lead to errors if not set correctly (Jendrik Johannes, 2022).

Gradle automates classpath construction by distinguishing between compile classpath and runtime classpath, and for tests it creates separate classpaths. The video shows how Gradle resolves dependencies from repositories, such as Maven Central, to build the appropriate classpaths for different tasks. It also covers running tests with Gradle, which uses a test classpath that includes the compiled production code, test code, and test-specific dependencies. A key takeaway is that Gradle manages these classpaths so developers don't need to manually list JARs, reducing the risk of missing dependencies or version conflicts (Jendrik Johannes, 2022).

- The classpath is a list of file and directory locations where Java tools search for classes.
- Both javac and java use the classpath; the `-cp` flag sets it manually.
- Gradle automatically constructs distinct classpaths for compilation, runtime, and testing.
- Gradle resolves dependencies from repositories to build classpaths, eliminating manual JAR management.
- Understanding classpaths helps prevent runtime errors like ClassNotFoundException and NoClassDefFoundError.