# Knowledge Base

A curated repository of high-signal concepts synthesized from trusted sources, organized as a browsable directory tree.

## Language

**Concept**:
A single, tightly-scoped idea captured in one markdown file at `domain/subdomain/concept.md`.
_Avoid_: Entry, leaf-node entry, knowledge item

**Domain**:
A category of engineering knowledge, stored under `concepts/`. One of `android-kotlin`, `system-design`, `python-backend`, `ai-workflows`, `engineering-culture`.

**Subdomain**:
A sub-category within a domain. Examples: `architecture`, `coroutines`, `fastapi`, `coding-agents`.

**Trusted Source**:
An individual or publication whose content is auto-ingested regardless of medium. All other sources must pass the audit gate.
_Avoid_: Tier 1, auto-include source

**Pipeline**:
The automated process that fetches content from trusted sources, classifies it into a domain/subdomain/concept, writes a concept file, and runs audit checks. Does not interact with git — the scheduler handles version control.

**Daily Ingest**:
A scheduled GitHub Actions workflow that runs the pipeline on a timer (06:00 UTC), creates a feature branch with any new/changed concept files, and opens a pull request for review. Skips the PR entirely if no new content was found.
_Avoid_: Cron job, launchd job, scheduled task

**Weekly Digest**:
A recurring 30-minute review of newly added concepts.

**State**:
Persistent tracking of which source URLs have already been processed, stored outside the KB tree.
_Avoid_: Processed hashes

**Cold Start**:
The decision to begin ingesting from today only, without backfilling historical content from trusted sources.

**Audit**:
A post-ingestion review of a concept entry, split into two independent passes:
- **Classification Audit** — verifies the assigned domain/subdomain/concept is correct.
- **Content Audit** — verifies the summary body accurately reflects the source text.
_Avoid_: Review, verification pass

**Draft**:
A concept file that has passed LLM generation but not yet cleared audit. Stored under `drafts/` in the KB tree. Moved into `domain/subdomain/concept.md` only after both audits pass.

**Audit Loop**:
The retry cycle: audit fails → surgical feedback to LLM → regenerate (up to 2 iterations). If still failing after max retries, the pipeline halts and notifies the user.

**Auth Cookie**:
A browser session cookie required to access paywalled or authenticated content (e.g., Substack paid posts). Stored as an environment variable and referenced by `Source.cookie_env_var`. Validated at pipeline startup; if missing or expired, the pipeline files a GitHub issue and aborts.

## Trusted Sources

| Person | Domain | Primary Channel |
|---|---|---|
| Jake Wharton | Android / Kotlin | Blog |
| Manuel Vivo | Android / Compose | Blog, Medium |
| Martin Fowler | System Design | Blog |
| MIT | Distributed Systems | MIT 6.824 (YouTube) |
| Simon Willison | AI Workflows | Blog |
| Kent Beck | AI + Software Design | Substack |
| Charity Majors | Engineering Culture | Blog |
| Gergely Orosz | Engineering Culture | Substack |
| ByteByteGo | System Design | Substack |
| Matt Pocock | TypeScript | Newsletter, YouTube |
