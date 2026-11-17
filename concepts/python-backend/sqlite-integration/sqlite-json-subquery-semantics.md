---
domain: python-backend
subdomain: sqlite-integration
concept: sqlite-json-subquery-semantics
title: LLM 0.37.3: SQLite 3.54.1 JSON Subquery Behavior Change
sources:
  - title: "llm 0.37.3"
    url: "https://simonwillison.net/2026/Nov/16/llm/"
    author: "Simon Willison"
    date: "2026-11-16"
---

# LLM 0.37.3: SQLite 3.54.1 JSON Subquery Behavior Change

LLM 0.37.3 is a bug-fix release addressing a breakage introduced by Homebrew shipping SQLite 3.54.1. The new SQLite version includes a fix that changed how nested JSON subqueries are handled, which broke LLM's logging code (per the release notes).

The behavioral difference: in SQLite 3.54.0, `select json_object('a', (select json_array(1)))` returned `{"a":[1]}`, but in 3.54.1 the same query returns `{"a":"[1]"}`. According to D. Richard Hipp, this is a correction rather than a regression: per the documentation, `(SELECT json_array(...))` returns SQL text, not JSON, so 3.54.1's behavior is correct and 3.54.0 was buggy.

The workaround is to wrap the subquery in `json()`, e.g. `select json_object('a', json((select json_array(1))))`, which restores the intended nested-JSON output.

- SQLite 3.54.1 changed how JSON subqueries are interpreted, breaking LLM's logging code
- Subquery results are SQL text, not JSON, per SQLite docs; 3.54.1 is the correct behavior
- Wrapping the subquery in json() restores nested JSON output