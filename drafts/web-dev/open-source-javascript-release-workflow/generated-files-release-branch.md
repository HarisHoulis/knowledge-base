---
domain: web-dev
subdomain: open-source-javascript-release-workflow
concept: generated-files-release-branch
title: Why I Don't Commit Generated Files to Master
sources:
  - title: "Why I don't commit generated files to master"
    url: "https://kentcdodds.com/blog/why-i-dont-commit-generated-files-to-master"
    author: "Kent C. Dodds"
    date: "2015-10-05"
---

# Why I Don't Commit Generated Files to Master

Kent C. Dodds explains that committing built files—the concatenated, compiled, and minified browser distribution of an open-source JavaScript library—to master creates problems. The temptations to do so include Bower requiring built files, easier direct downloads, and using rawgit for examples in tools like jsbin or plunker [source].

- Committing generated files to master makes Git history and diffs noisy and hard to interpret.
- Contributors often submit changes to dist files rather than source, causing overwrites or force-push resubmissions.
- The proposed solution is to push generated files only to a separate latest branch, automated with publish-latest.
- The latest branch preserves Bower tagging, direct downloads, and rawgit/CDNJS examples while master remains source-only.
- The author later notes this is no longer his approach, as he moved to relying on unpkg.