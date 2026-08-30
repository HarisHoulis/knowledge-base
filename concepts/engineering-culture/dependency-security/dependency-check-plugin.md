---
domain: engineering-culture
subdomain: dependency-security
concept: dependency-check-plugin
title: Understanding Gradle #30 – Discover Security Vulnerabilities
sources:
  - title: "Understanding Gradle #30 – Discover Security Vulnerabilities"
    url: "https://www.youtube.com/watch?v=g4PyEmYotwk"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2023-02-20T16:34:20+00:00"
---

# Understanding Gradle #30 – Discover Security Vulnerabilities

This video explains how to configure Gradle to discover security vulnerabilities in project dependencies using the OWASP DependencyCheck plugin. The main focus is on integrating the plugin into a Gradle build, running the analysis task, and responding to vulnerabilities in both direct and transitive dependencies. The author emphasizes that it is important to check the runtime classpath because it includes all dependencies that are actually used when the application runs (source: https://www.youtube.com/watch?v=g4PyEmYotwk).

- Apply the 'org.owasp.dependencycheck' plugin to a Gradle project to enable vulnerability scanning.
- Configure the plugin appropriately, for example by setting the output format and failure criteria.
- Run the ':dependencyCheckAnalysis' task to generate a report of known security issues.
- The plugin can be configured to fail the build when vulnerabilities are found, helping to enforce security in CI.
- It is essential to check the runtime classpath, as transitive dependencies on that classpath may also introduce vulnerabilities.