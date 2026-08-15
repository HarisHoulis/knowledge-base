import importlib.util
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "check-fitness.py"


def _load_check_fitness() -> Any:
    spec = importlib.util.spec_from_file_location("check_fitness", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CHECK = _load_check_fitness()


def _write_package(tmp_path: Path, modules: dict[str, str]) -> Path:
    pkg = tmp_path / "kb_pipeline"
    pkg.mkdir()
    for name, content in modules.items():
        (pkg / name).write_text(content)
    return pkg


def _write_baseline(tmp_path: Path, lines: int) -> Path:
    baseline = tmp_path / "baselines.json"
    baseline.write_text(json.dumps({"pipeline.py_lines": lines}))
    return baseline


CLEAN_MODULES: dict[str, str] = {
    "config.py": "VALUE = 1\n",
    "audit.py": "from .config import VALUE\n",
    "fetcher.py": "from .config import VALUE\n",
    "llm.py": "from .config import VALUE\n",
    "state.py": "from .config import VALUE\n",
    "writer.py": "from .config import VALUE\n",
    "pipeline.py": (
        "from .audit import a\n"
        "from .config import VALUE\n"
        "from .fetcher import f\n"
        "from .llm import l\n"
        "from .state import s\n"
        "from .writer import w\n"
    ),
    "cli.py": "from . import pipeline\n",
    "__main__.py": "from .cli import main\n",
}


class TestDependencyMatrix:
    def test_clean_graph_passes(self, tmp_path):
        pkg = _write_package(tmp_path, CLEAN_MODULES)
        baseline = _write_baseline(tmp_path, 100)
        assert CHECK.run(pkg, baseline) == []

    def test_forbidden_edge_fails(self, tmp_path):
        modules = dict(CLEAN_MODULES)
        modules["fetcher.py"] = "from .config import VALUE\nfrom .writer import w\n"
        pkg = _write_package(tmp_path, modules)
        baseline = _write_baseline(tmp_path, 100)
        violations = CHECK.run(pkg, baseline)
        assert "forbidden edge: fetcher -> writer" in violations

    def test_from_import_form_collected(self, tmp_path):
        modules = dict(CLEAN_MODULES)
        modules["state.py"] = "from . import config\n"
        pkg = _write_package(tmp_path, modules)
        baseline = _write_baseline(tmp_path, 100)
        assert CHECK.run(pkg, baseline) == []


class TestSizeGuard:
    def test_growth_beyond_ten_percent_fails(self, tmp_path):
        modules = dict(CLEAN_MODULES)
        modules["pipeline.py"] = "# padded\n" * 100
        pkg = _write_package(tmp_path, modules)
        baseline = _write_baseline(tmp_path, 10)
        violations = CHECK.run(pkg, baseline)
        assert any("pipeline.py size regression" in v for v in violations)

    def test_growth_within_tolerance_passes(self, tmp_path):
        modules = dict(CLEAN_MODULES)
        modules["pipeline.py"] = "# padded\n" * 11
        pkg = _write_package(tmp_path, modules)
        baseline = _write_baseline(tmp_path, 10)
        assert CHECK.run(pkg, baseline) == []


class TestUpdateBaseline:
    def test_rewrites_baseline_with_current_line_count(self, tmp_path):
        modules = dict(CLEAN_MODULES)
        modules["pipeline.py"] = "# padded\n" * 100
        pkg = _write_package(tmp_path, modules)
        baseline = _write_baseline(tmp_path, 10)
        assert CHECK.run(pkg, baseline, update_baseline=True) == []
        assert json.loads(baseline.read_text()) == {"pipeline.py_lines": 100}


class TestMain:
    def test_forbidden_edge_exits_nonzero_with_message(
        self, tmp_path, monkeypatch, capsys
    ):
        modules = dict(CLEAN_MODULES)
        modules["fetcher.py"] = "from .config import VALUE\nfrom .writer import w\n"
        pkg = _write_package(tmp_path, modules)
        baseline = _write_baseline(tmp_path, 100)
        monkeypatch.setattr(CHECK, "PACKAGE_DIR", pkg)
        monkeypatch.setattr(CHECK, "BASELINE_PATH", baseline)
        assert CHECK.main([]) == 1
        assert "forbidden edge: fetcher -> writer" in capsys.readouterr().out

    def test_clean_graph_exits_zero(self, tmp_path, monkeypatch):
        pkg = _write_package(tmp_path, CLEAN_MODULES)
        baseline = _write_baseline(tmp_path, 100)
        monkeypatch.setattr(CHECK, "PACKAGE_DIR", pkg)
        monkeypatch.setattr(CHECK, "BASELINE_PATH", baseline)
        assert CHECK.main([]) == 0
