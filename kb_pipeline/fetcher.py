import logging
import subprocess
from typing import Any

import feedparser
import requests
import trafilatura

from .config import Source

logger = logging.getLogger(__name__)


def fetch_rss(source: Source) -> list[Any]:
    if source.headers:
        try:
            r = requests.get(source.url, headers=source.headers, timeout=30)
            r.raise_for_status()
            feed = feedparser.parse(r.text)
        except requests.RequestException as e:
            logger.warning("  [!] RSS fetch error (%s): %s", source.id, e)
            return []
    else:
        feed = feedparser.parse(source.url)
    if feed.bozo and not feed.entries:
        logger.warning("  [!] RSS parse error (%s): %s", source.id, feed.bozo_exception)
        return []
    return feed.entries


def fetch_youtube(source: Source) -> list[Any]:
    if source.playlist:
        url = f"https://www.youtube.com/feeds/videos.xml?playlist_id={source.playlist}"
    elif source.channel:
        url = f"https://www.youtube.com/feeds/videos.xml?channel_id={source.channel}"
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
