---
domain: python-backend
subdomain: sqlite-storage
concept: compressed-text-history
title: SQLite compressed text-history prototypes
sources:
  - title: "SQLite compressed text-history prototypes"
    url: "https://simonwillison.net/2026/Aug/9/sqlite-text-history-prototype/#atom-everything"
    date: "2026-08-09"
---

# SQLite compressed text-history prototypes

Simon Willison explores a novel approach to storing revision histories in SQLite: keeping the full text of every prior version in a JSON array, then compressing that array with zlib or Zstandard. The idea is that repeated strings across versions compress extremely well, avoiding the need for a separate row per edit. Prototypes with Python and GPT-5.6 Sol Pro demonstrated that 1,000 simulated revisions totaling 20.4 MB of raw text compressed to just 80.3 KB when stored as a Zstandard-compressed JSON array (source).

To avoid decompressing and recompressing the entire array on every edit, the prototype breaks history into multiple rows, each containing at most 128 revisions or 3 MB of uncompressed JSON. This chunking minimizes overhead and makes the scheme practical for constantly edited documents. The approach is presented as a promising alternative to traditional row-per-version storage, leveraging modern compression algorithms to handle redundant text efficiently.

- Store all prior versions of a document as a JSON array of strings in a SQLite BLOB column, compressed with zlib or Zstandard.
- Compression exploits redundancy across versions: 20.4 MB of raw revision text compressed to 80.3 KB using Zstandard.
- Use a separate uncompressed JSON array of Unix timestamps to track edit times.
- Break history into multiple rows (e.g., max 128 revisions or 3 MB uncompressed) to avoid rewriting the entire compressed array on each edit.