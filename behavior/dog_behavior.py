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

# def behavior(weblink):
#   url = requests.get(weblink) #, headers=headers
#   url.encoding = 'UTF-8'
#   sp = BeautifulSoup(url.text, 'html.parser')
#   with open("behavior.txt", "a", encoding="utf-8", newline="") as fp:
#     for a in sp.find_all("p"):
#         a = a.text+"\n"
#         data=[]
#         data.append(a)
#         print(data)    
#         for b in data:
#             fp.write(b)
# behavior('https://justdog.tw/%e7%bc%ba%e6%84%9b%e7%9a%84%e7%8b%97%e7%8b%97%ef%bc%8c%e6%9c%89%e9%80%99%e4%ba%9b%e8%88%89%e5%8b%95%ef%bc%8c%e4%b8%bb%e4%ba%ba%e7%9a%84%e4%b8%8d%e9%87%8d%e8%a6%96%e8%ae%93%e4%ba%ba%e5%bf%83%e7%96%bc/')
# behavior('https://justdog.tw/%e7%8b%97%e7%8b%97%e9%80%99%e4%ba%9b%e8%a1%8c%e7%82%ba%ef%bc%8c%e6%98%af%e6%83%b3%e7%95%b6%e4%bd%a0%e7%9a%84%e3%80%8c%e4%bf%9d%e9%8f%a2%e3%80%8d%ef%bc%8c%e4%bf%9d%e8%ad%b7%e4%bd%a0%e5%ae%89%e5%85%a8/')
# behavior("https://justdog.tw/%e7%8b%97%e7%8b%97%e6%9c%89%e9%80%996%e5%80%8b%e8%a1%8c%e7%82%ba%ef%bc%8c%e5%be%88%e5%8f%af%e8%83%bd%e6%98%af%e6%8a%8a%e8%87%aa%e5%b7%b1%e3%80%8c%e7%95%b6%e4%ba%ba%e3%80%8d%e4%ba%86/")
# behavior("https://justdog.tw/%e7%8b%97%e7%8b%97%e6%9c%89%e9%80%99%e4%ba%9b%e3%80%8c%e6%80%aa%e7%95%b0%e3%80%8d%e8%a1%a8%e7%8f%be%ef%bc%8c%e6%98%af%e5%9c%a8%e5%91%8a%e8%a8%b4%e4%b8%bb%e4%ba%ba%ef%bc%9a%e6%88%91%e7%97%85%e4%ba%86/")
# behavior("https://justdog.tw/%e7%8b%97%e7%8b%97%e7%aa%81%e7%84%b6%e7%99%bc%e5%87%ba%e3%80%8c%e5%97%9a%e5%97%9a%e3%80%8d%e8%81%b2%ef%bc%8c%e6%98%af%e5%9c%a8%e5%91%8a%e8%a8%b4%e4%bd%a0%ef%bc%8c%e6%9c%89%e4%ba%8b%e8%a6%81%e7%99%bc/")
# behavior("https://www.hills.com.tw/dog-care/behavior-appearance/types-of-common-dog-behavior")
list=[]
jieba.load_userdict("dog_behavior_dict.txt")
with open("dog_behavior.txt", "r", encoding="utf-8") as fp:
    for word in fp.readlines():
        main = word.strip() 
        list.append(main)

data = ";".join(list)
with open('stopwords.txt', 'rt', encoding='utf-8') as fp:
    stopwords = [word.strip() for word in fp.readlines()]

keyterms = [keyterm for keyterm in jieba.cut(data) 
            if keyterm not in stopwords 
                and keyterm.strip()!=""
                and keyterm.strip()!="狗"
                and keyterm.strip()!="話"
                and keyterm.strip()!="非常"
                and keyterm.strip()!="情況"
                and keyterm.strip()!=";"
                and keyterm.strip()!="動作"
                and keyterm.strip()!="寵主"
                and keyterm.strip()!="發現"
                and keyterm.strip()!="愛犬"
                and keyterm.strip()!="不好"
                and keyterm.strip()!="不理"
                and keyterm.strip()!="狗狗"
                and keyterm.strip()!="睡"
                and keyterm.strip()!="更"
                and keyterm.strip()!="想要"
                and keyterm.strip()!="我家"
                and keyterm.strip()!="就會"]
text = ",".join(keyterms)
# print(text)
#做成長條圖
word_counts = collections.Counter(keyterms) # 對分詞做詞頻統計
word_counts_top10 = word_counts.most_common(13) # 獲取前10最高頻的詞

myfont=FontProperties(fname=r'C:\Users\howar\Desktop\msj.ttf',size=16)
sns.set(font=myfont.get_family())
sns.set_style("white",{"font.sans-serif":['Microsoft JhengHei']})
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
   word_counts_top10[9],
   word_counts_top10[10],
   word_counts_top10[11],
   word_counts_top10[12]],columns=['關鍵詞', '次數'])
ax = sns.barplot(x='關鍵詞', y='次數',data=df)
ax.set_title('狗狗行為表現')
plt.show()
# # 文字雲
mask = np.array(Image.open('dog_behavior.jpg'))
wordcloud = WordCloud(background_color="white",random_state=42,
                      margin=2, font_path="simhei.ttf",max_words=200,prefer_horizontal=0.8,
                      mask=mask,scale=2).generate(text)

plt.figure(figsize=(8,8),dpi=100)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
