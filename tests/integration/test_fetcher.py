import shutil
import subprocess
import sys

import pytest

from kb_pipeline.fetcher import transcript_youtube


def test_yt_dlp_available():
    cmd = "yt-dlp" if shutil.which("yt-dlp") else [sys.executable, "-m", "yt_dlp"]
    result = subprocess.run(
        [*([cmd] if isinstance(cmd, str) else cmd), "--version"],
        capture_output=True, text=True, timeout=15,
    )
    assert result.returncode == 0


KNOWN_CAPTIONED_VIDEO = "dQw4w9WgXcQ"


@pytest.mark.integration
class TestTranscriptYoutube:
    def test_returns_non_empty_text(self):
        text = transcript_youtube(KNOWN_CAPTIONED_VIDEO)
        assert text, "expected non-empty transcript"
        assert len(text) > 50, "expected substantive transcript text"
        assert isinstance(text, str)

    def test_contains_expected_words(self):
        text = transcript_youtube(KNOWN_CAPTIONED_VIDEO)
        assert "never" in text.lower() or "gonna" in text.lower() or "love" in text.lower()

    def test_unknown_video_returns_empty(self):
        text = transcript_youtube("nonexistent_video_id_12345")
        assert text == ""
