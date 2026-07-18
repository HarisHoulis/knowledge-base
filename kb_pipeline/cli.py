import logging
import sys
from datetime import datetime, timezone
from typing import Optional, Tuple

from .pipeline import run_pipeline

logger = logging.getLogger(__name__)


def parse_args() -> Tuple[bool, Optional[int], bool]:
    dry_run = "--dry-run" in sys.argv
    audit = "--audit" in sys.argv
    limit: Optional[int] = None
    for a in sys.argv:
        if a.startswith("--limit="):
            limit = int(a.split("=", 1)[1])
    return dry_run, limit, audit


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    dry_run, limit, audit = parse_args()

    logger.info("[pipeline] %s - %s", "dry-run" if dry_run else "live", datetime.now(timezone.utc).isoformat())

    stats = run_pipeline(dry_run=dry_run, limit=limit, audit=audit)

    logger.info("done  %d sources, %d seen, %d written, %d skipped",
                stats["sources"], stats["seen"], stats["written"], stats["skipped"])
