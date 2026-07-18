import json

from kb_pipeline.audit import classification_audit, content_audit


def stub_pass(prompt: str) -> str:
    return json.dumps({"pass": True})


def stub_fail(prompt: str) -> str:
    return json.dumps({"pass": False, "issues": [{"field": "summary", "description": "test issue"}]})


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
        assert result == {"pass": False, "issues": [{"field": "summary", "description": "test issue"}]}

    def test_malformed_json_falls_back(self):
        result = classification_audit(DATA, TEXT, audit_fn=stub_malformed)
        assert result == {"pass": True}

    def test_exception_falls_back(self):
        result = classification_audit(DATA, TEXT, audit_fn=stub_exception)
        assert result == {"pass": True}

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
        assert result == {"pass": False, "issues": [{"field": "summary", "description": "test issue"}]}

    def test_malformed_json_falls_back(self):
        result = content_audit(DATA, TEXT, audit_fn=stub_malformed)
        assert result == {"pass": True}

    def test_exception_falls_back(self):
        result = content_audit(DATA, TEXT, audit_fn=stub_exception)
        assert result == {"pass": True}

    def test_prompt_contains_summary(self):
        prompts = []

        def capture(p: str) -> str:
            prompts.append(p)
            return json.dumps({"pass": True})

        content_audit(DATA, TEXT, audit_fn=capture)
        assert len(prompts) == 1
        assert "some summary" in prompts[0]
