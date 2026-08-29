---
domain: engineering-culture
subdomain: build-tooling
concept: gradle-dependency-security
title: Configure Gradle to Discover Security Vulnerabilities
sources:
  - title: "Understanding Gradle #30 – Discover Security Vulnerabilities"
    url: "https://www.youtube.com/watch?v=g4PyEmYotwk"
    author: "onepiece.Software by Jendrik Johannes"
    date: "2023-02-20"
---

# Configure Gradle to Discover Security Vulnerabilities

This video from the 'Understanding Gradle' series focuses on using the OWASP DependencyCheck plugin in Gradle to detect security vulnerabilities in project dependencies. It is part of a broader discussion on Java modularity, specifically addressing the classes and dependencies on the classpath. The plugin helps identify known vulnerabilities in both direct and transitive dependencies, enabling developers to react proactively.

The presentation covers practical steps: determining which classpath to check, applying the 'org.owasp.dependencycheck' plugin, configuring the plugin, and running the ':dependencyCheckAnalysisTask'. It also discusses how to respond when a vulnerability is found, both in direct dependencies and in transitive dependencies, with an emphasis on understanding the dependency tree and managing version collisions.

- Use the OWASP DependencyCheck Gradle plugin to scan dependencies for known security vulnerabilities.
- Check the appropriate classpath(s) – often the runtime classpath – to cover what actually ends up in the application.
- Apply and configure the 'org.owasp.dependencycheck' plugin, then run the ':dependencyCheckAnalysisTask'.
- Understand how to react to vulnerabilities in both direct and transitive dependencies, including version updates and collision resolution.