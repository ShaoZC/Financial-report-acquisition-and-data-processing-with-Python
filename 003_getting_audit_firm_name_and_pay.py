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

# coding=UTF-8
file_folder= "C:/"
file_name="stock_workbook.xls"
file_source="stock.txt"

# print(file_foler+file_name)

########################
import urllib.request
import re
import os
import time
import random


f=open(file_folder+file_name)
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
    # url='http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_Bulletin/stockid/'+each+'/page_type/ndbg.phtml'
    req = urllib.request.Request(url)
    print('2',each)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
    page = urllib.request.urlopen(req)
    time.sleep(random.random() * 3)
    print('3',each)
    try:
        html = page.read().decode('gbk')
        target = r'&id=[_0-9_]{7}'
        print('4',each)
        # target = r'&id=[_0-9_]{6}'
        target_list = re.findall(target,html)
        # os.mkdir('./')
        # os.mkdir('./'+each)
        # os.mkdir('./'+'electricity-'+each)
        sid = each1
        if len(target_list)>0:
            print('5',each1,'2018和2015年target_list',target_list)
            print("6sid is",sid)
            year=2018
            each2=target_list[0]
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
            title = selector.xpath('//table/tr/td//text()')

            # 去除其中的冒号
            title_1 = []
            for i in title:
                i = i.strip()
                i = i.strip('：')
                title_1.append(i)
            print("title_1", title_1[00:1500])
            path1 = file_folder + '6' + file_name
            print(path1)
            for title in range(len(title_1)):
                if title_1[title].find('境内会计师事务所名称')>-1:
                    print("境内会计师事务所名称",title_1[title+1])
                    print("境内会计师事务所名称",title_1[title+2])
                    print("境内会计师事务所名称",title_1[title+3])
                    print("境内会计师事务所名称",title_1[title+4])
                    print("境内会计师事务所名称",title_1[title+5])
                    # print("境内会计师事务所名称",title_1[title+6])
                    # 存入excel

                    write_excel_xls(path1, [each[0:7], each[8:], target_url, title_1[title],title_1[title+1],title_1[title+2],title_1[title+3],title_1[title+4],title_1[title+5],title_1[title+6],title_1[title+7],title_1[title+8]], iinum)
                    workbook.save(path1)  # 保存工作簿
                    # 存入excel

            # 去除其中的冒号


            iinum=iinum+1

    except:
        print('年报列表页面编码错误;',path1,+title_1[0])