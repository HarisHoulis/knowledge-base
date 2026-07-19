import logging
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Callable, Optional

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


def _strip_subtitle_formatting(raw: str) -> str:
    lines: list[str] = []
    for line in raw.splitlines():
        stripped = line.strip()
        if (stripped
            and not stripped.startswith("WEBVTT")
            and not stripped.startswith("Kind:")
            and not stripped.startswith("Language:")
            and "-->" not in stripped
            and not stripped.replace(",", "").replace(".", "").replace(" ", "").isdigit()):
            cleaned = re.sub(r"<[^>]+>", "", stripped)
            if cleaned:
                lines.append(cleaned)
    return " ".join(lines)


def transcript_youtube(video_id: str, *, run_cmd: Optional[Callable[..., Any]] = None) -> str:
    if run_cmd is None:
        cmd = (["yt-dlp"] if shutil.which("yt-dlp") else
               [sys.executable, "-m", "yt_dlp"]
               if subprocess.run([sys.executable, "-m", "yt_dlp", "--version"],
                                 capture_output=True, text=True).returncode == 0
               else None)
        if not cmd:
            logger.warning("  [!] yt-dlp not found")
            return ""
        _run = subprocess.run
    else:
        cmd = ["yt-dlp"]
        _run = run_cmd

    with tempfile.TemporaryDirectory() as tmpdir:
        base_args = [
            *cmd,
            "--write-auto-subs", "--sub-lang", "en",
            "--skip-download",
            "-o", f"{tmpdir}/%(id)s.%(ext)s",
            f"https://www.youtube.com/watch?v={video_id}",
        ]
        attempts = [
            [*base_args, "--extractor-args", "youtube:player_client=android"],
            base_args,
        ]
        last_error: Optional[Exception] = None
        for attempt_cmd in attempts:
            try:
                _run(
                    attempt_cmd,
                    capture_output=True, text=True, timeout=120, check=True,
                )
                last_error = None
                break
            except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired) as e:
                last_error = e
                stderr = e.stderr if isinstance(e, subprocess.CalledProcessError) else ""
                logger.debug("  [!] yt-dlp attempt failed for %s:\n%s", video_id, stderr)

        if last_error is not None:
            stderr = last_error.stderr if isinstance(last_error, subprocess.CalledProcessError) else ""
            logger.warning("  [!] yt-dlp failed for %s: %s", video_id, stderr or last_error)
            return ""

        sub_files = sorted(Path(tmpdir).iterdir())
        if not sub_files:
            logger.warning("  [!] no subtitle files for %s", video_id)
            return ""

        raw = sub_files[0].read_text()
        return _strip_subtitle_formatting(raw)


def extract_text(html: str) -> str:
    if not html.strip():
        return ""
    if not html.strip().startswith("<"):
        return html.strip()
    return trafilatura.extract(html, output_format="markdown", include_links=True) or ""
