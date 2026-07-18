import hashlib
import logging
import time
from typing import Optional

from .config import SOURCES, Source
from .state import load_state, save_state
from .fetcher import fetch_rss, fetch_youtube, extract_text
from .llm import classify_summarize
from .writer import write_draft, write_entry, promote_draft
from .audit import classification_audit, content_audit

logger = logging.getLogger(__name__)


def run_pipeline(
    dry_run: bool = False,
    limit: Optional[int] = None,
    audit: bool = False,
    sources: Optional[list[Source]] = None,
) -> dict[str, int]:
    sources = sources or SOURCES
    state = load_state()
    processed: set[str] = set(state["processed_hashes"])
    stats = {"sources": 0, "seen": 0, "written": 0, "skipped": 0}

    for src in sources:
        logger.info("[%s]", src.id)
        entries = fetch_rss(src) if src.type == "rss" else fetch_youtube(src)
        logger.info("  %d in feed", len(entries))
        stats["sources"] += 1

        count = 0
        for entry in entries:
            if limit and count >= limit:
                break
            stats["seen"] += 1

            url = entry.get("link", "")
            h = hashlib.sha256(url.encode()).hexdigest()[:16]
            if h in processed:
                stats["skipped"] += 1
                continue

            content = ""
            if entry.get("content"):
                content = entry["content"][0].get("value", "")
            if not content:
                content = entry.get("summary", "")
            if not content:
                logger.info("  skipping (no content): %s", entry.get("title", "")[:60])
                stats["skipped"] += 1
                continue

            text = extract_text(content)
            if not text or len(text) < 200:
                logger.info("  skipping (too short): %s", entry.get("title", "")[:60])
                stats["skipped"] += 1
                continue

            result = classify_summarize(text, entry)
            if not result:
                stats["skipped"] += 1
                continue

            if dry_run:
                logger.info("  would write: %s/%s/%s.md", result.get("domain"), result.get("subdomain"), result.get("concept"))
                if audit:
                    logger.info("  would audit and promote to concepts/%s/%s/%s.md", result.get("domain"), result.get("subdomain"), result.get("concept"))
            elif audit:
                draft_path = write_draft(result, url)
                ca_result = classification_audit(result, text)
                co_result = content_audit(result, text)
                if ca_result.get("pass") and co_result.get("pass"):
                    promote_draft(draft_path)
                else:
                    logger.warning("  audit failed: classification=%s content=%s", ca_result.get("pass"), co_result.get("pass"))
            else:
                write_entry(result, url)

            if not dry_run:
                processed.add(h)

            stats["written"] += 1
            count += 1
            time.sleep(0.5)

    if not dry_run:
        state["processed_hashes"] = list(processed)
        save_state(state)

    return stats
