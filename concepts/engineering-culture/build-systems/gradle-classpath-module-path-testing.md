---
domain: engineering-culture
subdomain: build-systems
concept: gradle-classpath-module-path-testing
title: Understanding Gradle #33 – Classpath and Module Path in Testing
sources:
  - title: "Understanding Gradle #33 – Classpath and Module Path in Testing"
    url: "https://www.youtube.com/watch?v=6rFEDcP8Noc"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2023-06-19T13:38:43+00:00"
---

# Understanding Gradle #33 – Classpath and Module Path in Testing

This video explains how Gradle handles testing for Java projects with both the traditional classpath and the newer module path. In classpath-based testing, each source set has its own compile and runtime classpaths, which allows fine-grained dependency management but can also introduce conflicts when multiple dependencies provide different versions of the same library. The video demonstrates how Gradle configures these classpaths for the test source set and how conflict resolution works, emphasizing the need to understand the classpath structure to avoid surprises.

For module path testing, the video introduces two testing strategies: blackbox and whitebox. Blackbox testing treats the module as an external JAR, requiring test modules to declare dependencies on the module under test. Whitebox testing, on the other hand, allows tests to access internal parts of the module by patching the module with test classes. The video showcases the java-module-testing plugin, which simplifies whitebox testing by automatically patching the module under test and managing module dependencies. It also illustrates how test modules can be packaged as JARs for blackbox scenarios, providing a comprehensive overview of testing Java modular applications in Gradle.

- Each Gradle source set has its own classpaths, so the test source set can have separate dependencies from main code.
- Classpath-based testing can lead to dependency version conflicts that need explicit resolution in Gradle.
- Module path testing offers blackbox (testing the module as a JAR) and whitebox (patching the module to access internals) approaches.
- The java-module-testing plugin automates whitebox testing, making it easier to test Java modules with Gradle.