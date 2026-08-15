import importlib.util
import json
from pathlib import Path
from typing import Any, Optional

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "check-fitness.py"


def _load_check_fitness() -> Any:
    spec = importlib.util.spec_from_file_location("check_fitness", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CHECK_FITNESS = _load_check_fitness()


def _write_package(tmp_path: Path, modules: dict[str, str]) -> Path:
    pkg = tmp_path / "kb_pipeline"
    pkg.mkdir()
    for name, content in modules.items():
        (pkg / name).write_text(content)
    return pkg


def _write_config(
    tmp_path: Path,
    *,
    allowed_edges: Optional[list[list[str]]] = None,
    modules: Optional[list[str]] = None,
    size_limits: Optional[dict[str, int]] = None,
) -> Path:
    config = {
        "allowed_edges": DEFAULT_EDGES if allowed_edges is None else allowed_edges,
        "modules": DEFAULT_MODULES if modules is None else modules,
        "size_limits": DEFAULT_SIZE_LIMITS if size_limits is None else size_limits,
    }
    baseline = tmp_path / "baselines.json"
    baseline.write_text(json.dumps(config))
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

DEFAULT_MODULES: list[str] = [
    "__main__",
    "audit",
    "cli",
    "config",
    "fetcher",
    "llm",
    "pipeline",
    "state",
    "writer",
]

DEFAULT_EDGES: list[list[str]] = [
    ["audit", "config"],
    ["fetcher", "config"],
    ["llm", "config"],
    ["state", "config"],
    ["writer", "config"],
    ["pipeline", "audit"],
    ["pipeline", "config"],
    ["pipeline", "fetcher"],
    ["pipeline", "llm"],
    ["pipeline", "state"],
    ["pipeline", "writer"],
    ["cli", "pipeline"],
    ["__main__", "cli"],
]

DEFAULT_SIZE_LIMITS: dict[str, int] = {
    "__main__": 10,
    "audit": 10,
    "cli": 10,
    "config": 10,
    "fetcher": 10,
    "llm": 10,
    "pipeline": 10,
    "state": 10,
    "writer": 10,
}


class TestDependencyMatrix:
    def test_clean_graph_passes(self, tmp_path):
        pkg = _write_package(tmp_path, CLEAN_MODULES)
        baseline = _write_config(tmp_path)
        assert CHECK_FITNESS.run(pkg, baseline) == []

    def test_forbidden_edge_fails(self, tmp_path):
        modules = dict(CLEAN_MODULES)
        modules["fetcher.py"] = "from .config import VALUE\nfrom .writer import w\n"
        pkg = _write_package(tmp_path, modules)
        baseline = _write_config(tmp_path)
        violations = CHECK_FITNESS.run(pkg, baseline)
        assert any("forbidden edge: fetcher -> writer" in v for v in violations)

    def test_from_import_form_collected(self, tmp_path):
        modules = dict(CLEAN_MODULES)
        modules["state.py"] = "from . import config\n"
        pkg = _write_package(tmp_path, modules)
        baseline = _write_config(tmp_path)
        assert CHECK_FITNESS.run(pkg, baseline) == []


class TestCoverageGuard:
    def test_new_module_fails(self, tmp_path):
        modules = dict(CLEAN_MODULES)
        modules["searcher.py"] = "QUERY = 1\n"
        pkg = _write_package(tmp_path, modules)
        baseline = _write_config(tmp_path)
        violations = CHECK_FITNESS.run(pkg, baseline)
        assert any("module `searcher` not in coverage set" in v for v in violations)

    def test_stale_matrix_entry_fails(self, tmp_path):
        pkg = _write_package(tmp_path, CLEAN_MODULES)
        baseline = _write_config(tmp_path, modules=[*DEFAULT_MODULES, "ghost"])
        violations = CHECK_FITNESS.run(pkg, baseline)
        assert any("module `ghost` in matrix but missing" in v for v in violations)

    def test_renamed_module_reported_as_new_and_stale(self, tmp_path):
        modules = dict(CLEAN_MODULES)
        modules.pop("audit.py")
        modules["auditor.py"] = "VALUE = 1\n"
        pkg = _write_package(tmp_path, modules)
        baseline = _write_config(tmp_path)
        violations = CHECK_FITNESS.run(pkg, baseline)
        assert any("module `auditor` not in coverage set" in v for v in violations)
        assert any("module `audit` in matrix but missing" in v for v in violations)


class TestUpdateMatrix:
    def test_adds_new_module_without_touching_edges(self, tmp_path):
        modules = dict(CLEAN_MODULES)
        modules["searcher.py"] = "QUERY = 1\n"
        pkg = _write_package(tmp_path, modules)
        baseline = _write_config(tmp_path)
        assert CHECK_FITNESS.run(pkg, baseline, update_matrix=True) == []
        config = json.loads(baseline.read_text())
        assert "searcher" in config["modules"]
        assert config["allowed_edges"] == DEFAULT_EDGES

    def test_does_not_clear_forbidden_edge(self, tmp_path):
        modules = dict(CLEAN_MODULES)
        modules["searcher.py"] = "from .writer import w\n"
        pkg = _write_package(tmp_path, modules)
        baseline = _write_config(tmp_path)
        violations = CHECK_FITNESS.run(pkg, baseline, update_matrix=True)
        assert any("forbidden edge: searcher -> writer" in v for v in violations)
        assert json.loads(baseline.read_text())["allowed_edges"] == DEFAULT_EDGES


class TestSizeGuard:
    def test_non_pipeline_growth_beyond_ten_percent_fails(self, tmp_path):
        modules = dict(CLEAN_MODULES)
        modules["llm.py"] = "# padded\n" * 100
        pkg = _write_package(tmp_path, modules)
        baseline = _write_config(tmp_path, size_limits={"llm": 10})
        violations = CHECK_FITNESS.run(pkg, baseline)
        assert any("llm.py size regression" in v for v in violations)

    def test_growth_within_tolerance_passes(self, tmp_path):
        modules = dict(CLEAN_MODULES)
        modules["llm.py"] = "# padded\n" * 11
        pkg = _write_package(tmp_path, modules)
        baseline = _write_config(tmp_path, size_limits={"llm": 10})
        assert CHECK_FITNESS.run(pkg, baseline) == []


class TestUpdateBaseline:
    def test_rewrites_size_limits_with_current_line_counts(self, tmp_path):
        modules = dict(CLEAN_MODULES)
        modules["llm.py"] = "# padded\n" * 100
        pkg = _write_package(tmp_path, modules)
        baseline = _write_config(tmp_path, size_limits={"llm": 10})
        assert CHECK_FITNESS.run(pkg, baseline, update_baseline=True) == []
        config = json.loads(baseline.read_text())
        assert config["size_limits"]["llm"] == 100
        assert config["modules"] == DEFAULT_MODULES


class TestMain:
    def test_forbidden_edge_exits_nonzero_with_message(
        self, tmp_path, monkeypatch, capsys
    ):
        modules = dict(CLEAN_MODULES)
        modules["fetcher.py"] = "from .config import VALUE\nfrom .writer import w\n"
        pkg = _write_package(tmp_path, modules)
        baseline = _write_config(tmp_path)
        monkeypatch.setattr(CHECK_FITNESS, "PACKAGE_DIR", pkg)
        monkeypatch.setattr(CHECK_FITNESS, "BASELINE_PATH", baseline)
        assert CHECK_FITNESS.main([]) == 1
        assert "forbidden edge: fetcher -> writer" in capsys.readouterr().out

    def test_clean_graph_exits_zero(self, tmp_path, monkeypatch):
        pkg = _write_package(tmp_path, CLEAN_MODULES)
        baseline = _write_config(tmp_path)
        monkeypatch.setattr(CHECK_FITNESS, "PACKAGE_DIR", pkg)
        monkeypatch.setattr(CHECK_FITNESS, "BASELINE_PATH", baseline)
        assert CHECK_FITNESS.main([]) == 0
