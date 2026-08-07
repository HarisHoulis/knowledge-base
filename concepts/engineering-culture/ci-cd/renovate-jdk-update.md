---
domain: engineering-culture
subdomain: ci-cd
concept: renovate-jdk-update
title: Using Renovate to update build JDK
sources:
  - title: "Using Renovate to update build JDK"
    url: "https://jakewharton.com/using-renovate-to-update-build-jdk/"
---

# Using Renovate to update build JDK

To automate JDK updates, Renovate is configured with a custom manager that reads the `.java-version` file and uses the `java-version` datasource to detect the latest JDK version. The config includes `ignorePresets: ['workarounds:javaLTSVersions']` to ensure the newest version is not constrained to LTS releases, and an `extractVersionTemplate` to only write the major version (e.g., `21`) [2]. Custom manager regex matches the `.java-version` file and replaces its content when a new JDK is available [2]. After pushing this configuration, Renovate automatically creates PRs to update the JDK version, as shown in example PRs [3].

- Use a `.java-version` file to centralize JDK version specification and reference it from `setup-java` with `java-version-file`.
- Avoid Gradle toolchains; instead, build on the latest JDK and test on older JVM versions.
- Configure Renovate with a custom regex manager and `java-version` datasource to automatically bump the JDK version.
- The `extractVersionTemplate` ensures only the major version is written, keeping the file clean.
- Renovate then sends PRs to update the JDK, keeping CI builds current without manual edits.