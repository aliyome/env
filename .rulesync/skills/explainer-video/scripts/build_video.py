#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["pygments"]
# ///
"""Build a HyperFrames project from script.json and the timeline written by gen_voice.py.

Writes index.html (one sub-composition slot per scene), compositions/<scene>.html and
assets/gsap.min.js into the current folder. Titles and visuals come from script.json, so a
visual-only edit needs no new voices. Run gen_voice.py again when sentences change.
The look comes from ./theme.css when the folder has one, otherwise from the skill's assets/theme.css.
Usage: uv run build_video.py [script.json] [timeline.json]
"""

import html
import json
import re
import shutil
import sys
import unicodedata
from pathlib import Path

from image_size import image_aspect
from pygments import lex
from pygments.lexers import TextLexer, get_lexer_by_name, get_lexer_for_filename
from pygments.token import Token
from pygments.util import ClassNotFound

ASSETS = Path(__file__).resolve().parent.parent / "assets"
FPS, W, H = 30, 1920, 1080
KINDS = {"card", "big", "step", "note", "img", "code"}
LAYOUTS = {"grid", "steps", "split", "stack"}
MAX_CHARS = 36  # a caption wraps at about 36 full-width characters; half-width counts 0.5
SCENE_ID = re.compile(r"^[a-z0-9][a-z0-9-]*$")  # used in file names and element ids
# ponytail: measured break-even with 1-2 line cards below (a 1.9:1 image is half as wide in stack);
# tune per scene with an explicit layout if it misjudges.
STACK_ASPECT = 3.0  # a split image wider than this (width / height) is laid out as stack
# Code excerpts: font size range in px, monospace advance per half-width char and line height in em.
CODE_MIN, CODE_MAX, CHAR_EM, LINE_EM = 24, 34, 0.61, 1.45
# Board and gaps from base.css / theme.css, used to estimate the box a code item gets.
BOARD_W, BOARD_H, GAP_SM, GAP_MD = W - 200, H - 400, 24, 32
CODE_CHROME_W, CODE_CHROME_H = 48, 80  # .code-body padding; padding + the head line above the panel
STACK_ROW = 256  # cards under a stacked code item, plus the gap

# Motion: short, ease-out, small distances, no bounce or loops. Seconds.
REVEAL = '{opacity:0,y:24},{opacity:1,y:0,duration:0.6,ease:"expo.out"}'
SOFT_REVEAL = '{opacity:0,y:16,scale:0.98},{opacity:1,y:0,scale:1,duration:0.7,ease:"power3.out"}'
ARROW_REVEAL = '{opacity:0,x:-12},{opacity:1,x:0,duration:0.5,ease:"power3.out"}'
STAGGER = 0.08  # between items that appear on the same sentence
FOCUS_DELAY, FOCUS_IN, FOCUS_OUT = 0.15, 0.35, 0.45
COUNT_UP = 0.9
SCENE_IN, SCENE_OUT = 0.5, 0.35
ARROW_SVG = (
    '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6" fill="none" '
    'stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
)
def js_str(value: str) -> str:
    """Return a JS string literal that is safe inside an inline <script> (no raw "<")."""
    return json.dumps(value).replace("<", "\\u003c")


NUMBER = re.compile(r"^(\D*?)(\d[\d,]*(?:\.\d+)?)(.*)$", re.DOTALL)
# Pygments token -> tok-* class (colors in theme.css). First match wins, so subtypes come before parents.
TOKEN_CLASSES = [
    (Token.Comment, "comment"),
    (Token.Keyword.Type, "type"),
    (Token.Keyword, "keyword"),
    (Token.Operator.Word, "keyword"),
    (Token.Literal.String, "string"),
    (Token.Literal.Number, "number"),
    (Token.Name.Builtin, "type"),
    (Token.Name.Class, "type"),
    (Token.Name.Function, "function"),
    (Token.Name.Decorator, "function"),
    (Token.Operator, "punct"),
    (Token.Punctuation, "punct"),
]

e = html.escape


def sec(frames: int) -> float:
    """Convert frames to seconds."""
    return round(frames / FPS, 3)


def width(text: str) -> float:
    """Count full-width characters as 1 and half-width ones as 0.5."""
    return sum(1 if unicodedata.east_asian_width(c) in "WFA" else 0.5 for c in text)


def code_size(body: str, box: tuple[float, float]) -> tuple[int, bool, bool]:
    """Pick the largest size in CODE_MIN..CODE_MAX at which every line fits the code box.

    Returns the size, whether long lines must wrap (they would need less than CODE_MIN to fit),
    and whether the lines overflow the height even at the returned size.
    """
    w, h = box[0] - CODE_CHROME_W, box[1] - CODE_CHROME_H
    lines = body.split("\n")
    cols = [width(line) * 2 for line in lines]
    by_width = w / ((max(cols) or 1) * CHAR_EM)
    size = int(max(CODE_MIN, min(CODE_MAX, by_width, h / (len(lines) * LINE_EM))))
    rows = sum(max(1, -(-c * CHAR_EM * size // w)) for c in cols)  # lines after wrapping
    return size, by_width < CODE_MIN, rows * size * LINE_EM > h


def highlight(body: str, lang: str | None, head: str) -> str:
    """Return escaped code with tok-* spans, using `lang` or the file extension in `head`."""
    opts = {"stripnl": False, "ensurenl": False}
    if lang:
        lexer = get_lexer_by_name(lang, **opts)
    else:
        try:
            lexer = get_lexer_for_filename(re.sub(r":[\d-]+$", "", head).rsplit("/", 1)[-1], **opts)
        except ClassNotFound:
            lexer = TextLexer(**opts)
    tokens = list(lex(body, lexer))
    out = []
    for n, (ttype, text) in enumerate(tokens):
        cls = next((c for t, c in TOKEN_CLASSES if ttype in t), None)
        if cls is None and ttype in Token.Name and n + 1 < len(tokens) and tokens[n + 1][1].startswith("("):
            cls = "function"  # some lexers (TypeScript) leave function names as plain names
        # Close spans at line ends so each line can be wrapped in its own element.
        out.append("\n".join(f'<span class="tok-{cls}">{e(p)}</span>' if cls and p else e(p) for p in text.split("\n")))
    return "".join(out)


class Scene:
    """One scene: markup for the board and the tweens of its timeline."""

    def __init__(self, sc: dict, tl: dict, index: int, tones: set[str]) -> None:
        """Merge the script scene with its timeline entry."""
        self.id, self.title, self.index, self.tones = sc["id"], sc["title"], index, tones
        self.visual = sc.get("visual") or {}
        self.sentences = tl["sentences"]
        self.dur = sec(tl["durationInFrames"])
        self.starts = [sec(s["from"]) for s in self.sentences]
        self.ends = [*self.starts[1:], self.dur]
        self.js: list[str] = []
        self.seen: dict[int, int] = {}
        self.code_box = (BOARD_W, BOARD_H)  # set per layout in board()
        self.check()

    def fail(self, msg: str) -> None:
        """Stop with a message that names the scene."""
        sys.exit(f"{self.id}: {msg}")

    def warn(self, msg: str) -> None:
        """Print a warning that names the scene and keep building."""
        print(f"warning: {self.id}: {msg}")

    def check(self) -> None:
        """Warn about sentences and items that will not show as written, and fall back to something that renders."""
        last = len(self.sentences) - 1
        for n, s in enumerate(self.sentences):
            if width(s["text"]) > MAX_CHARS:
                self.warn(f"sentence {n} is {width(s['text']):g} characters (max {MAX_CHARS}); split it")
        if "component" in self.visual:
            return
        if self.visual.get("layout", "grid") not in LAYOUTS:
            self.warn(f"unknown layout {self.visual['layout']!r}, using grid")
            self.visual["layout"] = "grid"
        for n, it in enumerate(self.visual.get("items", [])):
            if it.get("kind", "card") not in KINDS:
                self.warn(f"item {n}: unknown kind {it['kind']!r}, shown as card")
                it["kind"] = "card"
            if it.get("tone", "blue") not in self.tones:
                self.warn(f"item {n}: unknown tone {it['tone']!r}, using blue (theme.css has {sorted(self.tones)})")
                it["tone"] = "blue"
            at = it.get("at", 0)
            if not 0 <= at <= last:
                it["at"] = min(max(at, 0), last)
                self.warn(f"item {n}: at={at} is out of range (0..{last}), using {it['at']}")
            until = it.get("until")
            if until is not None and not it.get("at", 0) <= until <= last:
                self.warn(f"item {n}: until={until} must be between at and {last}; ignored")
                del it["until"]
            if it.get("kind") == "img" and not Path(it.get("src", "")).is_file():
                self.warn(f"item {n}: image not found: {it.get('src', '')}")

    def start(self, at: int) -> float:
        """Return when an item that appears on sentence `at` starts, staggering items on the same sentence."""
        k = self.seen.get(at, 0)
        self.seen[at] = k + 1
        return round(self.starts[at] + k * STAGGER, 3)

    def focus(self, ring: str, at: int, t: float) -> None:
        """Show a ring around the item while its sentence is narrated, then let it settle."""
        hold = max(0.0, self.ends[at] - t - FOCUS_DELAY - FOCUS_IN - FOCUS_OUT)
        self.js.append(
            f'tl.to("#{ring}",{{keyframes:[{{opacity:1,duration:{FOCUS_IN},ease:"power2.out"}},'
            f'{{opacity:1,duration:{hold:.3f}}},{{opacity:0,duration:{FOCUS_OUT},ease:"power2.inOut"}}]}},{t + FOCUS_DELAY:.3f});'
        )

    def count_up(self, el: str, value: str, t: float) -> None:
        """Count a number in a big card up from zero."""
        m = NUMBER.match(value)
        if not m:
            return
        pre, num, post = m.groups()
        digits = len(num.split(".")[1]) if "." in num else 0
        n = float(num.replace(",", ""))
        fmt = f'{{minimumFractionDigits:{digits},maximumFractionDigits:{digits},useGrouping:{str("," in num).lower()}}}'
        self.js.append(
            f'{{const el=document.getElementById("{el}"),o={{v:0}};tl.fromTo(o,{{v:0}},{{v:{n},duration:{COUNT_UP},'
            f'ease:"power3.out",immediateRender:false,onUpdate:()=>{{el.textContent={js_str(pre)}+o.v.toLocaleString("en-US",{fmt})'
            f"+{js_str(post)};}}}},{t});}}"
        )

    def item(self, it: dict, n: int, fill: bool) -> str:
        """Render one board item and add its tweens."""
        kind, at, tone = it.get("kind", "card"), it.get("at", 0), it.get("tone", "blue")
        sid = f"{self.id}-i{n}"
        t = self.start(at)
        head = e(it.get("head", ""))
        body = e(it.get("body", ""))
        ring = f'<div class="ring" id="{sid}-ring"></div>'
        if kind == "img":
            src = it.get("src", "")
            inner = (
                (f'<div class="shot-label">{head}</div>' if head else "")
                + f'<div class="shot-frame"><img src="{e(src)}" alt="{head}"></div>'
                + (f'<div class="shot-source">出典 {e(it["source"])}</div>' if it.get("source") else "")
            )
            inner = f'<div class="shot">{inner}</div>'
        elif kind == "code":
            raw = it.get("body", "")
            try:
                body = highlight(raw, it.get("lang"), it.get("head", ""))
            except ClassNotFound:
                self.fail(f"unknown lang {it['lang']!r} (use a Pygments lexer name such as typescript or python)")
            size, wrap, overflow = code_size(raw, self.code_box)
            if wrap:
                self.warn(f"item {n}: code lines are too long for {CODE_MIN}px and wrap; trim them or crop columns")
                # Each line is a block with a hanging indent, so a wrapped line continues 2ch right of its own indent.
                body = "".join(
                    f'<span class="ln" style="--in:{len(r) - len(r.lstrip(" ")) + 2}ch">{b or " "}</span>'
                    for r, b in zip(raw.split("\n"), body.split("\n"), strict=True)
                )
            if overflow:
                self.warn(f"item {n}: code is cut off at the bottom even at {CODE_MIN}px; show fewer lines")
            inner = (
                f'<div class="code">{f"<div class=code-head>{head}</div>" if head else ""}<div class="code-panel">'
                f'<pre class="code-body{" wrap" if wrap else ""}" style="font-size:{size}px">{body}</pre>{ring}</div></div>'
            )
            self.focus(f"{sid}-ring", at, t)
        elif kind == "note":
            inner = f'<div class="note">{body}</div>'
        elif kind == "big":
            value = it.get("value", "")
            inner = (
                f'<div class="card filled">{f"<div class=bh>{head}</div>" if head else ""}'
                f'<div class="bv" id="{sid}-v">{e(value)}</div>{f"<div class=bb>{body}</div>" if body else ""}{ring}</div>'
            )
            self.focus(f"{sid}-ring", at, t)
            if it.get("count", True):
                self.count_up(f"{sid}-v", value, t)
        else:
            cls = "card filled step" if kind == "step" else "card"
            inner = (
                f'<div class="{cls}">{f"<div class=ch>{head}</div>" if head else ""}'
                f'{f"<div class=cb>{body}</div>" if body else ""}{ring}</div>'
            )
            self.focus(f"{sid}-ring", at, t)
        self.js.append(f'tl.fromTo("#{sid}",{SOFT_REVEAL if kind in ("img", "code") else REVEAL},{t});')
        until = it.get("until")
        if until is not None and until < len(self.sentences) - 1:
            self.js.append(
                f'tl.fromTo("#{sid}-slot",{{opacity:1}},{{opacity:0,duration:0.3,ease:"power2.out"}},{self.starts[until + 1]});'
            )
        return (
            f'<div class="slot{" fill" if fill else ""} tone-{tone}" id="{sid}-slot">'
            f'<div class="item" id="{sid}">{inner}</div></div>'
        )

    def board(self) -> str:
        """Lay out the items as grid, steps, split or stack.

        Notes listed before every other item go above the rest; the other notes go below.
        A split whose image is wider than STACK_ASPECT becomes a stack.
        """
        if comp := self.visual.get("component"):
            return self.custom(comp)
        layout = self.visual.get("layout", "grid")
        items = list(enumerate(self.visual.get("items", [])))
        first = next((n for n, it in items if it.get("kind", "card") != "note"), len(items))

        def kinds(ks: set[str]) -> list[tuple[int, dict]]:
            return [(n, it) for n, it in items if it.get("kind", "card") in ks]

        def notes(top: bool) -> str:
            group = [(n, it) for n, it in kinds({"note"}) if (n < first) == top]
            cells = "".join(self.item(it, n, fill=False) for n, it in group)
            return f'<div class="notes">{cells}</div>' if group else ""

        top = notes(top=True)
        if layout in ("split", "stack"):
            media = kinds({"img", "code"})
            img = next((it for _, it in media if it.get("kind") == "img" and Path(it.get("src", "")).is_file()), None)
            ar = image_aspect(img["src"]) if img else None
            if layout == "split" and ar and ar > STACK_ASPECT:
                layout = "stack"
                print(f"{self.id}: image is {ar:.1f}:1, laid out as stack instead of split")
            if layout == "stack":
                self.code_box = (BOARD_W, BOARD_H - (STACK_ROW if kinds({"card", "big", "step", "note"}) else 0))
            else:
                self.code_box = ((BOARD_W - GAP_MD) * 1.2 / 2.2, BOARD_H)  # .split-left is flex 1.2 : 1
            left = "".join(self.item(it, n, fill=True) for n, it in media)
            right = "".join(self.item(it, n, fill=False) for n, it in kinds({"card", "big", "step"}))
            side = top + right + notes(top=False)
            if layout == "stack":
                return f'<div class="stack"><div class="stack-media">{left}</div><div class="stack-row">{side}</div></div>'
            attrs = f'class="split fit" style="--ar:{ar:.3f}"' if ar else 'class="split"'
            return f'<div {attrs}><div class="split-left">{left}</div><div class="split-right">{side}</div></div>'
        out = top
        if steps := kinds({"step"}):
            row = ""
            for k, (n, it) in enumerate(steps):
                if k:
                    aid = f"{self.id}-a{n}"
                    row += f'<div class="arrow" id="{aid}">{ARROW_SVG}</div>'
                    self.js.append(f'tl.fromTo("#{aid}",{ARROW_REVEAL},{self.starts[it.get("at", 0)]});')
                row += self.item(it, n, fill=True)
            out += f'<div class="steps">{row}</div>'
        if grid := kinds({"card", "big", "img", "code"}):
            cols = self.visual.get("cols", 2)
            if isinstance(cols, bool) or not isinstance(cols, int) or cols < 1:
                self.warn(f"cols={cols!r} must be a positive integer; using 2")
                cols = 2
            rows = -(-len(grid) // cols)
            self.code_box = ((BOARD_W - GAP_SM * (cols - 1)) / cols, (BOARD_H - GAP_SM * (rows - 1)) / rows)
            cells = "".join(self.item(it, n, fill=True) for n, it in grid)
            out += f'<div class="grid" style="--cols:{cols}">{cells}</div>'
        return out + notes(top=False)

    def custom(self, name: str) -> str:
        """Inline custom/<name>.html: its markup goes on the board, its <script> body joins the scene timeline.

        The script can use tl (the scene timeline), S (sentence start seconds) and E (sentence end seconds).
        """
        path = Path(f"custom/{name}.html")
        if not path.is_file():
            self.fail(f"custom scene not found: {path}")
        src = path.read_text(encoding="utf-8")
        script = re.compile(r"<script\b[^>]*>(.*?)</script>", re.DOTALL | re.IGNORECASE)
        self.js.extend(script.findall(src))
        return script.sub("", src)

    def html(self) -> str:
        """Return the sub-composition file for this scene."""
        board = self.board()
        caps = "".join(
            f'<div class="clip caption" id="{self.id}-cap{n}" data-start="{self.starts[n]}" '
            f'data-duration="{round(self.ends[n] - self.starts[n], 3)}" data-track-index="2">'
            f'<div class="capbox">{e(s["text"].removesuffix("。"))}</div></div>'
            for n, s in enumerate(self.sentences)
        )
        audio = "".join(
            f'<audio id="{self.id}-vo{n}" src="{e(s["file"])}" data-start="{self.starts[n]}" '
            f'data-duration="{sec(s["frames"])}" data-hf-media-start-basis="local" '
            f'data-track-index="{10 + self.index}"></audio>'
            for n, s in enumerate(self.sentences)
        )
        js = "\n".join(
            [
                "const tl = gsap.timeline({ paused: true });",
                f"const S = {json.dumps(self.starts)}, E = {json.dumps(self.ends)};",
                f'tl.fromTo("#{self.id}-inner",{{opacity:0,y:16}},{{opacity:1,y:0,duration:{SCENE_IN},ease:"power3.out"}},0);',
                f'tl.fromTo("#{self.id}-content",{{opacity:1}},{{opacity:0,duration:{SCENE_OUT},ease:"power2.in"}},'
                f"{round(self.dur - SCENE_OUT - 0.05, 3)});",
                *self.js,
                f'window.__timelines["{self.id}"] = tl;',
            ]
        )
        return f"""<template id="{self.id}-template">
<div data-composition-id="{self.id}" data-width="{W}" data-height="{H}" data-duration="{self.dur}">
<div class="scene"><div class="content" id="{self.id}-content"><div class="inner" id="{self.id}-inner">
<div class="head"><div class="title">{e(self.title)}</div></div>
<div class="board">{board}</div>
</div>{caps}</div>{audio}</div>
<script>
{js}
</script>
</div>
</template>
"""


def main() -> None:
    """Write the HyperFrames project into the current folder."""
    args = sys.argv[1:]
    script_path = args[0] if args else "script.json"
    timeline_path = args[1] if len(args) > 1 else "timeline.json"
    script = json.loads(Path(script_path).read_text(encoding="utf-8"))
    timeline = {s["id"]: s for s in json.loads(Path(timeline_path).read_text(encoding="utf-8"))}
    theme_path = Path("theme.css") if Path("theme.css").is_file() else ASSETS / "theme.css"
    print(f"theme: {theme_path}")
    theme = theme_path.read_text(encoding="utf-8")
    tones = set(re.findall(r"^\.tone-([a-z0-9-]+)", theme, re.MULTILINE))
    gsap = Path("node_modules/gsap/dist/gsap.min.js")
    if not gsap.is_file():
        sys.exit("node_modules/gsap not found. Run: npm i -D hyperframes@0.8.139 gsap")
    Path("assets").mkdir(exist_ok=True)
    shutil.copy(gsap, "assets/gsap.min.js")
    comps = Path("compositions")
    if comps.exists():
        shutil.rmtree(comps)
    comps.mkdir()

    slots, settled, t = [], [], 0.0
    for i, sc in enumerate(script["scenes"], 1):
        if not SCENE_ID.match(sc["id"]):
            sys.exit(f"scene id {sc['id']!r} must be lowercase letters, digits and hyphens (e.g. s01-opening).")
        tl = timeline.get(sc["id"])
        if tl is None or [s["text"] for s in tl["sentences"]] != sc["sentences"]:
            sys.exit(f"{sc['id']}: sentences differ from {timeline_path}. Run gen_voice.py again.")
        scene = Scene(sc, tl, i, tones)
        (comps / f"{sc['id']}.html").write_text(scene.html(), encoding="utf-8")
        slots.append(
            f'<div class="clip" id="el-{sc["id"]}" data-composition-id="{sc["id"]}" '
            f'data-composition-src="compositions/{sc["id"]}.html" data-start="{round(t, 3)}" '
            f'data-duration="{scene.dur}" data-track-index="1" data-width="{W}" data-height="{H}"></div>'
        )
        settled.append(f"{t + scene.starts[-1] + 1.2:.1f}")  # every item of the scene is on screen
        t += scene.dur
    base = (ASSETS / "base.css").read_text(encoding="utf-8")
    Path("index.html").write_text(
        f"""<!doctype html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width={W}, height={H}">
<script src="assets/gsap.min.js"></script>
<style>
{theme}
{base}
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{round(t, 3)}" data-width="{W}" data-height="{H}" data-fps="{FPS}">
{chr(10).join(slots)}
</div>
<script>
window.__timelines["main"] = gsap.timeline({{ paused: true }});
</script>
</body>
</html>
""",
        encoding="utf-8",
    )
    print(f"{len(slots)} scenes, {round(t / 60, 2)} min -> index.html")
    print(f"snapshot --at {','.join(settled)}")


if __name__ == "__main__":
    main()
