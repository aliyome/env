#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Print each sentence in a script alongside the reading-replaced text sent to speech.cpp.

Readings come from the dictionaries merged with script.json readings (see yomi.py).
Usage: uv run check_readings.py [script.json] [scene id prefix ...]
"""

import json
import sys
from pathlib import Path

from yomi import compile_readings


def main() -> None:
    """Print each sentence with its reading-replaced TTS input."""
    args = sys.argv[1:]
    script = args.pop(0) if args and args[0].endswith(".json") else "script.json"
    cfg = json.loads(Path(script).read_text(encoding="utf-8"))
    only = tuple(args)
    tts_text = compile_readings(cfg.get("readings", {}))
    for sc in cfg["scenes"]:
        if only and not sc["id"].startswith(only):
            continue
        for s in sc["sentences"]:
            spoken = tts_text(s)
            print(f"{sc['id']}\t{s}\n\t{spoken}")


if __name__ == "__main__":
    main()
