#!/usr/bin/env python3
"""fetch.py — automated knowledge-base ingestion.

Polls RSS feeds (trusted sources), extracts content,
classifies + summarizes via DeepSeek V4 Flash API,
and writes concepts as domain/subdomain/concept.md.

Usage:
  python3 fetch.py                     # live run
  python3 fetch.py --dry-run           # preview without writing
  python3 fetch.py --limit 3           # max entries per source
"""

import hashlib
import json
import logging
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional, Tuple

import feedparser
import requests
import trafilatura


# ── Config ────────────────────────────────────────────────────────

DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
DEEPSEEK_API_URL = os.environ.get("DEEPSEEK_API_URL", "https://api.deepseek.com/v1")
DEEPSEEK_MODEL   = os.environ.get("DEEPSEEK_MODEL", "deepseek-chat")

KB_PATH    = Path(os.environ.get("KB_PATH", str(Path.home() / "knowledge-base")))
STATE_PATH = Path(os.environ.get("KB_STATE", str(Path.home() / ".kb-pipeline" / "state.json")))

VALID_DOMAINS = {
    "android-kotlin", "system-design", "python-backend",
    "ai-workflows", "engineering-culture",
}

SOURCES: list[dict[str, Any]] = [
    {"id": "jake-wharton",     "type": "rss",  "url": "https://jakewharton.com/atom.xml"},
    {"id": "manuel-vivo",      "type": "rss",  "url": "https://medium.com/feed/@manuelvicnt"},
    {"id": "martin-fowler",    "type": "rss",  "url": "https://martinfowler.com/feed.atom"},
    {"id": "simon-willison",   "type": "rss",  "url": "https://simonwillison.net/atom/everything/"},
    {"id": "kent-beck",        "type": "rss",  "url": "https://kentbeck.substack.com/feed"},
    {"id": "charity-majors",   "type": "rss",  "url": "https://charity.wtf/feed/"},
    {"id": "gergely-orosz",    "type": "rss",  "url": "https://newsletter.pragmaticengineer.com/feed"},
    {"id": "matt-pocock",      "type": "youtube", "channel": "UCswG6FSbgZjbWtdf_hMLaow"},
    {"id": "mit-6.824",        "type": "youtube", "playlist": "PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB"},
]

SYSTEM_PROMPT = """You are a knowledge-base curator. Given an article or transcript, output a JSON object with:
- "domain": one of ["android-kotlin", "system-design", "python-backend", "ai-workflows", "engineering-culture"]
- "subdomain": a concise subdomain name
- "concept": short kebab-case identifier (e.g. "structured-concurrency")
- "title": human-readable title
- "summary": 2-4 paragraphs synthesizing the key ideas, with inline citations to the source
- "key_points": a list of 2-5 bullet-point takeaways
- "sources": list of {"title": str, "url": str, "author": str, "date": str}

Be concise. Strip fluff. Only include claims directly supported by the source text."""


# ── Logging ────────────────────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
)
logger = logging.getLogger(__name__)


# ── State ─────────────────────────────────────────────────────────

def load_state() -> dict[str, Any]:
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text())
    return {"processed_hashes": []}


def save_state(state: dict[str, Any]) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2, default=str))


# ── Fetch ─────────────────────────────────────────────────────────

def fetch_rss(source: dict[str, Any]) -> list[Any]:
    url = source["url"]
    headers = source.get("headers", {})
    if headers:
        try:
            r = requests.get(url, headers=headers, timeout=30)
            r.raise_for_status()
            feed = feedparser.parse(r.text)
        except requests.RequestException as e:
            logger.warning("  [!] RSS fetch error (%s): %s", source["id"], e)
            return []
    else:
        feed = feedparser.parse(url)
    if feed.bozo and not feed.entries:
        logger.warning("  [!] RSS parse error (%s): %s", source["id"], feed.bozo_exception)
        return []
    return feed.entries


def fetch_youtube(source: dict[str, Any]) -> list[Any]:
    pid = source.get("playlist", "")
    cid = source.get("channel", "")
    if pid:
        url = f"https://www.youtube.com/feeds/videos.xml?playlist_id={pid}"
    elif cid:
        url = f"https://www.youtube.com/feeds/videos.xml?channel_id={cid}"
    else:
        return []
    feed = feedparser.parse(url)
    return feed.entries if not feed.bozo else []


def transcript_youtube(video_id: str) -> str:
    try:
        r = subprocess.run(
            ["yt-dlp", "--write-auto-subs", "--sub-lang", "en",
             "--skip-download", "--print", "subtitle",
             f"https://www.youtube.com/watch?v={video_id}"],
            capture_output=True, text=True, timeout=120,
        )
        r.check_returncode()
        return r.stdout.strip()
    except (FileNotFoundError, subprocess.TimeoutExpired, subprocess.CalledProcessError) as e:
        logger.warning("  [!] yt-dlp failed for %s: %s", video_id, e)
        return ""


# ── Extract ───────────────────────────────────────────────────────

def extract_text(html: str) -> str:
    return trafilatura.extract(html, output_format="markdown", include_links=True) or ""


# ── LLM ───────────────────────────────────────────────────────────

def validate_llm_output(data: dict[str, Any]) -> list[str]:
    required = ["domain", "subdomain", "concept", "title", "summary", "key_points"]
    errors: list[str] = []
    for field in required:
        if field not in data:
            errors.append(f"missing '{field}'")
    if "domain" in data and data["domain"] not in VALID_DOMAINS:
        errors.append(f"invalid domain '{data['domain']}'")
    if "key_points" in data and not isinstance(data["key_points"], list):
        errors.append("'key_points' must be a list")
    return errors


def classify_summarize(text: str, meta: dict[str, Any]) -> Optional[dict[str, Any]]:
    if not DEEPSEEK_API_KEY:
        logger.warning("  [!] DEEPSEEK_API_KEY not set, skipping LLM")
        return None

    prompt = (
        f"Title: {meta.get('title', '')}\n"
        f"Author: {meta.get('author', '')}\n"
        f"URL: {meta.get('link', '')}\n"
        f"Date: {meta.get('published', '')}\n\n"
        f"---\n\n{text[:15000]}"
    )
    try:
        r = requests.post(
            f"{DEEPSEEK_API_URL}/chat/completions",
            headers={"Authorization": f"Bearer {DEEPSEEK_API_KEY}"},
            json={
                "model": DEEPSEEK_MODEL,
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt},
                ],
                "response_format": {"type": "json_object"},
                "temperature": 0.3,
                "max_tokens": 2000,
            },
            timeout=60,
        )
        r.raise_for_status()
        body = r.json()
        content = body["choices"][0]["message"]["content"]
        data = json.loads(content)
        errors = validate_llm_output(data)
        if errors:
            logger.warning("  [!] LLM output validation failed: %s", "; ".join(errors))
            return None
        return data
    except requests.RequestException as e:
        logger.warning("  [!] LLM request failed: %s", e)
    except (json.JSONDecodeError, KeyError, IndexError, TypeError) as e:
        logger.warning("  [!] LLM response parse failed: %s", e)
    return None


# ── Write ─────────────────────────────────────────────────────────

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


# ── CLI ──────────────────────────────────────────────────────────

def parse_args() -> Tuple[bool, Optional[int]]:
    dry_run = "--dry-run" in sys.argv
    limit: Optional[int] = None
    for a in sys.argv:
        if a.startswith("--limit="):
            limit = int(a.split("=", 1)[1])
    return dry_run, limit


# ── Main ──────────────────────────────────────────────────────────

def main() -> None:
    dry_run, limit = parse_args()

    logger.info("[pipeline] %s — %s", "dry-run" if dry_run else "live", datetime.now(timezone.utc).isoformat())
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

    state["processed_hashes"] = list(processed)
    save_state(state)
    logger.info("%s", "[dry-run] no files written" if dry_run else "done")


if __name__ == "__main__":
    main()
