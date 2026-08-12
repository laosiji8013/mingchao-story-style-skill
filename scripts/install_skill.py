#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "mingchao-story-style"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Install mingchao-story-style into a Skills folder")
    parser.add_argument(
        "--target",
        type=Path,
        default=Path.home() / ".codex" / "skills",
        help="Skills root directory (default: ~/.codex/skills)",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    target_root = args.target.expanduser().resolve()
    destination = target_root / SOURCE.name

    if not SOURCE.is_dir():
        raise SystemExit(f"Source Skill not found: {SOURCE}")
    if destination.exists():
        raise SystemExit(
            f"Destination already exists: {destination}\n"
            "Remove or rename the existing Skill after reviewing it, then run the installer again."
        )

    target_root.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SOURCE, destination)
    print(f"Installed: {destination}")
    print("Restart or reload your Agent, then invoke $mingchao-story-style.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
