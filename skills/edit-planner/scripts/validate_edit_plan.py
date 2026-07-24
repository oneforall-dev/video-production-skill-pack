#!/usr/bin/env python3
"""Perform dependency-free semantic checks on edit-plan.json."""

from __future__ import annotations

import json
import sys
from pathlib import Path


EVENT_KEYS = ("cuts", "captions", "overlays", "zooms", "reframes", "broll", "music", "soundEffects", "transitions")


def main() -> int:
    if len(sys.argv) != 2:
        print("Uso: validate_edit_plan.py <edit-plan.json>")
        return 2
    path = Path(sys.argv[1])
    data = json.loads(path.read_text(encoding="utf-8"))
    failures: list[str] = []
    seen: set[str] = set()
    duration = float(data.get("timeline", {}).get("duration", 0))
    for key in EVENT_KEYS:
        for index, event in enumerate(data.get(key, [])):
            event_id = event.get("id")
            start = event.get("start")
            end = event.get("end")
            if not event_id or event_id in seen:
                failures.append(f"{key}[{index}]: id ausente o duplicado")
            else:
                seen.add(event_id)
            if not isinstance(start, (int, float)) or not isinstance(end, (int, float)) or start < 0 or end <= start:
                failures.append(f"{key}[{index}]: rango inválido")
            elif duration and end > duration + 0.001:
                failures.append(f"{key}[{index}]: termina después de la timeline")
    if failures:
        print("\n".join(failures))
        return 1
    print(f"OK: {len(seen)} eventos válidos")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
