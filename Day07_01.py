import requests
import json

# 收集
url = "https://raw.githubusercontent.com/kiang/pharmacies/master/json/points.json"

# 整理
r = requests.get(url)
data = r.text

# 儲存
# with open("test.json", "w") as f :
#     f.write(json.dumps(data))
# print("=========================================")

# # 計算各地區的藥局數量：
from collections import defaultdict
med_count = defaultdict(int)

with open("test.json", "r") as f :
    data = json.loads(data)
# 填入欄位名稱
for row in data['features']:
    conunty = row['properties']['county']
    if conunty == "" :               # 處理資料中的缺失值   ""
        conunty = row["properties"]["address"][0:3]

    med_count[conunty] += 1

print(med_count)
# print("=========================================")


# 計算每個地區的剩餘口罩數量(分成人的和小孩的)，並且從大到小排列
with open('test.json', 'r') as f:
  data = json.loads(data)

from collections import defaultdict

# 宣告 dictionary 用來存放資料
child_count = defaultdict(int)
adult_count = defaultdict(int) 
 
# 將資料迭代印出做計算
for row in data['features']:
    conunty = row['properties']['county']
    mask_child = row['properties']["mask_child"]
    mask_adult = row['properties']["mask_adult"]
    child_count[conunty] += mask_child
    adult_count[conunty] += mask_adult

# 排序
print(sorted(adult_count.items(), key=lambda kv: kv[1], reverse=True))
print(sorted(child_count.items(), key=lambda kv: kv[1], reverse=True))
