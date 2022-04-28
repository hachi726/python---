# txt檔案路徑
txt_file_path = "test.txt"

# 載入檔案到變數中
with open(txt_file_path, "r",encoding="utf-8") as fn:
    lines = fn.readlines()
    lines = list(map(lambda x: x.strip(),lines)) # 移除斷行字元

# 載入套件與字典檔
import jieba


# 精確模式斷詞
tokens_1 = list(map(lambda x: list(jieba.cut(str(x), HMM=False)), lines))

# 全模式斷詞
tokens_2 = list(map(lambda x: list(jieba.cut(str(x), cut_all=True, HMM=False)), lines))

# 搜尋引擎模式斷詞
tokens_3 = list(map(lambda x: list(jieba.cut_for_search(str(x), HMM=False)), lines))

word_count = {}
for sent in tokens_1: # 放入斷詞之後的變數
  for word in sent:
    if word not in word_count:
      word_count[word] = 0
    word_count[word] += 1 

print(word_count)


# from collections import Counter
# word_count_list = []
# for sent in tokens_1:
#     for item in sent:
#         word_count_list.append(item)

# print(Counter(word_count_list).most_common(5))
