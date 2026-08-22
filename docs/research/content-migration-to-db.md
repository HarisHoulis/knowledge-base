# Content Migration to the Canonical DB (kb_pipeline rework)

## Question

How does content get from all md files under `concepts/` into the canonical database — the current 731 files, plus any md files added to `concepts/` between now and cutover? This covers the migration path for existing files, the rework of `kb_pipeline` to write to the DB instead of the filesystem/git, what happens to the git md tree / `CONTEXT.md` / the daily-ingest PR flow, and superseding ADR-0001 with a new ADR.

Ticket: [Decide how content reaches the DB (migration + rework daily ingest, supersede ADR-0001)](https://github.com/HarisHoulis/knowledge-base/issues/127).

## Context (fixed constraints)

- DB is canonical; the app serves from the DB. Schema per #125: `domain`, `subdomain`, `concept`, `source`, `concept_source`, `concept_progress`; upserts keyed on natural keys make migration idempotent.
- Path `concepts/<domain>/<subdomain>/<concept>.md` → upsert domain, subdomain, concept. Frontmatter: YAML with `domain`/`subdomain`/`concept`/`title`/`sources` (list of `{title,url,author,date}`) + body + trailing takeaways bullets.
- Pipeline is reworked to write the DB directly, not through the API (#126: no ingestion-through-this-API).
- 17 empty `.gitkeep` dirs exist under `concepts/` and must not create concepts.
- Stack/schema settled in #122/#123/#125/#126; ingest-runner location still open (#128).

## Findings

### 1. How kb_pipeline works today

- `cli.py` (`main()`) → `pipeline.run_pipeline()` → per source: fetch (RSS/YouTube via `fetcher.py`), dedup on sha256 URL hash against `state.json` (`~/.kb-pipeline/state.json`, key `processed_hashes`), extract via trafilatura, classify/summarize via LLM (`llm.py`, `response_format: json_object`, validated by `validate_llm_output` against `VALID_DOMAINS`), write via `writer.write_entry`.
- `writer.py` is the only format authority and is **write-only**: `_render` emits frontmatter + `# title` + summary + trailing `- ` takeaway bullets. **No md parser exists anywhere** — nothing ever reads a concept file back.
- Audit (`--audit`, `audit.py`) applies only to freshly generated drafts, then `promote_draft` renames `drafts/…` → `concepts/…`. `state.json` is a fetch-side URL-hash cache only; it knows nothing about concepts/files, and dry-run never touches it.
- `daily-ingest.yml` (schedule `15 20 * * *`) → `scripts/daily-ingest.sh` runs the pipeline, then git-commits any changes, opens a PR on `daily-ingest/YYYY-MM-DD`, and auto-merges only if changed paths are `.md` under `concepts/` or `drafts/`; exits early when `git status` is clean.

### 2. Shape of the existing tree (verified across all 731 files)

- 5 domains (exactly `VALID_DOMAINS`), 516 subdomain dirs, 731 `.md`, 17 `.gitkeep` (12 pure placeholders, 5 mixed with `.md`).
- **Dead regular**: every file starts `---` with exactly the 5 keys `domain, subdomain, concept, title, sources` and no others; path === frontmatter in 0 mismatches; body is `# <title>` then paragraphs then trailing `- ` takeaways (0 files with 0 takeaways; counts 3–8).
- **Sources**: 770 blocks, 23 files with 2+ sources (max 5), 16 files with neither author nor date; 329 distinct URLs, 131 shared by 2+ concepts (top: a URL referenced 11×). Date formats are a mess (244 `YYYY-MM-DD`, 238 ISO-timestamps, 113 RFC822, 13 oddballs like bare year / `Jul 30` / `unknown`) — stored as text per #125, no normalization.
- **Irregularities that matter**:
  - 17 subdomain dirs contain spaces (e.g. `android-kotlin/dependency management/`). 8 slugified-collision groups once spaces→dashes+lowercase (e.g. `distributed transactions` vs `distributed-transactions`; `test-driven development` vs `test-driven-development`). Verbatim storage keeps them 8 distinct rows; slugification would conflate them.
  - 108 concept slugs repeat across subdomains (all distinct content, 0 identical md5s); no two files share the full `domain/subdomain/concept` key, so the composite UNIQUE is never violated.
  - 9 concept slugs contain dots (`qwen-3.8-27b.md`) — keep verbatim, don't regex-validate as kebab.

### 3. What a migration needs; parse logic must be written

- The md parser is the exact inverse of `writer._render` and **must be written new** (single function suffices — the format is uniform): strip frontmatter → read 5 keys + `sources[]` (author/date optional lines) → skip blank → `# title` (verify == frontmatter title) → summary = prose between H1 and the first trailing `- ` line → takeaways = remaining `- ` lines. No fallbacks needed for current data; only tolerance required is optional `author`/`date`.
- Natural CLI placement: `python -m kb_pipeline --migrate` (reusing `--dry-run`), consistent with ADR-0002's single-script rule, vs a separate `scripts/migrate-concepts.py`.
- **Fitness gate cost**: `scripts/check-fitness.py` runs on every PR against `scripts/baselines.json` (module set, inter-module import edges, per-module line budgets). `pipeline.py` is already exactly at its 359-line budget. Any new module (`db.py`), new edge (`pipeline → db`, `writer → db`), or line growth requires regenerating baselines as part of the migration work.

### 4. Cleanest seam: one shared upsert path

- The LLM output dict (`llm.py`: `domain/subdomain/concept/title/summary/key_points/sources`) and a parsed-file dict are the same shape modulo the bullets key (`key_points` vs `takeaways` — trivial mapping to the DB `takeaways text[]` column).
- A single `sync_concept()` — upsert domain → subdomain → concept → sources → `concept_source` (with `position` = source list index) on natural keys — serves both: the pipeline calls it after classification/audit; the migration calls it per file.
- **No obstacle in `state.py`** (fetch-side only; migration ignores and never writes it). **No obstacle in `audit.py`** (audit is for freshly generated drafts only; existing files already passed the gate when written — migration skips audit).
- **Idempotency mismatch is the only real seam**: filesystem writes are unconditional overwrites keyed on path; the DB needs `ON CONFLICT … DO UPDATE` on natural keys, plus a **deterministic source of UUIDs** (e.g. UUID5 over natural keys, or insert-only `gen_random_uuid()`) — otherwise re-runs churn `concept.id` and orphan `concept_progress`.

### 5. Idempotent-migration complications

1. Empty `.gitkeep` dirs: a file-driven `glob("**/*.md")` walk yields exactly the 731; a dir-driven walk would create 12 phantom empty subdomains. Rule: skip subdomain dirs with zero `.md` files.
2. No duplicate concept keys possible — path == natural key, 0 mismatches confirmed.
3. Frontmatter edge cases are minimal but real: optional author/date, 13 malformed dates, 9 dot-bearing slugs, 17 space-bearing subdomain dirs, 23 multi-source files.
4. `state.json` cache: persisted across CI runs by `actions/cache` (key `kb-state-v1`). Migration must ignore it (it hashes URLs, not paths). After the pipeline moves to DB writes, the cache keeps working for new content.
5. **`daily-ingest.sh` git gate breaks**: it auto-merges only `.md` under `concepts/`/`drafts/` and exits early when `git status` is clean — with the DB canonical, DB-only writes produce no git diff, so both the "skip PR" and "content-only PR" logic must be reworked (or the git/PR shell removed entirely per the #127 grill decision: DB-only, tree freezes).
6. `concept_progress` rows don't exist yet (no progress data in files) — but idempotent re-runs must not orphan progress if `concept.id` is regenerated; pin UUIDs to natural keys.

## Decision (from the #127 grill)

- **DB-only output after cutover**: the reworked pipeline writes concepts straight to the DB; no md files produced, no commit/PR; the `concepts/` tree freezes as a static archive (731 files, git history intact). `daily-ingest.yml` loses its git/PR shell.
- **Migration mechanism**: one shared upsert path — `sync_concept()` called by the pipeline after classification and by a new `python -m kb_pipeline --migrate` subcommand. Deterministic UUIDs (UUID5 over natural keys). File-driven `glob("**/*.md")` walk. Mechanical costs: regenerate `scripts/baselines.json`; delete/replace the `daily-ingest.sh` git gate.
- **Subdomain slugs**: direction = normalize, but the LLM-driven naming (17 space-dirs, 8 slugified collision groups, near-dupe families) needs its own decision **before the migration executes** — split to ticket [Decide how subdomain slugs are normalized (LLM-driven naming)](https://github.com/HarisHoulis/knowledge-base/issues/162), which blocks #127.
- **Paperwork**: new ADR (e.g. `0009-database-as-canonical-concept-store`) supersedes ADR-0001; `CONTEXT.md` glossary updated (Pipeline/Daily Ingest now DB-targeted); git history untouchable.

## Open / downstream

- Where the reworked ingest (and the one-shot `--migrate` run) executes — GH Actions vs host cron: ticket [Decide where daily ingest runs](https://github.com/HarisHoulis/knowledge-base/issues/128).
- Slugs: ticket [Decide how subdomain slugs are normalized](https://github.com/HarisHoulis/knowledge-base/issues/162).
