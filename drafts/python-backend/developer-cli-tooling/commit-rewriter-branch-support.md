---
domain: python-backend
subdomain: developer-cli-tooling
concept: commit-rewriter-branch-support
title: commit-rewriter 0.2: branch support for non-default branches
sources:
  - title: "commit-rewriter 0.2"
    url: "https://simonwillison.net/2026/Sep/24/commit-rewriter/"
    author: "Simon Willison"
    date: "2026-09-24"
---

# commit-rewriter 0.2: branch support for non-default branches

commit-rewriter 0.2 is a release-note post announcing a single new capability: the tool can now operate on branches other than the default branch (simonwillison.net). The feature addresses previously limited scope, since earlier versions were effectively constrained to the default branch.

The new behavior is exposed through a `--branch` flag. The documented invocation is `uvx commit-rewriter --branch other`, which runs the tool against a branch named `other` (simonwillison.net). Distribution via `uvx` indicates the tool is run as a Python CLI package without a separate install step.

The post credits issue #3 for this change and tags the entry under git (simonwillison.net). No other changes, performance claims, or implementation details are described in the source.

- Version 0.2 adds support for branches other than the default branch.
- Usage: `uvx commit-rewriter --branch other`, passing the target branch via `--branch`.
- The change is tracked as issue #3 on the project.