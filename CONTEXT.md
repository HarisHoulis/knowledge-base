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
A scheduled GitHub Actions workflow that runs the pipeline on a timer (06:00 UTC), creates a feature branch with any new/changed concept files, and opens a pull request. When the PR contains only content (`.md` under `concepts/` or `drafts/`) it enables squash auto-merge, so it lands once CI is green; a PR touching any non-content or non-`.md` path is left open with a comment listing the offending paths. Skips the PR entirely if no new content was found.
_Avoid_: Cron job, launchd job, scheduled task

**Weekly Digest**:
A recurring 30-minute review of newly added concepts.

**Workflow Proposal**:
A markdown file under `docs/workflow-proposals/` capturing an agent's intended changes to `.github/workflows/*` as a unified diff. Committed to the agent's PR but never applied by the agent — the run token lacks `workflows` permission. A human applies the diff manually after review.
_Avoid_: Workflow suggestion, proposed workflow change

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
A browser session cookie required to access paywalled or authenticated content (e.g., Substack paid posts). Stored as an environment variable and referenced by `Source.cookie_env_var`. Validated at pipeline startup; if missing, the pipeline files a GitHub issue and skips only that source — all other sources continue. If a fetch returns empty despite a passing check (expired mid-run), the pipeline files a similar issue and aborts that source's entries for the run.

**YouTube Cookie**:
A Netscape-format cookie file from a dedicated throwaway YouTube account, required by yt-dlp to bypass IP-based bot detection from GitHub Actions cloud IPs. Stored as a base64-encoded GitHub secret (`YOUTUBE_COOKIES`), decoded at runtime to `/tmp/yt-cookies.txt`. Distinct from **Auth Cookie** — this is for the ingest subprocess tooling, not for source-level content access.

**Content Extraction Error**:
A failure to extract article text from fetched content. Two distinct types:
- **Exception** — extraction raised (e.g., malformed HTML that breaks the extractor).
- **Silent empty result** — extraction returned no text (e.g., paywalled, JS-rendered, or malformed pages), so the entry is dropped without an error being raised.

All errors collected during a single Pipeline run are surfaced as one cumulative GitHub issue, so the operator can triage failing Sources in one place.

## Agent Triage

**ready-for-agent**:
An open, unassigned issue that the automated agent is permitted to claim and implement. The canonical state for claimable work.
_Avoid_: unblocked, todo

**in-progress**:
An issue that an agent run has claimed by atomically replacing its labels with this one. An issue in this state is not claimable — the triage script skips it.

**needs-triage**:
Applied to an issue when the agent failed to implement it. Signals a human must act.

**Claimability gate**:
The predicate an issue must satisfy for the triage script to pick it: open, unassigned, unblocked, and labeled `ready-for-agent`. Applied to both top-level candidates and sub-issues.

**Viable candidate**:
An issue that passes the **Claimability gate**.

**Parent / Sub-issue**:
A GitHub parent issue and its native sub-issues. A parent with sub-issues is never implemented directly by the agent — it descends into sub-issues and claims the first claimable one. If none are claimable, the parent is skipped.

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
