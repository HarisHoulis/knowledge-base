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
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import feedparser
import requests
import trafilatura


# ── Config ────────────────────────────────────────────────────────

DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
DEEPSEEK_API_URL = os.environ.get("DEEPSEEK_API_URL", "https://api.deepseek.com/v1")
DEEPSEEK_MODEL   = os.environ.get("DEEPSEEK_MODEL", "deepseek-chat")

KB_PATH    = Path(os.environ.get("KB_PATH", str(Path.home() / "knowledge-base")))
STATE_PATH = Path(os.environ.get("KB_STATE", str(Path.home() / ".kb-pipeline" / "state.json")))

SOURCES = [
    {"id": "jake-wharton",     "type": "rss",  "url": "https://jakewharton.com/atom.xml"},
    {"id": "manuel-vivo",      "type": "rss",  "url": "https://medium.com/feed/@manuelvicnt"},
    {"id": "martin-fowler",    "type": "rss",  "url": "https://martinfowler.com/feed.atom"},
    {"id": "simon-willison",   "type": "rss",  "url": "https://simonwillison.net/atom/everything/"},
    {"id": "kent-beck",        "type": "rss",  "url": "https://kentbeck.substack.com/feed"},
    {"id": "charity-majors",   "type": "rss",  "url": "https://charity.wtf/feed/"},
    {"id": "gergely-orosz",    "type": "rss",  "url": "https://newsletter.pragmaticengineer.com/feed"},
    {"id": "john-ousterhout",  "type": "youtube", "channel": "UC_Stanford_CS190"},
    {"id": "matt-pocock",      "type": "youtube", "channel": "UC_mattpocockuk"},
]

DOMAINS = [
    "android-kotlin", "system-design", "python-backend",
    "ai-workflows", "engineering-culture",
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


# ── State ─────────────────────────────────────────────────────────

def load_state():
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text())
    return {"processed_hashes": []}


def save_state(state):
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2, default=str))


# ── Fetch ─────────────────────────────────────────────────────────

def fetch_rss(source):
    feed = feedparser.parse(source["url"])
    if feed.bozo and not feed.entries:
        print(f"  [!] RSS error ({source['id']}): {feed.bozo_exception}")
        return []
    return feed.entries


def fetch_youtube(source):
    channel = source.get("channel", "")
    if not channel:
        return []
    url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel}"
    feed = feedparser.parse(url)
    return feed.entries if not feed.bozo else []


def transcript_youtube(video_id):
    try:
        r = subprocess.run(
            ["yt-dlp", "--write-auto-subs", "--sub-lang", "en",
             "--skip-download", "--print", "subtitle",
             f"https://www.youtube.com/watch?v={video_id}"],
            capture_output=True, text=True, timeout=120,
        )
        return r.stdout.strip()
    except (FileNotFoundError, subprocess.TimeoutExpired) as e:
        print(f"  [!] yt-dlp failed for {video_id}: {e}")
        return ""


# ── Extract ───────────────────────────────────────────────────────

def extract_text(html):
    return trafilatura.extract(html, output_format="markdown", include_links=True) or ""


# ── LLM ───────────────────────────────────────────────────────────

def classify_summarize(text, meta):
    if not DEEPSEEK_API_KEY:
        print("  [!] DEEPSEEK_API_KEY not set, skipping LLM")
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
        return json.loads(r.json()["choices"][0]["message"]["content"])
    except Exception as e:
        print(f"  [!] LLM error: {e}")
        return None


# ── Write ─────────────────────────────────────────────────────────

def write_entry(data, source_url):
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
    print(f"  → {fp.relative_to(KB_PATH)}")


# ── Main ──────────────────────────────────────────────────────────

def main():
    dry_run = "--dry-run" in sys.argv
    limit = None
    for a in sys.argv:
        if a.startswith("--limit="):
            limit = int(a.split("=", 1)[1])

    print(f"[pipeline] {'dry-run' if dry_run else 'live'} — {datetime.now(timezone.utc).isoformat()}")
    state = load_state()
    processed = set(state["processed_hashes"])

    for src in SOURCES:
        print(f"\n[{src['id']}]")
        entries = fetch_rss(src) if src["type"] == "rss" else fetch_youtube(src)
        print(f"  {len(entries)} in feed")

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
                print(f"  ⏭ no content: {entry.get('title', '')[:60]}")
                continue

            text = extract_text(content)
            if not text or len(text) < 200:
                print(f"  ⏭ too short: {entry.get('title', '')[:60]}")
                continue

            result = classify_summarize(text, entry)
            if not result:
                continue

            if dry_run:
                print(f"  ✓ would write: {result.get('domain')}/{result.get('subdomain')}/{result.get('concept')}.md")
            else:
                write_entry(result, url)
                processed.add(h)
                state["processed_hashes"] = list(processed)
                save_state(state)

            count += 1
            time.sleep(0.5)

    print(f"\n{'[dry-run] no files written' if dry_run else '✓ done'}")


if __name__ == "__main__":
    main()
