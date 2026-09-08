---
domain: java-tools
subdomain: dependency-management
concept: major-version-interop-policy
title: Java Interoperability Policy for Major Version Updates
sources:
  - title: "Java Interoperability Policy for Major Version Updates"
    url: "https://jakewharton.com/java-interoperability-policy-for-major-version-updates/"
---

# Java Interoperability Policy for Major Version Updates

The article discusses a policy for handling major version updates in foundational Java/Android libraries to mitigate transitive dependency conflicts. When a library like Retrofit releases a major version with breaking API changes, other libraries that depend on the older version can prevent consumers from upgrading. The proposed solution is to rename the Java package to include the major version number (e.g., `com.example.retrofit2` for version 2.x), which allows multiple major versions to coexist on the same classpath without conflicting. This enables users to upgrade gradually or incrementally, and shims for older versions can be built in a sibling artifact. The policy also recommends including the library name in the Maven group ID (e.g., `com.example.retrofit:retrofit`) to organize modules, and renaming the group ID to include the version number (e.g., `com.example.retrofit2`) so dependency resolvers treat each major version independently. The choice to rename the group ID rather than the artifact ID is explained, as a single artifact ID change would affect Maven coordinates and require broader changes. This approach is not strict semantic versioning but adheres to its spirit for major bumps. The first libraries to adopt this policy are Retrofit 2.0 and OkHttp 3.0.

- Rename the Java package to include the major version for foundational libraries starting at major version 2, enabling coexistence of multiple versions on the classpath.
- Include the library name as part of the Maven group ID to organize artifacts and avoid root namespace pollution.
- Rename the group ID to include the major version so dependency resolution treats each major version independently, preventing forced upgrades of transitive dependencies.
- This policy allows users to upgrade major versions gradually rather than all at once, reducing migration friction.
- Retrofit 2.0 and OkHttp 3.0 will be the first libraries to apply this policy.