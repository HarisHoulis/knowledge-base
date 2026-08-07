import subprocess
from collections.abc import Callable
from pathlib import Path
from unittest.mock import MagicMock

import pytest
import requests

from kb_pipeline.config import Source
from kb_pipeline.fetcher import (
    _strip_subtitle_formatting,
    extract_text,
    fetch_article,
    fetch_url_text,
    transcript_youtube,
    verify_source_auth,
)

SAMPLE_VTT = """WEBVTT
Kind: captions
Language: en

00:00:00.320 --> 00:00:18.790 align:start position:0%

[Music]

00:00:18.800 --> 00:00:21.790 align:start position:0%
We're<00:00:19.039><c> no</c><00:00:19.359><c> strangers</c><00:00:19.840><c> to</c>

00:00:21.800 --> 00:00:25.950 align:start position:0%
love. You know the rules and so do"""


class TestStripSubtitleFormatting:
    def test_strips_webvtt_header(self):
        result = _strip_subtitle_formatting(SAMPLE_VTT)
        assert "WEBVTT" not in result
        assert "Kind:" not in result
        assert "Language:" not in result

    def test_strips_timestamps(self):
        result = _strip_subtitle_formatting(SAMPLE_VTT)
        assert "-->" not in result

    def test_strips_inline_tags(self):
        result = _strip_subtitle_formatting(SAMPLE_VTT)
        assert "<c>" not in result
        assert "We're no strangers to" in result

    def test_preserves_text_content(self):
        result = _strip_subtitle_formatting(SAMPLE_VTT)
        assert "We're no strangers to" in result
        assert "love" in result
        assert "You know the rules" in result

    def test_returns_single_string(self):
        result = _strip_subtitle_formatting(SAMPLE_VTT)
        assert isinstance(result, str)
        assert len(result) > 0


SAMPLE_VTT_EMPTY = "WEBVTT\nKind: captions\nLanguage: en\n"

SAMPLE_VTT_NONTEXT = """WEBVTT
Kind: captions
Language: en

00:00:01.000 --> 00:00:02.000 align:start position:0%

1

00:00:02.000 --> 00:00:03.000 align:start position:0%

2"""


class TestStripSubtitleFormattingEdgeCases:
    def test_empty_returns_empty_string(self):
        assert _strip_subtitle_formatting("") == ""

    def test_only_metadata_returns_empty_string(self):
        assert _strip_subtitle_formatting(SAMPLE_VTT_EMPTY) == ""

    def test_only_timestamp_lines_returns_empty_string(self):
        assert _strip_subtitle_formatting("00:00:01.000 --> 00:00:02.000") == ""

    def test_numeric_index_lines_skipped(self):
        result = _strip_subtitle_formatting(SAMPLE_VTT_NONTEXT)
        assert result == ""


SAMPLE_PLAIN_TEXT = """Exploring /grill-me new batch-based question system.
Learn how Matt is improving the skill by asking questions in rounds
instead of one-by-one, reducing wait times and context switching."""


class TestExtractText:
    def test_empty_returns_empty_string(self):
        assert extract_text("") == ""

    def test_whitespace_only_returns_empty_string(self):
        assert extract_text("   \n  \t  ") == ""

    def test_plain_text_returns_unchanged(self):
        result = extract_text(SAMPLE_PLAIN_TEXT)
        assert result == SAMPLE_PLAIN_TEXT

    def test_html_delegates_to_trafilatura(self):
        html = "<html><body><p>Hello world</p></body></html>"
        result = extract_text(html)
        assert isinstance(result, str)
        assert len(result) > 0


SAMPLE_HTML = (
    "<html><body><article><h1>Real Article</h1><p>This is the full article content "
    "that should be fetched from the link URL when the RSS entry content is too "
    "short.</p><p>It has enough text to pass the 200 character threshold for "
    "classification.</p></article></body></html>"
)


class TestFetchArticle:
    def test_fetches_article_with_headers_and_returns_markdown(self):
        response = MagicMock()
        response.text = SAMPLE_HTML
        response.raise_for_status = MagicMock()
        seen_headers = {}

        def fake_get(url, **kwargs):
            seen_headers.update(kwargs.get("headers", {}))
            return response

        result = fetch_article(
            "https://example.com/article", {"Cookie": "session=abc"}, get=fake_get
        )
        assert len(result) >= 200
        assert seen_headers == {"Cookie": "session=abc"}

    @pytest.mark.parametrize(
        "status_code,message", [(404, "404 Client Error"), (500, "500 Server Error")]
    )
    def test_http_error_status_returns_empty(self, caplog, status_code, message):
        caplog.set_level("WARNING")

        def fake_get(url, **kwargs):
            r = requests.Response()
            r.status_code = status_code
            r.url = url
            raise requests.HTTPError(message, response=r)

        assert (
            fetch_article("https://example.com/article", {"Cookie": "x"}, get=fake_get)
            == ""
        )
        assert "fetch failed" in caplog.text

    def test_empty_response_returns_empty(self, caplog):
        caplog.set_level("WARNING")

        response = MagicMock()
        response.text = ""
        response.raise_for_status = MagicMock()

        def fake_get(url, **kwargs):
            return response

        assert (
            fetch_article("https://example.com/article", {"Cookie": "x"}, get=fake_get)
            == ""
        )

    def test_connection_error_returns_empty(self, caplog):
        caplog.set_level("WARNING")

        def fake_get(url, **kwargs):
            raise requests.ConnectionError("connection failed")

        assert (
            fetch_article("https://example.com/article", {"Cookie": "x"}, get=fake_get)
            == ""
        )
        assert "fetch failed" in caplog.text


class TestVerifySourceAuth:
    def test_returns_true_when_env_var_set_and_non_empty(self, monkeypatch):
        monkeypatch.setenv("BYTEBYTEGO_SUBSTACK_COOKIE", "auth_cookie_value")
        source = Source(
            id="bytebytego",
            type="rss",
            url="https://blog.bytebytego.com/feed",
            cookie_env_var="BYTEBYTEGO_SUBSTACK_COOKIE",
        )
        assert verify_source_auth(source) is True

    def test_returns_false_when_env_var_unset(self, monkeypatch):
        monkeypatch.delenv("BYTEBYTEGO_SUBSTACK_COOKIE", raising=False)
        source = Source(
            id="bytebytego",
            type="rss",
            url="https://blog.bytebytego.com/feed",
            cookie_env_var="BYTEBYTEGO_SUBSTACK_COOKIE",
        )
        assert verify_source_auth(source) is False

    def test_returns_false_when_env_var_empty(self, monkeypatch):
        monkeypatch.setenv("BYTEBYTEGO_SUBSTACK_COOKIE", "")
        source = Source(
            id="bytebytego",
            type="rss",
            url="https://blog.bytebytego.com/feed",
            cookie_env_var="BYTEBYTEGO_SUBSTACK_COOKIE",
        )
        assert verify_source_auth(source) is False

    def test_returns_false_when_no_cookie_env_var_declared(self):
        source = Source(
            id="jake-wharton", type="rss", url="https://jakewharton.com/atom.xml"
        )
        assert verify_source_auth(source) is False

    def test_getenv_seam_is_injected(self):
        source = Source(
            id="bytebytego",
            type="rss",
            url="https://blog.bytebytego.com/feed",
            cookie_env_var="BYTEBYTEGO_SUBSTACK_COOKIE",
        )
        assert (
            verify_source_auth(
                source,
                getenv=lambda var: (
                    "cookie" if var == "BYTEBYTEGO_SUBSTACK_COOKIE" else None
                ),
            )
            is True
        )
        assert verify_source_auth(source, getenv=lambda var: None) is False


class TestFetchUrlText:
    def test_fetches_url_and_returns_text(self):
        response = MagicMock()
        response.text = SAMPLE_HTML
        response.raise_for_status = MagicMock()

        def fake_get(url, **kwargs):
            return response

        result = fetch_url_text("https://example.com/article", get=fake_get)
        assert len(result) >= 200

    def test_network_error_returns_empty(self, caplog):
        caplog.set_level("WARNING")

        def fake_get(url, **kwargs):
            raise requests.RequestException("connection failed")

        result = fetch_url_text("https://example.com/article", get=fake_get)
        assert result == ""
        assert "fetch failed" in caplog.text

    def test_timeout_returns_empty(self, caplog):
        caplog.set_level("WARNING")

        def fake_get(url, **kwargs):
            raise requests.Timeout("timed out")

        result = fetch_url_text("https://example.com/article", get=fake_get)
        assert result == ""
        assert "timed out" in caplog.text or "fetch failed" in caplog.text

    def test_non_html_response_returns_empty(self, caplog):
        caplog.set_level("WARNING")

        response = MagicMock()
        response.text = "not html content"
        response.raise_for_status = MagicMock()

        def fake_get(url, **kwargs):
            return response

        result = fetch_url_text("https://example.com/article", get=fake_get)
        assert result == ""
        assert "extract failed" in caplog.text


class TestTranscriptYoutube:
    def test_retry_succeeds_on_second_attempt(self):
        """First (android) fails, second (default) succeeds."""
        calls = []

        sample_transcript = "WEBVTT\n\n00:00:01.000 --> 00:00:02.000\nHello world"

        def fake_run(cmd, **kwargs):
            calls.append(cmd)
            if len(calls) == 1:
                raise subprocess.CalledProcessError(1, cmd)
            try:
                o_idx = cmd.index("-o")
                parent = Path(cmd[o_idx + 1]).parent
                (parent / "test_id.en.vtt").write_text(sample_transcript)
            except (ValueError, IndexError):
                pass
            return MagicMock(stdout="", stderr="")

        result = transcript_youtube("test_id", run_cmd=fake_run)

        assert result == "Hello world"
        assert len(calls) == 2

    def test_retry_both_fail_return_empty_and_log_stderr(self, caplog):
        caplog.set_level("WARNING")

        def fake_run(cmd, **kwargs):
            raise subprocess.CalledProcessError(1, cmd, stderr="no longer available")

        result = transcript_youtube("test_id", run_cmd=fake_run)

        assert result == ""
        assert "no longer available" in caplog.text


def _fake_run_collector(calls: list) -> Callable:
    def fake_run(cmd, **kwargs):
        calls.append(cmd)
        return MagicMock(stdout="", stderr="")

    return fake_run


class TestTranscriptYoutubeArgs:
    def test_js_runtime_flag_in_all_attempts(self):
        calls = []
        transcript_youtube("test_id", run_cmd=_fake_run_collector(calls))

        assert len(calls) >= 1
        for cmd in calls:
            assert "--js-runtimes" in cmd
            js_idx = cmd.index("--js-runtimes")
            assert js_idx + 1 < len(cmd)
            assert cmd[js_idx + 1] == "node"

    def test_cookies_arg_present_when_path_given(self):
        calls = []
        transcript_youtube(
            "test_id",
            cookies_path="/tmp/yt-cookies.txt",
            run_cmd=_fake_run_collector(calls),
        )

        assert len(calls) >= 1
        for cmd in calls:
            assert "--cookies" in cmd
            ck_idx = cmd.index("--cookies")
            assert ck_idx + 1 < len(cmd)
            assert cmd[ck_idx + 1] == "/tmp/yt-cookies.txt"

    def test_no_cookies_arg_when_path_not_given(self):
        calls = []
        transcript_youtube("test_id", run_cmd=_fake_run_collector(calls))

        for cmd in calls:
            assert "--cookies" not in cmd

    def test_cookies_path_from_env_var(self, monkeypatch):
        monkeypatch.setenv("YT_COOKIES_PATH", "/env/cookies.txt")
        calls = []
        transcript_youtube("test_id", run_cmd=_fake_run_collector(calls))

        for cmd in calls:
            assert "--cookies" in cmd
            ck_idx = cmd.index("--cookies")
            assert cmd[ck_idx + 1] == "/env/cookies.txt"

    def test_explicit_cookies_path_overrides_env_var(self, monkeypatch):
        monkeypatch.setenv("YT_COOKIES_PATH", "/env/cookies.txt")
        calls = []
        transcript_youtube(
            "test_id",
            cookies_path="/explicit/cookies.txt",
            run_cmd=_fake_run_collector(calls),
        )

        for cmd in calls:
            assert "--cookies" in cmd
            ck_idx = cmd.index("--cookies")
            assert cmd[ck_idx + 1] == "/explicit/cookies.txt"
