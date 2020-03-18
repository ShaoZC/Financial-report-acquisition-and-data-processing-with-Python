def sleep(n):
    import time
    import random
    time.sleep(random.random() * n)
    print('~~~~~~sleeping~~~~~~~~')
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
# def write_excel_xls_append(path, value):
#     import xlutils  # 需要安装xlutils
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
def read_txt(file_folder,txt_name):
    f = open(file_folder + txt_name)
    stock_list=[]
    for line in f.readlines():
        line = line.replace('\n', '')
        stock_list.append(line)
    f.close()
    return stock_list
def read_excel(file_folder,excel_name):
    import xlrd
    stock_list=[]
    data=xlrd.open_workbook(file_folder+excel_name)
    sheet = data.sheet_by_index(0)
    for i in range(sheet.nrows):
        # print(i,sheet.row_values(i)[0])
        stock_list.append(sheet.row_values(i)[0])
    print(stock_list)
    return stock_list
def requested(url,xpath1):
    import requests
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    response=requests.get(url,headers=headers);sleep(3)
    response.encoding=response.apparent_encoding
    # return response
    import lxml
    from lxml import etree
    title_1=etree.HTML(response.text).xpath(xpath1);
    return title_1

def get_annual_report_url(url_report_list):
    import requests;import re;from lxml import etree
    import urllib;import urllib.request
    req = urllib.request.Request(url_report_list)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
    page = urllib.request.urlopen(req)
    html = page.read().decode('gbk')
    # headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    # response=requests.get(url_report_list,headers=headers)
    # sleep(5)
    # response.encoding=response.apparent_encoding
    # html=etree.HTML(response.text)
    target = r'&id=[_0-9_]{7}'
    target_list = re.findall(target,html)
    target_url_0 = 'http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid='
    target_url=target_url_0+each[2:8]+target_list[0]
    print(target_url)
    return target_url
# def get_audit_firm(url_year_report):
#     audit_firm=[0,0]
#     url_2018_report=get_annual_report_url(url_year_report)
#     xpath1='//table/tr/td//text()'
#     audit_firm=requested(url_2018_report,xpath1)
#     return audit_firm

# coding=UTF-8
file_folder='C:/Users/wade z shao/Documents/GitHub/yunzhuan/Financial-report-acquisition-and-data-processing-with-Python/'
txt_name="stock_list/20200320.txt";stock_list=read_txt(file_folder,txt_name)
excel_name= "stock_list/新能源电池20200320.xlsx";stock_list=read_excel(file_folder,excel_name)
file_name='excel/2020-03-20_' +"光伏发电（新表）20200320"+'_4'+".xls"

iinum = 1
for each in stock_list[1:26]:
    print("----",iinum,"-------",'26',"------",each[:8])
    print(len(each[2:8]),each[2:8])
    if each[2:8].isdigit() and len(each[2:8])>4:
        # 爬取上市公司基本信息，得到信息为title_1,经过处理得到title_2
        url_intro_0 = 'http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CorpInfo/stockid/'
        url_intro=url_intro_0+each[2:8]+'.phtml'#公司简介
        xpath1='//table/tr/td//text()'
        title_1=requested(url_intro,xpath1)
        sleep(5);
        title_2 = [0,0,0,0,0];
        if len(title_1)>0:
            title_2.clear()
            for i in range(len(title_1)):
                title_1[i] = title_1[i].strip();title_1[i] = title_1[i].strip('：')# 去除其中的冒号
                if title_1[i].find('公司名称')>-1:
                    title_2.append(title_1[i+1])
                if title_1[i].find('公司英文名称')>-1:
                    title_2.append(title_1[i+1])
                if title_1[i].find('公司网址')>-1:
                    title_2.append(title_1[i+1])
                if title_1[i].find('办公地址')>-1:
                    title_2.append(title_1[i+1])
                if title_1[i].find('经营范围')>-1:
                    title_2.append(title_1[i+1])
        # 爬取上市公司基本信息，得到信息为title_1,经过处理得到title_2

        #获取2018年报链接url_2018_report，并提取内容
        url_index='http://finance.sina.com.cn/realstock/company/'+each[:8]+'/nc.shtml'#公司主页
        url_report_list_0='http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_Bulletin/stockid/'#公司年报列表
        url_report_list=url_report_list_0+each[2:8]+'/page_type/ndbg.phtml'#公司年报列表
        url_2018_report=get_annual_report_url(url_report_list)#获取2018年报页面
        xpath1='//table/tr/td//text()'
        title_1=requested(url_2018_report,xpath1)#爬取上市公司年审事务所
        audit_firm=[0,0]
        for i in range(len(title_1)):
            title_1[i] = title_1[i].strip();title_1[i] = title_1[i].strip('：')# 去除其中的冒号
            if title_1[i].find('境内会计师事务所名称')>-1:
                audit_firm.clear()
                audit_firm.append(title_1[i+1])
            if title_1[i].find('境内会计师事务所报酬')>-1:
                audit_firm.append(title_1[i+1])
        # 获取2018年报链接url_2018_report，并提取内容

        # 保存工作簿
        path1 = file_folder + file_name
        write_excel_xls(path1,[each[:8],each[8:],url_intro,url_2018_report]+ audit_firm+title_2,iinum)
        workbook.save(path1)
        iinum = iinum + 1
        # 保存工作簿