# -*- coding: utf-8 -*-
# Time       : 2024/3/12 3:14
# Author     : QIN2DIM
# GitHub     : https://github.com/QIN2DIM
# Description: find funds with the lowest fees
import pandas as pd
from xueqiu_funds import XueQiuFunds

xqf = XueQiuFunds()
data = xqf.get_fund_traces(symbol="SH000688")

comparison = []

for item in data["data"]["items"]:
    for fund in item["funds"]:
        info = {
            "基金代码": fund["fund_code"],
            "基金名称": fund["fund_name"],
            "基金类型": item["fund_type"],
            "运作费率": fund["operating_rate"],
            "申购费率": fund["declare_rate"],
        }
        comparison.append(info)

df = pd.DataFrame(comparison)
df.sort_values("运作费率", inplace=True)
print(df.to_markdown(index=False, tablefmt="grid"))
