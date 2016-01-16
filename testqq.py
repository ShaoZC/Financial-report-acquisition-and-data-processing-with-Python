print('hello world')
import urllib2
request=urllib2.Request(url="http://www.qq.com")
result=urllib2.urlopen(request).read()
print result