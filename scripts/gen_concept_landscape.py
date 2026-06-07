#!/usr/bin/env python3
"""Generate a clean research-landscape SVG bubble map (v2) for all papers in 01_source.

Key changes from v1:
- Canvas 3200 × 2300 (was 1700 × 1180): ample room for all elements.
- Cluster centroids widely spaced; halos are verified non-overlapping.
- Citekey labels only for the 14 landmark papers (bolder, white-backed).
  All other bubbles carry a SVG <title> tooltip — visible on hover in browsers.
- Gap-link label boxes repositioned (t_frac) to avoid cluster halo collisions.
- Cluster heading boxes placed just above each halo with clear background.
"""
from __future__ import annotations
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC  = ROOT / "01_source"
OUT  = ROOT / "figure" / "concept_landscape.svg"

# ── cluster definitions ────────────────────────────────────────────────────────
# id: (display_label, fill, stroke, cx, cy, spread_radius)
# Layout is on an A3-landscape canvas: viewBox 0 0 4200 2970 (10 px ≈ 1 mm at print).
# Centroids are placed so that halos (spread + halo_pad) never overlap each other,
# and so that no cluster halo intrudes on the YOU-ARE-HERE node region.
CLUSTERS: dict[str, tuple] = {
    "G": ("Foundational DT Theory\n(aerospace · manufacturing)", "#e8e2f5", "#7d5fb2",  560,  720, 270),
    "H": ("Reviews & Taxonomies (SLR)",                           "#dfeaf6", "#3b6fa0", 1700,  600, 290),
    "F": ("Lifecycle Continuity\n& Governance",                   "#e3ecdc", "#5f7d46", 3380,  680, 245),
    "A": ("BIM-to-DT Architecture\n& Data Assimilation",          "#dceede", "#3f8f5b",  640, 1500, 240),
    "B": ("Semantic Interoperability\n& Ontologies",              "#fbeede", "#c08a3e", 1380, 1450, 195),
    "C": ("Perception, Registration\n& Computer Vision",          "#dbeef1", "#2f8f9d", 2080, 1620, 240),
    "D": ("Design-for-Safety (DfS)\nAutomation",                  "#f6e2e2", "#b6534f",  780, 2370, 285),
    "E": ("Predictive Analytics\n& Decision Support",             "#eae6da", "#8a7d4a", 1820, 2510, 280),
    "I": ("Uncertainty\nQuantification",                          "#fde8e6", "#e74c3c", 3160, 1750, 130),
    "J": ("NLP / Cross-modal\nMethods",                           "#ede0ef", "#9b59b6", 2880, 2530, 125),
}

# dashed-halo gap clusters
GAP_CLUSTERS = {"I", "J"}

# ── paper → cluster assignments ────────────────────────────────────────────────
ASSIGN = {
    # A ── BIM-to-DT architecture & data assimilation
    "Wang2022": "A",      "Lu2020": "A",         "Lu&Parlikad2020": "A", "Jiang2022": "A",
    "Jiang2022-81": "A",  "Jiang2021": "A",      "Sacks2020": "A",      "Tang2019": "A",
    "Hartmann2017": "A",  "Pome2023": "A",
    # B ── semantic interoperability & ontologies
    "Boje2020": "B",      "Theiler2018": "B",    "Zhang2015": "B",      "El-Gohary2016": "B",
    # C ── perception, registration & computer vision
    "Akhavian2025": "C",  "Spinner2024": "C",    "Degani2024": "C",     "Gan2025": "C",
    "Qiao2025-15": "C",   "Zhang2024": "C",      "Kim2025": "C",        "Kulinan2024": "C",
    "Pereira2025": "C",
    # D ── Design-for-Safety automation
    "Zhang2013": "D",     "Zhang2015-24": "D",   "Qi2014": "D",         "Hossain2018": "D",
    "Teizer2010": "D",    "Teo2005": "D",        "Sacks2009": "D",      "Akinci2002": "D",
    "Liu2020": "D",       "Liu2021": "D",        "Liu&Meng2021": "D",   "Ruppert2020": "D",
    "Ruppert2018": "D",   "Greif2020": "D",      "RajratnaKharat2018": "D", "Zhou2012": "D",
    # E ── predictive analytics & decision support
    "Choi2021": "E",      "Pan&Zhang2021": "E",  "Zhang2021": "E",      "Lee2025": "E",
    "Lu&Xie2020": "E",    "Hosamo2022": "E",     "Hosamo1988": "E",     "Hamel2024": "E",
    "AlOmari2026": "E",   "Pragna2026": "E",     "Fung2010": "E",       "Sun2023": "E",
    "Zhao2023": "E",      "Adibi2024": "E",
    # F ── lifecycle continuity & governance
    "19650-12018": "F",   "Bolpagni2025": "F",   "Broo2022": "F",       "Chen2021": "F",
    "Lee2021": "F",       "Harty2013": "F",      "Love2014": "F",       "Matthews2021": "F",
    "Xu2019": "F",        "Zhao2022": "F",       "Zhang2023": "F",      "Teisserenc2021": "F",
    # G ── foundational DT theory
    "23247-12021": "G",   "Glaessgen2012": "G",  "Stargel2012": "G",    "Glatt2021": "G",
    "Grieves2026": "G",   "Vickers2017": "G",    "Schleich2017": "G",   "Tao2018": "G",
    "Tao2019": "G",       "TaoZhang2017": "G",   "Uhlemann2017": "G",   "Lu2020-90": "G",
    "Qi2021": "G",        "Singh2021": "G",      "Rasheed1980": "G",    "MinQi2019": "G",
    "Holmstrom2010": "G",
    # H ── reviews & taxonomies
    "Deng2021": "H",      "Fuller2020": "H",     "Jones2020": "H",      "Kritzinger2018": "H",
    "Liu2021b": "H",      "Omrany2023": "H",     "Opoku2021": "H",      "Ozturk2021": "H",
    "Page2021": "H",      "Sepasgozar2020": "H", "Sepasgozar2021": "H", "Shahzad2022": "H",
    "Rasheed2020": "H",   "Wang2026": "H",       "Martinez-Aires2018": "H", "Hakimi2024": "H",
    "Machado2023": "H",   "Götz2022": "H",
    # I ── uncertainty quantification (the gap)
    "Abdar2021": "I",     "Grenyer2021": "I",    "Fu2026": "I",
    # J ── NLP / cross-modal methods (the gap)
    "Radford2021": "J",   "Tixier2016": "J",
}

# 14 landmark papers get a larger bubble AND a visible citekey label
LANDMARKS = {
    "Grieves2026", "Vickers2017", "Glaessgen2012", "Tao2019",
    "Jones2020",   "Sepasgozar2021", "Lu2020",     "Akhavian2025",
    "Zhang2013",   "Boje2020",       "Page2021",   "Abdar2021",
    "Deng2021",    "Omrany2023",
}

# established (solid) relationships between cluster centroids
SOLID_LINKS = [
    ("G", "H"), ("G", "A"), ("A", "H"), ("A", "B"), ("B", "C"),
    ("C", "D"), ("B", "D"), ("D", "E"), ("C", "E"), ("H", "E"),
    ("A", "F"), ("H", "F"),
]

# research gaps — (from, to, label, t_frac)
# t_frac = fraction along the line where the label box sits (avoids halo collisions)
GAP_LINKS = [
    ("C", "B", "no backward\nrule revision",          0.50),
    ("B", "E", "no forward\nforecasting",              0.50),
    ("I", "E", "UQ not\npropagated",                   0.50),
    ("I", "D", "no calibrated\nsafety bounds",         0.50),
    ("F", "D", "governance gap /\nphase discontinuity", 0.18),
]

# YOU-ARE-HERE node
HERE = (2540, 1170)

# (target_cluster, label, t_frac for label box along the arrow)
HERE_ARROWS = [
    ("I", "conformal UQ",            0.42),
    ("B", "LLM \u2192 brittle rules", 0.18),
    ("E", "backward + forward loop", 0.18),
    ("F", "cross-phase convergence", 0.42),
    ("D", "calibrated DfX",          0.14),
]

# A3 landscape, 10 px ≈ 1 mm
W, H_SVG = 4200, 2970


# ── helpers ───────────────────────────────────────────────────────────────────

def discover() -> dict[str, str]:
    found = {p.stem: ASSIGN.get(p.stem, "H") for p in SRC.glob("*.md")}
    missing = [k for k in found if k not in ASSIGN]
    if missing:
        print("WARN unassigned (defaulted to H):", missing)
    return found


def layout(found: dict[str, str]) -> dict[str, tuple[float, float, float]]:
    """Golden-angle phyllotaxis packing inside each cluster halo."""
    pos: dict[str, tuple[float, float, float]] = {}
    by_cluster: dict[str, list[str]] = {}
    for key, cid in found.items():
        by_cluster.setdefault(cid, []).append(key)
    for cid, keys in by_cluster.items():
        keys.sort()
        _, _, _, cx, cy, spread = CLUSTERS[cid]
        n = len(keys)
        for i, key in enumerate(keys):
            r = spread * math.sqrt((i + 0.5) / n) if n > 1 else 0
            ang = i * 2.399963          # golden angle ≈ 137.5°
            x = cx + r * math.cos(ang)
            y = cy + r * math.sin(ang)
            rad = 32 if key in LANDMARKS else 21
            pos[key] = (x, y, rad)
    return pos


def esc(s: str) -> str:
    return (s.replace("&", "&amp;")
             .replace("<", "&lt;")
             .replace(">", "&gt;")
             .replace('"', "&quot;"))


def multiline(x: float, y: float, text: str, size: float,
              color: str, weight: str = "normal",
              anchor: str = "middle", lh: float | None = None) -> str:
    lh = lh or size + 3
    lines = text.split("\n")
    y0 = y - (len(lines) - 1) * lh / 2
    out = [
        f'<text x="{x:.1f}" y="{y0 + i * lh:.1f}" font-size="{size}" '
        f'fill="{color}" font-weight="{weight}" text-anchor="{anchor}" '
        f'font-family="Segoe UI, Arial, sans-serif">{esc(ln)}</text>'
        for i, ln in enumerate(lines)
    ]
    return "\n".join(out)


def landmark_label(x: float, y: float, key: str, rad: float) -> list[str]:
    """White-backed citekey label drawn below a landmark bubble."""
    fs = 18
    tw = max(len(key) * 10.0, 100)
    top = y + rad + 6
    return [
        f'<rect x="{x - tw/2:.1f}" y="{top:.1f}" '
        f'width="{tw:.0f}" height="26" rx="3" '
        f'fill="white" fill-opacity="0.92" stroke="none"/>',
        f'<text x="{x:.1f}" y="{top + 19:.1f}" font-size="{fs}" fill="#1a1a2e" '
        f'font-weight="bold" text-anchor="middle" '
        f'font-family="Segoe UI, Arial, sans-serif">{esc(key)}</text>',
    ]


def cluster_heading(cid: str, label: str, stroke: str,
                    cx: float, cy: float, spread: float) -> list[str]:
    """Label box placed just above the cluster halo circle.

    Solid white fill + dark navy text for maximum legibility; the cluster
    colour is conveyed by the box border and a coloured ID chip on the left.
    """
    n_lines = label.count("\n") + 1
    bh = 24 + n_lines * 26
    bw = 460
    box_bottom = cy - (spread + 50) - 18
    box_top    = box_bottom - bh
    # ID chip on the left edge of the box
    chip_w = 56
    chip_x = cx - bw / 2
    chip_cx = chip_x + chip_w / 2
    chip_cy = (box_top + box_bottom) / 2
    text_cy = chip_cy + 2
    text_cx = chip_x + chip_w + (bw - chip_w) / 2
    return [
        f'<rect x="{chip_x:.1f}" y="{box_top:.1f}" '
        f'width="{bw}" height="{bh}" rx="8" '
        f'fill="#ffffff" stroke="{stroke}" stroke-width="2.5"/>',
        f'<rect x="{chip_x:.1f}" y="{box_top:.1f}" '
        f'width="{chip_w}" height="{bh}" rx="8" '
        f'fill="{stroke}" stroke="none"/>',
        f'<rect x="{chip_x + chip_w - 8:.1f}" y="{box_top:.1f}" '
        f'width="8" height="{bh}" fill="{stroke}" stroke="none"/>',
        f'<text x="{chip_cx:.1f}" y="{chip_cy + 10:.1f}" font-size="28" '
        f'fill="#ffffff" font-weight="bold" text-anchor="middle" '
        f'font-family="Segoe UI, Arial, sans-serif">{esc(cid)}</text>',
        multiline(text_cx, text_cy, label, 19, "#1a1a2e", weight="bold", lh=24),
    ]


def star_points(cx: float, cy: float, ro: float, ri: float, n: int = 5) -> str:
    pts = []
    for i in range(2 * n):
        r = ro if i % 2 == 0 else ri
        a = -math.pi / 2 + i * math.pi / n
        pts.append(f"{cx + r * math.cos(a):.1f},{cy + r * math.sin(a):.1f}")
    return " ".join(pts)


# ── main build ────────────────────────────────────────────────────────────────

def build() -> str:
    found = discover()
    pos = layout(found)
    s: list[str] = []

    s.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="420mm" height="297mm" viewBox="0 0 {W} {H_SVG}" '
        f'font-family="Segoe UI, Arial, sans-serif">'
    )
    s.append(
        '<defs>'
        '<marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" '
        'orient="auto" markerUnits="strokeWidthBased">'
        '<path d="M0,0 L9,3 L0,6 Z" fill="#1f8a4c"/></marker>'
        '<marker id="gap" markerWidth="10" markerHeight="10" refX="8" refY="3" '
        'orient="auto" markerUnits="strokeWidthBased">'
        '<path d="M0,0 L9,3 L0,6 Z" fill="#e74c3c"/></marker>'
        '</defs>'
    )

    # ── background + title bar
    s.append(f'<rect width="{W}" height="{H_SVG}" fill="#fbfbfd"/>')
    s.append(f'<rect x="0" y="0" width="{W}" height="148" fill="#f5f5fa" '
             f'stroke="#d8d8e8" stroke-width="1.5"/>')
    s.append(multiline(60, 60,
                       "AECO Digital-Twin Research Landscape  —  103 papers",
                       38, "#1a1a2e", weight="bold", anchor="start"))
    s.append(multiline(60, 110,
                       "Solid lines = established field relationships   \u00b7   "
                       "Dashed red = unresolved gaps   \u00b7   "
                       "\u2605 = candidate position (RP.md)   \u00b7   "
                       "Hover over an unlabelled bubble to see its citekey",
                       20, "#555", anchor="start"))

    def centroid(cid: str) -> tuple[float, float]:
        return float(CLUSTERS[cid][3]), float(CLUSTERS[cid][4])

    # ── cluster halos (drawn first, semi-transparent)
    for cid, (label, fill, stroke, cx, cy, spread) in CLUSTERS.items():
        dash = ' stroke-dasharray="14 10"' if cid in GAP_CLUSTERS else ''
        op   = 0.30 if cid in GAP_CLUSTERS else 0.48
        s.append(
            f'<circle cx="{cx}" cy="{cy}" r="{spread + 50}" fill="{fill}" '
            f'fill-opacity="{op}" stroke="{stroke}" stroke-width="3"{dash}/>'
        )

    # ── established solid links
    for a, b in SOLID_LINKS:
        ax, ay = centroid(a)
        bx, by = centroid(b)
        s.append(
            f'<line x1="{ax}" y1="{ay}" x2="{bx}" y2="{by}" '
            f'stroke="#9aa6b2" stroke-width="3.2" stroke-opacity="0.55"/>'
        )

    # ── gap links (dashed red with label boxes)
    for a, b, lbl, t in GAP_LINKS:
        ax, ay = centroid(a)
        bx, by = centroid(b)
        lx = ax + (bx - ax) * t
        ly = ay + (by - ay) * t
        n_lbl = lbl.count("\n") + 1
        bh_lbl = 18 + n_lbl * 22
        bw_lbl = 230
        s.append(
            f'<line x1="{ax}" y1="{ay}" x2="{bx}" y2="{by}" '
            f'stroke="#e74c3c" stroke-width="3.2" stroke-dasharray="14 9" '
            f'marker-end="url(#gap)" stroke-opacity="0.85"/>'
        )
        s.append(
            f'<rect x="{lx - bw_lbl/2:.1f}" y="{ly - bh_lbl/2:.1f}" '
            f'width="{bw_lbl}" height="{bh_lbl}" rx="6" '
            f'fill="#fff8f8" stroke="#e74c3c" stroke-opacity="0.6" stroke-width="1.5"/>'
        )
        s.append(multiline(lx, ly, lbl, 17, "#b03a2e", weight="bold", lh=22))

    # ── paper bubbles
    for key, cid in found.items():
        x, y, rad = pos[key]
        _, fill, stroke, *_ = CLUSTERS[cid]
        big = key in LANDMARKS
        sw  = "3.6" if big else "2.0"
        s.append(f'<g><title>{esc(key)}</title>')
        s.append(
            f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{rad}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
        )
        s.append('</g>')

    # ── citekey labels: bold white-backed for landmarks; small inline for the rest
    for key, cid in found.items():
        x, y, rad = pos[key]
        if key in LANDMARKS:
            s.extend(landmark_label(x, y, key, rad))
        else:
            _, _, stroke, *_ = CLUSTERS[cid]
            top = y + rad + 2
            tw  = max(len(key) * 7.2, 60)
            s.append(
                f'<rect x="{x - tw/2:.1f}" y="{top:.1f}" '
                f'width="{tw:.0f}" height="16" rx="2" '
                f'fill="#ffffff" fill-opacity="0.85" stroke="none"/>'
            )
            s.append(
                f'<text x="{x:.1f}" y="{top + 12:.1f}" font-size="12" '
                f'fill="#1a1a2e" text-anchor="middle" '
                f'font-family="Segoe UI, Arial, sans-serif">{esc(key)}</text>'
            )

    # ── cluster heading boxes (drawn last so they sit on top)
    for cid, (label, fill, stroke, cx, cy, spread) in CLUSTERS.items():
        s.extend(cluster_heading(cid, label, stroke, cx, cy, spread))

    # ── YOU ARE HERE arrows into gap zones
    hx, hy = HERE
    for cid, lbl, t in HERE_ARROWS:
        cx_t, cy_t = centroid(cid)
        s.append(
            f'<line x1="{hx}" y1="{hy}" x2="{cx_t}" y2="{cy_t}" '
            f'stroke="#1f8a4c" stroke-width="4.6" '
            f'marker-end="url(#arrow)" stroke-opacity="0.88"/>'
        )
        alx = hx + (cx_t - hx) * t
        aly = hy + (cy_t - hy) * t
        tw  = max(len(lbl) * 11.0, 170)
        s.append(
            f'<rect x="{alx - tw/2:.1f}" y="{aly - 18:.1f}" '
            f'width="{tw:.0f}" height="36" rx="6" '
            f'fill="#eafaf0" stroke="#1f8a4c" stroke-opacity="0.6" stroke-width="1.5"/>'
        )
        s.append(
            f'<text x="{alx:.1f}" y="{aly + 8:.1f}" font-size="17" fill="#15703d" '
            f'font-weight="bold" text-anchor="middle" '
            f'font-family="Segoe UI, Arial, sans-serif">{esc(lbl)}</text>'
        )

    # ── YOU ARE HERE star node
    star = star_points(hx, hy, 100, 42)
    s.append(
        f'<circle cx="{hx}" cy="{hy}" r="140" fill="#fff6da" '
        f'stroke="#d97706" stroke-width="4.5"/>'
    )
    s.append(f'<polygon points="{star}" fill="#f1c40f" stroke="#d97706" stroke-width="3"/>')
    s.append(multiline(hx, hy - 14, "YOU ARE HERE",                    21,   "#7a4a00", weight="bold"))
    s.append(multiline(hx, hy + 18, "Cognitive cross-phase\nself-improving DT", 17, "#7a4a00", lh=22))

    # ── legend box (bottom-right)
    lx, ly_leg = 3260, 2680
    s.append(
        f'<rect x="{lx}" y="{ly_leg}" width="860" height="260" rx="12" '
        f'fill="#ffffff" stroke="#bbb" stroke-width="1.8"/>'
    )
    s.append(multiline(lx + 28, ly_leg + 44,
                       "Legend", 24, "#222", weight="bold", anchor="start"))
    legend_rows = [
        (94,  "#9aa6b2", "3.2", None,   "Established field relationship"),
        (140, "#e74c3c", "3.2", "14 9", "Unresolved link \u2014 research gap"),
        (186, "#1f8a4c", "4.6", None,   "Candidate contribution closes the gap"),
    ]
    for row_y, col, sw, dash, txt in legend_rows:
        da = f' stroke-dasharray="{dash}"' if dash else ''
        s.append(
            f'<line x1="{lx+28}" y1="{ly_leg+row_y}" '
            f'x2="{lx+120}" y2="{ly_leg+row_y}" '
            f'stroke="{col}" stroke-width="{sw}"{da}/>'
        )
        s.append(
            f'<text x="{lx+140}" y="{ly_leg+row_y+8}" font-size="19" fill="#444" '
            f'font-family="Segoe UI, Arial, sans-serif">{esc(txt)}</text>'
        )
    s.append(
        f'<circle cx="{lx+50}" cy="{ly_leg+228}" r="17" '
        f'fill="#dde8ff" stroke="#3b6fa0" stroke-width="3"/>'
    )
    s.append(
        f'<text x="{lx+140}" y="{ly_leg+236}" font-size="19" fill="#444" '
        f'font-family="Segoe UI, Arial, sans-serif">'
        f'Larger bubble = landmark / high-influence paper</text>'
    )

    s.append('</svg>')
    return "\n".join(s)


if __name__ == "__main__":
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(build(), encoding="utf-8")
    print("wrote", OUT)
