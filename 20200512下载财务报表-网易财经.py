def download_financial_table(stock_code):
    import re,urllib
    import xlwt
    from bs4 import BeautifulSoup
    from time import sleep
    # url_lrb = 'http://quotes.money.163.com/service/lrb_'+str(stock_code[2:8])+'.html'
    url_zcfzb = 'http://quotes.money.163.com/service/zcfzb_' + str(stock_code[2:8]) + '.html'
    url_xjllb = 'http://quotes.money.163.com/service/xjllb_' + str(stock_code[2:8]) + '.html'
    while True:
        try:
            # content_lrb = urllib.request.urlopen(url_lrb,timeout=2).read()
            content_zcfzb= urllib.request.urlopen(url_zcfzb, timeout=2).read()
            content_xjllb = urllib.request.urlopen(url_xjllb, timeout=2).read()
            # print(content_lrb)
            # with open('C://TEMP/Excel/financial_table/'+str(stock_code[0:-1].strip('*'))+'利润表.csv','wb') as f:
            #     f.write(content_lrb)
            sleep(1)
            with open('C://TEMP/Excel/financial_table/'+str(stock_code[0:-1].strip('*'))+'资产负债表.csv','wb') as f:
                f.write(content_zcfzb)
            sleep(1)
            with open('C://TEMP/Excel/financial_table/'+str(stock_code[0:-1].strip('*'))+'现金流量表.csv','wb') as f:
                f.write(content_xjllb)
            print(stock_code)
            sleep(1)

            break
        except Exception as e:
            if str(e) =='HTTP Error 404: Not Found':
                break
            else:
                print(e)
                continue
###########################################################
# ——————————————————————主程序——————————————————————————————
###########################################################
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

for each in stock[1:]:
    print('~~~~each is',each.strip('*'))
    each1=each[2:8];each0=each[0:8];each3=each
    print(each3)
    download_financial_table(each.strip('*ST'))

# count = 1
# for count in range(600500,600501):
#     url = 'http://quotes.money.163.com/service/lrb_'+str(count)+'.html'
#     while True:
#         try:
#             content = urllib.request.urlopen(url,timeout=2).read()
#             print(content)
#             with open('C://TEMP/Excel/financial_table/'+str(count)+'利润表.csv','wb') as f:
#                 f.write(content)
#             print(count)
#             sleep(1)
#             break
#         except Exception as e:
#             if str(e) =='HTTP Error 404: Not Found':
#                 break
#             else:
#                 print(e)
#                 continue