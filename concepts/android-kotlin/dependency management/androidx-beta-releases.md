---
domain: android-kotlin
subdomain: dependency management
concept: androidx-beta-releases
title: You should use AndroidX betas
sources:
  - title: "You should use AndroidX betas"
    url: "https://jakewharton.com/you-should-use-androidx-betas/"
    author: "Jake Wharton"
---

# You should use AndroidX betas

Jake Wharton's article explains that AndroidX libraries follow a stricter versioning model than normal semantic versioning. Once an AndroidX library reaches `beta01`, its API is locked and no new APIs can be added; only bug fixes are permitted. This means `1.2.0-beta01` is functionally equivalent to a normal library's `1.2.0` stable release. Google's first-party apps build against AndroidX HEAD, including alpha and beta versions, so these artifacts receive extensive real-world testing before final release (Jake Wharton, "You should use AndroidX betas").

Sticking only to stable AndroidX versions can mean waiting months for a bug fix between major releases. Adopting betas—especially for mature libraries like `collection`, `core`, and `activity`—lets you get fixes sooner and reduces upgrade friction. This approach requires solid testing infrastructure: unit tests, screenshot tests, and instrumented tests as a safety net. Users also have a responsibility to report bugs upstream so the entire ecosystem benefits (Jake Wharton, "You should use AndroidX betas").

- AndroidX beta01 is API-stable and equivalent to a normal stable release.
- Google's first-party apps use AndroidX alpha and beta versions, so they are production-tested.
- Using betas avoids long waits for fixes between stable AndroidX releases.
- Start with mature libraries and rely on comprehensive testing for confidence.
- Report bugs upstream to improve AndroidX for everyone.