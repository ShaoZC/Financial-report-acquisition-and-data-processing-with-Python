import urllib.request
import re
import os
import time
import random
file_folder= "C://TEMP/Excel/";file_name="stock-list-20200512-electricity.txt"
f=open(file_folder+file_name,'rb')
stock = []
for line in f.readlines():
    line=line.decode('utf-8')
    print(line,end = '')
    line = line.replace('\n','')
    stock.append(line)
#print(stock)
f.close()
print('stock is',stock[:5])

for each in stock[5:]:
    print('~~~~each is',each)
    each1=each[2:8];each0=each[0:8];each3=each
    print(each3)
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
        print(target_list)
        # os.mkdir('./'+str(each))
        # os.mkdir('./'+'electricity-'+each)
        sid = each1
        print('5',each1,'2019和2015年target_list',target_list[0])
        print("6sid is",sid)
        year=2019
        try:
            each2=target_list[0]
        # for each2 in target_list[0]:
        # for each2 in target_list[0,3]:
            #print(a)
            print('7',each1,each2)
            target_url='http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid='+sid+each2
            print('--8--',each1)
            print('下载链接target_url,',target_url)
            treq = urllib.request.Request(target_url)
            time.sleep(random.random() * 3)
            treq.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
            tpage = urllib.request.urlopen(treq)
            time.sleep(random.random() * 3)
            print("--9--file_url is")
            try:
                print("--9-1-file_url is")
                thtml = tpage.read().decode('gbk')
                #print(thtml)
                file_url = re.search('http://file.finance.sina.com.cn/211.154.219.97:9494/.*?PDF',thtml)
                print('--9--file_url is',file_url.group(0))
                try:
                    #print(file_url.group(0))
                    report_year=file_url.group(0).split("/")[-4]
                    print('report_year',report_year)
                    report_year=str(int(report_year)-1)
                    print('report_year',report_year)
                    each3 = each[0:-1]
                    print(each3)
                    report_file=each3+report_year
                    print(report_file,report_file,report_file,report_file)
                    local = file_folder+'annual_report_2019/'+report_file+'.pdf'
                    # local = './' +'annual_report_2019'+ '/' +each3+report_year+'.pdf'
                    # print('local',local)
                    # # local = './'+each+'/'+file_url.group(0).split("/")[-4]+'.pdf'
                    # # local = './'+each+'/'+file_url.group(0).split("/")[-1]+'.pdf'
                    # # local = './'+sid+'/'+file_url.group(0).split("/")[-1]+'.pdf'
                    # print("10 local is",local)
                    #调试用作文件占位
                    #open(local, 'wb').write(b'success')
                    # print('11',each1,'local',local)
                    urllib.request.urlretrieve(file_url.group(0),local,None)
                except:
                    print('PDF失效;'+target_url)
            except:
                print(each1,'年报下载页面编码错误;'+target_url)
        except:
            print('each2',each2)
    except:
        print('年报列表页面编码错误;'+url)