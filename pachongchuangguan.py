# coding=utf-8

import requests
import re

website = 'http://www.heibanke.com/lesson/crawler_ex00/'
ruler = re.compile(r'数字[^\d]*(\d+)[\.<]')

html = requests.get(website).content
number = ruler.findall(html)
index = 1
while number:
    website2 = website + number[0]
    html = requests.get(website2).content
    number = ruler.findall(html)
    print "访问网页%d: %s" %(index, website2)
    index += 1
else:
    print "\n下一关的入口: %s" % website2