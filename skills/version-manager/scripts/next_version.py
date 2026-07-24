#!/usr/bin/env python3
"""Reserve the next immutable vNNN version directory."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", type=Path)
    parser.add_argument("--parent")
    parser.add_argument("--note", default="")
    args = parser.parse_args()
    project = args.project.resolve()
    versions = project / "versions"
    versions.mkdir(parents=True, exist_ok=True)
    numbers = [
        int(path.name[1:]) for path in versions.iterdir()
        if path.is_dir() and len(path.name) == 4 and path.name.startswith("v") and path.name[1:].isdigit()
    ]
    version = f"v{(max(numbers, default=0) + 1):03d}"
    folder = versions / version
    folder.mkdir(exist_ok=False)
    record = {
        "version": version,
        "parent": args.parent,
        "createdAt": datetime.now(timezone.utc).isoformat(),
        "note": args.note,
        "status": "draft"
    }
    (folder / "version.json").write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
    print(folder)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
