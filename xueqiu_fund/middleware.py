# -*- coding: utf-8 -*-
# Time       : 2024/3/11 23:30
# Author     : QIN2DIM
# GitHub     : https://github.com/QIN2DIM
# Description:
from pydantic import BaseModel, Field


class FundDetailResponse(BaseModel):
    fund_company: str = Field(..., description="基金公司介绍")
    fund_position: FundPosition
    fund_rates: FundRates
    manager_list: List[FundManager]
    fund_date_conf: FundDateConf
    pension_fund: bool

class Stock(BaseModel):
    name: str = Field(default="", description="股票名称", examples=["比亚迪"])
    code: str = Field(default="", description="股票代码", examples=["002594"])
    percent: float = Field(default=0.0, description="涨跌幅", examples=[14.99])
    current_price: float = Field(default=0.0, description="当前价格", examples=[198.74])
    change_percentage: float = Field(default=0.0, description="涨跌百分比", examples=[5.66])
    xq_symbol: str = Field(default="", description="雪球股票代码", examples=["SZ002594"])
    xq_url: str = Field(default="", description="雪球股票链接", examples=["https://xueqiu.com/S/SZ002594"])
    change_of_pre_quarter: str = Field(default="", description="上一季度涨跌幅", examples=["2.74%"])
    change_of_pre_quarter_type: int = Field(default=0, description="上一季度涨跌类型", examples=[1])
    industry_label: str = Field(default="", description="行业标签", examples=["汽车"])
    amarket: bool = Field(default=False, description="是否为 A 股市场", examples=[True])
    percent_double: float = Field(default=0.0, description="涨跌幅（双精度）", examples=[14.99])
