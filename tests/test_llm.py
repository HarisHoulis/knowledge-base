import json

import pytest
import requests

from kb_pipeline.llm import ClassifyFailure, ClassifyFailureKind, classify_summarize


class _StubPost:
    def __init__(self, body):
        self._body = body

    def raise_for_status(self):
        pass

    def json(self):
        return self._body


def _body(content, finish_reason="stop", usage=None):
    return {
        "choices": [{"message": {"content": content}, "finish_reason": finish_reason}],
        "usage": usage or {},
    }


VALID = {
    "domain": "ai-workflows",
    "subdomain": "coding-agents",
    "concept": "observability",
    "title": "t",
    "summary": "s",
    "key_points": [],
}


def _valid_content():
    return json.dumps(VALID)


@pytest.fixture(autouse=True)
def _api_key(monkeypatch):
    monkeypatch.setattr("kb_pipeline.llm.LLM_API_KEY", "test-key")


def _run(body, meta):
    return classify_summarize(
        "some text", meta, post_fn=lambda *a, **k: _StubPost(body)
    )


def test_empty_content_logs_shape(caplog):
    body = _body(
        "",
        finish_reason="length",
        usage={
            "completion_tokens": 1,
            "completion_tokens_details": {"reasoning_tokens": 1999},
        },
    )
    meta = {"title": "Some Title"}
    result = _run(body, meta)
    assert isinstance(result, ClassifyFailure)
    assert result.kind is ClassifyFailureKind.PARSE
    assert "len(content)=0" in caplog.text
    assert "finish_reason='length'" in caplog.text
    assert "Some Title" in caplog.text
    assert "content_excerpt=''" in caplog.text
    assert "reasoning_tokens" in caplog.text


def test_truncated_content_surfaces_excerpt(caplog):
    content = '{"domain": "android-kotlin", "summ'
    body = _body(content, finish_reason="length")
    result = _run(body, {"title": "Trunc"})
    assert isinstance(result, ClassifyFailure)
    assert result.kind is ClassifyFailureKind.PARSE
    assert "finish_reason='length'" in caplog.text
    assert "android-kotlin" in caplog.text
    assert "len(content)=" in caplog.text and "len(content)=0" not in caplog.text


def test_fenced_content_surfaces_excerpt(caplog):
    content = "```json\n" + _valid_content() + "\n```"
    body = _body(content)
    result = _run(body, {"title": "Fenced"})
    assert isinstance(result, ClassifyFailure)
    assert result.kind is ClassifyFailureKind.PARSE
    assert "```json" in caplog.text


def test_valid_json_returns_dict_no_warning(caplog):
    body = _body(_valid_content())
    assert _run(body, {"title": "Valid"}) == VALID
    assert "parse failed" not in caplog.text


def test_request_exception_keeps_message(caplog):
    def raising(*a, **k):
        raise requests.RequestException("boom")

    result = classify_summarize("some text", {"title": "X"}, post_fn=raising)
    assert isinstance(result, ClassifyFailure)
    assert result.kind is ClassifyFailureKind.REQUEST
    assert "LLM request failed" in caplog.text
    assert "content_excerpt" not in caplog.text
