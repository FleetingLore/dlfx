#!/usr/bin/env python3
"""
批量生成所有电路图 SVG。

用法:
    python gen_circuits.py          # 生成所有
    python gen_circuits.py --dry    # 仅列出将要生成的文件
"""

import importlib.util
import sys
from pathlib import Path

CIRCUITS_DIR = Path(__file__).parent / "circuits"


def run_module(module_path: Path):
    """动态加载并执行单个 circuits/*.py 模块（执行其 __main__ 部分）"""
    spec = importlib.util.spec_from_file_location(module_path.stem, module_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)


def main():
    dry = "--dry" in sys.argv

    py_files = sorted(CIRCUITS_DIR.glob("*.py"))
    if not py_files:
        print("⚠️  没有找到 circuits/*.py 文件")
        return

    for f in py_files:
        if dry:
            print(f"  → 将执行 {f.name}")
        else:
            print(f"⚡ 生成 {f.name} …")
            run_module(f)

    if not dry:
        print("✅ 全部完成。")


if __name__ == "__main__":
    main()
