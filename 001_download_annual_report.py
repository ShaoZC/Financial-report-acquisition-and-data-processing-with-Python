import urllib.request
import re
import os
import time
import random

f=open(file_folder+filename)
stock = []
for line in f.readlines():
    #print(line,end = '')
    line = line.replace('\n','')
    stock.append(line)
#print(stock)
f.close()
print('stock is',stock[:5])

for each in stock:
    # print(each[2:])
    each1=each[2:8]
    print('1股票代码',each1)
    url='http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_Bulletin/stockid/'+each1+'/page_type/ndbg.phtml'
    # url='http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_Bulletin/stockid/'+each+'/page_type/ndbg.phtml'
    req = urllib.request.Request(url)
    print('2',each1)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
    page = urllib.request.urlopen(req)
    time.sleep(random.random() * 3)
    print('3',each1)
    try:
        html = page.read().decode('gbk')
        target = r'&id=[_0-9_]{7}'
        print('4',each1)
        # target = r'&id=[_0-9_]{6}'
        target_list = re.findall(target,html)
        os.mkdir('./'+each)
        # os.mkdir('./'+'electricity-'+each)
        sid = each1
        print('5',each1,'2018和2015年target_list',target_list[0])
        print("6sid is",sid)
        year=2018
        for each2 in target_list:
        # for each2 in target_list[0,3]:
            #print(a)
            print('7',each1,each2)
            target_url='http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid='+sid+each2
            print('--8--',each1,year,'下载链接target_url,',target_url)
            treq = urllib.request.Request(target_url)
            time.sleep(random.random() * 3)
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
                    local = './'+each+'/'+file_url.group(0).split("/")[-4]+'.pdf'
                    # local = './'+each+'/'+file_url.group(0).split("/")[-1]+'.pdf'
                    # local = './'+sid+'/'+file_url.group(0).split("/")[-1]+'.pdf'
                    print("10 local is",local)
                    #调试用作文件占位
                    #open(local, 'wb').write(b'success')
                    print('11',each1,'local',local)
                    urllib.request.urlretrieve(file_url.group(0),local,None)
                except:
                    print('PDF失效;'+target_url)
            except:
                print(each1,'年报下载页面编码错误;'+target_url)
    except:
        print('年报列表页面编码错误;'+url)