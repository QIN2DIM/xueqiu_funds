# 雪球基金 Python Client

## Get started

### Install package

```shell
pip install xueqiu_funds
```

### Quick start

```python
from xueqiu_funds import XueQiuFunds

# 华夏上证科创板50成份ETF联接C
fd_code = "011613"

xqf = XueQiuFunds()

detail = xqf.get_fund_detail(fd_code)
intro = xqf.get_fund_intro(fd_code)

fd_name = intro["data"]["fd_name"]
other_rate_table = detail["data"]["fund_rates"]["other_rate_table"]

print({fd_name: other_rate_table})

```



