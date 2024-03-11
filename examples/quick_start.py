# -*- coding: utf-8 -*-
# Time       : 2024/3/12 3:01
# Author     : QIN2DIM
# GitHub     : https://github.com/QIN2DIM
# Description:
import asyncio

from xueqiu_funds import XueQiuFunds


async def main():
    # 华夏上证科创板50成份ETF联接C
    fd_code = "011613"

    xqf = XueQiuFunds()

    detail = await xqf.get_fund_detail(fd_code)
    intro = await xqf.get_fund_intro(fd_code)

    fd_name = intro["data"]["fd_name"]
    other_rate_table = detail["data"]["fund_rates"]["other_rate_table"]

    print({fd_name: other_rate_table})


if __name__ == "__main__":
    asyncio.run(main())
