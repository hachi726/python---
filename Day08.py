import requests
from bs4 import BeautifulSoup

payload = {
   'from': '/bbs/Gossiping/index.html',
  'yes': 'yes'
}

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
}

rs = requests.Session()
rs.post('https://www.ptt.cc/ask/over18', data=payload, headers=headers)
res = rs.get('https://www.ptt.cc/bbs/Gossiping/index.html', headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

# 填入每篇文章的class name
items = soup.find_all('div', class_='r-ent')

main_url='https://www.ptt.cc/'
# result = []
# for item in items:
#     try:
#         # 填入每篇文章title的class name
#         title = item.find('div', class_='title').text
        
#         # 填入每篇文章url的tag和attribute
#         url = main_url + item.find('a')['href']
#         # print(url)
#         result.append([title, url])
#     except: 
#         pass


# content_list = []
# for row in result:
#   title, url = row

#   # 填入session資訊並且透過request來得到HTML
#   r = requests.get(url, headers=headers, cookies={'over18':'1'})
#   soup = BeautifulSoup(r.text, 'html.parser')

#   # 填入正確的tag和名稱
#   items = soup.find('div', class_='main-content')
#   content = soup.find('div', id='main-content').text

#   content_list.append([title, url, content])

# # 存檔
# import pandas as pd
# pd.DataFrame(content_list, columns=['title','url','content']).to_excel('content.xlsx')

url =  'https://www.ptt.cc/bbs/Gossiping/index.html'
for i in range(3):
  res = requests.get(url, headers=headers, cookies={'over18':'1'})
  soup = BeautifulSoup(res.text, 'html.parser')
 
  url = main_url + soup.find('a',string="‹ 上頁")['href']
  print(url)
