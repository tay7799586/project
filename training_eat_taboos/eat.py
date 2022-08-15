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
import time
from matplotlib.font_manager import FontProperties


# def eat(weblink):
#   url = requests.get(weblink) #, headers=headers
#   url.encoding = 'UTF-8'
#   sp = BeautifulSoup(url.text, 'html.parser')
#   with open("eat.txt", "a", encoding="utf-8", newline="") as fp:
#     for a in sp.find_all("p"):
#         a = a.text+"\n"
#         data=[]
#         data.append(a)
#         print(a)
#         for b in data:
#             fp.write(b)
        # time.sleep(2)

# eat('https://justdog.tw/%e9%88%a3%e7%a3%b7%e5%b0%8d%e7%8b%97%e7%8b%97%e5%be%88%e9%87%8d%e8%a6%81%ef%bc%8c%e7%8b%97%e7%8b%97%e7%bc%ba%e5%b0%91%e6%88%96%e8%80%85%e9%81%8e%e5%88%86%e8%a3%9c%e5%85%85%e9%83%bd%e4%b8%8d%e5%a5%bd/')
# eat('https://justdog.tw/%e5%af%b5%e7%89%a9%e7%87%9f%e9%a4%8a%e8%a3%9c%e5%85%85%e5%8a%91%e4%b9%8b%e7%9b%8a%e7%94%9f%e8%8f%8c/')
# eat('https://justdog.tw/%e7%b6%ad%e7%94%9f%e7%b4%a0e-%e5%af%b5%e7%89%a9%e7%87%9f%e9%a4%8a%e9%a3%9f%e5%93%81%e6%8a%80%e8%a1%9332/')
# eat('https://justdog.tw/%e5%b9%ab%e4%bd%a0%e4%b8%80%e5%8f%a3%e6%b0%a3%e5%bc%84%e6%87%82%e7%8b%97%e7%8b%97%e7%bc%ba%e9%88%a3%e9%82%a3%e4%ba%9b%e4%ba%8b%e5%85%92%ef%bc%8c%e5%b0%b1%e7%8f%be%e5%9c%a8/')
# eat('https://gomopetfood.com/sub_pages/0449fd58-417d-45ec-8cd6-9e2a76730da4')


list=[]
jieba.load_userdict("dict.txt")
with open("eat.txt", "r", encoding="utf-8") as fp:
    for word in fp.readlines():
        main = word.strip() 
        list.append(main)

data = ";".join(list)
with open('stopwords.txt', 'rt', encoding='utf-8') as fp:
    stopwords = [word.strip() for word in fp.readlines()]

keyterms = [keyterm for keyterm in jieba.cut(data) 
            if keyterm not in stopwords 
                and keyterm.strip()!=""
                and keyterm.strip()!=","
                and keyterm.strip()!="犬"
                and keyterm.strip()!=";"
                and keyterm.strip()!="中"
                and keyterm.strip()!="食物"
                and keyterm.strip()!="重要"
                and keyterm.strip()!="健康"]
text = ",".join(keyterms)
# print(text)
#做成長條圖
word_counts = collections.Counter(keyterms) # 對分詞做詞頻統計
word_counts_top10 = word_counts.most_common(10) # 獲取前10最高頻的詞
myfont=FontProperties(fname=r'C:\Users\howar\Desktop\msj.ttf',size=16)
sns.set(font=myfont.get_family())
sns.set_style("dark",{"font.sans-serif":['Microsoft JhengHei']}) 

# plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
# plt.rcParams['axes.unicode_minus'] = False

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
   word_counts_top10[9]],columns=['關鍵詞', '次數'])
ax = sns.barplot(x='關鍵詞', y='次數', data=df)
ax.set_title('寵物保健')
plt.show()
# 文字雲
mask = np.array(Image.open('eat.jpg'))
wordcloud = WordCloud(background_color="white",random_state=42,
                      margin=2, font_path="simhei.ttf",max_words=200,prefer_horizontal=0.9,
                      mask=mask,scale=2).generate(text)

plt.figure(figsize=(8,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
