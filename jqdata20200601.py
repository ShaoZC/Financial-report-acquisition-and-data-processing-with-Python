import jqdatasdk
jqdatasdk.auth("13141315365", "315365")
# jqdatasdk.get_price("000001.XSHE")
# print(jqdatasdk.get_price("000001.XSHE", start_date="2017-01-01", end_date="2017-12-31"))


# # 获取所有沪深300的股票
# # stocks = jqdatasdk.get_index_stocks('000300.XSHG')
# # print(stocks)

# normalize_code-股票代码格式转化
# 将其他形式的股票代码转换为jqdatasdk函数可用的股票代码形式。 仅适用于A股市场股票代码、期货以及基金代码,支持传入单只股票或一个股票list 示例
# #输入
# normalize_code(['000001', 'SZ000001', '000001SZ', '000001.sz', '000001.XSHE'])
# #输出
# ['000001.XSHE', '000001.XSHE', '000001.XSHE', '000001.XSHE', '000001.XSHE']

# # 查询'000001.XSHE'的所有市值数据, 时间是2015-10-15
# q = jqdatasdk.query(
#     jqdatasdk.valuation
# ).filter(
#     jqdatasdk.valuation.code == '000001.XSHE'
# )
# df = jqdatasdk.get_fundamentals(q, '2015-10-15')
# # 打印出总市值
# print(df['market_cap'][0])

# # 查询平安银行2014年的年报
# q = jqdatasdk.query(
#         jqdatasdk.income.statDate,
#         jqdatasdk.income.code,
#         jqdatasdk.income.basic_eps,
#         jqdatasdk.cash_flow.goods_sale_and_service_render_cash
#     ).filter(
#         jqdatasdk.income.code == '000001.XSHE',
#     )
#
# ret = jqdatasdk.get_fundamentals(q, statDate='2014')
# print(ret)

# ####资产负债表#########
# ####资产负债表#########
# ####资产负债表#########
# ####资产负债表#########
# ####资产负债表#########
# # fixed_assets	固定资产
# # total_assets	资产总计
# from jqdatasdk import finance
#
# # codeqianyuandianli="002039.xshe"
# # codeqianyuandianli=jqdatasdk.normalize_code('002039')
# codeshuidian=['sh600900','sh600025','sh600886','sh600236','002039','sh600674','sz000722','sz000883','000791.SZ','000993','000601','600868']
# for code in codeshuidian:
#     codeqianyuandianli=jqdatasdk.normalize_code(code)
#     print("\n*********",code,"***********************")
#     qianyuandianli=finance.run_query(jqdatasdk.query(finance.STK_BALANCE_SHEET.fixed_assets,
#                                                  finance.STK_BALANCE_SHEET.total_assets,
#                                                  finance.STK_BALANCE_SHEET.code,
#                                                  finance.STK_BALANCE_SHEET.cash_equivalents,
#                                                  finance.STK_BALANCE_SHEET.pub_date,
#                                                  finance.STK_BALANCE_SHEET.start_date,
#                                                  finance.STK_BALANCE_SHEET.end_date,
#                                                  finance.STK_BALANCE_SHEET.company_name
#                                                  ).filter(finance.STK_BALANCE_SHEET.code==codeqianyuandianli,
#                                                           finance.STK_BALANCE_SHEET.pub_date>='2010-01-01',
#                                                           finance.STK_BALANCE_SHEET.report_type==0
#                                                           ).limit(50))
#     print(qianyuandianli)

###### 有息负债  ################
###### 有息负债  ################
###### 有息负债  ################
###### 有息负债  ################
# shortterm_loan	短期借款	decimal(20,4)
# non_current_liability_in_one_year	一年内到期的非流动负债	decimal(20,4)
# longterm_loan	长期借款	decimal(20,4)
# bonds_payable	应付债券	decimal(20,4)
import pandas
# qianyuandianli=pandas.DataFrame(columns=['A', 'B', 'C', 'D','A', 'B', 'C', 'D','A'])
from jqdatasdk import finance
codeshuidian=['sh600900','sh600025','sh600886','sh600236','002039','sh600674','sz000722','sz000883','000791.SZ','000993','000601','600868']
for code in codeshuidian:
    codeqianyuandianli=jqdatasdk.normalize_code(code)
    # print("\n*********",code,"***********************")
    qianyuandianli1=finance.run_query(jqdatasdk.query(finance.STK_BALANCE_SHEET.shortterm_loan,
                                                 finance.STK_BALANCE_SHEET.longterm_loan,
                                                 finance.STK_BALANCE_SHEET.non_current_liability_in_one_year,
                                                 finance.STK_BALANCE_SHEET.bonds_payable,
                                                 finance.STK_BALANCE_SHEET.total_assets,
                                                 finance.STK_BALANCE_SHEET.code,finance.STK_BALANCE_SHEET.pub_date,
                                                 finance.STK_BALANCE_SHEET.start_date,
                                                 finance.STK_BALANCE_SHEET.end_date,
                                                 finance.STK_BALANCE_SHEET.company_name
                                                 ).filter(finance.STK_BALANCE_SHEET.code==codeqianyuandianli,
                                                          finance.STK_BALANCE_SHEET.pub_date>='2010-01-01',
                                                          finance.STK_BALANCE_SHEET.report_type==0
                                                          ).limit(50))
    qianyuandianli1=qianyuandianli1.fillna(0)
    # qianyuandianli1.append(qianyuandianli1)
    print((qianyuandianli1['shortterm_loan']
          +qianyuandianli1['longterm_loan']
          +qianyuandianli1['non_current_liability_in_one_year']
          +qianyuandianli1['bonds_payable'])
          /qianyuandianli1['total_assets'],qianyuandianli1['company_name'])
# qianyuandianli1.to_excel('C:/TEMP/Excel/loan_2010-2020_hydro_power_20200601.xlsx')

