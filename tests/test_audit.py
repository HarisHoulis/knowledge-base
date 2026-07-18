import os
import tempfile
from pathlib import Path

from kb_pipeline.audit import classification_audit, content_audit
from kb_pipeline.config import SOURCES, Source
from kb_pipeline.pipeline import run_pipeline


def test_classification_audit_stub_returns_pass():
    result = classification_audit({"domain": "ai-workflows"}, "some source text")
    assert result == {"pass": True}


def test_content_audit_stub_returns_pass():
    result = content_audit({"title": "test"}, "some source text")
    assert result == {"pass": True}


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
