import os
from pathlib import Path
from typing import Any

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
