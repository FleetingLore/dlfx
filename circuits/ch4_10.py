from pathlib import Path

import schemdraw.elements as elm
from schemdraw import Drawing
from schemdraw.flow import Box

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "assets" / "circuits"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

elm.style(elm.STYLE_IEC)
STYLE = {"fontsize": 14}

# 1 双口网络及其端口变量
with Drawing(show=False) as d:
    d.config(fontsize=STYLE["fontsize"])

    d += elm.Dot(open=True).at((-3, 1)).label("$+$", "left")
    d += elm.Dot(open=True).at((-3, -1)).label("$-$", "left")
    d += elm.Dot(open=True).at((3, 1)).label("$+$", "right")
    d += elm.Dot(open=True).at((3, -1)).label("$-$", "right")

    d += elm.Line().at((-1.5, +1.5)).to((+1.5, +1.5)).linewidth(3)
    d += elm.Line().at((+1.5, +1.5)).to((+1.5, -1.5)).linewidth(3)
    d += elm.Line().at((+1.5, -1.5)).to((-1.5, -1.5)).linewidth(3)
    d += elm.Line().at((-1.5, -1.5)).to((-1.5, +1.5)).linewidth(3)

    d += elm.Line().at((-3, 1)).to((-1.5, 1))
    d += elm.Line().at((-3, -1)).to((-1.5, -1))
    d += elm.Line().at((3, 1)).to((1.5, 1))
    d += elm.Line().at((3, -1)).to((1.5, -1))

    d += elm.Line().at((-3, 0)).to((-3, 0)).label("$u_1$")
    d += elm.Line().at((3, 0)).to((3, 0)).label("$u_2$")

    d.save(OUTPUT_DIR / "4_10_1.svg")

# 2 开路电阻参数的表征
with Drawing(show=False) as d:
    d.config(fontsize=STYLE["fontsize"])

    pad = -4

    d += elm.Dot(open=True).at((-2 + pad, +1))
    d += elm.Dot(open=True).at((+3 + pad, +1))
    d += elm.Dot(open=True).at((-2 + pad, -1))
    d += elm.Dot(open=True).at((+3 + pad, -1))

    d += elm.Dot(open=True).at((3 + pad, 1)).label("$+$", "right")
    d += elm.Dot(open=True).at((3 + pad, -1)).label("$-$", "right")

    d += elm.Line().at((-1.5 + pad, +1.5)).to((+1.5 + pad, +1.5)).linewidth(3)
    d += elm.Line().at((+1.5 + pad, +1.5)).to((+1.5 + pad, -1.5)).linewidth(3)
    d += elm.Line().at((+1.5 + pad, -1.5)).to((-1.5 + pad, -1.5)).linewidth(3)
    d += elm.Line().at((-1.5 + pad, -1.5)).to((-1.5 + pad, +1.5)).linewidth(3)

    d += elm.Line().at((-2 + pad, +1)).to((-1.5 + pad, +1))
    d += elm.Line().at((-2 + pad, -1)).to((-1.5 + pad, -1))
    d += elm.Line().at((+3 + pad, +1)).to((+1.5 + pad, +1))
    d += elm.Line().at((+3 + pad, -1)).to((+1.5 + pad, -1))

    d += elm.Line().at((-2 + pad, 0)).to((-2 + pad, 0)).label("$u_1$")
    d += elm.Line().at((+3 + pad, 0)).to((+3 + pad, 0)).label("$u_2$")

    d += elm.Line().at((-2 + pad, +1)).to((-3 + pad, +1))
    d += elm.Line().at((-3 + pad, -1)).to((-2 + pad, -1))
    d += elm.SourceI().at((-3 + pad, -1)).to((-3 + pad, +1))

    pad = 4

    d += elm.Dot(open=True).at((-3 + pad, +1))
    d += elm.Dot(open=True).at((+2 + pad, +1))
    d += elm.Dot(open=True).at((-3 + pad, -1))
    d += elm.Dot(open=True).at((+2 + pad, -1))

    d += elm.Dot(open=True).at((-3 + pad, 1)).label("$+$", "left")
    d += elm.Dot(open=True).at((-3 + pad, -1)).label("$-$", "left")

    d += elm.Line().at((-1.5 + pad, +1.5)).to((+1.5 + pad, +1.5)).linewidth(3)
    d += elm.Line().at((+1.5 + pad, +1.5)).to((+1.5 + pad, -1.5)).linewidth(3)
    d += elm.Line().at((+1.5 + pad, -1.5)).to((-1.5 + pad, -1.5)).linewidth(3)
    d += elm.Line().at((-1.5 + pad, -1.5)).to((-1.5 + pad, +1.5)).linewidth(3)

    d += elm.Line().at((-3 + pad, +1)).to((-1.5 + pad, +1))
    d += elm.Line().at((-3 + pad, -1)).to((-1.5 + pad, -1))
    d += elm.Line().at((+2 + pad, +1)).to((+1.5 + pad, +1))
    d += elm.Line().at((+2 + pad, -1)).to((+1.5 + pad, -1))

    d += elm.Line().at((-3 + pad, 0)).to((-3 + pad, 0)).label("$u_1$")
    d += elm.Line().at((+2 + pad, 0)).to((+2 + pad, 0)).label("$u_2$")

    d += elm.Line().at((+2 + pad, +1)).to((+3 + pad, +1))
    d += elm.Line().at((+3 + pad, -1)).to((+2 + pad, -1))
    d += elm.SourceI().at((+3 + pad, -1)).to((+3 + pad, +1))

    d.save(OUTPUT_DIR / "4_10_2.svg")
