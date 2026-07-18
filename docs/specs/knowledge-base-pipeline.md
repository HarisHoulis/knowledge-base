# Knowledge Base Pipeline

## Problem Statement

A senior mobile tech lead needs to future-proof himself against the AI-driven reduction in engineering headcount by building a high-signal, low-noise knowledge base. He manually consumes content from 9 trusted sources but has no system to capture, organize, or retrieve the signal. The existing approach (read in Substack/YouTube, lose the insight) creates anxiety and wasted repetition.

## Solution

An automated pipeline (`kb_pipeline`) that polls RSS feeds from 9 trusted individuals daily, extracts article text, classifies and summarizes each piece via DeepSeek V4 Flash API into a `domain/subdomain/concept.md` concept, writes it to a local directory tree, and git-commits to a private GitHub repo. The user consumes the output as a reference library + weekly digest.

## User Stories

1. As a knowledge worker, I want the pipeline to fetch new content from my trusted sources daily, so that I don't have to manually check each site.
2. As a knowledge worker, I want the AI to classify content into the correct `domain/subdomain`, so that entries land in the right place in the tree without manual filing.
3. As a knowledge worker, I want the AI to produce a concise summary with key points and source citations, so that I can skim in <5 min per entry.
4. As a knowledge worker, I want duplicate entries detected by source URL, so that processing the same article twice produces one entry.
5. As a consumer, I want a `--dry-run` mode, so that I can preview what the pipeline would write before committing.
6. As a consumer, I want a `--limit=N` flag, so that I can cap per-source processing during testing.
7. As a consumer, I want the pipeline to skip low-content entries (extracted text <200 chars), so that trivial posts don't clutter the KB.
8. As a consumer, I want the pipeline to run via cron automatically, so that the KB stays current without manual triggers.
9. As a reviewer, I want an audit subagent (future) to verify factual accuracy and correct placement of generated entries before I trust the pipeline fully.

## Implementation Decisions

- **Pipeline architecture**: Multi-module Python package `kb_pipeline`. No external orchestrator (n8n/Make.com). No database — filesystem tree is the store.
- **Content retrieval**: RSS polling via `feedparser` for all blog/Substack sources. YouTube RSS for video channels (Ousterhout, Matt Pocock). Transcripts via `yt-dlp --write-auto-subs`.
- **Text extraction**: `trafilatura` with markdown output. Falls back to raw summary text if no HTML content available.
- **LLM classification + summarization**: DeepSeek V4 Flash via OpenAI-compatible API. Single prompt requesting JSON output with `response_format: {"type": "json_object"}`. Temperature 0.3 for consistent classification. Max 2000 output tokens.
- **State management**: `~/.kb-pipeline/state.json` — tracks `processed_hashes[]` (SHA-256[:16] of source URL). Prevents re-processing.
- **Deduplication**: By source URL hash. No embedding-based fuzzy matching (overkill for this volume).
- **Entry format**: YAML frontmatter (domain, subdomain, concept, title, sources[]) + summary body + key points list.
- **File naming**: `{concept}.md` where `concept` is a kebab-case identifier from the LLM.
- **Git workflow**: No auto-commit in the pipeline. User's cron wraps: `python -m kb_pipeline && cd kb_path && git add -A && git commit -m "feat(kb): daily ingest"`.
- **Entry limit**: `--limit=N` flag caps per-source processing. First run will backfill all existing RSS entries (capped if limit set).
- **No RAG / vector DB**: Filesystem tree is the canonical store. Search is via `grep` or file browser.

## Testing Decisions

- **Seam**: Integration test with `--dry-run` mode. One test feeds a known RSS fixture to `kb_pipeline` and asserts correct JSON output without writing files.
- **Good test**: Feeds a real RSS XML file as input, verifies the LLM returns valid JSON with expected fields, verifies no files are written under `--dry-run`. Does not mock the LLM (the API integration is the core value).
- **Prior art**: None in repo (greenfield). Test lives at `tests/test_pipeline.py`.
- **What NOT to test**: Pure helper functions (`extract_text`, `entry_path` — too simple to break). LLM prompt quality (tested implicitly by dry-run output). Cron/git setup (system config, not code).

## Out of Scope

- Audit subagent (separate session)
- Backfill of existing material (cold start)
- Perplexity Spaces / Claude Projects integration
- Vector DB / semantic search
- Web UI for the KB
- Multi-user / team sharing
- Mobile consumption interface

## Further Notes

- Sources whose RSS feeds are behind login walls may require cookies or session tokens in the HTTP request. `feedparser` may need custom headers for some feeds. If a source consistently fails, the user should check with `curl -I <feed_url>` to see if auth is required.
- YouTube channel IDs for Ousterhout (Stanford CS190) and Matt Pocock need to be resolved and hardcoded. The current placeholder IDs will produce no results.
- The first run will process all existing RSS entries (typically 10-20 per feed). Set `--limit=3` for a lighter first test.
