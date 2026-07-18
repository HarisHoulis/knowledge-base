import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
DEEPSEEK_API_URL = os.environ.get("DEEPSEEK_API_URL", "https://api.deepseek.com/v1")
DEEPSEEK_MODEL   = os.environ.get("DEEPSEEK_MODEL", "deepseek-chat")

KB_PATH    = Path(os.environ.get("KB_PATH", str(Path.home() / "knowledge-base")))
STATE_PATH = Path(os.environ.get("KB_STATE", str(Path.home() / ".kb-pipeline" / "state.json")))

CONCEPTS_DIR = "concepts"
DRAFTS_DIR = "drafts"

VALID_DOMAINS = {
    "android-kotlin", "system-design", "python-backend",
    "ai-workflows", "engineering-culture",
}


@dataclass
class Source:
    id: str
    type: Literal["rss", "youtube"]
    url: str = ""
    channel: str = ""
    playlist: str = ""
    headers: dict[str, str] = field(default_factory=dict)


SOURCES: list[Source] = [
    Source(id="jake-wharton",     type="rss",  url="https://jakewharton.com/atom.xml"),
    Source(id="manuel-vivo",      type="rss",  url="https://medium.com/feed/@manuelvicnt"),
    Source(id="martin-fowler",    type="rss",  url="https://martinfowler.com/feed.atom"),
    Source(id="simon-willison",   type="rss",  url="https://simonwillison.net/atom/everything/"),
    Source(id="kent-beck",        type="rss",  url="https://kentbeck.substack.com/feed"),
    Source(id="charity-majors",   type="rss",  url="https://charity.wtf/feed/"),
    Source(id="gergely-orosz",    type="rss",  url="https://newsletter.pragmaticengineer.com/feed"),
    Source(id="matt-pocock",      type="youtube", channel="UCswG6FSbgZjbWtdf_hMLaow"),
    Source(id="john-ousterhout",  type="youtube", playlist="PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB"),
    Source(id="gilded-rose",      type="youtube", playlist="PL1ssMPpyqociJNwykAOB9_KEZVW7BW7m2"),
    Source(id="ai-engineer",      type="youtube", channel="UCLKPca3kwwd-B59HNr-_lvA"),
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
