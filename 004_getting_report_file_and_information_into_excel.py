import xlrd #（excel read）来读取Excel文件
import xlwt #（excel write）来生成Excel文件
workbook = xlwt.Workbook()  # 新建一个工作簿
sheet = workbook.add_sheet("sheet1")  # 在工作簿中新建一个表格
def write_excel_xls(path,value,inum):
    index = len(value)  # 获取需要写入数据的行数
    # print("index is",index)
    for num in range(0, index):
        sheet.write(inum,num,value[num])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~xls格式表格写入数据成功！~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
##########################################################################
# coding=UTF-8
file_folder1= "C:/Users/wade z shao/Documents/202001Shennandonglu5016#29F/XXX/"
file_folder= file_folder1+"python/"
# file_name="test.xls";f=open(file_folder1+'stock_electricity_3.txt')
# file_name="沪深300.xls";f=open(file_folder1+'sh_sz_300.txt')
##########################################################################
import urllib.request
import re
import os
import time
import random
import requests
##########################################################################
stock = []
for line in f.readlines():
    #print(line,end = '')
    line = line.replace('\n','')
    stock.append(line)
f.close()
print('stock is',stock[:5])
##########################################################################
iinum = 1
for each in stock:
# for each in stock:
    print("**********************************")
    print("******",iinum,"******",len(stock))
    print("**********************************")
    # print(each[2:])
    each1=each[2:8]
    print('1',each)
    #新浪行情中心#新浪行情中心#新浪行情中心
    url_sina_introduction='http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CorpInfo/stockid/'+each1+'.phtml'
    url_sina_report='http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_Bulletin/stockid/'+each1+'/page_type/ndbg.phtml'
    #网易财经#网易财经#网易财经#网易财经
    url_netease_index='http://quotes.money.163.com/'+each1+'.html' #网易个股主页
    url_netease_introduction='http://quotes.money.163.com/f10/gszl_'+each1+'.html#11c01#' #网易个股公司简介
    url_netease_report='http://quotes.money.163.com/f10/gsgg_'+each1+',dqbg.html' #网易公司定期报告，无法下载，但是有详细全文内容很全
    #网易财经如宁波韵升( 600366) 公司公告http://quotes.money.163.com/f10/gsgg_600366,dqbg.html
    url_xueqiu_index="https://xueqiu.com/S/"+each[0:8]
    url_eastmoney_report="http://data.eastmoney.com/notices/stock/300644.html"#年报混编了，不方便下载
    url_ifeng='http://app.finance.ifeng.com/data/stock/dqbg.php?symbol='+each1#凤凰财经的年报链接，不过无法访问了暂时
    print('###########公司信息##############################')
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    # print(url)
    response_sina_introduction = requests.get(url_sina_introduction, headers=headers)
    response_sina_introduction.encoding = 'gbk'  # 解决乱码问题
    html_text_sina_introduction = response_sina_introduction.text
    # 开始爬虫# 开始爬虫# 开始爬虫# 开始爬虫# 开始爬虫
    import lxml
    from lxml import etree
    selector = etree.HTML(html_text_sina_introduction)
    title_sina_introduction = selector.xpath('//table/tr/td//text()')
    # 去除其中的冒号# 去除其中的冒号
    title_1_sina_introduction = []
    for i in title_sina_introduction:
        i = i.strip()
        i = i.strip('：')
        title_1_sina_introduction.append(i)
    print("title_1_sina_introduction", title_1_sina_introduction[0:4])
    # 去除其中的冒号# 去除其中的冒号
    print('###########公司信息##############################')
    print('###########年报审计的会计师事务所#################')

    req = urllib.request.Request(url_sina_report)
    print('2',each)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
    page = urllib.request.urlopen(req)
####    time.sleep(random.random() * 15)
    time.sleep(random.random() * 15)
####    time.sleep(random.random() * 15)
    print('3',each)


    #嗅探年报的网站链接    #嗅探年报的网站链接
    try:
        html = page.read().decode('gbk');target = r'&id=[_0-9_]{7}';target_list = re.findall(target,html)
        sid = each1;target_url = 'http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid=' + sid
        if len(target_list)>0:
            year = 2018;each2018 = target_list[0];target_url_2018=target_url+each2018
            print('----2018----',each1,year,'年报链接,',target_url_2018)
    # 嗅探年报的网站链接    #嗅探年报的网站链接

    ### 爬取会计师事务所### 爬取会计师事务所
    ####    time.sleep(random.random() * 15)
            time.sleep(random.random() *15)
    ####    time.sleep(random.random() * 15)
            import requests
            headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
            response = requests.get(target_url_2018, headers=headers)
            response.encoding = 'gbk'  # 解决乱码问题
            html_text = response.text
            import lxml
            from lxml import etree
            selector = etree.HTML(html_text)
            title = selector.xpath('//table/tr/td//text()')#2018年会计师事务所
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
            time_now=int(time.time())
            time_now=str(time_now)[0:7]
            path1 =file_folder+time_now+"_"+str(year)+file_name+'.xls'
            print(path1)
            for title in range(len(title_1)):
                if title_1[title].find('境内会计师事务所名称')>-1:
                    for i in range(1):
                    # for i in range(20):
                        print(i,title_1[title+i])
                    # 存入excel
                    # write_excel_xls(path1, [each[0:7], each[8:], year,target_url, title_1[title],title_1[title+1],title_1[title+2],title_1[title+3],title_1[title+4],title_1[title+5],title_1[title+6],title_1[title+7],title_1[title+8],title_1[title+9],title_1[title+10],title_1[title+11],title_1[title+12]]+title_1_sina_introduction, iinum)
                    # workbook.save(path1)  # 保存工作簿
                    # 存入excel
            iinum=iinum+1
    ### 爬取会计师事务所### 爬取会计师事务所



    ###下载年报 ###下载年报 ###下载年报
        # if len(target_list) > 0:
        #     year = 2018;
        #     each2018 = target_list[0];
        #     target_url_2018 = target_url + each2018
        #     os.mkdir('./'+file_name+each[2:])
            time.sleep(random.random() * 8)
            treq = urllib.request.Request(target_url_2018)
            treq.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
            tpage = urllib.request.urlopen(treq)
            time.sleep(random.random() * 3)
            try:
                thtml = tpage.read().decode('gbk')
                #print(thtml)
                file_url = re.search('http://file.finance.sina.com.cn/211.154.219.97:9494/.*?PDF',thtml)
                print("--9--file_url is",file_url.group(0))

                try:
                    #print(file_url.group(0))
                    local = './'+file_name+each[2:]+'/'+each[2:]+'2018年年报'+'.pdf'
                    # local = './'+each+'/'+file_url.group(0).split("/")[-4]+'.pdf'
                    # local = './'+each+'/'+file_url.group(0).split("/")[-1]+'.pdf'
                    # local = './'+sid+'/'+file_url.group(0).split("/")[-1]+'.pdf'
                    print("10 local is",local)
                    #调试用作文件占位
                    #open(local, 'wb').write(b'success')
                    print('11',each1,'local',local)
                    # urllib.request.urlretrieve(file_url.group(0),local,None)
                except:
                    print('2018PDF失效;'+target_url)
            except:
                print(each1,'2018年报下载页面编码错误;'+target_url)
        if len(target_list)>3:
            print('----2015----',each1,'2015年target_list',target_list[3])
            each2015 = target_list[3];target_url_2015=target_url+each2015
            # year=2017;each2017=target_list[1]
            time.sleep(random.random() * 8)
            treq_2015 = urllib.request.Request(target_url_2015)
            treq_2015.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
            tpage = urllib.request.urlopen(treq_2015)
            time.sleep(random.random() * 8)
            try:
                thtml_2015 = tpage.read().decode('gbk')
                #print(thtml)
                file_url_2015 = re.search('http://file.finance.sina.com.cn/211.154.219.97:9494/.*?PDF',thtml_2015)
                print("--2015--file_url is",file_url_2015.group(0))

                try:
                    #print(file_url.group(0))
                    local = './'+file_name+each[2:]+'/'+each[2:]+'2015年年报'+'.pdf'
                    # report_year=(file_url_2015.group(0).split("/")[-4])
                    # local = './'+file_name+each+'/'+report_year+'.pdf'
                    # local = './'+each+'/'+file_url.group(0).split("/")[-1]+'.pdf'
                    # local = './'+sid+'/'+file_url.group(0).split("/")[-1]+'.pdf'
                    print("2015 local is",local)
                    #调试用作文件占位
                    #open(local, 'wb').write(b'success')
                    print('2015',each1,'local',local)
                    urllib.request.urlretrieve(file_url_2015.group(0),local,None)
                except:
                    print('2015PDF失效;'+target_url)
            except:
                print(each1,'2015年报下载页面编码错误;'+target_url)

    ###下载年报 ###下载年报 ###下载年报
    except:
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print(each,'年报列表页面编码错误;',path1,str(year)+title_1[0])
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')