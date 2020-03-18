
import requests
import re
from lxml import etree
def requested(url,xpath1):
    response=requests.get(url);print(response)
    response.encoding=response.apparent_encoding
    # response.encoding='utf-8'
    print(response.content)
    html=etree.HTML(response.text)
    items=html.xpath(xpath1)
    print(len(items))
    if len(items)>1:
        for i in range(len(items)):
            print(i,items[i])


# url='http://www.bidchance.com/freesearch.do?filetype=&channel=zhongbiao&currentpage=1&searchtype=&queryword=&displayStyle=&pstate=&field=&leftday=&province=&bidfile=&project=&heshi=&recommend=&field=&jing=&starttime=&endtime=&attachment='
# xpath1='//text()'
# requested(url,xpath1)

# 虎嗅网
# url='https://m.huxiu.com/'
# xpath1='//div/h1//text()'
# requested(url,xpath1)

#豆瓣网
# url='https://book.douban.com/'
# xpath1='//div/h4/text()'#<Response [418]>
# requested(url,xpath1)

#新浪网
# url='https://sports.sina.cn/?vt=4&pos=108'
# xpath1='//h2//em/text()'
# requested(url,xpath1)

#豆瓣网
import requests
import ssl
from lxml import etree


ssl._create_default_https_context = ssl._create_unverified_context

session = requests.Session()
for id in range(0, 251, 25):
    URL = 'https://movie.douban.com/top250/?start=' + str(id)
    req = session.get(URL)
    print(req)
    # 设置网页编码格式
    req.encoding = 'utf8'
    # 将request.content 转化为 Element
    root = etree.HTML(req.content)
    # 选取 ol/li/div[@class="item"] 不管它们在文档中的位置
    items = root.xpath('//ol/li/div[@class="item"]')
    for item in items:
        # 注意可能只有中文名，没有英文名；可能没有quote简评
        rank, name, alias, rating_num, quote, url = "", "", "", "", "", ""
        try:
            url = item.xpath('./div[@class="pic"]/a/@href')[0]
            rank = item.xpath('./div[@class="pic"]/em/text()')[0]
            title = item.xpath('./div[@class="info"]//a/span[@class="title"]/text()')
            name = title[0].encode('gb2312', 'ignore').decode('gb2312')
            alias = title[1].encode('gb2312', 'ignore').decode('gb2312') if len(title) == 2 else ""
            rating_num = item.xpath('.//div[@class="bd"]//span[@class="rating_num"]/text()')[0]
            quote_tag = item.xpath('.//div[@class="bd"]//span[@class="inq"]')
            if len(quote_tag) is not 0:
                quote = quote_tag[0].text.encode('gb2312', 'ignore').decode('gb2312').replace('\xa0', '')
            # 输出 排名，评分，简介
            print(rank, rating_num, quote)
            # 输出 中文名，英文名
            print(name.encode('gb2312', 'ignore').decode('gb2312'),
                  alias.encode('gb2312', 'ignore').decode('gb2312').replace('/', ','))
        except:
            print('faild!')
            pass
# ————————————————
# 版权声明：本文为CSDN博主「jeikerxiao」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/jeikerxiao/article/details/73530529


#新浪微博
import requests
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
url="https://weibo.com"
res = requests.get(url,headers=headers)
print(res)
xpath1='//div//text()'
requested(url,xpath1)
# ————————————————
# 版权声明：本文为CSDN博主「阿叶_」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_43902320/article/details/104342771