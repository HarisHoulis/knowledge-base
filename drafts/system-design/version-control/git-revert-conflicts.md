---
domain: system-design
subdomain: version-control
concept: git-revert-conflicts
title: Why Git Revert Causes Conflicts
sources:
  - title: "EP225: Why Does Git Revert Cause Conflicts?"
    url: "https://blog.bytebytego.com/p/ep225-why-does-git-revert-cause-conflicts"
    author: "ByteByteGo"
    date: "2026-09-12"
---

# Why Git Revert Causes Conflicts

Git revert does not rewrite history; instead it creates a new commit that undoes the changes from an earlier commit, keeping shared branch history clean and traceable [ByteByteGo]. A revert conflict occurs when a later commit has changed the same lines as the commit being reverted [ByteByteGo].

In the example, commit C2 adds a feature and commit C3 changes those same lines, so reverting C2 collides with C3's changes. Git cannot determine which version is correct, so it pauses the revert [ByteByteGo]. To resolve, run `git revert C2`, manually fix the conflict, stage the file, and continue the revert. Git then creates a new commit that cleanly undoes C2 while keeping C3 intact [ByteByteGo].

- `git revert` creates a new commit that reverses an earlier commit instead of rewriting history.
- Revert conflicts happen when a later commit edits the same lines as the commit being undone.
- Resolution requires manually fixing the conflict, staging it, and continuing the revert.
- The resulting commit undoes the target commit while preserving later changes.