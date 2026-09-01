---
domain: engineering-culture
subdomain: dependency-security
concept: owasp-dependency-check
title: Understanding Gradle #30 – Discover Security Vulnerabilities
sources:
  - title: "Understanding Gradle #30 – Discover Security Vulnerabilities"
    url: "https://www.youtube.com/watch?v=g4PyEmYotwk"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2023-02-20"
---

# Understanding Gradle #30 – Discover Security Vulnerabilities

In this video, Jendrik Johannes (2023) explains how to configure Gradle to identify known security vulnerabilities in project dependencies using the OWASP DependencyCheck plugin. The video is part of the 'Understanding Gradle' series and focuses on practical steps for integrating security scanning into a Gradle build, particularly for Java modularity projects. It covers which classpath should be checked, how to apply and configure the plugin, and how to run the analysis task.

The video demonstrates adding the `org.owasp.dependencycheck` plugin, configuring it to check the appropriate classpath (e.g., the runtime classpath), and executing the `dependencyCheckAnalysis` task to generate a vulnerability report. It emphasizes the importance of reacting to vulnerabilities not only in direct dependencies but also in transitive dependencies, which are often overlooked. The examples are provided in both Kotlin DSL and Groovy DSL, making the approach accessible to different Gradle users.

By integrating the OWASP plugin, developers can automate the detection of known vulnerabilities and take corrective action, such as upgrading dependency versions or excluding problematic transitive dependencies. The video concludes with a summary of the key steps, highlighting that regular vulnerability scanning should be part of a robust software development lifecycle.

- Add the OWASP DependencyCheck Gradle plugin (`org.owasp.dependencycheck`) to the build.
- Configure the plugin to check the relevant classpath, such as `runtimeClasspath`, for accurate vulnerability detection.
- Run the `dependencyCheckAnalysis` task to produce a report of known vulnerabilities in dependencies.
- Address vulnerabilities in both direct and transitive dependencies by upgrading versions or adjusting dependency configurations.