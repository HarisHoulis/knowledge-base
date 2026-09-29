---
domain: python-backend
subdomain: developer tooling
concept: commit-message-rewriting
title: commit-rewriter 0.1
sources:
  - title: "commit-rewriter 0.1"
    url: "https://simonwillison.net/2026/Sep/14/commit-rewriter/"
    author: "Simon Willison"
    date: "2026-09-14"
  - title: "commit-rewriter 0.1 release"
    url: "https://github.com/simonw/commit-rewriter/releases/tag/0.1"
    author: "Simon Willison"
    date: "2026-09-14"
---

# commit-rewriter 0.1

commit-rewriter 0.1 is a small web app built to help edit commit messages in a Git repository. Simon Willison created it to clean up the commit messages for the Datasette security releases, whose initial commits "were full of coding agent cruft and references to issue IDs from our private repository, so they weren't fit for publication" (simonwillison.net).

The tool is run against a repository with `uvx commit-rewriter path/to/repo`, and the path can be omitted if you are already in the directory for that repo. It is distributed as a numbered 0.1 release on GitHub (github.com/simonw/commit-rewriter).

Safety is handled by branching before rewriting: when you submit your edits, the tool creates a timestamped branch of your current repo state to allow you to revert if needed, and then rewrites every commit from the first one you edited to the most recent. The project is tagged git, projects, python, and ai-assisted-programming.

- commit-rewriter is a Python web app for editing Git commit messages, released as version 0.1.
- It was motivated by Datasette security release commits containing coding agent cruft and private issue ID references that weren't fit for publication.
- Run it with `uvx commit-rewriter path/to/repo`; omit the path when already in the repo directory.
- On submit it creates a timestamped branch of the current repo state for revertibility, then rewrites all commits from the first edited one to the most recent.