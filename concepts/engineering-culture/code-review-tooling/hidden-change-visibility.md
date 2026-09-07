---
domain: engineering-culture
subdomain: code-review-tooling
concept: hidden-change-visibility
title: Surfacing Hidden Change to Pull Requests
sources:
  - title: "Surfacing Hidden Change to Pull Requests"
    url: "https://developer.squareup.com/blog/surfacing-hidden-change-to-pull-requests"
---

# Surfacing Hidden Change to Pull Requests

Programming deals with visible changes like logic and declared dependencies, but hidden changes such as transitive dependencies, generated code, and manifest files also matter. The Cash Android team found these hidden changes caused problems late in the release process, so they built tooling to surface them in pull requests via CI comments (source: https://developer.squareup.com/blog/surfacing-hidden-change-to-pull-requests). The CI computes diffs for APK size, method count, full dependency graphs, and merged manifests, then posts these as comments on the pull request to alert authors and reviewers (source: https://developer.squareup.com/blog/surfacing-hidden-change-to-pull-requests). This helps catch unexpected bloat or incompatibilities early—for example, seeing a new dependency's method impact or an unexpected permission in the merged manifest. Not all details are included in the comment; smaller reports and full diffs are attached to the CI build for deeper investigation when needed (source: https://developer.squareup.com/blog/surfacing-hidden-change-to-pull-requests). The project-specific metrics they choose aim to make important but otherwise invisible information visible during review.

- Hidden changes like transitive dependencies, generated code, and manifests can cause issues late in release and are often overlooked in code review.
- The Cash Android team automated CI comments that show diffs in APK size, method count, dependency graph, and merged manifest on pull requests.
- Unexpected manifest changes, such as added permissions or exposed components, can lead to compatibility or security problems.
- Detailed reports are attached to CI builds rather than placed in comments, keeping the comment readable while still allowing deep inspection.