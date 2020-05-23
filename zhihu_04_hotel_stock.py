###############################################
######数据写入excel############################
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

###############################################
######爬虫############################
import time
import random
# coding=UTF-8
# coding=gbk
import requests
def requested(url):    
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    # print(url)
    response = requests.get(url, headers=headers)
    response.encoding = 'gbk'  # 解决乱码问题
    html_text = response.text
    time.sleep(2)
    return html_text

###############################################
######节点选取############################    
def selected(html):
    # import lxml
    from lxml import etree
    selector = etree.HTML(html)
    title = selector.xpath('//table/tr/td//text()')
    # 去除其中的冒号
    title_1 = []
    title_1.append(mkt_value(each0))
    for i in title:
        # i = i.strip()
        i = i.strip('：')
        title_1.append(i)
    print("title_1", title_1[0:40]) 
    return title_1    
###############################################
######获取总市值############################
def mkt_value(stock_no):
    url='http://qt.gtimg.cn/q=s_'+stock_no
    # url='http://qt.gtimg.cn/q='+'sz000858'
    response=requests.get(url)
    # print(response.content)
    # content1=response.content
    content1=str(response.content).split('~')
    print(content1[-2])
    return content1[-2]
###############################################
######主程序############################
############################################### 
file_folder= "D:/OneDrive/文档/stock2020/"
file_name="20200511-2酒店旅游概念.xls"
file_source="stock_hotel_code.txt"
# file_folder= "C:/Users/wade z shao/Documents/202001Shennandonglu5016#29F/202003电力行业调研/"
# file_name="electricity_stock_workbook.xls"
# file_source="stock_electricity_3.txt"
# print(file_folder+file_name)

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
for each in stock:
    # print(each[2:])
    each0=each[:8]
    each1=each[2:8]
    # print(each)
    url = 'http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CorpInfo/stockid/'+each1+'.phtml'
###########################################################
    html=requested(url)# 开始爬虫
    title_1=selected(html)    
    path1 = file_folder+file_name
    print(path1)

    # mkt_value=str(mkt_value(each0))
    # print(mkt_value)
    write_excel_xls(path1,title_1,iinum)# 存入excel
    workbook.save(path1)  # 保存工作簿
    iinum=iinum+1