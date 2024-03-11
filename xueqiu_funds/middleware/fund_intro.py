# -*- coding: utf-8 -*-
# Time       : 2024/3/12 1:04
# Author     : QIN2DIM
# GitHub     : https://github.com/QIN2DIM
# Description:
from pydantic import BaseModel, Field


class FundIntro(BaseModel):
    """仅关注必要的数据统计字段，忽略用于前端渲染的定位字段"""

    fd_code: str = Field("", description="基金代码", examples=["011613"])
    fd_name: str = Field("", description="雪球基金名称", examples=["华夏上证科创板50成份ETF联接C"])
    found_date: str = Field("", description="基金发布时间", examples=["2021-03-04"])
    totshare: str = Field("", description="基金管理规模", examples=["62.91亿"])
    keeper_name: str = Field("", description="持有公司", examples=["华夏基金管理有限公司"])
    manager_name: str = Field("", description="基金经理", examples=["荣膺 张弘弢", "陆志明"])
    trup_name: str = Field("", description="券商", examples=["招商银行股份有限公司"])
