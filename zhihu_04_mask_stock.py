import xlrd #（excel read）来读取Excel文件
import xlwt #（excel write）来生成Excel文件
workbook = xlwt.Workbook()  # 新建一个工作簿
sheet = workbook.add_sheet("sheet_name")  # 在工作簿中新建一个表格
def write_excel_xls(path,value,inum):
    index = len(value)  # 获取需要写入数据的行数
    # print("index is",index)
    for num in range(0, index):
        sheet.write(inum,num,value[num])
    # for i in range(0, index):
    #     for j in range(0, len(value[i])):
    #         sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）

    print("xls格式表格写入数据成功！")
# import xlutils #暂时没有办法安装xlutils
# def write_excel_xls_append(path, value):
#     index = len(value)  # 获取需要写入数据的行数
#     workbook = xlrd.open_workbook(path)  # 打开工作簿
#     sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
#     worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
#     rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
#     new_workbook = xlutils.copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
#     new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
#     for i in range(0, index):
#         for j in range(0, len(value[i])):
#             new_worksheet.write(i+rows_old, j, value[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
#     new_workbook.save(path)  # 保存工作簿
#     print("xls格式表格【追加】写入数据成功！")
import time
import random
# coding=UTF-8
# coding=gbk
file_folder= "D:/OneDrive/文档/stock2020/"
file_name="口罩概念.xls"
file_source="stock_mask_code.txt"
# file_folder= "C:/Users/wade z shao/Documents/202001Shennandonglu5016#29F/202003电力行业调研/"
# file_name="electricity_stock_workbook.xls"
# file_source="stock_electricity_3.txt"
# print(file_folder+file_name)
###########################################################
#构造url
url_source=open(file_folder+file_source)
f=open(file_folder+file_source,'rb')
stock = []
for line in f.readlines():
    line=line.decode()
    print(line)
    #print(line,end = '')
    # line = line[1:].replace(' ','')
    line = line.replace('\n','')
    stock.append(line)
print("#########################")
print(stock)
f.close()
###########################################################
iinum = 1
for each in stock[1:2]:
    # print(each[2:])
    each1=each[2:8]
    # print(each)
    url = 'http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CorpInfo/stockid/'+each1+'.phtml'
###########################################################
    # 开始爬虫
    import requests
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    # print(url)
    response = requests.get(url, headers=headers)
    response.encoding = 'gbk'  # 解决乱码问题
    html_text = response.text
    time
    # 开始爬虫
###########################################################
    import lxml
    from lxml import etree
    selector = etree.HTML(html_text)
    title = selector.xpath('//table/tr/td//text()')
    # 去除其中的冒号
    title_1 = []
    for i in title:
        i = i.strip()
        i = i.strip('：')
        title_1.append(i)
    print("title_1", title_1[0:40])
    # 去除其中的冒号
    # import json
    # import tushare
    # # price=tushare.get_today_all()
    # price=tushare.get_hist_data(each1,start='2020-03-09',end='2020-03-09')
    # price20200309=price['date':'2020-03-09']
    # price20200309=price['date':'2020-03-09']
    # print(each,price20200309)
    # time_now=time.time()
    # 存入excel
    path1 = file_folder + '20200310' + file_name
    print(path1)
    # write_excel_xls(path1, title_1,iinum)
    # workbook.save(path1)  # 保存工作簿
    # 存入excel
    iinum=iinum+1