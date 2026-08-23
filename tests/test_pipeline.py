import re
import subprocess
from pathlib import Path
from typing import Any, Optional
from unittest.mock import MagicMock

from kb_pipeline.audit import AuditResult
from kb_pipeline.config import SOURCES, Source

SAMPLE_TEXT = "some source text"
SAMPLE_URL = "https://example.com/article"
SAMPLE_META: dict[str, Any] = {"title": "Test", "link": SAMPLE_URL}
SAMPLE_DRAFT = Path("/tmp/drafts/test.md")
SAMPLE_RESULT: dict[str, Any] = {
    "domain": "a",
    "subdomain": "b",
    "concept": "c",
    "summary": "test",
    "key_points": [],
}


def stub_audit_pass(data: Any, source_text: str) -> AuditResult:
    return {"pass": True}


def stub_audit_fail(data: Any, source_text: str) -> AuditResult:
    return {
        "pass": False,
        "issues": [{"field": "summary", "description": "test issue"}],
    }


def stub_classify_ok(
    text: str, meta: dict[str, Any], audit_feedback: Optional[str] = None
) -> dict[str, Any]:
    return dict(SAMPLE_RESULT)


class CountedAuditStub:
    def __init__(self, *results: AuditResult) -> None:
        self.results = list(results)
        self.call_count = 0

    def __call__(self, data: Any, source_text: str) -> AuditResult:
        idx = (
            self.call_count
            if self.call_count < len(self.results)
            else len(self.results) - 1
        )
        self.call_count += 1
        return self.results[idx]


def make_escalation_stub() -> tuple[list[tuple[str, Path, str]], Any]:
    calls: list[tuple[str, Path, str]] = []

    def stub(url: str, entry_path: Path, feedback: str) -> None:
        calls.append((url, entry_path, feedback))

    return calls, stub


def make_promote_stub() -> tuple[list[Path], Any]:
    calls: list[Path] = []

    def stub(draft_path: Path) -> None:
        calls.append(draft_path)

    return calls, stub


class TestAuditWithRetry:
    def test_all_audits_pass_first_try(self) -> None:
        from kb_pipeline.pipeline import _audit_with_retry

        promote_calls, promote_fn = make_promote_stub()
        esc_calls, esc_fn = make_escalation_stub()

        ok = _audit_with_retry(
            SAMPLE_RESULT,
            SAMPLE_TEXT,
            SAMPLE_URL,
            SAMPLE_META,
            SAMPLE_DRAFT,
            classify_fn=stub_classify_ok,
            ca_audit_fn=stub_audit_pass,
            co_audit_fn=stub_audit_pass,
            promote_fn=promote_fn,
            escalation_fn=esc_fn,
        )

        assert ok is True
        assert promote_calls == [SAMPLE_DRAFT]
        assert esc_calls == []

    def test_content_fails_once_then_passes(self) -> None:
        from kb_pipeline.pipeline import _audit_with_retry

        promote_calls, promote_fn = make_promote_stub()
        esc_calls, esc_fn = make_escalation_stub()
        co_stub = CountedAuditStub(
            {
                "pass": False,
                "issues": [{"field": "summary", "description": "wrong summary"}],
            },
            {"pass": True},
        )

        ok = _audit_with_retry(
            SAMPLE_RESULT,
            SAMPLE_TEXT,
            SAMPLE_URL,
            SAMPLE_META,
            SAMPLE_DRAFT,
            classify_fn=stub_classify_ok,
            ca_audit_fn=stub_audit_pass,
            co_audit_fn=co_stub,
            promote_fn=promote_fn,
            escalation_fn=esc_fn,
        )

        assert ok is True
        assert promote_calls == [SAMPLE_DRAFT]
        assert esc_calls == []
        assert co_stub.call_count == 2

    def test_classification_fails_once_then_passes(self) -> None:
        from kb_pipeline.pipeline import _audit_with_retry

        promote_calls, promote_fn = make_promote_stub()
        esc_calls, esc_fn = make_escalation_stub()
        ca_stub = CountedAuditStub(
            {
                "pass": False,
                "issues": [{"field": "domain", "description": "wrong domain"}],
            },
            {"pass": True},
        )

        ok = _audit_with_retry(
            SAMPLE_RESULT,
            SAMPLE_TEXT,
            SAMPLE_URL,
            SAMPLE_META,
            SAMPLE_DRAFT,
            classify_fn=stub_classify_ok,
            ca_audit_fn=ca_stub,
            co_audit_fn=stub_audit_pass,
            promote_fn=promote_fn,
            escalation_fn=esc_fn,
        )

        assert ok is True
        assert promote_calls == [SAMPLE_DRAFT]
        assert esc_calls == []
        assert ca_stub.call_count == 2

    def test_surgical_retry_only_failing_audit_reruns(self) -> None:
        from kb_pipeline.pipeline import _audit_with_retry

        promote_calls, promote_fn = make_promote_stub()
        esc_calls, esc_fn = make_escalation_stub()
        ca_stub = CountedAuditStub({"pass": True})
        co_stub = CountedAuditStub(
            {
                "pass": False,
                "issues": [{"field": "summary", "description": "bad summary"}],
            },
            {"pass": True},
        )

        ok = _audit_with_retry(
            SAMPLE_RESULT,
            SAMPLE_TEXT,
            SAMPLE_URL,
            SAMPLE_META,
            SAMPLE_DRAFT,
            classify_fn=stub_classify_ok,
            ca_audit_fn=ca_stub,
            co_audit_fn=co_stub,
            promote_fn=promote_fn,
            escalation_fn=esc_fn,
        )

        assert ok is True
        assert promote_calls == [SAMPLE_DRAFT]
        # classification ran once (not retried), content ran twice (failed then retried)
        assert ca_stub.call_count == 1
        assert co_stub.call_count == 2

    def test_always_fails_escalates(self) -> None:
        from kb_pipeline.pipeline import _audit_with_retry

        promote_calls, promote_fn = make_promote_stub()
        esc_calls, esc_fn = make_escalation_stub()

        ok = _audit_with_retry(
            SAMPLE_RESULT,
            SAMPLE_TEXT,
            SAMPLE_URL,
            SAMPLE_META,
            SAMPLE_DRAFT,
            classify_fn=stub_classify_ok,
            ca_audit_fn=stub_audit_fail,
            co_audit_fn=stub_audit_fail,
            promote_fn=promote_fn,
            escalation_fn=esc_fn,
        )

        assert ok is False
        assert promote_calls == []
        assert len(esc_calls) == 1
        esc_url, esc_path, esc_feedback = esc_calls[0]
        assert esc_url == SAMPLE_URL
        assert esc_path == SAMPLE_DRAFT

    def test_max_retries_is_two(self) -> None:
        from kb_pipeline.pipeline import _audit_with_retry

        promote_calls, promote_fn = make_promote_stub()
        esc_calls, esc_fn = make_escalation_stub()
        co_stub = CountedAuditStub(
            {
                "pass": False,
                "issues": [{"field": "summary", "description": "still wrong"}],
            },
            {
                "pass": False,
                "issues": [{"field": "summary", "description": "still wrong 2"}],
            },
        )

        ok = _audit_with_retry(
            SAMPLE_RESULT,
            SAMPLE_TEXT,
            SAMPLE_URL,
            SAMPLE_META,
            SAMPLE_DRAFT,
            classify_fn=stub_classify_ok,
            ca_audit_fn=stub_audit_pass,
            co_audit_fn=co_stub,
            promote_fn=promote_fn,
            escalation_fn=esc_fn,
        )

        assert ok is False
        assert promote_calls == []
        assert len(esc_calls) == 1
        # initial + 2 retries = 3 calls, but the stub passes after exhausting
        assert co_stub.call_count == 3  # initial + retry 1 + retry 2


class TestExtractYoutubeVideoId:
    def test_watch_url(self) -> None:
        from kb_pipeline.pipeline import _extract_youtube_video_id

        assert (
            _extract_youtube_video_id("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            == "dQw4w9WgXcQ"
        )

    def test_short_url(self) -> None:
        from kb_pipeline.pipeline import _extract_youtube_video_id

        assert (
            _extract_youtube_video_id("https://youtu.be/dQw4w9WgXcQ") == "dQw4w9WgXcQ"
        )

    def test_with_query_params(self) -> None:
        from kb_pipeline.pipeline import _extract_youtube_video_id

        assert (
            _extract_youtube_video_id(
                "https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=30s"
            )
            == "dQw4w9WgXcQ"
        )

    def test_non_youtube_url(self) -> None:
        from kb_pipeline.pipeline import _extract_youtube_video_id

        assert _extract_youtube_video_id("https://example.com/article") is None

    def test_empty_url(self) -> None:
        from kb_pipeline.pipeline import _extract_youtube_video_id

        assert _extract_youtube_video_id("") is None

    def test_invalid_video_id_length(self) -> None:
        from kb_pipeline.pipeline import _extract_youtube_video_id

        assert (
            _extract_youtube_video_id("https://www.youtube.com/watch?v=invalid") is None
        )


SHORT_CONTENT = "<p>Read it at code.cash.app/...</p>"


class TestRunPipelineLinkFallback:
    def test_rss_short_content_falls_back_to_link(self):
        from kb_pipeline.pipeline import run_pipeline

        fixture = Path(__file__).parent / "fixtures" / "redirect-rss.xml"
        source = Source(id="test", type="rss", url=str(fixture))

        def stub_fetch_url(url: str) -> str:
            if "real-article" in url:
                return (
                    "This is the full article content with enough text to pass the 200 "
                    "character threshold for classification. " * 10
                )
            return ""

        stats = run_pipeline(
            dry_run=True,
            sources=[source],
            fetch_url_text_fn=stub_fetch_url,
            classify_fn=stub_classify_ok,
        )

        assert stats["written"] == 1

    def test_rss_short_content_link_fails_skips_gracefully(self, caplog):
        from kb_pipeline.pipeline import run_pipeline

        caplog.set_level("INFO")
        fixture = Path(__file__).parent / "fixtures" / "redirect-rss.xml"
        source = Source(id="test", type="rss", url=str(fixture))

        def stub_fetch_url(url: str) -> str:
            return ""

        stats = run_pipeline(
            dry_run=True,
            sources=[source],
            fetch_url_text_fn=stub_fetch_url,
        )

        assert stats["skipped"] >= 1
        assert "link fallback" in caplog.text

    def test_link_fallback_uses_fetched_markdown_directly(self):
        from kb_pipeline.pipeline import run_pipeline

        fixture = Path(__file__).parent / "fixtures" / "redirect-rss.xml"
        source = Source(id="test", type="rss", url=str(fixture))

        raw_html = (
            "<html><body><p>full article content here</p>" * 30 + "</body></html>"
        )

        received: list[str] = []

        def capturing_classify(
            text: str, meta: dict[str, Any], audit_feedback: Optional[str] = None
        ) -> dict[str, Any]:
            received.append(text)
            return dict(SAMPLE_RESULT)

        def stub_fetch_url(url: str) -> str:
            return raw_html

        run_pipeline(
            dry_run=True,
            sources=[source],
            fetch_url_text_fn=stub_fetch_url,
            classify_fn=capturing_classify,
        )

        assert received == [raw_html]

    def test_youtube_short_content_no_fallback(self, monkeypatch):
        from kb_pipeline.pipeline import run_pipeline

        def mock_fetch(src):
            from feedparser import FeedParserDict

            return [
                FeedParserDict(
                    {
                        "link": "https://www.youtube.com/watch?v=test123",
                        "title": "Test Video",
                    }
                )
            ]

        monkeypatch.setattr("kb_pipeline.pipeline.fetch_youtube", mock_fetch)

        source = Source(
            id="test",
            type="youtube",
            url="https://www.youtube.com/feeds/videos.xml?channel_id=UC_test",
        )

        def stub_transcript(video_id: str) -> str:
            return "short"

        fetch_calls: list[str] = []

        def stub_fetch_url(url: str) -> str:
            fetch_calls.append(url)
            return "should not be called"

        stats = run_pipeline(
            dry_run=True,
            sources=[source],
            transcript_fn=stub_transcript,
            fetch_url_text_fn=stub_fetch_url,
        )

        assert fetch_calls == []
        assert stats["skipped"] >= 1

    def test_normal_content_no_fallback(self):
        from kb_pipeline.pipeline import run_pipeline

        fixture = Path(__file__).parent / "fixtures" / "plain-rss.xml"
        source = Source(id="test", type="rss", url=str(fixture))

        fetch_calls: list[str] = []

        def stub_fetch_url(url: str) -> str:
            fetch_calls.append(url)
            return ""

        stats = run_pipeline(
            dry_run=True,
            sources=[source],
            fetch_url_text_fn=stub_fetch_url,
            classify_fn=stub_classify_ok,
        )

        assert fetch_calls == []
        assert stats["written"] == 1


class TestRunPipelineWithTranscript:
    def test_rss_source_does_not_call_transcript(self) -> None:
        from kb_pipeline.pipeline import run_pipeline

        calls: list[str] = []

        def spy_transcript(video_id: str) -> str:
            calls.append(video_id)
            return ""

        fixture = Path(__file__).parent / "fixtures" / "simple-rss.xml"
        source = Source(id="test", type="rss", url=str(fixture))

        stats = run_pipeline(
            dry_run=True, sources=[source], transcript_fn=spy_transcript
        )

        assert calls == [], "transcript_fn should not be called for RSS sources"
        assert stats["sources"] == 1


def test_source_cookie_env_var_defaults_to_empty() -> None:
    source = Source(id="x", type="rss")
    assert source.cookie_env_var == ""


def test_existing_sources_instantiate_without_error() -> None:
    for s in SOURCES:
        assert isinstance(s, Source)


def test_bytebytego_source_has_cookie_env_var() -> None:
    src = next((s for s in SOURCES if s.id == "bytebytego"), None)
    assert src is not None
    assert src.cookie_env_var == "BYTEBYTEGO_SUBSTACK_COOKIE"


def _rss_entry(
    link: str, title: str, content: str = "<p>some html</p>"
) -> dict[str, Any]:
    from feedparser import FeedParserDict

    return FeedParserDict(
        {"link": link, "title": title, "content": [{"value": content}]}
    )


def _make_rss_fetch_stub(entries: list[dict[str, Any]]) -> Any:
    def mock_fetch(src: Source) -> list[Any]:
        return entries

    return mock_fetch


def _make_report_stub() -> tuple[list[list[Any]], Any]:
    reported: list[list[Any]] = []

    def report_stub(failures: list[Any]) -> None:
        reported.append(failures)

    return reported, report_stub


def _make_failing_extract(error_type: str) -> Any:
    def fake_extract(html: str, *, extract_fn: Any = None, on_error: Any = None) -> str:
        if on_error is not None:
            on_error(error_type)
        return ""

    return fake_extract


def _patch_live_run(monkeypatch: Any) -> None:
    monkeypatch.setattr("kb_pipeline.pipeline.save_state", lambda state: None)
    monkeypatch.setattr("kb_pipeline.pipeline.write_entry", lambda result, url: None)


def _patch_gh_run(monkeypatch: Any, calls: list[list[str]]) -> None:
    def fake_run(cmd: list[str], **kwargs: Any) -> MagicMock:
        calls.append(cmd)
        return MagicMock(stdout="", stderr="")

    monkeypatch.setattr("kb_pipeline.pipeline.subprocess.run", fake_run)


class TestRunPipelineExtractionFailures:
    def test_live_run_reports_all_failures_once(self, monkeypatch):
        from kb_pipeline.pipeline import run_pipeline

        reported, report_stub = _make_report_stub()
        _patch_live_run(monkeypatch)
        monkeypatch.setattr(
            "kb_pipeline.pipeline.extract_text", _make_failing_extract("exception")
        )
        monkeypatch.setattr(
            "kb_pipeline.pipeline.fetch_rss",
            _make_rss_fetch_stub(
                [
                    _rss_entry("https://example.com/a", "Alpha"),
                    _rss_entry("https://example.com/b", "Beta"),
                ]
            ),
        )

        source = Source(id="test", type="rss", url="https://example.com/feed")

        stats = run_pipeline(
            dry_run=False,
            sources=[source],
            fetch_url_text_fn=lambda url: "",
            classify_fn=stub_classify_ok,
            report_fn=report_stub,
        )

        assert stats["failed"] == 2
        assert len(reported) == 1
        failures = reported[0]
        assert len(failures) == 2
        assert failures[0].source_id == "test"
        assert failures[0].title == "Alpha"
        assert failures[0].url == "https://example.com/a"
        assert failures[0].error_type == "exception"
        assert failures[1].title == "Beta"
        assert failures[1].error_type == "exception"

    def test_silent_empty_final_result_is_recorded_as_empty(self, monkeypatch):
        from kb_pipeline.pipeline import run_pipeline

        reported, report_stub = _make_report_stub()
        _patch_live_run(monkeypatch)
        monkeypatch.setattr(
            "kb_pipeline.pipeline.extract_text", _make_failing_extract("empty")
        )
        monkeypatch.setattr(
            "kb_pipeline.pipeline.fetch_rss",
            _make_rss_fetch_stub([_rss_entry("https://example.com/a", "Alpha")]),
        )

        source = Source(id="test", type="rss", url="https://example.com/feed")

        stats = run_pipeline(
            dry_run=False,
            sources=[source],
            fetch_url_text_fn=lambda url: "",
            classify_fn=stub_classify_ok,
            report_fn=report_stub,
        )

        assert stats["failed"] == 1
        failures = reported[0]
        assert failures[0].title == "Alpha"
        assert failures[0].url == "https://example.com/a"
        assert failures[0].error_type == "empty"

    def test_transient_empty_recovered_by_fallback_not_recorded(self, monkeypatch):
        from kb_pipeline.pipeline import run_pipeline

        reported, report_stub = _make_report_stub()
        calls: list[str] = []

        def fake_extract(
            html: str, *, extract_fn: Any = None, on_error: Any = None
        ) -> str:
            calls.append(html)
            if on_error is not None:
                on_error("empty")
            if len(calls) == 1:
                return ""
            return SAMPLE_TEXT * 20

        _patch_live_run(monkeypatch)
        monkeypatch.setattr("kb_pipeline.pipeline.extract_text", fake_extract)
        monkeypatch.setattr(
            "kb_pipeline.pipeline.fetch_rss",
            _make_rss_fetch_stub([_rss_entry("https://example.com/a", "Alpha")]),
        )

        source = Source(id="test", type="rss", url="https://example.com/feed")

        stats = run_pipeline(
            dry_run=False,
            sources=[source],
            fetch_url_text_fn=lambda url: SAMPLE_TEXT * 20,
            classify_fn=stub_classify_ok,
            report_fn=report_stub,
        )

        assert len(reported) == 0
        assert stats["failed"] == 0
        assert len(calls) == 1

    def test_short_fallback_recovery_is_not_recorded_as_failure(self, monkeypatch):
        from kb_pipeline.pipeline import run_pipeline

        reported, report_stub = _make_report_stub()
        calls: list[str] = []

        def fake_extract(
            html: str, *, extract_fn: Any = None, on_error: Any = None
        ) -> str:
            calls.append(html)
            if on_error is not None:
                on_error("empty")
            if len(calls) == 1:
                return ""
            return "too short to ingest"

        _patch_live_run(monkeypatch)
        monkeypatch.setattr("kb_pipeline.pipeline.extract_text", fake_extract)
        monkeypatch.setattr(
            "kb_pipeline.pipeline.fetch_rss",
            _make_rss_fetch_stub([_rss_entry("https://example.com/a", "Alpha")]),
        )

        source = Source(id="test", type="rss", url="https://example.com/feed")

        stats = run_pipeline(
            dry_run=False,
            sources=[source],
            fetch_url_text_fn=lambda url: "<p>recovered via link</p>",
            classify_fn=stub_classify_ok,
            report_fn=report_stub,
        )

        assert reported == []
        assert stats["failed"] == 0
        assert stats["skipped"] >= 1

    def test_live_run_with_zero_failures_creates_no_report(self, monkeypatch):
        from kb_pipeline.pipeline import run_pipeline

        reported, report_stub = _make_report_stub()
        _patch_live_run(monkeypatch)
        monkeypatch.setattr(
            "kb_pipeline.pipeline.fetch_rss",
            _make_rss_fetch_stub(
                [
                    _rss_entry(
                        "https://example.com/a",
                        "Alpha",
                        content="A plain text body that is long enough to be "
                        "considered a usable extraction result without triggering "
                        "the link fallback. " * 10,
                    )
                ]
            ),
        )

        source = Source(id="test", type="rss", url="https://example.com/feed")

        stats = run_pipeline(
            dry_run=False,
            sources=[source],
            fetch_url_text_fn=lambda url: "",
            classify_fn=stub_classify_ok,
            report_fn=report_stub,
        )

        assert reported == []
        assert stats["failed"] == 0
        assert stats["written"] == 1

    def test_dry_run_collects_failures_but_creates_no_report(self, monkeypatch):
        from kb_pipeline.pipeline import run_pipeline

        reported, report_stub = _make_report_stub()
        monkeypatch.setattr(
            "kb_pipeline.pipeline.extract_text", _make_failing_extract("exception")
        )
        monkeypatch.setattr(
            "kb_pipeline.pipeline.fetch_rss",
            _make_rss_fetch_stub([_rss_entry("https://example.com/a", "Alpha")]),
        )

        source = Source(id="test", type="rss", url="https://example.com/feed")

        stats = run_pipeline(
            dry_run=True,
            sources=[source],
            fetch_url_text_fn=lambda url: "",
            classify_fn=stub_classify_ok,
            report_fn=report_stub,
        )

        assert reported == []
        assert stats["failed"] == 1


class TestReportExtractionFailures:
    def _failure(self) -> Any:
        from kb_pipeline.pipeline import ExtractionFailure

        return ExtractionFailure(
            "bytebytego", "The Paywalled Post", "https://example.com/1", "exception"
        )

    def test_issue_title_matches_format(self, monkeypatch):
        from kb_pipeline.pipeline import _report_extraction_failures

        calls: list[list[str]] = []
        _patch_gh_run(monkeypatch, calls)

        _report_extraction_failures([self._failure(), self._failure()])

        assert len(calls) == 1
        args = calls[0]
        assert args[0] == "gh"
        assert args[1] == "issue"
        assert args[2] == "create"
        title = args[args.index("--title") + 1]
        assert re.fullmatch(
            r"Content extraction errors: \d{4}-\d{2}-\d{2} \(2 entries\)", title
        )

    def test_issue_body_shows_source_title_url_and_failure_type(self, monkeypatch):
        from kb_pipeline.pipeline import ExtractionFailure, _report_extraction_failures

        calls: list[list[str]] = []
        _patch_gh_run(monkeypatch, calls)

        _report_extraction_failures(
            [
                ExtractionFailure(
                    "bytebytego",
                    "The Paywalled Post",
                    "https://example.com/1",
                    "exception",
                ),
                ExtractionFailure(
                    "jake-wharton", "Kotlin Bits", "https://example.com/2", "empty"
                ),
            ]
        )

        body = calls[0][calls[0].index("--body") + 1]
        lines = body.splitlines()
        assert len(lines) == 2
        assert "bytebytego" in lines[0]
        assert "The Paywalled Post" in lines[0]
        assert "https://example.com/1" in lines[0]
        assert "exception" in lines[0]
        assert "jake-wharton" in lines[1]
        assert "Kotlin Bits" in lines[1]
        assert "https://example.com/2" in lines[1]
        assert "empty" in lines[1]

    def test_gh_failure_is_logged_not_raised(self, monkeypatch, caplog):
        from kb_pipeline.pipeline import _report_extraction_failures

        def fake_run(cmd, **kwargs):
            raise subprocess.CalledProcessError(1, cmd)

        monkeypatch.setattr("kb_pipeline.pipeline.subprocess.run", fake_run)
        caplog.set_level("WARNING")

        _report_extraction_failures([self._failure()])

        assert "escalation failed" in caplog.text

    def test_gh_missing_is_logged_not_raised(self, monkeypatch, caplog):
        from kb_pipeline.pipeline import _report_extraction_failures

        def fake_run(cmd, **kwargs):
            raise FileNotFoundError("gh not installed")

        monkeypatch.setattr("kb_pipeline.pipeline.subprocess.run", fake_run)
        caplog.set_level("WARNING")

        _report_extraction_failures([self._failure()])

        assert "escalation failed" in caplog.text


class TestRunPipelineAuthFetch:
    def test_auth_source_fetches_article_with_cookie_and_skips_summary(
        self, monkeypatch
    ) -> None:
        from kb_pipeline.pipeline import run_pipeline

        monkeypatch.setenv("BYTEBYTEGO_SUBSTACK_COOKIE", "cookie-value")
        fixture = Path(__file__).parent / "fixtures" / "simple-rss.xml"
        auth_source = Source(
            id="bytebytego",
            type="rss",
            url=str(fixture),
            cookie_env_var="BYTEBYTEGO_SUBSTACK_COOKIE",
        )

        calls: list[tuple[str, dict[str, str]]] = []

        def stub_fetch_article(url: str, headers: dict[str, str], on_error: Any) -> str:
            calls.append((url, headers))
            return "markdown text " * 60

        notify_calls, notify_fn = make_notify_stub()

        stats = run_pipeline(
            dry_run=True,
            sources=[auth_source],
            notify_fn=notify_fn,
            fetch_article_fn=stub_fetch_article,
            classify_fn=stub_classify_ok,
        )

        assert calls == [
            ("https://example.com/structured-concurrency", {"Cookie": "cookie-value"})
        ]
        assert notify_calls == []
        assert stats["written"] == 1


def make_auth_source() -> Source:
    return Source(
        id="bytebytego",
        type="rss",
        url="https://blog.bytebytego.com/feed",
        cookie_env_var="BYTEBYTEGO_SUBSTACK_COOKIE",
    )


def mock_two_entry_fetch(monkeypatch) -> None:
    from feedparser import FeedParserDict

    from kb_pipeline.fetcher import fetch_rss as real_fetch_rss

    def mock_fetch(src):
        if src.id == "bytebytego":
            return [
                FeedParserDict(
                    {"link": "https://example.com/paid-1", "title": "Paid 1"}
                ),
                FeedParserDict(
                    {"link": "https://example.com/paid-2", "title": "Paid 2"}
                ),
            ]
        return real_fetch_rss(src)

    monkeypatch.setattr("kb_pipeline.pipeline.fetch_rss", mock_fetch)


class TestRunPipelineAuthMidFetch:
    def test_empty_extraction_reports_failure_not_auth_issue(
        self, monkeypatch, tmp_path
    ) -> None:
        from kb_pipeline import state as state_module
        from kb_pipeline.pipeline import ExtractionFailure, run_pipeline

        monkeypatch.setenv("BYTEBYTEGO_SUBSTACK_COOKIE", "cookie")
        monkeypatch.setattr(state_module, "STATE_PATH", tmp_path / "state.json")
        mock_two_entry_fetch(monkeypatch)

        notify_calls, notify_fn = make_notify_stub()
        reported, report_stub = _make_report_stub()

        def stub_fetch_article(url: str, headers: dict[str, str], on_error: Any) -> str:
            on_error("empty")
            return ""

        stats = run_pipeline(
            dry_run=False,
            sources=[make_auth_source()],
            notify_fn=notify_fn,
            fetch_article_fn=stub_fetch_article,
            report_fn=report_stub,
        )

        assert notify_calls == []
        assert stats["seen"] == 1
        assert stats["sources"] == 1
        assert stats["failed"] == 1
        assert reported == [
            [
                ExtractionFailure(
                    "bytebytego",
                    "Paid 1",
                    "https://example.com/paid-1",
                    "empty",
                )
            ]
        ]

    def test_fetch_error_does_not_notify_and_aborts_source(
        self, monkeypatch, tmp_path, caplog
    ) -> None:
        from kb_pipeline import state as state_module
        from kb_pipeline.pipeline import run_pipeline

        monkeypatch.setenv("BYTEBYTEGO_SUBSTACK_COOKIE", "cookie")
        monkeypatch.setattr(state_module, "STATE_PATH", tmp_path / "state.json")
        mock_two_entry_fetch(monkeypatch)
        caplog.set_level("WARNING")

        notify_calls, notify_fn = make_notify_stub()

        def stub_fetch_article(url: str, headers: dict[str, str], on_error: Any) -> str:
            return ""

        stats = run_pipeline(
            dry_run=False,
            sources=[make_auth_source()],
            notify_fn=notify_fn,
            fetch_article_fn=stub_fetch_article,
            report_fn=lambda failures: None,
        )

        assert notify_calls == []
        assert stats["seen"] == 1
        assert stats["sources"] == 1
        assert stats["failed"] == 0
        assert "auth fetch failed for bytebytego" in caplog.text

    def test_empty_fetch_aborts_only_that_source(self, monkeypatch) -> None:
        from kb_pipeline.pipeline import run_pipeline

        monkeypatch.setenv("BYTEBYTEGO_SUBSTACK_COOKIE", "cookie")
        mock_two_entry_fetch(monkeypatch)
        fixture = Path(__file__).parent / "fixtures" / "plain-rss.xml"
        ok_source = Source(id="ok", type="rss", url=str(fixture))

        notify_calls, notify_fn = make_notify_stub()

        def stub_fetch_article(url: str, headers: dict[str, str], on_error: Any) -> str:
            return ""

        stats = run_pipeline(
            dry_run=True,
            sources=[make_auth_source(), ok_source],
            notify_fn=notify_fn,
            fetch_article_fn=stub_fetch_article,
            classify_fn=stub_classify_ok,
        )

        assert notify_calls == []
        assert stats["sources"] == 2
        assert stats["seen"] == 2
        assert stats["written"] == 1


class TestNotifyAuthFailure:
    def test_issue_body_contains_source_id_and_env_var(self, monkeypatch) -> None:
        from kb_pipeline.pipeline import _notify_auth_failure

        calls: list[list[str]] = []

        def fake_run(cmd, **kwargs):
            calls.append(cmd)

        monkeypatch.setattr("kb_pipeline.pipeline.subprocess.run", fake_run)

        _notify_auth_failure("bytebytego", "BYTEBYTEGO_SUBSTACK_COOKIE")

        assert len(calls) == 1
        cmd = calls[0]
        assert cmd[cmd.index("--title") + 1] == "Auth failure: bytebytego"
        body = cmd[cmd.index("--body") + 1]
        assert "bytebytego" in body
        assert "BYTEBYTEGO_SUBSTACK_COOKIE" in body

    def test_subprocess_failure_logs_warning(self, monkeypatch, caplog) -> None:
        from kb_pipeline.pipeline import _notify_auth_failure

        caplog.set_level("WARNING")

        def fake_run(cmd, **kwargs):
            raise FileNotFoundError("gh not found")

        monkeypatch.setattr("kb_pipeline.pipeline.subprocess.run", fake_run)

        _notify_auth_failure("bytebytego", "BYTEBYTEGO_SUBSTACK_COOKIE")

        assert "auth failure notification failed" in caplog.text


class TestRunPipelineAuthDryRun:
    def test_dry_run_logs_startup_failure_instead_of_issuing(
        self, monkeypatch, caplog
    ) -> None:
        from kb_pipeline.pipeline import run_pipeline

        monkeypatch.delenv("BYTEBYTEGO_SUBSTACK_COOKIE", raising=False)
        caplog.set_level("INFO")

        notify_calls, notify_fn = make_notify_stub()

        stats = run_pipeline(
            dry_run=True,
            sources=[make_auth_source()],
            notify_fn=notify_fn,
        )

        assert notify_calls == []
        assert "(dry run) would file auth issue" in caplog.text
        assert stats["sources"] == 0

    def test_dry_run_mid_fetch_empty_logs_no_issue(self, monkeypatch, caplog) -> None:
        from kb_pipeline.pipeline import run_pipeline

        monkeypatch.setenv("BYTEBYTEGO_SUBSTACK_COOKIE", "cookie")
        mock_two_entry_fetch(monkeypatch)
        caplog.set_level("INFO")

        notify_calls, notify_fn = make_notify_stub()

        def stub_fetch_article(url: str, headers: dict[str, str], on_error: Any) -> str:
            on_error("empty")
            return ""

        stats = run_pipeline(
            dry_run=True,
            sources=[make_auth_source()],
            notify_fn=notify_fn,
            fetch_article_fn=stub_fetch_article,
        )

        assert notify_calls == []
        assert stats["seen"] == 1
        assert stats["failed"] == 1
        assert "(dry run) would file auth issue" not in caplog.text


def make_notify_stub() -> tuple[list[tuple[str, str]], Any]:
    calls: list[tuple[str, str]] = []

    def stub(source_id: str, env_var: str) -> None:
        calls.append((source_id, env_var))

    return calls, stub


class TestRunPipelineAuthStartupCheck:
    def test_failed_auth_files_issue_and_skips_source(
        self, monkeypatch, tmp_path
    ) -> None:
        from kb_pipeline import state as state_module
        from kb_pipeline.pipeline import run_pipeline

        monkeypatch.delenv("BYTEBYTEGO_SUBSTACK_COOKIE", raising=False)
        monkeypatch.setattr(state_module, "STATE_PATH", tmp_path / "state.json")
        auth_source = make_auth_source()

        notify_calls, notify_fn = make_notify_stub()

        stats = run_pipeline(dry_run=False, sources=[auth_source], notify_fn=notify_fn)

        assert notify_calls == [("bytebytego", "BYTEBYTEGO_SUBSTACK_COOKIE")]
        assert stats["sources"] == 0
        assert stats["seen"] == 0

    def test_failed_auth_skips_only_that_source(self, monkeypatch, caplog) -> None:
        from kb_pipeline.pipeline import run_pipeline

        monkeypatch.delenv("BYTEBYTEGO_SUBSTACK_COOKIE", raising=False)
        caplog.set_level("INFO")
        fixture = Path(__file__).parent / "fixtures" / "plain-rss.xml"
        auth_source = make_auth_source()
        ok_source = Source(id="ok", type="rss", url=str(fixture))

        notify_calls, notify_fn = make_notify_stub()

        stats = run_pipeline(
            dry_run=True,
            sources=[auth_source, ok_source],
            notify_fn=notify_fn,
            classify_fn=stub_classify_ok,
        )

        assert notify_calls == []
        assert stats["sources"] == 1
        assert stats["written"] == 1
        assert "bytebytego" in caplog.text
        assert "BYTEBYTEGO_SUBSTACK_COOKIE" in caplog.text

    def test_passed_auth_check_does_not_notify(self, monkeypatch) -> None:
        from kb_pipeline.pipeline import run_pipeline

        monkeypatch.setenv("BYTEBYTEGO_SUBSTACK_COOKIE", "cookie")
        fixture = Path(__file__).parent / "fixtures" / "simple-rss.xml"
        auth_source = Source(
            id="bytebytego",
            type="rss",
            url=str(fixture),
            cookie_env_var="BYTEBYTEGO_SUBSTACK_COOKIE",
        )

        notify_calls, notify_fn = make_notify_stub()

        def stub_fetch_article(url: str, headers: dict[str, str], on_error: Any) -> str:
            return "markdown text " * 60

        stats = run_pipeline(
            dry_run=True,
            sources=[auth_source],
            notify_fn=notify_fn,
            fetch_article_fn=stub_fetch_article,
            classify_fn=stub_classify_ok,
        )

        assert notify_calls == []
        assert stats["sources"] == 1
        assert stats["written"] == 1
