from pathlib import Path

import schemdraw.elements as elm
from schemdraw import Drawing
from schemdraw.flow import Box

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "assets" / "circuits"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

elm.style(elm.STYLE_IEC)
STYLE = {"fontsize": 14}

# 1 具有初始电流的电感及其等效
with Drawing(show=False) as d:
    d += elm.Line().at((0, 0)).to((4, 0)).linewidth(3)
    d += elm.Line().at((4, 0)).to((4, 5)).linewidth(3)
    d += elm.Line().at((4, 5)).to((0, 5)).linewidth(3)
    d += elm.Line().at((0, 5)).to((0, 0)).linewidth(3)

    d += elm.Line().at((4, 0.5)).to((5, 0.5))
    d += elm.Dot(open=True).at((5, 0.5))

    d += elm.Line().at((4, 4.5)).to((5, 4.5))
    d += elm.Dot(open=True).at((5, 4.5))

    d += elm.Line().at((5, 0.5)).to((7, 0.5))
    d += (
        elm.Inductor(polar=True)
        .at((7, 0.5))
        .to((7, 4.5))
        .label("$i_L(t_0)=I_0$", "bottom")
    )
    d += elm.Line().at((7, 4.5)).to((5, 4.5))

    base = 12

    d += elm.Line().at((base + 0, 0)).to((base + 4, 0)).linewidth(3)
    d += elm.Line().at((base + 4, 0)).to((base + 4, 5)).linewidth(3)
    d += elm.Line().at((base + 4, 5)).to((base + 0, 5)).linewidth(3)
    d += elm.Line().at((base + 0, 5)).to((base + 0, 0)).linewidth(3)

    d += elm.Line().at((base + 4, 0.5)).to((base + 5, 0.5))
    d += elm.Dot(open=False).at((base + 5, 0.5))

    d += elm.Line().at((base + 4, 4.5)).to((base + 5, 4.5))
    d += elm.Dot(open=False).at((base + 5, 4.5))

    d += (
        elm.SourceI(polar=False)
        .at((base + 5, 0.5))
        .to((base + 5, 4.5))
        .label("$i_L(t_0)=I0$", "bottom")
    )

    d += elm.Line().at((base + 5, 0.5)).to((base + 8, 0.5))
    d += elm.Line().at((base + 5, 4.5)).to((base + 8, 4.5))
    d += (
        elm.Inductor()
        .at((base + 8, 0.5))
        .to((base + 8, 4.5))
        .label("$i_1(t_0)=0$", "bottom")
    )

    d.save(OUTPUT_DIR / "5_7_1.svg")
