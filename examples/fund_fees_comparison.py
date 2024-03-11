import asyncio
import json
from pathlib import Path
from typing import List, Tuple, Dict, Any

import pandas as pd

from xueqiu_funds import XueQiuFunds

runtime_dir = Path(__file__).parent.joinpath("runtime")
runtime_dir.mkdir(parents=True, exist_ok=True)

fd_codes = [
    "004855",
    "016858",
    "008888",
    "012832",
    "010956",
    "003766",
    "007339",
    "007818",
    "014881",
    "017574",
    "011613",
    "008586",
    "008115",
    "019312",
    "000834",
    "008682",
]

FeeType = Tuple[str, List[Dict[str, Any]]]


def dump_showcase(data: List[FeeType]):
    # 创建一个空的 DataFrame
    df = pd.DataFrame(columns=["基金名称", "基金管理费", "基金托管费", "销售服务费"])

    for fund_name, fee_data in data:
        row = {"基金名称": fund_name}
        for fee in fee_data:
            row[fee["name"]] = float(fee["value"])
        df.loc[len(df)] = row

    # 计算合计列
    df["合计"] = df.iloc[:, 1:].sum(axis=1)

    # 按照合计列升序排列
    df.sort_values("合计", inplace=True)

    # 设置列名
    df.columns = ["基金名称", "基金管理费 (%)", "基金托管费 (%)", "销售服务费 (%)", "合计 (%)"]

    # 设置 DataFrame 的显示选项
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)
    pd.set_option("display.unicode.ambiguous_as_wide", True)
    pd.set_option("display.unicode.east_asian_width", True)
    pd.set_option("display.width", 0)

    print(df.to_string(index=False))

    # 将DataFrame写入Excel文件
    with pd.ExcelWriter("fund_fees_comparison.xlsx", engine="openpyxl") as writer:
        # 将 DataFrame 写入 Excel 文件
        df.to_excel(writer, index=False, sheet_name="Sheet1")

        # 获取openpyxl的worksheet对象
        worksheet = writer.sheets["Sheet1"]

        # 调整列宽
        for column_cells in worksheet.columns:
            length = max(len(str(cell.value)) for cell in column_cells)
            adjusted_width = (length + 2) * 1.3  # 根据内容长度调整列宽
            worksheet.column_dimensions[column_cells[0].column_letter].width = adjusted_width


async def main():
    xqf = XueQiuFunds()
    data: List[FeeType] = []

    for fd_code in fd_codes:
        detail = await xqf.get_fund_detail(fd_code)
        intro = await xqf.get_fund_intro(fd_code)

        if (fd_name := intro["data"]["fd_name"]) and (
            other_rate_table := detail["data"]["fund_rates"]["other_rate_table"]
        ):
            data.append((fd_name, other_rate_table))

            fdr = runtime_dir.joinpath(f"{fd_code}_{fd_name}")
            fdr.mkdir(parents=True, exist_ok=True)

            fdr.joinpath("fund_detail.json").write_text(
                json.dumps(detail, ensure_ascii=False), encoding="utf8"
            )
            fdr.joinpath("fund_intro.json").write_text(
                json.dumps(intro, ensure_ascii=False), encoding="utf8"
            )

    dump_showcase(data)


if __name__ == "__main__":
    asyncio.run(main())
