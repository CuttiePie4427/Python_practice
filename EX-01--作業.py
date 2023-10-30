# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
import requests

import csv
#Json格式>>不用美湯解
#從search的Network>>response 的資料拿去 Json Parser online解

url = 'https://www.thsrc.com.tw/TimeTable/Search' #從search的header找
header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
      }
    
thinfo = {'南港':'NanGang','台北':'TaiPei','板橋':'BanQiao','桃園':'TaoYuan','新竹':'XinZhu','苗栗':'MiaoLi','台中':'TaiZhong','彰化':'ZhangHua','雲林':'YunLin','嘉義':'JiaYi','台南':'TaiNan','左營':'ZuoYing'}    
# print('車站:',thinfo.keys())
gostation = input('出發站:')
endstation = input('抵達站:')
gotime = input('出發時間:')
go = thinfo.get(gostation,'NanGang')
end = thinfo.get(endstation,'ZuoYing') 

# print(go)
# print(end)
    
param = {'SearchType':'S',                 #這段param從Network的payload抓
'Lang':'TW',
'StartStation':go,
'EndStation':end,
'OutWardSearchDate':'2023/11/01',
'OutWardSearchTime':'21:30',
'ReturnSearchDate':'2023/11/01',
'ReturnSearchTime':'21:30',
         }

data = requests.post(url,data = param,headers = header).text
# print(data)

thrsc = json.loads(data)

items = thrsc['data']['DepartureTable']['TrainItem']
# print(items)
fileName = 'thrsc.csv'
fObj = open(fileName,'w',newline='')
csvWrite = csv.writer(fObj)
csvWrite.writerow(['車次','出發時間','抵達時間','旅行時間','停靠站'])
#作業<二>:輸入起訖站給出時刻表
# 上面要先新增字典，放入12個站，並設立兩個變數代表出發站(go)與抵達站(end) 
#額外內容>>轉成csv檔案

for row in items: 
    if row['DepartureTime'] >= gotime:
        print('-'*30)
        print(row['TrainNumber'])
        print(row['DepartureTime'])
        print(row['DestinationTime'])
        print(row['Duration'])
        print('停靠站:',end = '')
        msg = ""
    
#作業<一>:列出停靠站
        stn = row['StationInfo']
        for sn in stn:
            if sn['Show'] == True:
                print(sn['StationName'],end = '>'*2)
                msg += sn['StationName'] + ','
        print()
        csvWrite.writerow([row['TrainNumber'],row['DepartureTime'],row['DestinationTime'],row['Duration'],msg])
        
fObj.close()


