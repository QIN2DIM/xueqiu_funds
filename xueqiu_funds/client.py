# -*- coding: utf-8 -*-
# Time       : 2024/3/12 1:33
# Author     : QIN2DIM
# GitHub     : https://github.com/QIN2DIM
# Description:
from dataclasses import dataclass

from httpx import Client


@dataclass
class XueQiuFunds:
    client: Client | None = None

    BASE_URL = "https://danjuanfunds.com"

    def __post_init__(self):
        self.client = self.client or Client(
            base_url=self.BASE_URL,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"
            },
        )

    def get_fund_detail(self, fund_code: str):
        return self.client.get(f"/djapi/fund/detail/{fund_code}").json()

    def get_fund_intro(self, fund_code: str):
        return self.client.get(f"/djapi/fund/{fund_code}").json()

    def get_fund_traces(self, symbol: str):
        """
        查询跟踪某个指数的基金（被动/指增）
        :param symbol: SH000688 科创50
        :return:
        """
        return self.client.get("/djapi/fundx/base/index/traces", params={"symbol": symbol}).json()
