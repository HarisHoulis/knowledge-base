#!/usr/bin/env python3
"""Fitness functions for kb_pipeline/ (architectural #1/#3, design #6)."""

import argparse
import ast
import json
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parent.parent
PACKAGE_DIR = ROOT / "kb_pipeline"
BASELINE_PATH = ROOT / "scripts" / "baselines.json"

SIZE_TOLERANCE = 1.1

ALLOWED_EDGES = frozenset(
    {
        ("audit", "config"),
        ("fetcher", "config"),
        ("llm", "config"),
        ("state", "config"),
        ("writer", "config"),
        ("pipeline", "audit"),
        ("pipeline", "config"),
        ("pipeline", "fetcher"),
        ("pipeline", "llm"),
        ("pipeline", "state"),
        ("pipeline", "writer"),
        ("cli", "pipeline"),
        ("__main__", "cli"),
    }
)


def collect_edges(package_dir: Path) -> list[tuple[str, str]]:
    edges: list[tuple[str, str]] = []
    for path in sorted(package_dir.glob("*.py")):
        tree = ast.parse(path.read_text())
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.level == 1:
                if node.module is not None:
                    edges.append((path.stem, node.module))
                else:
                    for alias in node.names:
                        edges.append((path.stem, alias.name))
    return edges


def check_dependencies(edges: list[tuple[str, str]]) -> list[str]:
    return [
        f"forbidden edge: {source} -> {target}"
        for source, target in edges
        if (source, target) not in ALLOWED_EDGES
    ]


def pipeline_lines(package_dir: Path) -> int:
    return (package_dir / "pipeline.py").read_text().count("\n")


def check_size(package_dir: Path, baseline_lines: int) -> list[str]:
    lines = pipeline_lines(package_dir)
    limit = baseline_lines * SIZE_TOLERANCE
    if lines > limit:
        return [
            f"pipeline.py size regression: {lines} lines exceeds baseline "
            f"{baseline_lines} x {SIZE_TOLERANCE} = {limit:.1f}"
        ]
    return []


def run(
    package_dir: Path, baseline_path: Path, *, update_baseline: bool = False
) -> list[str]:
    violations = check_dependencies(collect_edges(package_dir))
    if update_baseline:
        baseline_path.write_text(
            json.dumps({"pipeline.py_lines": pipeline_lines(package_dir)}) + "\n"
        )
        return violations
    baseline = json.loads(baseline_path.read_text())
    return violations + check_size(package_dir, baseline["pipeline.py_lines"])


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--update-baseline",
        action="store_true",
        help="record the current pipeline.py line count as the new baseline",
    )
    args = parser.parse_args(argv)
    violations = run(PACKAGE_DIR, BASELINE_PATH, update_baseline=args.update_baseline)
    for message in violations:
        print(f"fitness: {message}")
    return 1 if violations else 0


if __name__ == "__main__":
    raise SystemExit(main())
