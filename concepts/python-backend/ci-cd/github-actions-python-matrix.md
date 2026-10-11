---
domain: python-backend
subdomain: ci-cd
concept: github-actions-python-matrix
title: Python 3.15.0 Added to actions/python-versions
sources:
  - title: "Python 3.15.0 added to actions/python-versions"
    url: "https://simonwillison.net/2026/Oct/10/python-actions/"
    author: "Simon Willison"
    date: "2026-10-10"
---

# Python 3.15.0 Added to actions/python-versions

Python 3.15.0 has been added to the actions/python-versions repository, meaning GitHub Actions workflows can now target the new stable release. The change is captured in a specific commit to that repository (https://github.com/actions/python-versions/commit/49858b91c92d27403416ee43117032e91d00ce24).

With this landing, developers can add "3.15" to a GitHub Actions testing matrix to run their test suites against Python 3.15.0 (https://www.python.org/downloads/release/python-3150/). The post frames this as the practical payoff of tracking the repository until the stable version appeared.

- Python 3.15.0 is now available in actions/python-versions.
- GitHub Actions testing matrices can include "3.15" to test against the new release.
- The update is tied to a specific commit in the actions/python-versions repository.