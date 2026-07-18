import os
import tempfile
from pathlib import Path

from kb_pipeline.audit import classification_audit, content_audit
from kb_pipeline.config import SOURCES, Source
from kb_pipeline.pipeline import run_pipeline


CORRECT_SOURCE = (
    "Structured concurrency is a programming paradigm that ensures coroutines are "
    "launched within a well-defined scope. When the scope completes or is cancelled, "
    "all coroutines within it are automatically cancelled, which prevents coroutine "
    "leaks and makes error handling predictable. Kotlin implements this through "
    "constructs like coroutineScope and supervisorScope. The key benefit is that "
    "developers no longer need to manually track and cancel coroutines; the scope "
    "manages the lifecycle automatically."
)

CORRECT_DATA = {
    "domain": "android-kotlin",
    "subdomain": "coroutines",
    "concept": "structured-concurrency",
    "title": "Structured Concurrency in Kotlin",
    "summary": (
        "Structured concurrency is a paradigm where coroutines are launched within "
        "defined scopes, ensuring automatic cancellation on scope completion or "
        "failure. This prevents coroutine leaks and simplifies error handling. "
        "Kotlin provides this through coroutineScope and supervisorScope, allowing "
        "developers to manage coroutine lifecycles without manual tracking."
    ),
    "key_points": [
        "Coroutines are tied to a scope that manages their lifecycle",
        "Automatic cancellation propagates from parent to child coroutines",
    ],
    "sources": [
        {"title": "Structured Concurrency in Kotlin", "url": "https://example.com/structured-concurrency"}
    ],
}


INCORRECT_SOURCE = (
    "Python is a high-level, interpreted programming language created by Guido van "
    "Rossum and first released in 1991. It emphasizes code readability with its "
    "notable use of significant indentation. Python's design philosophy, summed up "
    "by the Zen of Python, includes aphorisms like 'Beautiful is better than ugly' "
    "and 'Simple is better than complex'."
)

INCORRECT_DATA = {
    "domain": "python-backend",
    "subdomain": "language-basics",
    "concept": "python-intro",
    "title": "Python Overview",
    "summary": (
        "Python is a compiled programming language created by Brendan Eich and "
        "first released in 1995. It emphasizes code readability through the use "
        "of braces for block delimiters."
    ),
    "key_points": [
        "Python uses braces for block structure",
        "Python was created by Brendan Eich",
    ],
    "sources": [
        {"title": "Python History", "url": "https://example.com/python"}
    ],
}


def test_classification_audit_stub_returns_pass():
    result = classification_audit({"domain": "ai-workflows"}, "some source text")
    assert result == {"pass": True}


def test_content_audit_known_correct():
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        from pytest import skip
        skip("DEEPSEEK_API_KEY not set")
    result = content_audit(CORRECT_DATA, CORRECT_SOURCE)
    assert result == {"pass": True}


def test_content_audit_known_incorrect():
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        from pytest import skip
        skip("DEEPSEEK_API_KEY not set")
    result = content_audit(INCORRECT_DATA, INCORRECT_SOURCE)
    assert result["pass"] is False
    assert len(result["issues"]) >= 1
    assert all(i["field"] == "summary" for i in result["issues"])


def test_audit_dry_run_leaves_no_drafts():
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        from pytest import skip
        skip("DEEPSEEK_API_KEY not set")

    fixture = Path(__file__).parent / "fixtures" / "simple-rss.xml"
    source = Source(id="test", type="rss", url=str(fixture))

    with tempfile.TemporaryDirectory() as tmp:
        kb_path = Path(tmp)
        from kb_pipeline import config
        old_kb = config.KB_PATH
        config.KB_PATH = kb_path

        try:
            stats = run_pipeline(dry_run=True, audit=True, sources=[source])
            assert stats["sources"] == 1
            assert stats["seen"] >= 1

            drafts_dir = kb_path / config.DRAFTS_DIR
            if drafts_dir.exists():
                files = list(drafts_dir.rglob("*"))
                assert not files, f"expected no draft files left, found: {files}"
        finally:
            config.KB_PATH = old_kb
