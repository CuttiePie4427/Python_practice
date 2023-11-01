# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 21:07:46 2023

@author: USER
"""

import requests

from bs4 import BeautifulSoup


url = 'https://member.lccnet.com.tw/'


params = {
    'Account': '',
'Password': '',
'RememberMe': 'false',
'__RequestVerificationToken': 'eUsiN-yYE_pf0ZeUI2fGwkJGEmJakjsz3_0F6iDg9H82gvetftkKJ85CEThgO0NFFREp2LZJkCHqFhY9M3LeOvWSwBJ4BSMBBwbRnpYQuUE1'
    
    
    }

header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
'Cookie':
'_cuid=d26a0a7a-35eb-40c1-9152-2477ae6c9160; _cuserid=; _cusertrait=%7B%7D; _ctrait=%7B%7D; _cgrpid=; _cgrptrait=%7B%7D; _ss_pp_id=0c3944a69cfb0581c0a1687810088393; _hjSessionUser_1446807=eyJpZCI6ImM4MTE0NWFjLTg5YzEtNThlZi1iMGYyLTgwMGUyMzU0YTNkYiIsImNyZWF0ZWQiOjE2ODc4Mzg4ODY1MTEsImV4aXN0aW5nIjp0cnVlfQ==; script_flag=fd13385c-97e5-4e21-ac73-ac7f33c5bbc8; _ga_TDP4KNDS80=GS1.1.1689316045.3.0.1689316051.54.0.0; _gcl_au=1.1.1351874178.1698835542; _fbp=fb.2.1698835541785.371657679; _gid=GA1.3.1584351639.1698835542; url_flag=https://www.lccnet.com.tw/lccnet; _hjIncludedInSessionSample_1446807=0; _ga_Q39DSHDCZC=GS1.1.1698835542.1.1.1698835721.0.0.0; _ga_FNFG97HXYJ=GS1.1.1698835541.1.1.1698835721.0.0.0; cto_bundle=aijNQV8zV1puOTZzJTJGZ1BiZksxNW04dm82RFk3aXNkRFloQ0o0ZWNLeENINFprYlZFRzBGSmZ4eEwlMkJsN2pWbzgwaiUyQlQ3UXBnaWRCUVVYTEZERE5Ma2laJTJCVUtDNmpPZDVUUk9jNTFIQm9LV0tkSGhoMWlEdDBDSlp0OEJkck1TcUd5N1NZa29Rb0VuWDFFUHRpOHJmeXB3SjY3czd0dkFVMTFWcGwyMDQzaTdSVSUyRlpnJTNE; _td=16350bed-ab40-4982-aa57-0dd5cf0f17ec; _uetsid=cd91fd2078a311ee9c7cc97246e3bc28; _uetvid=3847673014a011eeabce1f9513625979; _ga_QY8DQDPMSR=GS1.1.1698843205.5.1.1698843209.56.0.0; __RequestVerificationToken=tpn63liWXPpl1c7W2im0wTcVxLNx64qx-jJvuvX4QKBweJf4Z5qTWbcFsC3BYQtXc9zTzrCftUVeCC72cYTRQy0ViUSMHerU01kV43GQpjo1; _ga=GA1.4.489821006.1687838887; _gid=GA1.4.1584351639.1698835542; adgeek_login_path=/; adgeek_lccnet_user_id=891031651; _ga_RV6BDWB9GV=GS1.1.1698843210.1.1.1698843436.0.0.0; _ga_ENRV8GBKH8=GS1.1.1698843209.2.1.1698843436.3.0.0; _ga=GA1.3.489821006.1687838887; adgeek_login_status=true; _ga_RHTTWMMSB7=GS1.1.1698843210.2.1.1698843875.59.0.0'
    
    }
    
    
session_requests = requests.session()

content = session_requests.post(url,data=params,headers=header).text


url2 = "https://member.lccnet.com.tw/Booking" 

content = session_requests.get(url2).text

soup = BeautifulSoup(content,'html.parser')

course = soup.find('ul',class_='courseListWrapper')

li = course.find_all('li')

for item in li:
    name = item.find('h4').text
    c = item.find_all('p')
    print(name)    
    for p in c:
        print(p.text)
        
    print()    
    







  
    





