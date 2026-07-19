import hashlib
import logging
import re
import subprocess
import time
from pathlib import Path
from typing import Any, Callable, Optional

from .config import SOURCES, Source
from .state import load_state, save_state
from .fetcher import fetch_rss, fetch_youtube, extract_text, transcript_youtube
from .llm import classify_summarize
from .writer import write_draft, write_entry, promote_draft
from .audit import classification_audit, content_audit, AuditResult

logger = logging.getLogger(__name__)


MAX_RETRIES = 2


def _build_audit_feedback_text(
    audit_results: list[tuple[str, AuditResult]],
) -> str:
    lines: list[str] = []
    for audit_name, result in audit_results:
        issues = result.get("issues", [])
        if issues:
            lines.append(f"[{audit_name}]")
            for issue in issues:
                field = issue.get("field", "?")
                desc = issue.get("description", "?")
                lines.append(f"- {field}: {desc}")
            lines.append("")
    return "\n".join(lines).strip()


def _escalate_failure(url: str, entry_path: Path, feedback: str) -> None:
    title = f"Audit exhaustion: {entry_path.name}"
    body = (
        f"## Pipeline halted — audit retries exhausted\n\n"
        f"- **Entry path:** `{entry_path}`\n"
        f"- **URL:** {url}\n\n"
        f"### Combined audit feedback\n\n```\n{feedback}\n```"
    )
    try:
        subprocess.run(
            ["gh", "issue", "create", "--title", title, "--body", body],
            capture_output=True,
            text=True,
            check=True,
            timeout=30,
        )
        logger.info("  escalation issue created for %s", entry_path)
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        logger.warning("  escalation failed: %s", e)


def _extract_youtube_video_id(url: str) -> Optional[str]:
    m = re.search(r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})", url)
    return m.group(1) if m else None


def _audit_with_retry(
    result: dict[str, Any],
    source_text: str,
    url: str,
    meta: dict[str, Any],
    draft_path: Path,
    *,
    classify_fn: Callable[..., Optional[dict[str, Any]]] = classify_summarize,
    ca_audit_fn: Callable[..., AuditResult] = classification_audit,
    co_audit_fn: Callable[..., AuditResult] = content_audit,
    promote_fn: Callable[[Path], None] = promote_draft,
    escalation_fn: Callable[[str, Path, str], None] = _escalate_failure,
) -> bool:
    ca_passed = False
    co_passed = False
    combined_feedback: list[tuple[str, AuditResult]] = []

    for retry in range(MAX_RETRIES + 1):
        if retry > 0:
            feedback_text = _build_audit_feedback_text(combined_feedback)
            if feedback_text:
                new_result = classify_fn(source_text, meta, audit_feedback=feedback_text)
                if new_result:
                    result = new_result

        if not ca_passed:
            ca_result = ca_audit_fn(result, source_text)
            ca_passed = ca_result.get("pass", False)
        if not co_passed:
            co_result = co_audit_fn(result, source_text)
            co_passed = co_result.get("pass", False)

        if ca_passed and co_passed:
            promote_fn(draft_path)
            return True

        failing: list[tuple[str, AuditResult]] = []
        if not ca_passed:
            failing.append(("Classification", ca_result if ca_result is not None else {"pass": False}))
        if not co_passed:
            failing.append(("Content", co_result if co_result is not None else {"pass": False}))
        combined_feedback = failing

        if retry < MAX_RETRIES:
            logger.info("  retry %d/%d: %d audit(s) failing", retry + 1, MAX_RETRIES, len(failing))

    logger.warning("  audit exhausted after %d retries for %s", MAX_RETRIES, url)

    all_feedback = _build_audit_feedback_text(combined_feedback)
    escalation_fn(url, draft_path, all_feedback)
    return False


def run_pipeline(
    dry_run: bool = False,
    limit: Optional[int] = None,
    audit: bool = False,
    sources: Optional[list[Source]] = None,
    *,
    transcript_fn: Callable[[str], str] = transcript_youtube,
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

            text = ""
            if src.type == "youtube":
                video_id = _extract_youtube_video_id(url)
                if video_id:
                    text = transcript_fn(video_id)

            if not text:
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
                ok = _audit_with_retry(result, text, url, entry, draft_path)
                if not ok:
                    logger.warning("  audit exhausted for %s", url)
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
