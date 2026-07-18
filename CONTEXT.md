# Knowledge Base — Glossary

## Domain Structure

The KB organizes concepts in a three-level tree: `domain/subdomain/concept.md`.

### Domains and Subdomains

| Domain | Subdomains | Scope |
|---|---|---|
| `android-kotlin` | `architecture`, `coroutines`, `compose`, `build-tooling` | Android app development, Kotlin idioms, tooling |
| `system-design` | `complexity`, `ddd`, `microservices` | Software architecture principles, trade-offs, patterns |
| `python-backend` | `fastapi`, `async-python`, `service-patterns` | Python BE services (the team's expansion area) |
| `ai-workflows` | `coding-agents`, `local-models`, `mcp`, `prompt-engineering` | AI-assisted development, agent configs, local/cloud LLM |
| `engineering-culture` | `observability`, `team-dynamics`, `incident-management` | Engineering org practices, reducing headcount adaptation |

### Leaf-Node Entry

A `concept.md` file captures one tightly-scoped idea. Format: YAML frontmatter (domain, subdomain, concept, sources list) followed by a concise summary with inline citations.

## Trusted Sources (Auto-Include)

Tier 1 — auto-ingested regardless of medium. All others must pass the audit gate.

| Person | Domain | Primary Channel | Feed |
|---|---|---|---|
| Jake Wharton | Android/Kotlin | Blog | `jakewharton.com/atom.xml` |
| Manuel Vivo | Android/Compose | Blog, Medium | `medium.com/feed/@manuelvicnt` |
| Martin Fowler | System Design | Blog | `martinfowler.com/feed.atom` |
| John Ousterhout | Software Design | Stanford CS190 (YouTube) | YouTube channel RSS |
| Simon Willison | AI Workflows | Blog | `simonwillison.net/atom/everything/` |
| Kent Beck | AI + Software Design | Substack | `kentbeck.substack.com/feed` |
| Charity Majors | Engineering Culture | Blog | `charity.wtf/feed/` |
| Gergely Orosz | Engineering Culture | Substack | `newsletter.pragmaticengineer.com/feed` |
| Matt Pocock | TypeScript | Newsletter, YouTube | YouTube RSS |

## Pipeline

- `fetch.py` — single Python script, runs daily via cron
- RSS polling via `feedparser`, YouTube transcripts via `yt-dlp`
- Text extraction via `trafilatura`
- Classification + summarization via DeepSeek V4 Flash API (OpenAI-compatible)
- Output: `domain/subdomain/concept.md` with YAML frontmatter
- Dedup by source URL hash
- State tracked in `~/.kb-pipeline/state.json`
- Storage: private GitHub repo, auto-committed

## Consumption Model

- **Reference library** — search/browse by domain tree
- **Weekly digest** — skim new entries during a recurring 30-min slot

## Architecture Decisions

See `docs/adr/` for decisions that are hard to reverse, surprising without context, or the result of a real trade-off.
