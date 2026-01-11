#!/usr/bin/env python3
from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COMMUNITY_DIR = ROOT / "community-resources"
DOCS_DIR = ROOT / "docs"
DEST_DIR = DOCS_DIR / "community-resources"
ASSETS_DIR = DOCS_DIR / "assets"

QR_SRC = ROOT / "qrcode_for_gh_616fda3e82ab_258.jpg"
QR_DEST = ASSETS_DIR / "wechat-qrcode.jpg"


def _copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def _sync_dir(src_dir: Path, dst_dir: Path, patterns: list[str]) -> None:
    dst_dir.mkdir(parents=True, exist_ok=True)
    for pattern in patterns:
        for src in src_dir.glob(pattern):
            if src.is_dir():
                continue
            # Avoid README.md -> index.html collisions in MkDocs directories.
            if src.name.lower() == "readme.md":
                continue
            rel = src.relative_to(src_dir)
            _copy_file(src, dst_dir / rel)


def main() -> None:
    if not COMMUNITY_DIR.exists():
        raise SystemExit(f"Missing directory: {COMMUNITY_DIR}")

    # Ensure directories exist
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)

    # Clean previously generated content so deletions propagate.
    # Keep any hand-written index.md pages.
    for p in list(DEST_DIR.rglob("*")):
        # Only remove generated files/dirs, keep index pages.
        if p.is_file() and p.name == "index.md":
            continue
        if p.is_file():
            try:
                p.unlink()
            except FileNotFoundError:
                pass
        elif p.is_dir():
            # We'll attempt to remove empty dirs after file deletions.
            continue
    # Remove empty directories bottom-up (but keep DEST_DIR itself)
    for d in sorted([x for x in DEST_DIR.rglob("*") if x.is_dir()], reverse=True):
        try:
            d.rmdir()
        except OSError:
            # Not empty
            pass

    # Copy QR for site usage
    if QR_SRC.exists():
        _copy_file(QR_SRC, QR_DEST)

    # Copy top-level markdown resources
    _sync_dir(
        COMMUNITY_DIR,
        DEST_DIR,
        patterns=[
            "*.md",
        ],
    )

    # Copy data files we want exposed
    if (COMMUNITY_DIR / "data").exists():
        _sync_dir(COMMUNITY_DIR / "data", DEST_DIR / "data", patterns=["*.json"])

    # Copy reports
    if (COMMUNITY_DIR / "reports").exists():
        _sync_dir(COMMUNITY_DIR / "reports", DEST_DIR / "reports", patterns=["*.md"])

    # Copy articles (public-account posts / essays)
    if (COMMUNITY_DIR / "articles").exists():
        _sync_dir(COMMUNITY_DIR / "articles", DEST_DIR / "articles", patterns=["*.md"])

    # Ensure reports index exists for MkDocs nav/linking (do not rely on git-tracked file).
    reports_dir = DEST_DIR / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    reports_index = reports_dir / "index.md"
    if not reports_index.exists():
        # Auto-list common daily search reports if present.
        items: list[str] = []
        for p in sorted(reports_dir.glob("daily-search-*.md")):
            items.append(f"- [{p.stem.replace('daily-search-', '')}]({p.name})")
        body = "\n".join(items) if items else "- （暂无）"
        reports_index.write_text(
            "# 搜索日报（Reports）\n\n"
            "这里汇总展示 `community-resources/reports/` 中生成的日报/简报。\n\n"
            "## Daily Search\n\n"
            f"{body}\n\n"
            "> 说明：本目录下的日报文件由脚本自动同步；新增新的日报后，commit + push 即会自动更新 GitHub Pages。\n",
            encoding="utf-8",
        )

    # Ensure an index exists (kept in repo; don't overwrite)
    if not (DEST_DIR / "index.md").exists():
        (DEST_DIR / "index.md").write_text(
            "# 社区资源库\n\n请先运行生成脚本同步内容。\n", encoding="utf-8"
        )

    print("✓ GitHub Pages docs synced:")
    print(f"  - {DEST_DIR}")
    print(f"  - {QR_DEST if QR_DEST.exists() else '(no qr copied)'}")


if __name__ == "__main__":
    main()

