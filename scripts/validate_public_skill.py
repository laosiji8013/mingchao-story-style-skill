#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "mingchao-story-style"


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def main() -> int:
    required = [
        SKILL / "SKILL.md",
        SKILL / "agents/openai.yaml",
        SKILL / "references/style-profile.md",
        SKILL / "references/structure-patterns.md",
        SKILL / "references/output-rules.md",
        SKILL / "references/examples.md",
        SKILL / "references/anti-examples.md",
        SKILL / "references/test-prompts.json",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
    if missing:
        fail(f"missing required files: {', '.join(missing)}")

    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail("SKILL.md frontmatter is missing")
    fields = [line.split(":", 1)[0].strip() for line in match.group(1).splitlines() if ":" in line]
    if fields != ["name", "description"]:
        fail(f"SKILL.md frontmatter must contain only name and description, got {fields}")
    if "name: mingchao-story-style" not in match.group(0):
        fail("skill name is incorrect")

    tests = json.loads((SKILL / "references/test-prompts.json").read_text(encoding="utf-8"))
    if tests.get("skill_name") != "mingchao-story-style":
        fail("test prompt skill_name is incorrect")
    if len(tests.get("tests", [])) < 5:
        fail("at least five test prompts are required")

    forbidden_suffixes = {".zip", ".txt", ".epub", ".pdf"}
    forbidden_names = {".DS_Store"}
    files = [
        path
        for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.parts and "__pycache__" not in path.parts
    ]
    bad = [
        str(path.relative_to(ROOT))
        for path in files
        if path.name in forbidden_names or path.suffix.lower() in forbidden_suffixes
    ]
    if bad:
        fail(f"forbidden public artifacts found: {', '.join(bad)}")

    absolute_path_markers = ("/Volumes/", "/Users/", "C:\\Users\\")
    for path in files:
        if path == Path(__file__).resolve():
            continue
        if path.suffix.lower() not in {".md", ".json", ".yaml", ".yml", ".py"}:
            continue
        contents = path.read_text(encoding="utf-8")
        if any(marker in contents for marker in absolute_path_markers):
            fail(f"absolute local path found in {path.relative_to(ROOT)}")

    print(f"OK: validated {len(files)} public files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
