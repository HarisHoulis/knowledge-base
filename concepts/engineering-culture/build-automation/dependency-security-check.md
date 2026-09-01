---
domain: engineering-culture
subdomain: build-automation
concept: dependency-security-check
title: Configure Gradle to Discover Security Vulnerabilities
sources:
  - title: "Understanding Gradle #30 – Discover Security Vulnerabilities"
    url: "https://www.youtube.com/watch?v=g4PyEmYotwk"
    author: "Jendrik Johannes"
    date: "2023-02-20T16:34:20+00:00"
---

# Configure Gradle to Discover Security Vulnerabilities

This video demonstrates how to use the OWASP DependencyCheck plugin in Gradle to discover security vulnerabilities in project dependencies. The presenter explains the importance of checking the correct classpath, applying the 'org.owasp.dependencycheck' plugin, and configuring it as needed. The process includes running the ':dependencyCheckAnalysisTask' to analyze dependencies and react to any vulnerabilities found.

The video also highlights that vulnerabilities can exist not only in direct dependencies but also in transitive dependencies, and shows how to handle both cases. It provides practical examples in both Kotlin and Groovy DSL, making it applicable to a wide range of Gradle projects. The goal is to integrate security analysis into the build process to catch issues early.

- Apply the 'org.owasp.dependencycheck' plugin to enable security scanning.
- Configure the plugin according to project needs before running the analysis.
- Run the ':dependencyCheckAnalysis' task to identify vulnerabilities.
- Vulnerabilities may appear in both direct and transitive dependencies; review them all.
- Use the OWASP DependencyCheck plugin as a proactive security measure in Gradle builds.