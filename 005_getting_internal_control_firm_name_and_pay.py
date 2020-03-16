# coding=UTF-8
file_folder='C:/Users/wade z shao/Documents/GitHub/yunzhuan/Financial-report-acquisition-and-data-processing-with-Python/'
file_code='5';file_source='stock_list/'+file_code+".txt"
file_name="internal_control_firm"+file_code+'.xls'
print(file_folder+file_name)

import xlrd #（excel read）来读取Excel文件
import xlwt #（excel write）来生成Excel文件
workbook = xlwt.Workbook()  # 新建一个工作簿
sheet = workbook.add_sheet(file_code)  # 在工作簿中新建一个表格
def write_excel_xls(path,value,inum):
    index = len(value)  # 获取需要写入数据的行数
    # print("index is",index)
    for num in range(0, index):
        sheet.write(inum,num,value[num])
    # for i in range(0, index):
    #     for j in range(0, len(value[i])):
    #         sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）

    print("xls格式表格写入数据成功！")



########################
import urllib.request
import re
import os
import time
import random

f=open(file_folder+file_source)
stock = []
for line in f.readlines():
    #print(line,end = '')
    line = line.replace('\n','')
    stock.append(line)
#print(stock)
f.close()
print('stock is',stock[:5])
iinum = 1
for each in stock:
    # print(each[2:])
    each1=each[2:8]
    print('1股票代码',each)
    url='http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_Bulletin/stockid/'+each1+'/page_type/ndbg.phtml'
    print(url)
    # url='http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_Bulletin/stockid/'+each+'/page_type/ndbg.phtml'
    req = urllib.request.Request(url)
    print('2',each)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
    page = urllib.request.urlopen(req)
    time.sleep(random.random() * 10)
    print('3',each)
    try:
        html = page.read().decode('gbk')
        target = r'&id=[_0-9_]{7}'
        print('4',each)
        # target = r'&id=[_0-9_]{6}'
        target_list = re.findall(target,html)
        print('5',target_list)
        # os.mkdir('./')
        # os.mkdir('./'+each)
        # os.mkdir('./'+'electricity-'+each)
        sid = each1
        if len(target_list)>0:
            print('5',each1,'2018和2015年target_list',target_list)
            print("6sid is",sid)
            # year=2017;each2=target_list[1]
            year=2018;each2=target_list[0]
            target_url='http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid='+sid+each2
            print('--8--',each1,year,'年报详情链接target_url,',target_url)

            url=target_url
            # 开始爬虫
            import requests
            headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
            # print(url)
            response = requests.get(url, headers=headers)
            response.encoding = 'gbk'  # 解决乱码问题
            html_text = response.text
            # 开始爬虫

            import lxml
            from lxml import etree
            selector = etree.HTML(html_text)
            title = selector.xpath('//table/tr/td//text()')#2018
            # title = selector.xpath('//tbody/tr/td//text()')#2017
            # 去除其中的冒号
            title_1 = []
            for i in title:
                i = i.strip()
                i = i.strip('：')
                # title_1.append(i)
                for j in i.split():
                    # print("--------------",j)
                    title_1.append(j)
                # title_1.append(i)
            # print("title_1", title_1[00:1500])
            time_now=int(time.time()); time_now= str(time_now)
            path1 =file_folder+time_now[0:7]+"_"+str(year)+file_name
            print(path1)
            title_1_firm=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#21个
            for title in range(len(title_1)):
                if title_1[title].find('内部控制审计会计师') > -1:
                    title_1_firm.clear()
                # if title_1[title].find('内部控制审计会计师事务所')>-1:                  内部控制审
                    for i in range(20):
                        title_1_firm.append(title_1[title+i])
                        print(i, "境内会计师事务所名称",title_1[title+i])
                        print(title_1_firm[-1])
                elif title_1[title].find('内部控制审计机构') > -1:
                    title_1_firm.clear()
                    for i in range(20):
                        title_1_firm.append(title_1[title+i])
                        print(i, "内部控制审计机构",title_1[title+i])
                        print(title_1_firm[-1])
            # 存入excel
            write_excel_xls(path1, [each[0:7], each[8:], target_url]+title_1_firm, iinum)
            workbook.save(path1)  # 保存工作簿
            # 存入excel

            # 去除其中的冒号


            iinum=iinum+1
    except:
        print('年报列表页面编码错误;',path1,str(year)+title_1[0])