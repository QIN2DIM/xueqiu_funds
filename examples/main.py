import asyncio
import json
from dataclasses import dataclass
from pathlib import Path

from httpx import AsyncClient

runtime_dir = Path(__file__).parent.joinpath("runtime")
runtime_dir.mkdir(parents=True, exist_ok=True)


@dataclass
class XueQiuFunds:
    client: AsyncClient | None = None

    BASE_URL = "https://danjuanfunds.com"

    def __post_init__(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"
        }
        self.client = self.client or AsyncClient(base_url=self.BASE_URL, headers=headers)

    async def get_fund_detail(self, fund_code: str):
        res = await self.client.get(f"/djapi/fund/detail/{fund_code}")
        return res.json()

    async def get_fund_intro(self, fund_code: str):
        res = await self.client.get(f"/djapi/fund/{fund_code}")
        return res.json()


async def main():
    xqf = XueQiuFunds()
    for fd_code in [
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
    ]:
        detail = await xqf.get_fund_detail(fd_code)
        intro = await xqf.get_fund_intro(fd_code)

        other_rate_table = detail["data"]["fund_rates"]["other_rate_table"]
        fd_name = intro["data"]["fd_name"]

        print({fd_name: other_rate_table})

        fdr = runtime_dir.joinpath(f"{fd_code}_{fd_name}")
        fdr.mkdir(parents=True, exist_ok=True)

        fdr.joinpath("fund_detail.json").write_text(
            json.dumps(detail, ensure_ascii=False), encoding="utf8"
        )
        fdr.joinpath("fund_intro.json").write_text(
            json.dumps(intro, ensure_ascii=False), encoding="utf8"
        )


if __name__ == "__main__":
    asyncio.run(main())
