#!/usr/bin/env python3
"""
Validate demo SKILL.md usability in this repo.

What we check (lightweight, no external deps):
- YAML frontmatter presence + minimal required keys (name/description) for installable skills
- Common referenced paths in markdown: `scripts/...`, `resources/...`, and shell snippets like `python scripts/x.py`
- Basic JSON parse for referenced *.json
- Optional syntax checks: Python py_compile, Node --check (best-effort)

This is intentionally conservative: it won't execute arbitrary scripts.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Optional


FRONTMATTER_RE = re.compile(r"^---\s*$")
KEY_VALUE_RE = re.compile(r"^(?P<key>[A-Za-z0-9_-]+)\s*:\s*(?P<value>.*)\s*$")

INLINE_CODE_PATH_RE = re.compile(r"`(?P<path>(?:scripts|resources)/[^`\s]+?)`")
SHELL_PY_PATH_RE = re.compile(r"(?m)^\s*python(?:3)?\s+(?P<path>scripts/[^\s]+?\.py)\b")
SHELL_NODE_PATH_RE = re.compile(r"(?m)^\s*node\s+(?P<path>scripts/[^\s]+?\.js)\b")

PLACEHOLDER_BRACES_RE = re.compile(r"\{[^{}\n]{2,80}\}")


@dataclass
class SkillCheckResult:
    skill_md: Path
    category: str  # demo_example | template | installed_skill | other
    installable_location_ok: bool
    has_frontmatter: bool
    frontmatter_name_ok: bool
    frontmatter_description_ok: bool
    referenced_paths: list[str] = field(default_factory=list)
    missing_paths: list[str] = field(default_factory=list)
    json_parse_errors: list[str] = field(default_factory=list)
    python_syntax_errors: list[str] = field(default_factory=list)
    node_syntax_errors: list[str] = field(default_factory=list)
    placeholder_warnings: list[str] = field(default_factory=list)

    def is_pass_for_category(self) -> bool:
        # "Pass" means: nothing is obviously broken for the intended category.
        if self.category == "installed_skill":
            if not (self.installable_location_ok and self.has_frontmatter):
                return False
            if not (self.frontmatter_name_ok and self.frontmatter_description_ok):
                return False
        # For demos/templates, we don't require frontmatter; but broken references are still failures.
        if self.missing_paths:
            return False
        if self.json_parse_errors:
            return False
        if self.python_syntax_errors:
            return False
        if self.node_syntax_errors:
            return False
        return True


def _read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def _detect_category(skill_md: Path, repo_root: Path) -> str:
    rel = skill_md.relative_to(repo_root)
    parts = rel.parts
    if parts[:2] == (".claude", "skills"):
        return "installed_skill"
    if parts and parts[0] == "examples":
        return "demo_example"
    if parts and parts[0] == "templates":
        return "template"
    return "other"


def _is_installable_location_ok(skill_md: Path, repo_root: Path) -> bool:
    rel = skill_md.relative_to(repo_root)
    parts = rel.parts
    # Claude Code recognizes .claude/skills/<skill-name>/SKILL.md
    return len(parts) >= 4 and parts[:2] == (".claude", "skills") and parts[-1] == "SKILL.md"


def _parse_frontmatter(text: str) -> tuple[bool, dict[str, str]]:
    """
    Minimal frontmatter parsing:
    - must start at first non-empty line with '---'
    - collect key: value pairs until next '---'
    """
    lines = text.splitlines()
    i = 0
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    if i >= len(lines) or not FRONTMATTER_RE.match(lines[i]):
        return False, {}
    i += 1
    data: dict[str, str] = {}
    while i < len(lines) and not FRONTMATTER_RE.match(lines[i]):
        line = lines[i].rstrip("\n")
        m = KEY_VALUE_RE.match(line)
        if m:
            data[m.group("key")] = m.group("value").strip().strip('"').strip("'")
        i += 1
    if i >= len(lines) or not FRONTMATTER_RE.match(lines[i]):
        # no closing ---
        return False, {}
    return True, data


def _extract_referenced_paths(text: str) -> list[str]:
    refs: set[str] = set()
    for m in INLINE_CODE_PATH_RE.finditer(text):
        refs.add(m.group("path"))
    for m in SHELL_PY_PATH_RE.finditer(text):
        refs.add(m.group("path"))
    for m in SHELL_NODE_PATH_RE.finditer(text):
        refs.add(m.group("path"))
    return sorted(refs)


def _check_json_parse(target: Path) -> Optional[str]:
    try:
        json.loads(_read_text(target))
        return None
    except Exception as e:  # noqa: BLE001
        return f"{target.as_posix()}: {e}"


def _python_syntax_check(py_file: Path) -> Optional[str]:
    try:
        subprocess.run(
            [sys.executable, "-m", "py_compile", str(py_file)],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return None
    except Exception as e:  # noqa: BLE001
        return f"{py_file.as_posix()}: {e}"


def _node_syntax_check(js_file: Path) -> Optional[str]:
    # Best-effort: node may not exist in all environments.
    try:
        subprocess.run(
            ["node", "--check", str(js_file)],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return None
    except FileNotFoundError:
        return None
    except Exception as e:  # noqa: BLE001
        return f"{js_file.as_posix()}: {e}"


def validate_skill_md(skill_md: Path, repo_root: Path, do_syntax: bool) -> SkillCheckResult:
    text = _read_text(skill_md)
    category = _detect_category(skill_md, repo_root)
    installable_location_ok = _is_installable_location_ok(skill_md, repo_root)

    has_frontmatter, fm = _parse_frontmatter(text)
    name_ok = bool(fm.get("name", "").strip()) if has_frontmatter else False
    desc_ok = bool(fm.get("description", "").strip()) if has_frontmatter else False

    referenced = _extract_referenced_paths(text)
    base_dir = skill_md.parent

    missing: list[str] = []
    json_errors: list[str] = []
    py_errors: list[str] = []
    node_errors: list[str] = []

    for ref in referenced:
        # Template SKILL.md often contains placeholders like `scripts/{script_name}.py`
        # Treat these as non-actionable references.
        if "{" in ref or "}" in ref:
            continue
        p = (base_dir / ref).resolve()
        if not p.exists():
            missing.append(f"{ref} (expected at {p.as_posix()})")
            continue
        if p.suffix.lower() == ".json":
            err = _check_json_parse(p)
            if err:
                json_errors.append(err)
        if do_syntax and p.suffix.lower() == ".py":
            err = _python_syntax_check(p)
            if err:
                py_errors.append(err)
        if do_syntax and p.suffix.lower() == ".js":
            err = _node_syntax_check(p)
            if err:
                node_errors.append(err)

    placeholder_warnings: list[str] = []
    if category != "template":
        # Warn if we see obvious "{placeholder}" patterns in non-template skills
        for m in PLACEHOLDER_BRACES_RE.finditer(text):
            placeholder_warnings.append(m.group(0))
            if len(placeholder_warnings) >= 8:
                break

    return SkillCheckResult(
        skill_md=skill_md,
        category=category,
        installable_location_ok=installable_location_ok,
        has_frontmatter=has_frontmatter,
        frontmatter_name_ok=name_ok,
        frontmatter_description_ok=desc_ok,
        referenced_paths=referenced,
        missing_paths=missing,
        json_parse_errors=json_errors,
        python_syntax_errors=py_errors,
        node_syntax_errors=node_errors,
        placeholder_warnings=placeholder_warnings,
    )


def _iter_skill_mds(repo_root: Path) -> Iterable[Path]:
    # dot-dirs are included here explicitly by listing patterns
    yield from repo_root.rglob("SKILL.md")


def _short_rel(p: Path, repo_root: Path) -> str:
    try:
        return p.relative_to(repo_root).as_posix()
    except Exception:  # noqa: BLE001
        return p.as_posix()


def generate_report(results: list[SkillCheckResult], repo_root: Path, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)

    now = _dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines: list[str] = []
    lines.append(f"# Demo Skills 可用性检查报告")
    lines.append("")
    lines.append(f"- **生成时间**：`{now}`")
    lines.append(f"- **仓库根目录**：`{repo_root.as_posix()}`")
    lines.append("")
    lines.append("## 总览")
    lines.append("")

    total = len(results)
    passed = sum(1 for r in results if r.is_pass_for_category())
    failed = total - passed
    lines.append(f"- **总数**：{total}")
    lines.append(f"- **PASS**：{passed}")
    lines.append(f"- **FAIL**：{failed}")
    lines.append("")

    lines.append("## 逐项结果（PASS/FAIL）")
    lines.append("")
    lines.append("| 目标 | 分类 | Claude Code 直装可用 | 引用文件完整 | 备注 |")
    lines.append("|---|---|---:|---:|---|")

    def yesno(x: bool) -> str:
        return "✅" if x else "❌"

    for r in sorted(results, key=lambda x: _short_rel(x.skill_md, repo_root)):
        installable = (
            r.installable_location_ok
            and r.has_frontmatter
            and r.frontmatter_name_ok
            and r.frontmatter_description_ok
        )
        refs_ok = not (r.missing_paths or r.json_parse_errors or r.python_syntax_errors or r.node_syntax_errors)
        note_bits: list[str] = []
        if r.category != "installed_skill":
            note_bits.append("非 `.claude/skills/`")
        if r.category in ("demo_example", "other") and not r.has_frontmatter:
            note_bits.append("无 YAML 头（Claude Code 不会当 Skill 加载）")
        if r.missing_paths:
            note_bits.append(f"缺文件 {len(r.missing_paths)}")
        if r.placeholder_warnings:
            note_bits.append("疑似残留占位符")
        note = "；".join(note_bits) if note_bits else "-"
        lines.append(
            f"| `{_short_rel(r.skill_md, repo_root)}` | {r.category} | {yesno(installable)} | {yesno(refs_ok)} | {note} |"
        )

    lines.append("")
    lines.append("## 详细问题列表（仅 FAIL）")
    lines.append("")

    for r in sorted(results, key=lambda x: _short_rel(x.skill_md, repo_root)):
        if r.is_pass_for_category():
            continue
        lines.append(f"### `{_short_rel(r.skill_md, repo_root)}`")
        lines.append("")
        lines.append(f"- **分类**：{r.category}")
        lines.append(f"- **Claude Code 直装可用**：{'否' if r.category != 'installed_skill' else ('否' if not (r.has_frontmatter and r.frontmatter_name_ok and r.frontmatter_description_ok) else '是')}")
        if r.category == "installed_skill":
            if not r.has_frontmatter:
                lines.append("- **问题**：缺少 YAML frontmatter（`---` 开头）")
            else:
                if not r.frontmatter_name_ok:
                    lines.append("- **问题**：YAML 缺少 `name` 或为空")
                if not r.frontmatter_description_ok:
                    lines.append("- **问题**：YAML 缺少 `description` 或为空")
        if r.missing_paths:
            lines.append("- **缺失引用文件**：")
            for x in r.missing_paths:
                lines.append(f"  - `{x}`")
        if r.json_parse_errors:
            lines.append("- **JSON 解析错误**：")
            for x in r.json_parse_errors:
                lines.append(f"  - `{x}`")
        if r.python_syntax_errors:
            lines.append("- **Python 语法检查失败**：")
            for x in r.python_syntax_errors:
                lines.append(f"  - `{x}`")
        if r.node_syntax_errors:
            lines.append("- **Node 语法检查失败**：")
            for x in r.node_syntax_errors:
                lines.append(f"  - `{x}`")
        if r.placeholder_warnings:
            lines.append("- **疑似占位符片段（示例）**：")
            for x in r.placeholder_warnings:
                lines.append(f"  - `{x}`")
        lines.append("")

    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate demo skills usability")
    parser.add_argument("--root", default=".", help="Repo root path")
    parser.add_argument(
        "--output",
        default="docs/reports/demo-skills-usability-check.md",
        help="Output Markdown report path (relative to root or absolute)",
    )
    parser.add_argument(
        "--syntax",
        action="store_true",
        help="Best-effort syntax checks (python py_compile, node --check)",
    )
    args = parser.parse_args()

    repo_root = Path(args.root).resolve()
    out_path = Path(args.output)
    if not out_path.is_absolute():
        out_path = (repo_root / out_path).resolve()

    results: list[SkillCheckResult] = []
    for skill_md in _iter_skill_mds(repo_root):
        # skip vendored/irrelevant directories if any
        if any(part in ("node_modules", ".venv", "dist", "build") for part in skill_md.parts):
            continue
        try:
            results.append(validate_skill_md(skill_md, repo_root, do_syntax=args.syntax))
        except UnicodeDecodeError:
            # Treat unreadable files as failures
            results.append(
                SkillCheckResult(
                    skill_md=skill_md,
                    category=_detect_category(skill_md, repo_root),
                    installable_location_ok=_is_installable_location_ok(skill_md, repo_root),
                    has_frontmatter=False,
                    frontmatter_name_ok=False,
                    frontmatter_description_ok=False,
                    missing_paths=[],
                    referenced_paths=[],
                    json_parse_errors=[f"{skill_md.as_posix()}: unreadable (encoding)"],
                )
            )

    generate_report(results, repo_root, out_path)
    print(f"Wrote report: {out_path.as_posix()}")
    # exit non-zero if any FAIL
    return 0 if all(r.is_pass_for_category() for r in results) else 2


if __name__ == "__main__":
    raise SystemExit(main())

