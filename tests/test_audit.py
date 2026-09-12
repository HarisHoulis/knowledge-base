import json

import pytest
import requests

from kb_pipeline.audit import classification_audit, content_audit


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


def stub_pass(prompt: str) -> str:
    return json.dumps({"pass": True})


def stub_fail(prompt: str) -> str:
    return json.dumps(
        {"pass": False, "issues": [{"field": "summary", "description": "test issue"}]}
    )


def stub_malformed(prompt: str) -> str:
    return "not json"


def stub_exception(prompt: str) -> str:
    raise ConnectionError("test error")


DATA = {"domain": "a", "subdomain": "b", "concept": "c", "summary": "some summary"}
TEXT = "some source text"


class TestClassificationAudit:
    def test_returns_pass(self):
        result = classification_audit(DATA, TEXT, audit_fn=stub_pass)
        assert result == {"pass": True}

    def test_returns_fail(self):
        result = classification_audit(DATA, TEXT, audit_fn=stub_fail)
        assert result == {
            "pass": False,
            "issues": [{"field": "summary", "description": "test issue"}],
        }

    def test_malformed_json_is_not_a_pass(self):
        result = classification_audit(DATA, TEXT, audit_fn=stub_malformed)
        assert result == {"pass": False}

    def test_exception_is_not_a_pass(self):
        result = classification_audit(DATA, TEXT, audit_fn=stub_exception)
        assert result == {"pass": False}

    def test_prompt_contains_classification_fields(self):
        prompts = []

        def capture(p: str) -> str:
            prompts.append(p)
            return json.dumps({"pass": True})

        classification_audit(DATA, TEXT, audit_fn=capture)
        assert len(prompts) == 1
        body = prompts[0]
        assert "Domain: a" in body
        assert "Subdomain: b" in body
        assert "Concept: c" in body

    def test_empty_content_logs_shape(self, caplog):
        body = _body(
            "",
            finish_reason="length",
            usage={
                "completion_tokens": 1,
                "completion_tokens_details": {"reasoning_tokens": 1999},
            },
        )
        result = classification_audit(
            DATA, TEXT, post_fn=lambda *a, **k: _StubPost(body)
        )
        assert result == {"pass": False}
        assert "finish_reason='length'" in caplog.text
        assert "len(content)=0" in caplog.text
        assert "reasoning_tokens" in caplog.text
        assert "content_excerpt=''" in caplog.text

    def test_truncated_content_surfaces_excerpt(self, caplog):
        content = '{"pass": true'
        body = _body(content, finish_reason="length")
        result = classification_audit(
            DATA, TEXT, post_fn=lambda *a, **k: _StubPost(body)
        )
        assert result == {"pass": False}
        assert "finish_reason='length'" in caplog.text
        assert '"pass": true' in caplog.text
        assert "len(content)=0" not in caplog.text

    def test_fenced_content_surfaces_excerpt(self, caplog):
        content = '```json\n{"pass": true}\n```'
        body = _body(content)
        result = classification_audit(
            DATA, TEXT, post_fn=lambda *a, **k: _StubPost(body)
        )
        assert result == {"pass": False}
        assert "```json" in caplog.text

    def test_prose_leading_content_surfaces_excerpt(self, caplog):
        content = 'Here is the audit result: {"pass": true}'
        body = _body(content)
        result = classification_audit(
            DATA, TEXT, post_fn=lambda *a, **k: _StubPost(body)
        )
        assert result == {"pass": False}
        assert "Here is the audit result" in caplog.text

    def test_audit_fn_takes_precedence_over_post_fn(self):
        def post_should_not_run(*args, **kwargs):
            raise AssertionError("post_fn should not be called")

        result = classification_audit(
            DATA, TEXT, audit_fn=stub_pass, post_fn=post_should_not_run
        )
        assert result == {"pass": True}


class TestContentAudit:
    def test_returns_pass(self):
        result = content_audit(DATA, TEXT, audit_fn=stub_pass)
        assert result == {"pass": True}

    def test_returns_fail(self):
        result = content_audit(DATA, TEXT, audit_fn=stub_fail)
        assert result == {
            "pass": False,
            "issues": [{"field": "summary", "description": "test issue"}],
        }

    def test_malformed_json_is_not_a_pass(self):
        result = content_audit(DATA, TEXT, audit_fn=stub_malformed)
        assert result == {"pass": False}

    def test_exception_is_not_a_pass(self):
        result = content_audit(DATA, TEXT, audit_fn=stub_exception)
        assert result == {"pass": False}

    def test_prompt_contains_summary(self):
        prompts = []

        def capture(p: str) -> str:
            prompts.append(p)
            return json.dumps({"pass": True})

        content_audit(DATA, TEXT, audit_fn=capture)
        assert len(prompts) == 1
        assert "some summary" in prompts[0]

    def test_request_exception_logs_no_excerpt(self, caplog):
        def raising(*args, **kwargs):
            raise requests.RequestException("boom")

        result = content_audit(DATA, TEXT, post_fn=raising)
        assert result == {"pass": False}
        assert "boom" in caplog.text
        assert "content_excerpt" not in caplog.text

    @pytest.mark.parametrize("body", [{"usage": {}}, {"choices": [{}]}])
    def test_malformed_body_is_not_a_pass(self, caplog, body):
        result = content_audit(DATA, TEXT, post_fn=lambda *a, **k: _StubPost(body))
        assert result == {"pass": False}
        assert "audit failed" in caplog.text

    def test_non_string_content_is_not_a_pass(self, caplog):
        body = _body(None)
        result = content_audit(DATA, TEXT, post_fn=lambda *a, **k: _StubPost(body))
        assert result == {"pass": False}
        assert "audit failed" in caplog.text

    def test_valid_body_returns_dict_no_warning(self, caplog):
        body = _body(json.dumps({"pass": True}))
        result = content_audit(DATA, TEXT, post_fn=lambda *a, **k: _StubPost(body))
        assert result == {"pass": True}
        assert "audit failed" not in caplog.text
