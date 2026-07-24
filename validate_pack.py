#!/usr/bin/env python3
"""Validate pack completeness, frontmatter, names and UI metadata."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parent
    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    failures: list[str] = []
    for name in manifest["skills"]:
        folder = root / "skills" / name
        skill = folder / "SKILL.md"
        agent = folder / "agents" / "openai.yaml"
        if not skill.is_file():
            failures.append(f"{name}: falta SKILL.md")
            continue
        text = skill.read_text(encoding="utf-8")
        match = re.match(r"^---\s*\nname:\s*([^\n]+)\ndescription:\s*([^\n]+)\n---", text)
        if not match:
            failures.append(f"{name}: frontmatter inválido")
        elif match.group(1).strip() != name:
            failures.append(f"{name}: nombre de frontmatter no coincide")
        elif len(match.group(2).strip()) < 80:
            failures.append(f"{name}: descripción demasiado débil")
        if "[TODO" in text:
            failures.append(f"{name}: conserva TODO")
        if not agent.is_file() or f"${name}" not in agent.read_text(encoding="utf-8"):
            failures.append(f"{name}: agents/openai.yaml incompleto")
    if failures:
        print("\n".join(failures))
        return 1
    print(f"OK: {len(manifest['skills'])} skills completas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
