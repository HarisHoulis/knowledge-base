# ADR 0001: Filesystem Tree over Vector DB / Database

The KB stores concepts as markdown files in a `domain/subdomain/concept.md` directory tree rather than in a SQL database, vector DB, or RAG system. Search is via `grep`, file browser, or future lightweight tooling.

A database would enable schema enforcement, metadata queries, semantic search, and multi-user access. But for a single-user personal KB with <300 concepts/year, a filesystem tree is zero-infrastructure, trivially portable, diffable in git, editable with any text editor, and has no migration cost when the schema changes (the schema is just the file path). The moment the KB outgrows the filesystem (unlikely at this scale) is the right time to introduce a database — not before.
