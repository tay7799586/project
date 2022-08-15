from time import time
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import jieba
import collections
import pandas as pd
import seaborn as sns
from matplotlib.font_manager import FontProperties

# def diet(weblink):
#   url = requests.get(weblink) #, headers=headers
#   url.encoding = 'UTF-8'
#   sp = BeautifulSoup(url.text, 'html.parser')
#   with open("taboos.txt", "a", encoding="utf-8", newline="") as fp:
#     for a in sp.find_all("p"):
#         a = a.text+"\n"
#         data=[]
#         data.append(a)
#         print(a)
#         for b in data:
#             fp.write(b)
# diet('https://litomon.com/blog/donteatfood/')
# diet('https://crazypetter.com.tw/cats-and-dogs-cant-eat/')
# diet('https://health.ettoday.net/news/1112773')
list=[]
jieba.load_userdict("dict.txt")
with open("taboos.txt", "r", encoding="utf-8") as fp:
    for word in fp.readlines():
        main = word.strip() 
        list.append(main)

data = ";".join(list)
with open('stopwords.txt', 'rt', encoding='utf-8') as fp:
    stopwords = [word.strip() for word in fp.readlines()]

keyterms = [keyterm for keyterm in jieba.cut(data) 
            if keyterm not in stopwords 
                and keyterm.strip()!="時"
                and keyterm.strip()!="狗狗"
                and keyterm.strip()!="貓咪"
                and keyterm.strip()!="犬"
                and keyterm.strip()!="葡萄乾"
                and keyterm.strip()!=";"
                and keyterm.strip()!=""
                and keyterm.strip()!="狗"
                and keyterm.strip()!="中"
                and keyterm.strip()!="重要"
                and keyterm.strip()!="健康"
                and keyterm.strip()!="犬貓"
                and keyterm.strip()!="寵物"
                and keyterm.strip()!="家長"
                and keyterm.strip()!="蛋白"
                and keyterm.strip()!="鍾昇華"]
text = ",".join(keyterms)
# print(text)
#做成長條圖
word_counts = collections.Counter(keyterms) # 對分詞做詞頻統計
word_counts_top10 = word_counts.most_common(12) # 獲取前10最高頻的詞

myfont=FontProperties(fname=r'C:\Users\howar\Desktop\msj.ttf',size=16)
sns.set(font=myfont.get_family())
sns.set_style("darkgrid",{"font.sans-serif":['Microsoft JhengHei']}) #whitegrid

# plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
# plt.rcParams['axes.unicode_minus'] = False
# sns.set_context("talk")

df = pd.DataFrame([
   word_counts_top10[0],
   word_counts_top10[1],
   word_counts_top10[2],
   word_counts_top10[3],
   word_counts_top10[4],
   word_counts_top10[5],
   word_counts_top10[6],
   word_counts_top10[7],
   word_counts_top10[8],
   word_counts_top10[9],
   word_counts_top10[10],
   word_counts_top10[11]],columns=['關鍵詞', '次數'])
ax = sns.barplot(x='關鍵詞', y='次數',data=df)
ax.set_title('貓狗飲食禁忌')
plt.show()
#文字雲
mask = np.array(Image.open('cloud.jpg'))
wordcloud = WordCloud(background_color="white",random_state=42,
                      margin=2, font_path="simhei.ttf",max_words=200,prefer_horizontal=0.9,
                      mask=mask,scale=2).generate(text)

plt.figure(figsize=(7,7),dpi=100)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()