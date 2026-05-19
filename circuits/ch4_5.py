from pathlib import Path

import schemdraw
import schemdraw.elements as elm
from schemdraw import Drawing

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "assets" / "circuits"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

STYLE = {"fontsize": 14}
DEPTH = 1  # 端口到下方元件的垂直深度
GAP = 1  # 并联时上下支路间距


def _draw_series(d: Drawing, elem_cls, labels: list[str], tag: str):
    d.config(fontsize=STYLE["fontsize"])
    d += elm.Dot(open=True).label("a", "left")
    d += elm.Line().down().length(DEPTH)  # 下行
    d += elem_cls().right().label(labels[0]).length(4)  # 元件1
    d += elem_cls().right().label(labels[1]).length(4)  # 元件2
    d += elm.Line().up().length(DEPTH)  # 上行
    d += elm.Dot(open=True).label("b", "right")
    d.save(OUTPUT_DIR / f"4_5_{tag}.svg")


def fig_4_5_1_two_voltage_sources_series():
    _draw_series(
        Drawing(show=False), elm.Battery, ["$V_{s1}$", "$V_{s2}$"], "1_voltage_series"
    )


def fig_4_5_4_two_current_sources_series():
    _draw_series(
        Drawing(show=False), elm.SourceI, ["$I_{s1}$", "$I_{s2}$"], "4_current_series"
    )


def fig_4_5_5_two_resistors_series():
    _draw_series(
        Drawing(show=False), elm.Resistor, ["$R_1$", "$R_2$"], "5_resistors_series"
    )


def _draw_parallel(d: Drawing, elem_cls, labels: list[str], tag: str):
    d.config(fontsize=STYLE["fontsize"])

    d += elm.Dot(open=True).label("a", "left")
    d.push()  # 记左端子，供下支路用
    d += elm.Line().down().length(1.5)  # 到上支路高度
    d.push()  # 记上支路起点

    d += elem_cls().right().label(labels[0]).length(4)
    d += elm.Line().up().length(1.5)  # 上行到端子高度
    d += elm.Dot(open=True).label("b", "right")

    d.pop()  # 回到上支路起点
    d += elm.Line().down().length(GAP)  # 下行到下支路高度
    d += elem_cls().right().label(labels[1]).length(4)
    d += elm.Line().up().length(1.5 + GAP)  # 上行到右端子高度

    d.pop()  # 回到左端子（收尾，但不画线）
    d.save(OUTPUT_DIR / f"4_5_{tag}.svg")


def fig_4_5_2_two_voltage_sources_parallel():
    _draw_parallel(
        Drawing(show=False), elm.Battery, ["$V_{s1}$", "$V_{s2}$"], "2_voltage_parallel"
    )


def fig_4_5_3_two_current_sources_parallel():
    _draw_parallel(
        Drawing(show=False), elm.SourceI, ["$I_{s1}$", "$I_{s2}$"], "3_current_parallel"
    )


def fig_4_5_6_two_resistors_parallel():
    _draw_parallel(
        Drawing(show=False), elm.Resistor, ["$R_1$", "$R_2$"], "6_resistors_parallel"
    )


if __name__ == "__main__":
    fig_4_5_1_two_voltage_sources_series()
    fig_4_5_2_two_voltage_sources_parallel()
    fig_4_5_3_two_current_sources_parallel()
    fig_4_5_4_two_current_sources_series()
    fig_4_5_5_two_resistors_series()
    fig_4_5_6_two_resistors_parallel()
