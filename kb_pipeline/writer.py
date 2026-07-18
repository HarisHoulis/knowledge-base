import logging
from pathlib import Path
from typing import Any

from .config import CONCEPTS_DIR, DRAFTS_DIR, KB_PATH

logger = logging.getLogger(__name__)


def _render(data: dict[str, Any], source_url: str) -> tuple[str, str, str, str]:
    domain = data.get("domain", "uncategorized")
    sub    = data.get("subdomain", "misc")
    name   = data.get("concept", "untitled")
    title  = data.get("title", name)

    sources = data.get("sources") or [{"title": title, "url": source_url}]
    summary = data.get("summary", "")
    points  = data.get("key_points", [])

    md = "---\n"
    for k in ("domain", "subdomain", "concept", "title"):
        md += f"{k}: {data.get(k, '')}\n"
    md += "sources:\n"
    for s in sources:
        md += f'  - title: "{s.get("title", "")}"\n'
        md += f'    url: "{s.get("url", "")}"\n'
        if s.get("author"):
            md += f'    author: "{s["author"]}"\n'
        if s.get("date"):
            md += f'    date: "{s["date"]}"\n'
    md += "---\n\n"
    md += f"# {title}\n\n{summary}\n"
    for pt in points:
        md += f"\n- {pt}"

    return domain, sub, name, md


def _write_to(base: str, data: dict[str, Any], source_url: str) -> Path:
    domain, sub, name, md = _render(data, source_url)
    fp = KB_PATH / base / domain / sub / f"{name}.md"
    fp.parent.mkdir(parents=True, exist_ok=True)
    fp.write_text(md)
    logger.info("  -> %s", fp.relative_to(KB_PATH))
    return fp


def write_entry(data: dict[str, Any], source_url: str) -> None:
    _write_to(CONCEPTS_DIR, data, source_url)


def write_draft(data: dict[str, Any], source_url: str) -> Path:
    return _write_to(DRAFTS_DIR, data, source_url)


def promote_draft(draft_path: Path) -> None:
    relative = draft_path.relative_to(KB_PATH / DRAFTS_DIR)
    target = KB_PATH / CONCEPTS_DIR / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    draft_path.rename(target)
    logger.info("  promoted -> %s", target.relative_to(KB_PATH))

    for parent in [draft_path.parent, draft_path.parent.parent, draft_path.parent.parent.parent]:
        try:
            if parent != KB_PATH / DRAFTS_DIR and not any(parent.iterdir()):
                parent.rmdir()
        except OSError:
            pass
