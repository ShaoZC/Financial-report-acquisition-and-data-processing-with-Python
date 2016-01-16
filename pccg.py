# coding=utf-8
import urllib
import re
website='http://www.heibanke.com/lesson/crawler_ex00/'
html=urllib.urlopen(website).read()
index=re.findall(r'输入数字([0-9]{5})',html)
while index:
        url='http://www.heibanke.com/lesson/crawler_ex00/%s/' % index[0]
        print url
        tmp_re=urllib.urlopen(url) 
        html=tmp_re.read()
        index=re.findall(r'数字是([0-9]{5})',html)
print html
#print html
