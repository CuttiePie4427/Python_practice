
"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup
import requests

header = {   
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }

url = 'https://supertaste.tvbs.com.tw/food'

data = requests.get(url,headers=header).text 

soup = BeautifulSoup(data,'html.parser')

# food = soup.find('div',class_ = 'article__content')

food = soup.find('div',{'class':'article__content'}) #字典用法，結果一樣

# print(food)

a = food.find_all('a')
for row in a:
    img = row.find('img').get('data-original')
    title = row.find('h3').text.strip()
    post_date = row.find('span').text.strip()
    link = 'https://supertaste.tvbs.com.tw' + row.get('href')
    
    print('img:',img)
    print()
    print('title:',title)
    print()
    print('post_date:',post_date)
    print()
    print('link:',link)
    print('-'*30)
    
    
