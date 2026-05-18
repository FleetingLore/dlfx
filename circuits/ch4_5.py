"""
第四章 §4-5 一些简单的等效规律和公式 —— 电路图

统一布局风格：
  - 串联：上开口 + 元件水平同行在下方
  - 并联：上开口 + 上支路 / 下支路均在端口下方
"""

from pathlib import Path

import schemdraw
import schemdraw.elements as elm
from schemdraw import Drawing

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "assets" / "circuits"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

STYLE = {"fontsize": 14}
DEPTH = 4  # 端口到下方元件的垂直深度
GAP = 2  # 并联时上下支路间距


# ══════════════════════════════════════════════════════════════
#  串联：上开口 + 元件同行下方
# ══════════════════════════════════════════════════════════════


def _draw_series(d: Drawing, elem_cls, labels: list[str], tag: str):
    """
    通用串联画法：
        o a                o b
         │                  │
         └──[elem1]─[elem2]──┘

    elem_cls: 元件类 (如 elm.Battery, elm.Resistor, elm.SourceI)
    labels:   两个元件的标签
    tag:      文件名标记
    """
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


# ══════════════════════════════════════════════════════════════
#  并联：上开口 + 上支路/下支路均在端口下方
# ══════════════════════════════════════════════════════════════


def _draw_parallel(d: Drawing, elem_cls, labels: list[str], tag: str):
    """
    通用并联画法：
         o a              o b
          │                │
          ├───[elem1]──────┤    ← 上支路
          │                │
          ├───[elem2]──────┤    ← 下支路
          │                │
    """
    d.config(fontsize=STYLE["fontsize"])

    # ── 左端子 + 左竖线 ──
    d += elm.Dot(open=True).label("a", "left")
    d.push()  # 记左端子，供下支路用
    d += elm.Line().down().length(1.5)  # 到上支路高度
    d.push()  # 记上支路起点

    # ── 上支路 + 右上竖线 + 右端子 ──
    d += elem_cls().right().label(labels[0]).length(4)
    d += elm.Line().up().length(1.5)  # 上行到端子高度
    d += elm.Dot(open=True).label("b", "right")

    # ── 下支路（从上支路起点往下一格） ──
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


# ══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    fig_4_5_1_two_voltage_sources_series()
    fig_4_5_2_two_voltage_sources_parallel()
    fig_4_5_3_two_current_sources_parallel()
    fig_4_5_4_two_current_sources_series()
    fig_4_5_5_two_resistors_series()
    fig_4_5_6_two_resistors_parallel()
    print("✅ All 6 circuits saved to", OUTPUT_DIR)
