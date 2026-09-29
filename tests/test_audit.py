import json

import requests

from kb_pipeline.audit import _run_audit, classification_audit, content_audit
from kb_pipeline.config import LLM_API_KEY, LLM_API_URL


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


class _StubPost:
    def __init__(self, body):
        self._body = body

    def raise_for_status(self):
        pass

    def json(self):
        return self._body


def _body(content: str):
    return {"choices": [{"message": {"content": content}}]}


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


class TestRunAuditPostFn:
    def test_post_fn_receives_request_params(self):
        calls = []

        def post(*args, **kwargs):
            calls.append((args, kwargs))
            return _StubPost(_body(json.dumps({"pass": True})))

        _run_audit("audit prompt", post_fn=post)
        assert len(calls) == 1
        args, kwargs = calls[0]
        assert args == (f"{LLM_API_URL}/chat/completions",)
        assert kwargs["headers"] == {"Authorization": f"Bearer {LLM_API_KEY}"}
        assert kwargs["json"]["messages"][1] == {
            "role": "user",
            "content": "audit prompt",
        }
        assert kwargs["timeout"] == 60

    def test_post_fn_body_disables_thinking_and_raises_max_tokens(self):
        bodies = []

        def post(*args, **kwargs):
            bodies.append(kwargs["json"])
            return _StubPost(_body(json.dumps({"pass": True})))

        _run_audit("audit prompt", post_fn=post)
        assert len(bodies) == 1
        assert bodies[0]["thinking"] == {"type": "disabled"}
        assert bodies[0]["max_tokens"] == 1000
        assert bodies[0]["response_format"] == {"type": "json_object"}
        assert bodies[0]["temperature"] == 0.1

    def test_post_fn_valid_fail_json_returns_it_verbatim(self):
        issues = [{"field": "summary", "description": "test issue"}]

        def post(*args, **kwargs):
            return _StubPost(_body(json.dumps({"pass": False, "issues": issues})))

        assert _run_audit("p", post_fn=post) == {"pass": False, "issues": issues}

    def test_audit_fn_is_used_and_post_fn_is_not_called(self):
        def post(*args, **kwargs):
            raise AssertionError("post_fn must not be called when audit_fn is given")

        result = _run_audit("p", audit_fn=stub_pass, post_fn=post)
        assert result == {"pass": True}

    def test_post_fn_valid_json_returns_pass(self):
        def post(*args, **kwargs):
            return _StubPost(_body(json.dumps({"pass": True})))

        assert _run_audit("p", post_fn=post) == {"pass": True}

    def test_post_fn_empty_content_is_not_a_pass(self):
        def post(*args, **kwargs):
            return _StubPost(_body(""))

        assert _run_audit("p", post_fn=post) == {"pass": False}

    def test_post_fn_unparseable_content_is_not_a_pass(self):
        def post(*args, **kwargs):
            return _StubPost(_body("not json"))

        assert _run_audit("p", post_fn=post) == {"pass": False}

    def test_post_fn_exception_is_not_a_pass(self):
        def post(*args, **kwargs):
            raise requests.RequestException("boom")

        assert _run_audit("p", post_fn=post) == {"pass": False}
