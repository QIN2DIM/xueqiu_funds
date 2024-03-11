# -*- coding: utf-8 -*-
# Time       : 2024/3/12 1:33
# Author     : QIN2DIM
# GitHub     : https://github.com/QIN2DIM
# Description:
from dataclasses import dataclass

from httpx import AsyncClient


@dataclass
class XueQiuFunds:
    client: AsyncClient | None = None

    BASE_URL = "https://danjuanfunds.com"

    def __post_init__(self):
        self.client = self.client or AsyncClient(
            base_url=self.BASE_URL,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"
            },
        )

    async def get_fund_detail(self, fund_code: str):
        res = await self.client.get(f"/djapi/fund/detail/{fund_code}")
        return res.json()

    async def get_fund_intro(self, fund_code: str):
        res = await self.client.get(f"/djapi/fund/{fund_code}")
        return res.json()
