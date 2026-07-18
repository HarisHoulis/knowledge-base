import logging
import subprocess
from typing import Any

import feedparser
import requests
import trafilatura

from .config import SOURCES

logger = logging.getLogger(__name__)


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


def extract_text(html: str) -> str:
    return trafilatura.extract(html, output_format="markdown", include_links=True) or ""
