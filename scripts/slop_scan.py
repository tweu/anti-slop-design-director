#!/usr/bin/env python3
"""Heuristic scan for generic "AI slop" UI patterns in CSS/HTML/JSX/TSX/Vue/Svelte files.

Usage:
  python slop_scan.py <file-or-dir> [...]       # report findings
  python slop_scan.py --json <paths>            # machine-readable
  python slop_scan.py --contrast "#59606E" "#F7F4EE"   # WCAG contrast ratio
  python slop_scan.py --self-test

Findings are signals for a human/agent to judge, not verdicts: each one is fine when the
product, brief or settings justify it (see knowledge/evaluation/anti-patterns.md).
Standard library only.
"""
import json
import os
import re
import sys

EXTS = {".css", ".scss", ".sass", ".less", ".html", ".htm", ".jsx", ".tsx", ".js", ".ts", ".vue", ".svelte", ".astro", ".mdx"}
SKIP_DIRS = {"node_modules", ".git", "dist", "build", ".next", "out", ".nuxt", ".svelte-kit", "coverage", "vendor", ".turbo"}

# (id, regex, message). Counted per file.
RULES = [
    ("gradient-text", r"background-clip\s*:\s*text|-webkit-background-clip\s*:\s*text|\bbg-clip-text\b",
     "Gradient text: emphasis usually belongs to weight or size"),
    ("violet-gradient", r"\b(?:from|via|to)-(?:purple|violet|indigo|fuchsia)-\d{2,3}\b|linear-gradient\([^)]*(?:purple|violet|indigo|#(?:7c3aed|8b5cf6|6366f1|a855f7|9333ea|4f46e5))",
     "Purple/violet gradient: justified only by brand or request"),
    ("glass-blur", r"backdrop-filter\s*:|\bbackdrop-blur(?:-\w+)?\b",
     "Backdrop blur/glass: justified only over real content that must stay visible"),
    ("pill-shape", r"\brounded-full\b|border-radius\s*:\s*(?:9999px|999px|50vh|100vh|10rem)",
     "Pill shape: check the pills setting (avatars and dots are fine)"),
    ("hard-offset-shadow", r"box-shadow\s*:\s*-?\d+px\s+-?\d+px\s+0(?:px)?\s",
     "Hard offset shadow: brutalist direction only"),
    ("shadow", r"\bshadow-(?:sm|md|lg|xl|2xl|inner)\b|\bshadow\b(?=[\s\"'`])|box-shadow\s*:",
     "Shadow use: elevation should mean something"),
    ("scroll-reveal", r"\bwhileInView\b|data-aos\b|\bScrollTrigger\b|\buseInView\b",
     "Scroll reveal: one authored moment, not every section"),
    ("placeholder-copy", r"(?i)lorem ipsum|\bjohn doe\b|\bjane doe\b|\bacme\b|\[your [a-z]|\bTODO\b",
     "Placeholder copy or fake names"),
    ("generic-cta", r"(?i)>\s*(?:get started|learn more|click here|submit)\s*<",
     "Generic CTA: use verb + object"),
    ("eyebrow", r"\buppercase\b[^\"'`]*\btracking-(?:wide|wider|widest)\b|\btracking-(?:wide|wider|widest)\b[^\"'`]*\buppercase\b",
     "Possible eyebrow label (small tracked caps): keep only if it carries information"),
    ("emoji-icon", "[\U0001F300-\U0001FAFF✨⚡✅⭐]",
     "Emoji used in UI: prefer a consistent icon set"),
]
RAW_HEX = re.compile(r"#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b")
CARD_OPEN = re.compile(r"<(?:div|article|section|li)\b[^>]*class(?:Name)?=[\"'`{][^>]*\b(?:card|rounded-(?:lg|xl|2xl|3xl)[^\"'`]*\b(?:border|shadow)|(?:border|shadow)[^\"'`]*\brounded-(?:lg|xl|2xl|3xl))", re.I)
TAG = re.compile(r"<(/?)(div|article|section|li)\b[^>]*?(/?)>", re.I)


def is_card(tag_text):
    return bool(CARD_OPEN.match(tag_text))


def nested_cards(text):
    """Count card-like elements opened inside another card-like element (rough, markup-only)."""
    stack, hits = [], 0
    for m in TAG.finditer(text):
        closing, self_closing = m.group(1) == "/", m.group(3) == "/"
        if closing:
            if stack:
                stack.pop()
            continue
        card = is_card(m.group(0))
        if card and any(stack):
            hits += 1
        if not self_closing:
            stack.append(card)
    return hits


def scan_text(text, is_component):
    found = {}
    for rid, pat, _ in RULES:
        n = len(re.findall(pat, text))
        if n:
            found[rid] = n
    n = nested_cards(text)
    if n:
        found["nested-cards"] = n
    if is_component:
        # raw colours inside component files (token files are expected to hold them)
        n = len(RAW_HEX.findall(text))
        if n:
            found["raw-hex"] = n
    return found


MESSAGES = {rid: msg for rid, _, msg in RULES}
MESSAGES["nested-cards"] = "Card-like element inside another: check the containers setting"
MESSAGES["raw-hex"] = "Raw hex colours in a component: move to tokens"


def iter_files(paths):
    for p in paths:
        if os.path.isfile(p):
            yield p
        elif os.path.isdir(p):
            for root, dirs, files in os.walk(p):
                dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
                for f in files:
                    if os.path.splitext(f)[1].lower() in EXTS:
                        yield os.path.join(root, f)


def looks_like_token_file(path, text):
    name = os.path.basename(path).lower()
    return any(k in name for k in ("token", "theme", "variables", "globals", "tailwind.config")) or ":root" in text or "@theme" in text


def scan(paths):
    results = {}
    for f in iter_files(paths):
        try:
            with open(f, encoding="utf-8", errors="replace") as fh:
                text = fh.read()
        except OSError:
            continue
        ext = os.path.splitext(f)[1].lower()
        is_component = ext in {".jsx", ".tsx", ".vue", ".svelte", ".astro"} and not looks_like_token_file(f, text)
        found = scan_text(text, is_component)
        if found:
            results[f] = found
    return results


# ---------- contrast ----------
def _lin(c):
    c /= 255.0
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hexcolor):
    h = hexcolor.lstrip("#")
    if len(h) == 3:
        h = "".join(ch * 2 for ch in h)
    if not re.fullmatch(r"[0-9a-fA-F]{6}", h):
        raise ValueError("expected #RRGGBB or #RGB, got %r" % hexcolor)
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def contrast(fg, bg):
    a, b = sorted((luminance(fg), luminance(bg)), reverse=True)
    return (a + 0.05) / (b + 0.05)


def self_test():
    assert abs(contrast("#000", "#fff") - 21.0) < 0.01
    assert abs(contrast("#777777", "#ffffff") - 4.48) < 0.02
    t = '<div className="rounded-xl border p-4"><div className="card">x</div></div>'
    assert nested_cards(t) == 1, nested_cards(t)
    assert nested_cards('<div className="card">a</div><div className="card">b</div>') == 0
    f = scan_text('<h1 className="bg-clip-text bg-gradient-to-r from-purple-500">Hi</h1><button>Get started</button>', True)
    assert f.get("gradient-text") == 1 and f.get("violet-gradient") == 1 and f.get("generic-cta") == 1, f
    assert "pill-shape" in scan_text(".tag{border-radius:9999px}", False)
    assert "raw-hex" not in scan_text("a{color:#fff}", False)
    print("self-test ok")


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if argv[0] == "--self-test":
        self_test()
        return 0
    if argv[0] == "--contrast":
        if len(argv) != 3:
            print("usage: --contrast FG BG")
            return 2
        r = contrast(argv[1], argv[2])
        verdict = "AA body" if r >= 4.5 else "AA large/UI only" if r >= 3 else "FAIL"
        print("%.2f:1  %s" % (r, verdict))
        return 0
    as_json = argv[0] == "--json"
    paths = argv[1:] if as_json else argv
    results = scan(paths)
    if as_json:
        print(json.dumps(results, indent=2))
        return 0
    if not results:
        print("No slop signals found in %d path(s). Still review the render: a clean scan proves little." % len(paths))
        return 0
    totals = {}
    for f, found in sorted(results.items()):
        print(f)
        for rid, n in sorted(found.items()):
            totals[rid] = totals.get(rid, 0) + n
            print("  %-18s x%-3d %s" % (rid, n, MESSAGES[rid]))
    print("\nTotals: " + ", ".join("%s=%d" % kv for kv in sorted(totals.items(), key=lambda kv: -kv[1])))
    print("Signals, not verdicts: judge each against the product, brief and settings.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
