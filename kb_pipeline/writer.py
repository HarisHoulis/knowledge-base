import logging
from typing import Any

from .config import KB_PATH

logger = logging.getLogger(__name__)


def write_entry(data: dict[str, Any], source_url: str) -> None:
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

    fp = KB_PATH / domain / sub / f"{name}.md"
    fp.parent.mkdir(parents=True, exist_ok=True)
    fp.write_text(md)
    logger.info("  -> %s", fp.relative_to(KB_PATH))
