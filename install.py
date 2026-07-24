#!/usr/bin/env python3
"""Install the pack's skills without overwriting existing skills by default."""

from __future__ import annotations

import argparse
import json
import os
import shutil
from pathlib import Path


def default_target() -> Path:
    codex_home = os.environ.get("CODEX_HOME")
    return Path(codex_home).expanduser() / "skills" if codex_home else Path.home() / ".codex" / "skills"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", type=Path, default=default_target())
    parser.add_argument("--force", action="store_true", help="Replace matching skill folders.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    source_root = root / "skills"
    target = args.target.expanduser().resolve()
    target.mkdir(parents=True, exist_ok=True)

    conflicts = [name for name in manifest["skills"] if (target / name).exists()]
    if conflicts and not args.force:
        print("No se instaló nada. Ya existen: " + ", ".join(conflicts))
        print("Usa --force solo después de revisar esos directorios.")
        return 2

    for name in manifest["skills"]:
        source = source_root / name
        destination = target / name
        if args.dry_run:
            print(f"INSTALAR {source} -> {destination}")
            continue
        if destination.exists():
            shutil.rmtree(destination)
        shutil.copytree(source, destination)
        print(f"INSTALADA {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
