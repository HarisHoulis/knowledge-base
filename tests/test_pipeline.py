from pathlib import Path
from typing import Any, Callable, Optional

from kb_pipeline.audit import AuditResult
from kb_pipeline.config import SOURCES, Source

SAMPLE_TEXT = "some source text"
SAMPLE_URL = "https://example.com/article"
SAMPLE_META: dict[str, Any] = {"title": "Test", "link": SAMPLE_URL}
SAMPLE_DRAFT = Path("/tmp/drafts/test.md")
SAMPLE_RESULT: dict[str, Any] = {
    "domain": "a", "subdomain": "b", "concept": "c",
    "summary": "test", "key_points": [],
}


def stub_audit_pass(data: Any, source_text: str) -> AuditResult:
    return {"pass": True}


def stub_audit_fail(data: Any, source_text: str) -> AuditResult:
    return {"pass": False, "issues": [{"field": "summary", "description": "test issue"}]}


def stub_classify_ok(
    text: str, meta: dict[str, Any], audit_feedback: Optional[str] = None
) -> dict[str, Any]:
    return dict(SAMPLE_RESULT)


class CountedAuditStub:
    def __init__(self, *results: AuditResult) -> None:
        self.results = list(results)
        self.call_count = 0

    def __call__(self, data: Any, source_text: str) -> AuditResult:
        idx = self.call_count if self.call_count < len(self.results) else len(self.results) - 1
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
            SAMPLE_RESULT, SAMPLE_TEXT, SAMPLE_URL, SAMPLE_META, SAMPLE_DRAFT,
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
            {"pass": False, "issues": [{"field": "summary", "description": "wrong summary"}]},
            {"pass": True},
        )

        ok = _audit_with_retry(
            SAMPLE_RESULT, SAMPLE_TEXT, SAMPLE_URL, SAMPLE_META, SAMPLE_DRAFT,
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
            {"pass": False, "issues": [{"field": "domain", "description": "wrong domain"}]},
            {"pass": True},
        )

        ok = _audit_with_retry(
            SAMPLE_RESULT, SAMPLE_TEXT, SAMPLE_URL, SAMPLE_META, SAMPLE_DRAFT,
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
            {"pass": False, "issues": [{"field": "summary", "description": "bad summary"}]},
            {"pass": True},
        )

        ok = _audit_with_retry(
            SAMPLE_RESULT, SAMPLE_TEXT, SAMPLE_URL, SAMPLE_META, SAMPLE_DRAFT,
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
            SAMPLE_RESULT, SAMPLE_TEXT, SAMPLE_URL, SAMPLE_META, SAMPLE_DRAFT,
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
            {"pass": False, "issues": [{"field": "summary", "description": "still wrong"}]},
            {"pass": False, "issues": [{"field": "summary", "description": "still wrong 2"}]},
        )

        ok = _audit_with_retry(
            SAMPLE_RESULT, SAMPLE_TEXT, SAMPLE_URL, SAMPLE_META, SAMPLE_DRAFT,
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

        assert _extract_youtube_video_id("https://www.youtube.com/watch?v=dQw4w9WgXcQ") == "dQw4w9WgXcQ"

    def test_short_url(self) -> None:
        from kb_pipeline.pipeline import _extract_youtube_video_id

        assert _extract_youtube_video_id("https://youtu.be/dQw4w9WgXcQ") == "dQw4w9WgXcQ"

    def test_with_query_params(self) -> None:
        from kb_pipeline.pipeline import _extract_youtube_video_id

        assert _extract_youtube_video_id("https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=30s") == "dQw4w9WgXcQ"

    def test_non_youtube_url(self) -> None:
        from kb_pipeline.pipeline import _extract_youtube_video_id

        assert _extract_youtube_video_id("https://example.com/article") is None

    def test_empty_url(self) -> None:
        from kb_pipeline.pipeline import _extract_youtube_video_id

        assert _extract_youtube_video_id("") is None

    def test_invalid_video_id_length(self) -> None:
        from kb_pipeline.pipeline import _extract_youtube_video_id

        assert _extract_youtube_video_id("https://www.youtube.com/watch?v=invalid") is None


SHORT_CONTENT = "<p>Read it at code.cash.app/...</p>"


class TestRunPipelineLinkFallback:
    def test_rss_short_content_falls_back_to_link(self):
        from kb_pipeline.pipeline import run_pipeline

        fixture = Path(__file__).parent / "fixtures" / "redirect-rss.xml"
        source = Source(id="test", type="rss", url=str(fixture))

        def stub_fetch_url(url: str) -> str:
            if "real-article" in url:
                return "This is the full article content with enough text to pass the 200 character threshold for classification. " * 10
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

    def test_youtube_short_content_no_fallback(self, monkeypatch):
        from kb_pipeline.pipeline import run_pipeline

        def mock_fetch(src):
            from feedparser import FeedParserDict
            return [FeedParserDict({"link": "https://www.youtube.com/watch?v=test123", "title": "Test Video"})]

        monkeypatch.setattr("kb_pipeline.pipeline.fetch_youtube", mock_fetch)

        source = Source(id="test", type="youtube", url="https://www.youtube.com/feeds/videos.xml?channel_id=UC_test")

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

        stats = run_pipeline(dry_run=True, sources=[source], transcript_fn=spy_transcript)

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
