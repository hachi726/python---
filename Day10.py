!pip install jieba # jieba 中文斷詞套件
!pip install wordcloud # wordcloud 文字雲視覺化套件
!pip install matplotlib # matplotlib 畫圖工具套件# txt檔案路徑

# txt檔案路徑
txt_file_path = "/content/test.txt"

# 載入檔案到變數中
with open(txt_file_path, "r")as fn:
    lines = fn.readlines()
    lines = list(map(lambda x: x.strip(),lines)) # 移除斷行字元

import jieba

# 下載官方字典檔
!wget https://raw.githubusercontent.com/fxsjy/jieba/master/extra_dict/dict.txt.big

# 載入字典檔
jieba.load_userdict("/content/dict.txt.big")

# 精確模式斷詞
tokens_1 = list(map(lambda x: list(jieba.cut(str(x), HMM=False)), lines))

word_count = {}
# 計算詞頻
for sent in tokens_1: 
 for word in sent:
 if word not in word_count:
      word_count[word] = 0
    word_count[word] += 1 

# 篩選出出現次數大於 5 次的字詞
word_count_5 = {}

for word, count in word_count.items():
 if count > 3 :
    word_count_5[word] = count
print(word_count_5)

import wordcloud
from wordcloud import WordCloud
import matplotlib
import matplotlib.pyplot as plt

# 下載中文字型檔
!wget https://github.com/odek53r/Data-Science-Camp/raw/main/SourceHanSerifK-Light.otf

wordcloud = WordCloud(
        background_color = 'white',
        font_path = '/content/SourceHanSerifK-Light.otf', # 放入中文字型檔路徑
        colormap=matplotlib.cm.cubehelix,
        width = 1600,
        height = 800,
        margin = 2)

# wordcloud 套件 Input 需放入詞頻統計的 dict 型態變數
wordcloud = wordcloud.generate_from_frequencies(word_count_5) 
plt.figure(figsize=(20,10), facecolor='k')
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()
