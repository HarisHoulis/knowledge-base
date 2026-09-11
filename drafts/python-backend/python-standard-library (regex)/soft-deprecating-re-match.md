---
domain: python-backend
subdomain: python-standard-library (regex)
concept: soft-deprecating-re-match
title: Soft-deprecating re.match() in Python 3.15
sources:
  - title: "Soft-deprecating re.match()"
    url: "https://simonwillison.net/2026/Sep/11/soft-deprecating-re-match/"
    author: "Simon Willison"
    date: "2026-09-11"
  - title: "Soft deprecating re.match() (Lobste.rs submission)"
    url: "https://lobste.rs/s/u7dr96/soft_deprecating_re_match"
---

# Soft-deprecating re.match() in Python 3.15

In the upcoming Python 3.15 release, the long-standing `re.match()` function receives a soft deprecation, according to release manager Hugo van Kemenade. The function remains available, but a clearer alias, `re.prefixmatch()`, now exists — a name that accurately reflects its behaviour of anchoring the pattern at the beginning of the string but not at the end.

The rename addresses a persistent source of confusion: `re.match()` sounds like it matches a string, but it only anchors at the start. For most use cases, the guidance is to use `re.search()` to match a pattern anywhere in the string, or `re.fullmatch()` to require a match against the entire string.

- `re.match()` is soft-deprecated in Python 3.15; it still works but gains the clearer alias `re.prefixmatch()`.
- The new name documents the actual semantics: anchored at the string start, not the end.
- Prefer `re.search()` for anywhere-in-string matching and `re.fullmatch()` for whole-string matching.