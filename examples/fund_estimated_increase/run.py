from xueqiu_funds import XueQiuFunds, FundDetail

# 华夏上证科创板50成份ETF联接C
fd_code = "011613"

xqf = XueQiuFunds()

fund_detail = FundDetail(**xqf.get_fund_detail(fd_code)["data"])

print(fund_detail)
