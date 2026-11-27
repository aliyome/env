#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Apply the readings dictionaries and script.json readings to narration text.

Merged in increasing priority: the bundled references/readings.json, the user's
~/.config/<skill name>/readings.json, then script.json readings.
Usage: uv run yomi.py add <word> <reading>  (append to the user dictionary)
       uv run yomi.py                       (self-check the replacement rules)
"""

import json
import re
import sys
import tempfile
from collections.abc import Callable
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
BUNDLED = SKILL / "references/readings.json"
USER = Path.home() / ".config" / SKILL.name / "readings.json"


def load(path: Path) -> dict[str, str]:
    """Read a readings file, or return an empty dict when it does not exist."""
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def add(word: str, reading: str, path: Path = USER) -> None:
    """Append one reading to the user dictionary, creating the file on first use."""
    table = {**load(path), word: reading}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(table, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def compile_readings(
    script_readings: dict[str, str], dictionaries: list[dict[str, str]] | None = None
) -> Callable[[str], str]:
    """Return a function that replaces every key with its reading in one pass.

    `dictionaries` go in increasing priority (default: bundled, then user) and
    script_readings win over all of them. Longer keys win, and ASCII-only keys
    match on word boundaries so PI does not hit inside API.
    """
    if dictionaries is None:
        dictionaries = [load(BUNDLED), load(USER)]
    table = {k: v for d in [*dictionaries, script_readings] for k, v in d.items()}
    if not table:
        return lambda s: s

    def pattern(key: str) -> str:
        esc = re.escape(key)
        return rf"(?<![A-Za-z0-9]){esc}(?![A-Za-z0-9])" if re.fullmatch(r"[A-Za-z0-9]+", key) else esc

    rx = re.compile("|".join(pattern(k) for k in sorted(table, key=len, reverse=True)))
    return lambda s: rx.sub(lambda m: table[m.group(0)], s)


def self_check() -> None:
    """Check the replacement rules, the merge order and add()."""
    bundled = {"PI": "ピーアイ", "Acme": "アクメ", "AcmeAds": "アクメアッズ", "toC": "トゥーしー", "UI": "ユーアイ"}
    user = {"PI": "パイ", "Acme": "エイクミー"}
    f = compile_readings({"Acme": "あくめ"}, [bundled, user])
    cases = [
        ("API と PI", "API と パイ"),  # user beats bundled
        ("AcmeAdsとAcmeの", "アクメアッズとあくめの"),  # script beats user, longest first
        ("BtoC と toC と UI", "BtoC と トゥーしー と ユーアイ"),  # bundled-only keys still apply
        ("PIPI", "PIPI"),
    ]
    for src, want in cases:
        assert f(src) == want, (src, f(src))  # nosec B101
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "new/readings.json"
        add("PI", "パイ", path)
        add("UI", "ユーアイ", path)
        assert load(path) == {"PI": "パイ", "UI": "ユーアイ"}, load(path)  # nosec B101
    print("ok")


if __name__ == "__main__":
    if sys.argv[1:2] == ["add"] and len(sys.argv) == 4:
        add(sys.argv[2], sys.argv[3])
        print(f"{sys.argv[2]} -> {sys.argv[3]} added to {USER}")
    elif len(sys.argv) == 1:
        self_check()
    else:
        sys.exit(__doc__)
