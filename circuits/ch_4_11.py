from pathlib import Path

import schemdraw.elements as elm
from schemdraw import Drawing
from schemdraw.flow import Box

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "assets" / "circuits"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

elm.style(elm.STYLE_IEC)
STYLE = {"fontsize": 14}

# 1 互易性在流控型的一种实现
with Drawing(show=False) as d:
    d.config(fontsize=STYLE["fontsize"])

    pad = -4

    d += elm.Dot(open=True).at((-3 + pad, -2))
    d += elm.Dot(open=True).at((+3 + pad, -2))
    d += elm.Line().at((-3 + pad, -2)).to((+3 + pad, -2))

    d += elm.Resistor().at((0 + pad, 2)).to((0 + pad, -2))

    d += elm.Dot(open=True).at((-3 + pad, +2))
    d += elm.Resistor().at((0 + pad, 2)).to((-3 + pad, 2))

    d += elm.Dot(open=True).at((+3 + pad, +2))
    d += elm.Resistor().at((0 + pad, 2)).to((+3 + pad, 2))

    d += elm.Line().at((-3 + pad, +2)).to((-4 + pad, +2))
    d += elm.Line().at((-3 + pad, -2)).to((-4 + pad, -2))
    d += elm.SourceI().at((-4 + pad, -2)).to((-4 + pad, +2))

    d += (
        elm.Line()
        .at((-2.5 + pad, +2.5))
        .to((+2.5 + pad, +2.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )
    d += (
        elm.Line()
        .at((-2.5 + pad, -2.5))
        .to((+2.5 + pad, -2.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )
    d += (
        elm.Line()
        .at((+2.5 + pad, +2.5))
        .to((+2.5 + pad, -2.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )
    d += (
        elm.Line()
        .at((-2.5 + pad, +2.5))
        .to((-2.5 + pad, -2.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )

    pad = 4

    d += elm.Dot(open=True).at((+3 + pad, -2))
    d += elm.Dot(open=True).at((-3 + pad, -2))
    d += elm.Line().at((3 + pad, -2)).to((-3 + pad, -2))

    d += elm.Resistor().at((0 + pad, 2)).to((0 + pad, -2))

    d += elm.Dot(open=True).at((3 + pad, +2))
    d += elm.Resistor().at((0 + pad, 2)).to((3 + pad, 2))

    d += elm.Dot(open=True).at((-3 + pad, +2))
    d += elm.Resistor().at((0 + pad, 2)).to((-3 + pad, 2))

    d += elm.Line().at((3 + pad, +2)).to((4 + pad, +2))
    d += elm.Line().at((3 + pad, -2)).to((4 + pad, -2))
    d += elm.SourceI().at((4 + pad, -2)).to((4 + pad, +2))

    d += (
        elm.Line()
        .at((2.5 + pad, +2.5))
        .to((-2.5 + pad, +2.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )
    d += (
        elm.Line()
        .at((+2.5 + pad, -2.5))
        .to((-2.5 + pad, -2.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )
    d += (
        elm.Line()
        .at((-2.5 + pad, +2.5))
        .to((-2.5 + pad, -2.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )
    d += (
        elm.Line()
        .at((+2.5 + pad, +2.5))
        .to((+2.5 + pad, -2.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )

    d.save(OUTPUT_DIR / "4_11_1.svg")


# 2 对称性在流控型的一种实现
with Drawing(show=False) as d:
    d.config(fontsize=STYLE["fontsize"])

    pad = -4

    d += elm.Dot(open=True).at((-2 + pad, +1))
    d += elm.Dot(open=True).at((+3 + pad, +1))
    d += elm.Dot(open=True).at((-2 + pad, -1))
    d += elm.Dot(open=True).at((+3 + pad, -1))

    d += elm.Line().at((-1.5 + pad, +1.5)).to((+1.5 + pad, +1.5)).linewidth(3)
    d += elm.Line().at((+1.5 + pad, +1.5)).to((+1.5 + pad, -1.5)).linewidth(3)
    d += elm.Line().at((+1.5 + pad, -1.5)).to((-1.5 + pad, -1.5)).linewidth(3)
    d += elm.Line().at((-1.5 + pad, -1.5)).to((-1.5 + pad, +1.5)).linewidth(3)

    d += elm.Line().at((-2 + pad, +1)).to((-1.5 + pad, +1))
    d += elm.Line().at((-2 + pad, -1)).to((-1.5 + pad, -1))
    d += elm.Line().at((+3 + pad, +1)).to((+1.5 + pad, +1))
    d += elm.Line().at((+3 + pad, -1)).to((+1.5 + pad, -1))

    d += elm.Line().at((-2 + pad, +1)).to((-3 + pad, +1))
    d += elm.Line().at((-3 + pad, -1)).to((-2 + pad, -1))
    d += elm.SourceI().at((-3 + pad, -1)).to((-3 + pad, +1))

    pad = 4

    d += elm.Dot(open=True).at((-3 + pad, +1))
    d += elm.Dot(open=True).at((+2 + pad, +1))
    d += elm.Dot(open=True).at((-3 + pad, -1))
    d += elm.Dot(open=True).at((+2 + pad, -1))

    d += elm.Line().at((-1.5 + pad, +1.5)).to((+1.5 + pad, +1.5)).linewidth(3)
    d += elm.Line().at((+1.5 + pad, +1.5)).to((+1.5 + pad, -1.5)).linewidth(3)
    d += elm.Line().at((+1.5 + pad, -1.5)).to((-1.5 + pad, -1.5)).linewidth(3)
    d += elm.Line().at((-1.5 + pad, -1.5)).to((-1.5 + pad, +1.5)).linewidth(3)

    d += elm.Line().at((-3 + pad, +1)).to((-1.5 + pad, +1))
    d += elm.Line().at((-3 + pad, -1)).to((-1.5 + pad, -1))
    d += elm.Line().at((+2 + pad, +1)).to((+1.5 + pad, +1))
    d += elm.Line().at((+2 + pad, -1)).to((+1.5 + pad, -1))

    d += elm.Line().at((+2 + pad, +1)).to((+3 + pad, +1))
    d += elm.Line().at((+3 + pad, -1)).to((+2 + pad, -1))
    d += elm.SourceI().at((+3 + pad, -1)).to((+3 + pad, +1))

    d.save(OUTPUT_DIR / "4_11_2.svg")
