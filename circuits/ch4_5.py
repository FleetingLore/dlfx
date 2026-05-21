from pathlib import Path

import schemdraw.elements as elm
from schemdraw import Drawing
from schemdraw.flow import Box

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "assets" / "circuits"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

elm.style(elm.STYLE_IEC)
STYLE = {"fontsize": 14}

# 1 两电压源串联
with Drawing(show=False) as d:
    d.config(fontsize=STYLE["fontsize"])

    d += elm.Dot(open=True).at((3, 0)).label("$+$", "right")
    d += elm.Line().at((3, 0)).to((0, 0))

    d += elm.SourceV().at((0, -2)).to((0, 0)).label("$u_{S1}$")
    d += elm.SourceV().at((0, -4)).to((0, -2)).label("$u_{S2}$")

    d += elm.Line().at((0, -4)).to((3, -4))
    d += elm.Dot(open=True).at((3, -4)).label("$-$", "right")

    d += elm.Arrow().at((1, 0)).to((2, 0)).label("$i$", "top")

    d += (
        elm.Line().at((-1.5, +0.5)).to((+1.0, +0.5)).linestyle("dashdot").linewidth(0.5)
    )
    d += (
        elm.Line().at((+1.0, +0.5)).to((+1.0, -4.5)).linestyle("dashdot").linewidth(0.5)
    )
    d += (
        elm.Line().at((+1.0, -4.5)).to((-1.5, -4.5)).linestyle("dashdot").linewidth(0.5)
    )
    d += (
        elm.Line().at((-1.5, -4.5)).to((-1.5, +0.5)).linestyle("dashdot").linewidth(0.5)
    )

    d += elm.Line().at((3, -2)).to((3, -2)).label("$u$", "center")

    base = 6

    d += elm.Dot(open=True).at((base + 3, 0)).label("$+$", "right")
    d += elm.Line().at((base + 3, 0)).to((base + 0, 0))

    d += elm.SourceV().at((base + 0, -4)).to((base + 0, 0)).label("$u_S$")

    d += elm.Line().at((base + 0, -4)).to((base + 3, -4))
    d += elm.Dot(open=True).at((base + 3, -4)).label("$-$", "right")

    d += elm.Arrow().at((base + 1, 0)).to((base + 2, 0)).label("$i$", "top")

    d += (
        elm.Line()
        .at((base - 1.5, +0.5))
        .to((base + 1.0, +0.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )
    d += (
        elm.Line()
        .at((base + 1.0, +0.5))
        .to((base + 1.0, -4.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )
    d += (
        elm.Line()
        .at((base + 1.0, -4.5))
        .to((base - 1.5, -4.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )
    d += (
        elm.Line()
        .at((base - 1.5, -4.5))
        .to((base - 1.5, +0.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )

    d += elm.Line().at((base + 3, -2)).to((base + 3, -2)).label("$u$", "center")

    d.save(OUTPUT_DIR / "4_5_1.svg")

# 2 两电压源并联
with Drawing(show=False) as d:
    d.config(fontsize=STYLE["fontsize"])

    d += elm.Dot(open=True).at((5, 0)).label("$+$", "right")
    d += elm.Line().at((5, 0)).to((0, 0))

    d += elm.SourceV().at((0, -4)).to((0, 0)).label("$u_S$")

    d += elm.Dot(open=False).at((2, 0))
    d += elm.SourceV().at((2, -4)).to((2, 0)).label("$u_S$")
    d += elm.Dot(open=False).at((2, -4))

    d += elm.Line().at((0, -4)).to((5, -4))
    d += elm.Dot(open=True).at((5, -4)).label("$-$", "right")

    d += elm.Arrow().at((3, 0)).to((4, 0)).label("$i$", "top")

    d += (
        elm.Line().at((-1.5, +0.5)).to((+3.0, +0.5)).linestyle("dashdot").linewidth(0.5)
    )
    d += (
        elm.Line().at((+3.0, +0.5)).to((+3.0, -4.5)).linestyle("dashdot").linewidth(0.5)
    )
    d += (
        elm.Line().at((+3.0, -4.5)).to((-1.5, -4.5)).linestyle("dashdot").linewidth(0.5)
    )
    d += (
        elm.Line().at((-1.5, -4.5)).to((-1.5, +0.5)).linestyle("dashdot").linewidth(0.5)
    )

    d += elm.Line().at((5, -2)).to((5, -2)).label("$u$", "center")

    base = 8

    d += elm.Dot(open=True).at((base + 3, 0)).label("$+$", "right")
    d += elm.Line().at((base + 3, 0)).to((base + 0, 0))

    d += elm.SourceV().at((base + 0, -4)).to((base + 0, 0)).label("$u_S$")

    d += elm.Line().at((base + 0, -4)).to((base + 3, -4))
    d += elm.Dot(open=True).at((base + 3, -4)).label("$-$", "right")

    d += elm.Arrow().at((base + 1, 0)).to((base + 2, 0)).label("$i$", "top")

    d += (
        elm.Line()
        .at((base - 1.5, +0.5))
        .to((base + 1.0, +0.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )
    d += (
        elm.Line()
        .at((base + 1.0, +0.5))
        .to((base + 1.0, -4.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )
    d += (
        elm.Line()
        .at((base + 1.0, -4.5))
        .to((base - 1.5, -4.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )
    d += (
        elm.Line()
        .at((base - 1.5, -4.5))
        .to((base - 1.5, +0.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )

    d += elm.Line().at((base + 3, -2)).to((base + 3, -2)).label("$u$", "center")

    d.save(OUTPUT_DIR / "4_5_2.svg")

# 3 两电流源并联
with Drawing(show=False) as d:
    d.config(fontsize=STYLE["fontsize"])

    d += elm.Dot(open=True).at((5, 0)).label("$+$", "right")
    d += elm.Line().at((5, 0)).to((0, 0))

    d += elm.SourceI().at((0, -4)).to((0, 0)).label("$i_S$")

    d += elm.Dot(open=False).at((2, 0))
    d += elm.SourceI().at((2, -4)).to((2, 0)).label("$i_S$")
    d += elm.Dot(open=False).at((2, -4))

    d += elm.Line().at((0, -4)).to((5, -4))
    d += elm.Dot(open=True).at((5, -4)).label("$-$", "right")

    d += elm.Arrow().at((3, 0)).to((4, 0)).label("$i$", "top")

    d += (
        elm.Line().at((-1.5, +0.5)).to((+3.0, +0.5)).linestyle("dashdot").linewidth(0.5)
    )
    d += (
        elm.Line().at((+3.0, +0.5)).to((+3.0, -4.5)).linestyle("dashdot").linewidth(0.5)
    )
    d += (
        elm.Line().at((+3.0, -4.5)).to((-1.5, -4.5)).linestyle("dashdot").linewidth(0.5)
    )
    d += (
        elm.Line().at((-1.5, -4.5)).to((-1.5, +0.5)).linestyle("dashdot").linewidth(0.5)
    )

    d += elm.Line().at((5, -2)).to((5, -2)).label("$u$", "center")

    base = 8

    d += elm.Dot(open=True).at((base + 3, 0)).label("$+$", "right")
    d += elm.Line().at((base + 3, 0)).to((base + 0, 0))

    d += elm.SourceI().at((base + 0, -4)).to((base + 0, 0)).label("$i_S$")

    d += elm.Line().at((base + 0, -4)).to((base + 3, -4))
    d += elm.Dot(open=True).at((base + 3, -4)).label("$-$", "right")

    d += elm.Arrow().at((base + 1, 0)).to((base + 2, 0)).label("$i$", "top")

    d += (
        elm.Line()
        .at((base - 1.5, +0.5))
        .to((base + 1.0, +0.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )
    d += (
        elm.Line()
        .at((base + 1.0, +0.5))
        .to((base + 1.0, -4.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )
    d += (
        elm.Line()
        .at((base + 1.0, -4.5))
        .to((base - 1.5, -4.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )
    d += (
        elm.Line()
        .at((base - 1.5, -4.5))
        .to((base - 1.5, +0.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )

    d += elm.Line().at((base + 3, -2)).to((base + 3, -2)).label("$u$", "center")

    d.save(OUTPUT_DIR / "4_5_3.svg")

# 4 两电流源串联
with Drawing(show=False) as d:
    d.config(fontsize=STYLE["fontsize"])

    d += elm.Dot(open=True).at((3, 0)).label("$+$", "right")
    d += elm.Line().at((3, 0)).to((0, 0))

    d += elm.SourceI().at((0, -2)).to((0, 0)).label("$i_{S1}$")
    d += elm.SourceI().at((0, -4)).to((0, -2)).label("$i_{S2}$")

    d += elm.Line().at((0, -4)).to((3, -4))
    d += elm.Dot(open=True).at((3, -4)).label("$-$", "right")

    d += elm.Arrow().at((1, 0)).to((2, 0)).label("$i$", "top")

    d += (
        elm.Line().at((-1.5, +0.5)).to((+1.0, +0.5)).linestyle("dashdot").linewidth(0.5)
    )
    d += (
        elm.Line().at((+1.0, +0.5)).to((+1.0, -4.5)).linestyle("dashdot").linewidth(0.5)
    )
    d += (
        elm.Line().at((+1.0, -4.5)).to((-1.5, -4.5)).linestyle("dashdot").linewidth(0.5)
    )
    d += (
        elm.Line().at((-1.5, -4.5)).to((-1.5, +0.5)).linestyle("dashdot").linewidth(0.5)
    )

    d += elm.Line().at((3, -2)).to((3, -2)).label("$u$", "center")

    base = 6

    d += elm.Dot(open=True).at((base + 3, 0)).label("$+$", "right")
    d += elm.Line().at((base + 3, 0)).to((base + 0, 0))

    d += elm.SourceI().at((base + 0, -4)).to((base + 0, -0)).label("$i_S$")

    d += elm.Line().at((base + 0, -4)).to((base + 3, -4))
    d += elm.Dot(open=True).at((base + 3, -4)).label("$-$", "right")

    d += elm.Arrow().at((base + 1, 0)).to((base + 2, 0)).label("$i$", "top")

    d += (
        elm.Line()
        .at((base - 1.5, +0.5))
        .to((base + 1.0, +0.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )
    d += (
        elm.Line()
        .at((base + 1.0, +0.5))
        .to((base + 1.0, -4.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )
    d += (
        elm.Line()
        .at((base + 1.0, -4.5))
        .to((base - 1.5, -4.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )
    d += (
        elm.Line()
        .at((base - 1.5, -4.5))
        .to((base - 1.5, +0.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )

    d += elm.Line().at((base + 3, -2)).to((base + 3, -2)).label("$u$", "center")

    d.save(OUTPUT_DIR / "4_5_4.svg")

# 5 电压源与多余元件并联
with Drawing(show=False) as d:
    d.config(fontsize=STYLE["fontsize"])

    d += elm.Dot(open=True).at((5, 0)).label("$+$", "right")
    d += elm.Line().at((5, 0)).to((0, 0))

    d += elm.SourceV().at((0, -4)).to((0, 0)).label("$u_S$")

    d += elm.Dot(open=False).at((2, 0))
    d += elm.Line().at((2, 0)).to((2, -1.5))
    d += Box(w=1, h=1).at((2, -1.5)).label("$N′$")
    d += elm.Line().at((2, -2.5)).to((2, -4))
    d += elm.Dot(open=False).at((2, -4))

    d += elm.Line().at((0, -4)).to((5, -4))
    d += elm.Dot(open=True).at((5, -4)).label("$-$", "right")

    d += elm.Arrow().at((3, 0)).to((4, 0)).label("$i$", "top")

    d += (
        elm.Line().at((-1.5, +0.5)).to((+3.0, +0.5)).linestyle("dashdot").linewidth(0.5)
    )
    d += (
        elm.Line().at((+3.0, +0.5)).to((+3.0, -4.5)).linestyle("dashdot").linewidth(0.5)
    )
    d += (
        elm.Line().at((+3.0, -4.5)).to((-1.5, -4.5)).linestyle("dashdot").linewidth(0.5)
    )
    d += (
        elm.Line().at((-1.5, -4.5)).to((-1.5, +0.5)).linestyle("dashdot").linewidth(0.5)
    )

    d += elm.Line().at((5, -2)).to((5, -2)).label("$u$", "center")

    base = 8

    d += elm.Dot(open=True).at((base + 3, 0)).label("$+$", "right")
    d += elm.Line().at((base + 3, 0)).to((base + 0, 0))

    d += elm.SourceV().at((base + 0, -4)).to((base + 0, 0)).label("$u_S$")

    d += elm.Line().at((base + 0, -4)).to((base + 3, -4))
    d += elm.Dot(open=True).at((base + 3, -4)).label("$-$", "right")

    d += elm.Arrow().at((base + 1, 0)).to((base + 2, 0)).label("$i$", "top")

    d += (
        elm.Line()
        .at((base - 1.5, +0.5))
        .to((base + 1.0, +0.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )
    d += (
        elm.Line()
        .at((base + 1.0, +0.5))
        .to((base + 1.0, -4.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )
    d += (
        elm.Line()
        .at((base + 1.0, -4.5))
        .to((base - 1.5, -4.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )
    d += (
        elm.Line()
        .at((base - 1.5, -4.5))
        .to((base - 1.5, +0.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )

    d += elm.Line().at((base + 3, -2)).to((base + 3, -2)).label("$u$", "center")

    d.save(OUTPUT_DIR / "4_5_5.svg")

# 6 电流源与多余元件串联
with Drawing(show=False) as d:
    d.config(fontsize=STYLE["fontsize"])

    d += elm.Dot(open=True).at((3, 0)).label("$+$", "right")
    d += elm.Line().at((3, 0)).to((0, 0))

    d += elm.SourceI().at((0, -2)).to((0, 0)).label("$i_S$")
    d += elm.Line().at((0, -2)).to((0, -2.5))
    d += Box(w=1, h=1).at((0, -2.5)).label("$N′$")
    d += elm.Line().at((0, -3.5)).to((0, -4))

    d += elm.Line().at((0, -4)).to((3, -4))
    d += elm.Dot(open=True).at((3, -4)).label("$-$", "right")

    d += elm.Arrow().at((1, 0)).to((2, 0)).label("$i$", "top")

    d += (
        elm.Line().at((-1.5, +0.5)).to((+1.0, +0.5)).linestyle("dashdot").linewidth(0.5)
    )
    d += (
        elm.Line().at((+1.0, +0.5)).to((+1.0, -4.5)).linestyle("dashdot").linewidth(0.5)
    )
    d += (
        elm.Line().at((+1.0, -4.5)).to((-1.5, -4.5)).linestyle("dashdot").linewidth(0.5)
    )
    d += (
        elm.Line().at((-1.5, -4.5)).to((-1.5, +0.5)).linestyle("dashdot").linewidth(0.5)
    )

    d += elm.Line().at((3, -2)).to((3, -2)).label("$u$", "center")

    base = 6

    d += elm.Dot(open=True).at((base + 3, 0)).label("$+$", "right")
    d += elm.Line().at((base + 3, 0)).to((base + 0, 0))

    d += elm.SourceI().at((base + 0, -4)).to((base + 0, 0)).label("$i_S$")

    d += elm.Line().at((base + 0, -4)).to((base + 3, -4))
    d += elm.Dot(open=True).at((base + 3, -4)).label("$-$", "right")

    d += elm.Arrow().at((base + 1, 0)).to((base + 2, 0)).label("$i$", "top")

    d += (
        elm.Line()
        .at((base - 1.5, +0.5))
        .to((base + 1.0, +0.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )
    d += (
        elm.Line()
        .at((base + 1.0, +0.5))
        .to((base + 1.0, -4.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )
    d += (
        elm.Line()
        .at((base + 1.0, -4.5))
        .to((base - 1.5, -4.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )
    d += (
        elm.Line()
        .at((base - 1.5, -4.5))
        .to((base - 1.5, +0.5))
        .linestyle("dashdot")
        .linewidth(0.5)
    )

    d += elm.Line().at((base + 3, -2)).to((base + 3, -2)).label("$u$", "center")

    d.save(OUTPUT_DIR / "4_5_6.svg")

# 7 电压源和电流源的电阻电路相互等效
with Drawing(show=False) as d:
    d.config(fontsize=STYLE["fontsize"])

    d += elm.Dot(open=True).at((4.5, 0)).label("$+$", "right")
    d += elm.Line().at((3, 0)).to((4.5, 0))
    d += elm.Resistor().at((1, 0)).to((3, 0)).label("$R$", "bottom")
    d += elm.Line().at((0, 0)).to((1, 0))

    d += elm.SourceV().at((0, -4)).to((0, 0)).label("$u_S$")

    d += elm.Line().at((0, -4)).to((4.5, -4))
    d += elm.Dot(open=True).at((4.5, -4)).label("$-$", "right")

    d += elm.Arrow().at((3, 0)).to((3.5, 0)).label("$i$", "top")

    d += elm.Line().at((4.5, -2)).to((4.5, -2)).label("$u$", "center")

    base = 8

    d += elm.Dot(open=True).at((base + 5, 0)).label("$+$", "right")
    d += elm.Line().at((base + 5, 0)).to((base + 0, 0))

    d += elm.SourceI().at((base + 0, -4)).to((base + 0, 0)).label("$i_S$")

    d += elm.Dot(open=False).at((base + 2, 0))
    d += elm.Resistor().at((base + 2, 0)).to((base + 2, -4)).label("$R′$", loc="bottom")
    d += elm.Dot(open=False).at((base + 2, -4))

    d += elm.Line().at((base + 0, -4)).to((base + 5, -4))
    d += elm.Dot(open=True).at((base + 5, -4)).label("$-$", "right")

    d += elm.Arrow().at((base + 3, 0)).to((base + 4, 0)).label("$i$", "top")

    d += elm.Line().at((base + 5, -2)).to((base + 5, -2)).label("$u$", "center")

    d.save(OUTPUT_DIR / "4_5_7.svg")
