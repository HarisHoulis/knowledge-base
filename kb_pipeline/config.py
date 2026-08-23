import json
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

LLM_API_KEY = os.environ.get("LLM_API_KEY", "")
LLM_API_URL = os.environ.get("LLM_API_URL", "")
LLM_MODEL = os.environ.get("LLM_MODEL", "")

KB_PATH = Path(os.environ.get("KB_PATH", str(Path.home() / "knowledge-base")))
STATE_PATH = Path(
    os.environ.get("KB_STATE", str(Path.home() / ".kb-pipeline" / "state.json"))
)

CONCEPTS_DIR = "concepts"
DRAFTS_DIR = "drafts"

VALID_DOMAINS = {
    "android-kotlin",
    "system-design",
    "python-backend",
    "ai-workflows",
    "engineering-culture",
}


@dataclass
class Source:
    id: str
    type: Literal["rss", "youtube"]
    url: str = ""
    channel: str = ""
    playlist: str = ""
    headers: dict[str, str] = field(default_factory=dict)
    cookie_env_var: str = ""


SOURCES_FILE = Path(__file__).parent / "sources.json"


def load_sources() -> list[Source]:
    with SOURCES_FILE.open(encoding="utf-8") as f:
        data = json.load(f)
    if not data:
        raise ValueError(f"{SOURCES_FILE} contains no sources")
    return [Source(**s) for s in data]


SOURCES: list[Source] = load_sources()

SYSTEM_PROMPT = """You are a knowledge-base curator. Given an article or transcript, \
output a JSON object with:
- "domain": one of ["android-kotlin", "system-design", "python-backend", \
"ai-workflows", "engineering-culture"]
- "subdomain": a concise subdomain name
- "concept": short kebab-case identifier (e.g. "structured-concurrency")
- "title": human-readable title
- "summary": 2-4 paragraphs synthesizing the key ideas, with inline \
citations to the source
- "key_points": a list of 2-5 bullet-point takeaways
- "sources": list of {"title": str, "url": str, "author": str, "date": str}

Be concise. Strip fluff. Only include claims directly supported by the source text."""
