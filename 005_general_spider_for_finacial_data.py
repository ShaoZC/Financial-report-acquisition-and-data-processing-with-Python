
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
        print(len(items))
        return items

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

#采购与招标信息网
# # url='https://www.chinabidding.cn/'
# url1='https://www.chinabidding.cn/zbxx/zbgs/'
# url2='.html';
# xpath1='//tr//td//a/text()'
# for i in range(10):
#     url=url1+str(i)+url2;
#     items=requested(url,xpath1)
#     for i in range(len(items)):
#         if items[i].find('风险')>-1:
#             print('*****风险*****')
#         elif items[i].find('内控')>-1:
#             print('#####内控####')
#         elif items[i].find('山东')>-1:
#             print('山东')

#boss直聘首页
# url='https://www.zhipin.com/shenzhen/'
# xpath1='//ul/li/div/a/p/span/text()'
# items=requested(url,xpath1)
# url='https://www.zhipin.com/job_detail/?query=%E9%A3%8E%E9%99%A9&city=101280600&industry=&position='
# # url='https://www.zhipin.com/c101280600/?query=%E9%A3%8E%E9%99%A9&page=2&ka=page-2'
# xpath1='//div//text()'
# # xpath1='//span[@class="job-name"]//text()'
# # xpath1='//div/div/a//span/text()'
# items=requested(url,xpath1)