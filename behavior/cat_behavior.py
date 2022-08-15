from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
from matplotlib import colors
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import jieba
import collections
import pandas as pd
import seaborn as sns
from matplotlib.font_manager import FontProperties
# def cat_behavior(weblink):
#   url = requests.get(weblink) #, headers=headers
#   url.encoding = 'UTF-8'
#   sp = BeautifulSoup(url.text, 'html.parser')
#   with open("cat_behavior.txt", "a", encoding="utf-8", newline="") as fp:
#     for a in sp.find_all("p"):
#         a = a.text+"\n"
#         data=[]
#         data.append(a)
#         print(data)    
#         for b in data:
#             fp.write(b)
# cat_behavior('https://leedecat.com/%E8%B2%93%E5%92%AA%E8%A1%8C%E7%82%BA%E8%A7%A3%E6%9E%90%EF%BC%8C10%E5%80%8B%E8%B2%93%E5%92%AA%E8%A1%8C%E7%82%BA%EF%BC%8C%E8%A8%93%E7%B7%B4%E5%B8%AB%E6%95%99%E4%BD%A0%E8%AE%80%E6%87%82%E8%B2%93%E5%BF%83/')
# cat_behavior("https://justdog.tw/%e8%b2%93%e5%92%aa%e4%b9%9f%e6%9c%83%e8%aa%8d%e9%8c%af%ef%bc%9f%e9%80%99%e5%b9%be%e5%80%8b%e5%8b%95%e4%bd%9c%e5%85%b6%e5%af%a6%e6%98%af%e8%b2%93%e5%92%aa%e5%9c%a8%e5%90%91%e4%bd%a0%e9%81%93%e6%ad%89/")

list=[]
jieba.load_userdict("cat_behavior_dict.txt")
with open("cat_behavior.txt", "r", encoding="utf-8") as fp:
    for word in fp.readlines():
        main = word.strip() 
        list.append(main)

data = ";".join(list)
with open('stopwords.txt', 'rt', encoding='utf-8') as fp:
    stopwords = [word.strip() for word in fp.readlines()]

keyterms = [keyterm for keyterm in jieba.cut(data) 
            if keyterm not in stopwords 
                and keyterm.strip()!=""
                and keyterm.strip()!="母貓"
                and keyterm.strip()!="代表"
                and keyterm.strip()!="貓咪會"
                and keyterm.strip()!="話"
                and keyterm.strip()!="非常"
                and keyterm.strip()!="情況"
                and keyterm.strip()!=";"
                and keyterm.strip()!="寵主"
                and keyterm.strip()!="發現"
                and keyterm.strip()!="不好"
                and keyterm.strip()!="不理"
                and keyterm.strip()!="睡"
                and keyterm.strip()!="不要"
                and keyterm.strip()!="想要"
                and keyterm.strip()!="處"]

text = ",".join(keyterms)
# print(text)
#做成長條圖
word_counts = collections.Counter(keyterms) # 對分詞做詞頻統計
word_counts_top10 = word_counts.most_common(12) # 獲取前10最高頻的詞

myfont=FontProperties(fname=r'C:\Users\howar\Desktop\msj.ttf',size=16)
sns.set(font=myfont.get_family())
sns.set_style("darkgrid",{"font.sans-serif":['Microsoft JhengHei']})

# plt.rcParams['axes.unicode_minus'] = False
# plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
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
ax.set_title('貓貓行為表現')
plt.show()

# 文字雲
mask = np.array(Image.open('cat_behavior.jpg'))

wordcloud = WordCloud(background_color="white",random_state=42,
                      margin=2, font_path="simhei.ttf",max_words=200,prefer_horizontal=0.8,
                      mask=mask,scale=2).generate(text)
plt.figure(figsize=(6,6),dpi=100)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
# wordcloud.to_file('專題貓咪.png')