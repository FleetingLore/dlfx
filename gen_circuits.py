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
    mod = importlib.util.module_from_spec(spec) # type: ignore

    spec.loader.exec_module(mod) # type: ignore


def main():
    dry = "--dry" in sys.argv # 是否启用 dry-run 模式, 即仅列出将要生成的文件

    py_files = sorted(CIRCUITS_DIR.glob("*.py"))
    if not py_files:
        print("not found any circuits/*.py file.")
        return

    for file in py_files:
        if dry:
            print(f"todo {file.name}")
        else:
            print(f"processing {file.name}")
            run_module(file)

    if not dry:
        print("gen_circuits.py done.")


if __name__ == "__main__":
    main()
