import os
import tempfile
from pathlib import Path

import pytest

from kb_pipeline import config
from kb_pipeline.config import Source
from kb_pipeline.fetcher import fetch_rss, extract_text
from kb_pipeline.llm import classify_summarize
from kb_pipeline.pipeline import run_pipeline

FIXTURE = Path(__file__).parent.parent / "fixtures" / "simple-rss.xml"
EXPECTED_KEYS = {"domain", "subdomain", "concept", "title", "summary", "key_points", "sources"}


@pytest.mark.integration
class TestPipelineIntegration:

    def test_llm_returns_valid_json_from_fixture(self) -> None:
        if not os.environ.get("DEEPSEEK_API_KEY"):
            pytest.skip("DEEPSEEK_API_KEY not set")

        source = Source(id="test", type="rss", url=str(FIXTURE))
        entries = fetch_rss(source)
        assert len(entries) >= 1

        entry = entries[0]
        content = entry.get("content", [{}])[0].get("value", entry.get("summary", ""))
        text = extract_text(content)

        result = classify_summarize(text, entry)
        assert result is not None

        missing = EXPECTED_KEYS - set(result.keys())
        assert not missing, f"LLM output missing keys: {missing}"

        assert result["domain"] in config.VALID_DOMAINS
        for key in ("subdomain", "concept", "title", "summary"):
            assert isinstance(result[key], str) and len(result[key]) > 0
        assert isinstance(result["key_points"], list)
        assert isinstance(result["sources"], list)

    def test_dry_run_writes_no_files(self) -> None:
        if not os.environ.get("DEEPSEEK_API_KEY"):
            pytest.skip("DEEPSEEK_API_KEY not set")

        source = Source(id="test", type="rss", url=str(FIXTURE))

        with tempfile.TemporaryDirectory() as tmp:
            kb_path = Path(tmp)
            old_kb = config.KB_PATH
            config.KB_PATH = kb_path

            try:
                stats = run_pipeline(dry_run=True, sources=[source])

                assert stats["sources"] == 1
                assert stats["seen"] >= 1

                concepts = kb_path / config.CONCEPTS_DIR
                drafts = kb_path / config.DRAFTS_DIR
                concept_files = list(concepts.rglob("*")) if concepts.exists() else []
                draft_files = list(drafts.rglob("*")) if drafts.exists() else []
                assert not concept_files, f"dry-run wrote concept files: {concept_files}"
                assert not draft_files, f"dry-run wrote draft files: {draft_files}"
            finally:
                config.KB_PATH = old_kb
