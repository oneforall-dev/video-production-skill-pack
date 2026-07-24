#!/usr/bin/env python3
"""Run ffprobe safely and emit normalized JSON metadata."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    source = args.input.resolve()
    if not source.is_file():
        raise SystemExit(f"No existe el archivo: {source}")
    command = [
        "ffprobe", "-v", "error", "-show_format", "-show_streams",
        "-of", "json", str(source)
    ]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    probe = json.loads(result.stdout)
    video_streams = [s for s in probe.get("streams", []) if s.get("codec_type") == "video"]
    if not video_streams:
        raise SystemExit("El archivo no contiene un stream de video.")
    payload = {
        "schemaVersion": "1.0",
        "sourceId": sha256(source)[:16],
        "source": {"name": source.name, "sha256": sha256(source), "bytes": source.stat().st_size},
        "format": probe.get("format", {}),
        "streams": probe.get("streams", []),
        "warnings": []
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.output.with_suffix(args.output.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    temporary.replace(args.output)
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
