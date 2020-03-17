
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
url='https://sports.sina.cn/?vt=4&pos=108'
xpath1='//h2//em/text()'
requested(url,xpath1)