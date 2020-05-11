# -*- coding: utf-8 -*-
# 第一行必须有，否则报中文字符非ascii码错误

# import urllib.request
# from urllib.parse import quote
# import string
import json
import time
import requests

def sleep(n):
    time.sleep(n)
    print("~~~sleeping~~~~")
def requested(url):
    sleep(5)
    html=requests.get(url)
    data=html.json()
    return data
def write_txt(file,data):
    f=open(file,'a',encoding='utf-8')
    f.write(data)
    print(data,'写入',file,'成功')
    f.close()
def time_now():
    time_now=time.strftime('%Y-%m-%d-%H%M%S',time.localtime(time.time()))
    print(time_now)
    return str(time_now)

ak ="C75tUrXIZKbn3QOMB3e9cIx7g9fsMrUo"
url_1='http://api.map.baidu.com/place/v2/search?query='
url_2='南京路'#搜索关键词
url_3='&region='
url_4='信阳'#所在城市
url_5='&page_size=20&page_num='
url_6='1'
url_7='&output=json&ak='+ak
file=time_now()+url_4+'-'+url_2+"results.txt"
for url_6 in range(20):
    url=url_1+url_2+url_3+url_4+url_5+str(url_6)+url_7
    data=requested(url)
    for item in data['results']:
        jname = item['name']
        jlat = item['location']['lat']
        jlon = item['location']['lng']
        jadd = item['address']
        j_data=url_4+url_2+','+str(url_6)+','+jname+','+str(jlat)+','+str(jlon)+','+jadd+'\n'
        write_txt(file, j_data)



# for item in data['results']:
    # jname=item['name']
    # jadd=item['address']
    # j_data=jname+','+jadd+'\n'
    # write_txt(file,j_data)

#感谢https://blog.csdn.net/sinat_41310868/article/details/78746094


# page_size = 20
# page_num = 0
# scope = 1
# 范围：
# 左下坐标 30.379,114.118
# 右上坐标 30.703,114.665
# 中间坐标 30.541,114.3915
# bounds = [
#     [30.379, 114.118, 30.541, 114.3915],
#     [30.379, 114.3915, 30.541, 114.665],
#     [30.541, 114.118, 30.703, 114.3915],
#     [30.541, 114.3915, 30.703, 114.665]
# ]
#
# new_bounds = []
# # col_row 将bounds的每一小块继续细分为3行3列，可以防止区域内的搜索数量上限400
# col_row = 3
# for lst in bounds:
#     distance_lat = (lst[2] - lst[0]) / col_row
#     distance_lon = (lst[3] - lst[1]) / col_row
#     for i in range(col_row):
#         for j in range(col_row):
#             lst_temp = []
#             lst_temp.append(lst[0] + distance_lat * i)
#             lst_temp.append(lst[1] + distance_lon * j)
#             lst_temp.append(lst[0] + distance_lat * (i + 1))
#             lst_temp.append(lst[1] + distance_lon * (j + 1))
#             new_bounds.append(lst_temp)
#
# queryResults = []
#
# for bound in new_bounds[0:1]:
#     np = True
#     a = []
#     while np == True:
#         # 使用百度提供的url拼接条件
#         url = "http://api.map.baidu.com/place/v2/search?ak=" + str(ak) + "&output=json&query=" + str(
#             query[0]) + "&page_size=" + str(page_size) + "&page_num=" + str(page_num) + "&bounds=" + str(
#             bound[0]) + "," + str(bound[1]) + "," + str(bound[2]) + "," + str(bound[3])
#         url = quote(url, safe=string.printable)
#
#         # 请求url读取，创建网页对象
#         jsonf = urllib.request.urlopen(url)
#         page_num = page_num + 1
#
#         # 判断查询翻页进程
#         jsonfile = jsonf.read()
#         s = json.loads(jsonfile)
#         total = int(s["total"])
#         a.append(total)
#
#         queryResults.append(s)
#         print("queryResults\n",queryResults)
#         max_page = int(a[0] / page_size) + 1
#         # 防止并发过高，百度地图要求并发小于120
#         time.sleep(1)
#
#         if page_num > max_page:
#             np = False
#             page_num = 0
#             print("search complete")
#             print("output: " + str(bound))
#             print("total: " + str(a[0]))
#             print("")
#
# results = open("results.txt", 'a')
# results.write(str(queryResults).encode('utf-8').decode('unicode_escape'))
# results.close()
# print("ALL DONE!")
