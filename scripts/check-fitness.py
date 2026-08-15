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


def module_names(package_dir: Path) -> list[str]:
    return sorted(
        path.stem for path in package_dir.glob("*.py") if path.stem != "__init__"
    )


def line_counts(package_dir: Path) -> dict[str, int]:
    return {
        path.stem: path.read_text().count("\n")
        for path in sorted(package_dir.glob("*.py"))
        if path.stem != "__init__"
    }


def check_dependencies(
    edges: list[tuple[str, str]], allowed_edges: set[tuple[str, str]]
) -> list[str]:
    return [
        f"forbidden edge: {source} -> {target} - edit `allowed_edges` "
        "in `scripts/baselines.json`"
        for source, target in edges
        if (source, target) not in allowed_edges
    ]


def check_coverage(modules: list[str], config_modules: list[str]) -> list[str]:
    on_disk = set(modules)
    recorded = set(config_modules)
    messages = [
        f"module `{name}` not in coverage set - run `--update-matrix`"
        for name in sorted(on_disk - recorded)
    ]
    messages += [
        f"module `{name}` in matrix but missing from package - run `--update-matrix`"
        for name in sorted(recorded - on_disk)
    ]
    return messages


def check_size(counts: dict[str, int], size_limits: dict[str, int]) -> list[str]:
    messages = []
    for name, baseline in size_limits.items():
        lines = counts.get(name, 0)
        limit = baseline * SIZE_TOLERANCE
        if lines > limit:
            messages.append(
                f"{name}.py size regression: {lines} lines exceeds baseline "
                f"{baseline} x {SIZE_TOLERANCE} = {limit:.1f}"
            )
    return messages


def run(
    package_dir: Path,
    baseline_path: Path,
    *,
    update_matrix: bool = False,
    update_baseline: bool = False,
) -> list[str]:
    config = json.loads(baseline_path.read_text())
    violations = check_dependencies(
        collect_edges(package_dir), {tuple(e) for e in config["allowed_edges"]}
    )
    if update_matrix:
        config["modules"] = module_names(package_dir)
    else:
        violations += check_coverage(module_names(package_dir), config["modules"])
    if update_baseline:
        config["size_limits"] = line_counts(package_dir)
    else:
        violations += check_size(line_counts(package_dir), config["size_limits"])
    if update_matrix or update_baseline:
        baseline_path.write_text(json.dumps(config, indent=2) + "\n")
    return violations


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--update-matrix",
        action="store_true",
        help="record the current kb_pipeline module set as the coverage baseline",
    )
    parser.add_argument(
        "--update-baseline",
        action="store_true",
        help="record the current kb_pipeline line counts as the size baselines",
    )
    args = parser.parse_args(argv)
    violations = run(
        PACKAGE_DIR,
        BASELINE_PATH,
        update_matrix=args.update_matrix,
        update_baseline=args.update_baseline,
    )
    for message in violations:
        print(f"fitness: {message}")
    return 1 if violations else 0


if __name__ == "__main__":
    raise SystemExit(main())
