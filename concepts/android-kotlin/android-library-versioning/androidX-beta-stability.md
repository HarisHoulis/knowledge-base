---
domain: android-kotlin
subdomain: android-library-versioning
concept: androidX-beta-stability
title: You should use AndroidX betas
sources:
  - title: "You should use AndroidX betas"
    url: "https://jakewharton.com/you-should-use-androidx-betas/"
    author: "Jake Wharton"
---

# You should use AndroidX betas

AndroidX libraries follow a unique versioning strategy where beta and release candidate (RC) versions are API stable and production-ready, contrary to typical semantic versioning practices. Unlike standard libraries where stable releases can introduce bugs requiring patch releases, AndroidX ensures that once a library reaches beta, its API is frozen and cannot be changed or extended. This allows Google's first-party apps to ship against these prerelease versions, catching bugs early. By using AndroidX betas, developers can access bug fixes and new features months sooner than waiting for stable releases. However, this approach requires robust testing infrastructure, including unit, screenshot, and instrumented tests, to catch any issues. Users are also encouraged to report bugs upstream to benefit the entire community.

- AndroidX betas and RCs are API stable due to tooling that prevents API changes after beta01.
- Google's first-party apps build, test, and ship against alpha and beta versions of AndroidX libraries, ensuring widespread testing.
- Using betas allows faster access to bug fixes and features compared to waiting for stable releases, which can be months apart.
- Gradual adoption is possible; mature libraries like collection and core have low risk, while load-bearing libraries like Compose UI benefit from early testing.
- Proper testing infrastructure is essential for confidently using prerelease versions, and reporting bugs upstream helps the ecosystem.