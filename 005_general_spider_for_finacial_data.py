def sleep(n):
    print('~~~~~~缓冲中~~~~~loading~~~~~~~~')
    import time
    import random
    time.sleep(random.random() * n)
def time_now():
    import time
    return time.strftime('%Y-%m-%d-%H%M%S',time.localtime(time.time()))
def html_save(data):#filename为写入CSV文件的路径，data为要写入数据列表.
  filename='C:/data/html/' + str(time_now()) + '.html'
  with open(filename, 'w', encoding='utf-8') as f:
      # with open('C:/data/'+str(time_now())+'.html', 'w', encoding='gbk') as f:
      f.write(data)
  print("保存",filename,"文件成功")
def text_save(data):#filename为写入CSV文件的路径，data为要写入数据列表.
  filename='C:/data/text/'+str(time_now())+'.txt'
  file = open(filename,'a', encoding='utf-8')
  file.write(data)
  # for i in range(len(data)):
  #   s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
  #   s = s.replace("'",'').replace(',','') +'\n'  #去除单引号，逗号，每行末尾追加换行符
  #   file.write(s)
  file.close()
  print("保存",filename,"文件成功")
def write_csv(data):
    filename='C:/data/csv/'+str(time_now())+'.csv'
    import csv
    f = open(filename, 'w', encoding='utf-8')
    writer = csv.writer(f)
    writer.writerow(data)
    print("保存", filename, "文件成功")
def headers():
    USER_AGENT_LIST = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    ]
    import random
    USER_AGENT = random.choice(USER_AGENT_LIST)
    headers = {'user-agent': USER_AGENT}
    return headers
def get_521_content(url):
    import requests;import re
    headers={
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
    }
    req=requests.get(url,headers=headers)
    cookies=req.cookies
    cookies='; '.join(['='.join(item) for item in cookies.items()])
    txt_521=req.text
    txt_521=''.join(re.findall('<script>(.*?)</script>',txt_521))
    print(txt_521,txt_521)
    print('cookies','\n',cookies)
    return (txt_521,cookies)
def COOKIES(url):
    import selenium
    from selenium import webdriver
    driver=webdriver.Chrome()
    driver.get("url")
    cj= driver.get_cookies()
    cookie=''
    for c in cj:
        cookie += c['name'] +'='  +  c['value'] +';'
    return cookie
    driver.quit()
def requested(url,xpath1,*keywords):
    import requests
    import re
    from lxml import etree
    # response = requests.get(url, headers=headers(),cookie=get_521_content(url)[1]);
    response=requests.get(url,headers=headers());
    write_csv(response.text)
    html_save(response.text)
    text_save(response.text)
    if response.status_code== 200:
        pass
    else:
        print(response)
    # response=requests.get(url,headers=headers(),cookie=COOKIES(url));print(response)
    response.encoding=response.apparent_encoding
    # response.encoding='utf-8'
    # print(response.content)
    # print(response.text)
    html=etree.HTML(response.text)
    items=html.xpath(xpath1)
    print('共找到',len(items),'条符合条件的结果')
    if len(items)>1:
        for i in range(len(items)):
            # print(len(items),'-',i+1,'','',items[i])
            # print(keywords)
            if keywords==():
                pass
            elif items[i].find(keywords)>-1:
                print(i,len(items),keywords,items[i])
            else:
                print(keywords,'not found未找到')
        return items
    else:
        print(url,'未找到结果')
    sleep(5)


##############################################################################################
#############                         bidchance.com招标网                     #################
###############################################################################################
# # url='http://www.bidchance.com/freesearch.do?filetype=&channel=zhongbiao&currentpage=1&searchtype=&queryword=&displayStyle=&pstate=&field=&leftday=&province=&bidfile=&project=&heshi=&recommend=&field=&jing=&starttime=&endtime=&attachment='
# # xpath1='//text()'
# # requested(url,xpath1)
# url='http://www.bidchance.com/freesearch.do?filetype=&channel=&channels=zhongbiao&currentpage=1&searchtype=&queryword=%C4%DA%BF%D8&displayStyle=&pstate=&field=title&leftday=&province=&bidfile=&project=&heshi=&recommend=&field=title&jing=&starttime=&endtime=&attachment='
# ##内控标题搜索
# xpath1='//div//tr/td//text()'
# get_521_content(url)
# requested(url,xpath1)


##############################################################################################
#############                         铁路12306                              #################
##############################################################################################
# url='https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc'
# xpath1='//a//text()'
# requested(url,xpath1)
# 转到新的文件里面了



##############################################################################################
#############                         京东                                 #################
###############################################################################################
# url='https://www.jd.com/'
# xpath1='//a//text()'
# requested(url,xpath1)

##############################################################################################
#############                         淘宝                                 #################
###############################################################################################
# url='https://www.taobao.com/'
# xpath1='//a//text()'
# requested(url,xpath1)

##############################################################################################
#############                         36kr                                 #################
###############################################################################################
url='https://www.36kr.com/'
xpath1='//a//text()'
requested(url,xpath1)

##############################################################################################
#############                         虎嗅网                                 #################
###############################################################################################
#
# url='https://m.huxiu.com/'
# xpath1='//div/h1//text()'
# requested(url,xpath1)
##############################################################################################
#############                         豆瓣网                                 #################
###############################################################################################
# url='https://book.douban.com/'
# xpath1='//div/h4/text()'#<Response [418]>
# requested(url,xpath1)

##############################################################################################
#############                         新浪网                                 #################
##############################################################################################
# url='https://sports.sina.cn/?vt=4&pos=108'
# xpath1='//h2//em/text()'
# requested(url,xpath1)

##############################################################################################
#############                         应届生求职网                              #################
##############################################################################################
# url_0='http://www.yingjiesheng.com/'
# # city='jinan';url_1='job/list_'#济南
# city='shenzhen';url_1='-morejob-'
# url_2='.html'
# for i in range(10):
#     print(city,'-------------',i+1,'--------------------')
#     url=url_0+city+url_1+str(i+1)+url_2
#     xpath1='//td/a//text()'
#     xpath_date = '//td[contains(@class,"date cen")]/text()'
#     # xpath_date='//td[@class="date cen"]/text()'
#     xpath_url='//td[@class="item1"]/a/@href'
#     requested(url,xpath1,'风险')
#     requested(url, xpath1, '风控')
#     requested(url, xpath1, '数据')
#     # requested(url,xpath_date)
#     # requested(url,xpath_url)
#     sleep(10)


##############################################################################################
#############                         豆瓣网                                 #################
##############################################################################################
# import requests
# import ssl
# from lxml import etree
#
# ssl._create_default_https_context = ssl._create_unverified_context
#
# session = requests.Session()
# for id in range(0, 251, 25):
#     URL = 'https://movie.douban.com/top250/?start=' + str(id)
#     req = session.get(URL)
#     print(req)
#     # 设置网页编码格式
#     req.encoding = 'utf8'
#     # 将request.content 转化为 Element
#     root = etree.HTML(req.content)
#     # 选取 ol/li/div[@class="item"] 不管它们在文档中的位置
#     items = root.xpath('//ol/li/div[@class="item"]')
#     for item in items:
#         # 注意可能只有中文名，没有英文名；可能没有quote简评
#         rank, name, alias, rating_num, quote, url = "", "", "", "", "", ""
#         try:
#             url = item.xpath('./div[@class="pic"]/a/@href')[0]
#             rank = item.xpath('./div[@class="pic"]/em/text()')[0]
#             title = item.xpath('./div[@class="info"]//a/span[@class="title"]/text()')
#             name = title[0].encode('gb2312', 'ignore').decode('gb2312')
#             alias = title[1].encode('gb2312', 'ignore').decode('gb2312') if len(title) == 2 else ""
#             rating_num = item.xpath('.//div[@class="bd"]//span[@class="rating_num"]/text()')[0]
#             quote_tag = item.xpath('.//div[@class="bd"]//span[@class="inq"]')
#             if len(quote_tag) is not 0:
#                 quote = quote_tag[0].text.encode('gb2312', 'ignore').decode('gb2312').replace('\xa0', '')
#             # 输出 排名，评分，简介
#             print(rank, rating_num, quote)
#             # 输出 中文名，英文名
#             print(name.encode('gb2312', 'ignore').decode('gb2312'),
#                   alias.encode('gb2312', 'ignore').decode('gb2312').replace('/', ','))
#         except:
#             print('faild!')
#             pass
# ————————————————
# 版权声明：本文为CSDN博主「jeikerxiao」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/jeikerxiao/article/details/73530529

##############################################################################################
#############新浪微博#################
##############################################################################################
# import requests
# headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
# url="https://weibo.com"
# res = requests.get(url,headers=headers)
# print(res)
# xpath1='//div//text()'
# requested(url,xpath1)
# ————————————————
# 版权声明：本文为CSDN博主「阿叶_」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_43902320/article/details/104342771