#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Synthesize every sentence in script.json with speech.cpp and write the timeline.

Writes <voice dir>/<scene>/<n>.wav and timeline.json in the current folder (the video project).
Only sentences whose spoken text or voice changed are synthesized again
(<voice dir>/cache.json remembers what each wav was made from); timeline.json is always rebuilt.
Readings come from the dictionaries merged with script.json readings (see yomi.py).
Usage: uv run gen_voice.py [script.json] [timeline.json] [voice dir]
"""

import hashlib
import json
import os
import re
import struct
import sys
import urllib.error
import urllib.request
from pathlib import Path

from yomi import compile_readings

BASE = os.environ.get("SPEECH_BASE_URL", "http://localhost:11180").rstrip("/")
DEFAULT_VOICE = "narrator"
START_CMD = (
    'speech serve --port 11180 irodori-tts '
    '--add-voice="narrator=/Users/aliyome/repos/kikuhon/voices/irodori-tts/narrator.voice.gguf" '
    '--voice="narrator"'
)
FPS, GAP, HEAD, TAIL = 30, 9, 15, 24  # frames: pause after a sentence, scene head, scene tail
SCENE_ID = re.compile(r"^[a-z0-9][a-z0-9-]*$")  # same rule as build_video.py; ids become folder names
DEFAULTS = ["script.json", "timeline.json", "assets/voice"]


def synthesize(text: str, voice: str, speed: float | None = None) -> bytes:
    """POST to the local speech.cpp server, or exit with a message saying what to fix."""
    url = f"{BASE}/v1/audio/speech"
    payload: dict[str, object] = {
        "input": text,
        "voice": voice,
        "response_format": "wav",
    }
    if speed is not None:
        payload["speed"] = speed
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(url, data=body, method="POST", headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:  # nosec B310
            return r.read()
    except urllib.error.HTTPError as err:
        detail = err.read().decode("utf-8", "replace")[:300]
        sys.exit(
            f"speech server returned {err.code} for /v1/audio/speech: {detail}\n"
            f"Check the voice name (voice={voice!r}) registered with speech serve --add-voice."
        )
    except OSError as err:  # URLError, refused connection, timeout
        sys.exit(f"Cannot reach speech server at {BASE} ({err}). Start it with:\n  {START_CMD}")


def wav_seconds(b: bytes) -> float:
    """Read byteRate and the data chunk length from a RIFF header."""
    byte_rate = None
    i = 12
    while i + 8 <= len(b):
        cid, size = b[i : i + 4], struct.unpack("<I", b[i + 4 : i + 8])[0]
        if cid == b"fmt " and i + 20 <= len(b):
            byte_rate = struct.unpack("<I", b[i + 16 : i + 20])[0]
        elif cid == b"data":
            if byte_rate is None:
                byte_rate = struct.unpack("<I", b[28:32])[0]
            data_len = len(b) - (i + 8) if size in (0, 0xFFFFFFFF) else size
            return data_len / byte_rate
        i += 8 + size + (size & 1)
    msg = "no data chunk"
    raise ValueError(msg)


def main() -> None:
    """Generate voices and the timeline."""
    script, timeline_path, voice_dir = (sys.argv[1:] + DEFAULTS[len(sys.argv) - 1 :])[:3]
    cfg = json.loads(Path(script).read_text(encoding="utf-8"))
    voice_name = str(cfg.get("voice") or cfg.get("speaker") or DEFAULT_VOICE)
    speed = cfg.get("speed")
    tts_text = compile_readings(cfg.get("readings", {}))
    cache_path = Path(voice_dir) / "cache.json"
    cache = json.loads(cache_path.read_text(encoding="utf-8")) if cache_path.exists() else {}
    ids = [sc.get("id") for sc in cfg["scenes"]]
    bad = [i for i in ids if not isinstance(i, str) or not SCENE_ID.fullmatch(i)]
    dup = sorted({i for i in ids if ids.count(i) > 1})
    if bad or dup:
        sys.exit(f"scene id must be unique and match {SCENE_ID.pattern}: invalid {bad}, duplicate {dup}")
    timeline, made, total = [], 0, 0
    for sc in cfg["scenes"]:
        Path(f"{voice_dir}/{sc['id']}").mkdir(parents=True, exist_ok=True)
        t, items = HEAD, []
        for n, text in enumerate(sc["sentences"]):
            spoken = tts_text(text)
            key = hashlib.sha256(
                json.dumps(["speech", spoken, voice_name, speed], ensure_ascii=False).encode()
            ).hexdigest()
            path = f"{voice_dir}/{sc['id']}/{n:02d}.wav"
            if cache.get(path) == key and Path(path).is_file():
                wav = Path(path).read_bytes()
            else:
                wav = synthesize(spoken, voice_name, speed)
                Path(path).write_bytes(wav)
                cache[path] = key
                cache_path.write_text(json.dumps(cache, indent=1), encoding="utf-8")
                made += 1
            total += 1
            frames = int(wav_seconds(wav) * FPS + 0.999)
            items.append({"text": text, "file": path, "from": t, "frames": frames})
            t += frames + GAP
        timeline.append({"id": sc["id"], "durationInFrames": t + TAIL, "sentences": items})
        print(sc["id"], round((t + TAIL) / FPS, 1), "s")
    Path(timeline_path).write_text(json.dumps(timeline, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"synthesized {made} of {total} sentences (the rest were unchanged)")
    print("total", round(sum(s["durationInFrames"] for s in timeline) / FPS / 60, 2), "min")


if __name__ == "__main__":
    main()
