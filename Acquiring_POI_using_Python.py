# -*- coding: utf-8 -*-
# 第一行必须有，否则报中文字符非ascii码错误

import urllib.request
from urllib.parse import quote
import string
import json
import time

# ak需要在百度地图开放平台申请
# ak = "Qgnt7lFOgBR2NkDN963RL26zP0USR024"
ak ="C75tUrXIZKbn3QOMB3e9cIx7g9fsMrUo"

# 关键词
query = ["社会福利院"]
page_size = 20
page_num = 0
scope = 1

# 范围：
# 左下坐标 30.379,114.118
# 右上坐标 30.703,114.665
# 中间坐标 30.541,114.3915

bounds = [
    [30.379, 114.118, 30.541, 114.3915],
    [30.379, 114.3915, 30.541, 114.665],
    [30.541, 114.118, 30.703, 114.3915],
    [30.541, 114.3915, 30.703, 114.665]
]

new_bounds = []
# col_row 将bounds的每一小块继续细分为3行3列，可以防止区域内的搜索数量上限400
col_row = 3
for lst in bounds:
    distance_lat = (lst[2] - lst[0]) / col_row
    distance_lon = (lst[3] - lst[1]) / col_row
    for i in range(col_row):
        for j in range(col_row):
            lst_temp = []
            lst_temp.append(lst[0] + distance_lat * i)
            lst_temp.append(lst[1] + distance_lon * j)
            lst_temp.append(lst[0] + distance_lat * (i + 1))
            lst_temp.append(lst[1] + distance_lon * (j + 1))
            new_bounds.append(lst_temp)

queryResults = []

for bound in new_bounds[0:1]:
    np = True
    a = []
    while np == True:
        # 使用百度提供的url拼接条件
        url = "http://api.map.baidu.com/place/v2/search?ak=" + str(ak) + "&output=json&query=" + str(
            query[0]) + "&page_size=" + str(page_size) + "&page_num=" + str(page_num) + "&bounds=" + str(
            bound[0]) + "," + str(bound[1]) + "," + str(bound[2]) + "," + str(bound[3])
        url = quote(url, safe=string.printable)

        # 请求url读取，创建网页对象
        jsonf = urllib.request.urlopen(url)
        page_num = page_num + 1

        # 判断查询翻页进程
        jsonfile = jsonf.read()
        s = json.loads(jsonfile)
        total = int(s["total"])
        a.append(total)

        queryResults.append(s)
        print("queryResults\n",queryResults)
        max_page = int(a[0] / page_size) + 1
        # 防止并发过高，百度地图要求并发小于120
        time.sleep(1)

        if page_num > max_page:
            np = False
            page_num = 0
            print("search complete")
            print("output: " + str(bound))
            print("total: " + str(a[0]))
            print("")

results = open("results.txt", 'a')
results.write(str(queryResults).encode('utf-8').decode('unicode_escape'))
results.close()
print("ALL DONE!")
