from pathlib import Path

import schemdraw.elements as elm
from schemdraw import Drawing
from schemdraw.flow import Box

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "assets" / "circuits"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

elm.style(elm.STYLE_IEC)
STYLE = {"fontsize": 14}

# 1 电容
with Drawing(show=False) as d:
    d.config(fontsize=STYLE["fontsize"])

    d += elm.Dot(open=True).at((0, 0))
    d += elm.Line().at((0, 0)).to((3, 0))

    d += elm.Capacitor(polar=True).at((3, 0)).to((4, 0)).label("$u (t)$", "bottom")

    d += elm.Line().at((4, 0)).to((7, 0))
    d += elm.Dot(open=True).at((7, 0))

    d += elm.Arrow().at((1, 0)).to((1.5, 0)).label("$i (t)$", "top")

    d.save(OUTPUT_DIR / "5_1_1.svg")
