import hashlib
import logging
import sys
import time
from datetime import datetime, timezone
from typing import Optional, Tuple

from .config import SOURCES
from .state import load_state, save_state
from .fetcher import fetch_rss, fetch_youtube, extract_text
from .llm import classify_summarize
from .writer import write_entry

logger = logging.getLogger(__name__)


def parse_args() -> Tuple[bool, Optional[int]]:
    dry_run = "--dry-run" in sys.argv
    limit: Optional[int] = None
    for a in sys.argv:
        if a.startswith("--limit="):
            limit = int(a.split("=", 1)[1])
    return dry_run, limit


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    dry_run, limit = parse_args()

    logger.info("[pipeline] %s - %s", "dry-run" if dry_run else "live", datetime.now(timezone.utc).isoformat())
    state = load_state()
    processed: set[str] = set(state["processed_hashes"])

    for src in SOURCES:
        logger.info("[%s]", src["id"])
        entries = fetch_rss(src) if src["type"] == "rss" else fetch_youtube(src)
        logger.info("  %d in feed", len(entries))

        count = 0
        for entry in entries:
            if limit and count >= limit:
                break

            url = entry.get("link", "")
            h = hashlib.sha256(url.encode()).hexdigest()[:16]
            if h in processed:
                continue

            content = ""
            if entry.get("content"):
                content = entry["content"][0].get("value", "")
            if not content:
                content = entry.get("summary", "")
            if not content:
                logger.info("  skipping (no content): %s", entry.get("title", "")[:60])
                continue

            text = extract_text(content)
            if not text or len(text) < 200:
                logger.info("  skipping (too short): %s", entry.get("title", "")[:60])
                continue

            result = classify_summarize(text, entry)
            if not result:
                continue

            if dry_run:
                logger.info("  would write: %s/%s/%s.md", result.get("domain"), result.get("subdomain"), result.get("concept"))
            else:
                write_entry(result, url)
                processed.add(h)

            count += 1
            time.sleep(0.5)

    if not dry_run:
        state["processed_hashes"] = list(processed)
        save_state(state)
    logger.info("%s", "[dry-run] no files written" if dry_run else "done")
