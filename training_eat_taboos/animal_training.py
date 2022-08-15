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

data=[]
jieba.load_userdict("dict.txt")

with open("training.txt", "r", encoding="utf-8") as fp:
    for word in fp.readlines():
        main = word.strip() 
        data.append(main)

data = ";".join(data)
with open('stopwords.txt', 'rt', encoding='utf-8') as fp:
    stopwords = [word.strip() for word in fp.readlines()]

keyterms = [keyterm for keyterm in jieba.cut(data) 
            if keyterm not in stopwords 
                and keyterm.strip()!=""
                and keyterm.strip()!=","
                and keyterm.strip()!="XD"
                and keyterm.strip()!=";"
                and keyterm.strip()!="波比"
                and keyterm.strip()!="旺財"
                and keyterm.strip()!="老師"
                and keyterm.strip()!="咬"
                and keyterm.strip()!="漢克"
                and keyterm.strip()!="狗"]
text = ",".join(keyterms)
# print(text)
#做成長條圖
word_counts = collections.Counter(keyterms) # 對分詞做詞頻統計
word_counts_top10 = word_counts.most_common(10) # 獲取前10最高頻的詞
myfont=FontProperties(fname=r'C:\Users\howar\Desktop\msj.ttf',size=16)
sns.set(font=myfont.get_family())
sns.set_style("whitegrid",{"font.sans-serif":['Microsoft JhengHei']}) 
print(word_counts_top10)

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
   word_counts_top10[9]],columns=['關鍵詞', '次數'])
print(df)
ax = sns.barplot(x='關鍵詞', y='次數', data=df)
ax.set_title('寵物訓練')
plt.show()

#文字雲
mask = np.array(Image.open('animal_training.png'))
wordcloud = WordCloud(background_color="white",random_state=42,
                      margin=2, font_path="simhei.ttf",max_words=200,prefer_horizontal=0.9,
                      mask=mask,scale=2).generate(text) #contour_width=2 contour_color='blue'

plt.figure(figsize=(6,6),dpi=100)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()



#比較醜的
# Words=[]
# for i in range(0,10):
#     Words.append(word_counts_top10[i][0])

# Sta=[]
# for i in range(0,10):
#     Sta.append(word_counts_top10[i][1])

# x = np.arange(len(Words))
# plt.bar(x,Sta, color=['red', 'green', 'blue', 'yellow','red', 'green', 'blue', 'yellow','red', 'green'])
# plt.xticks(x, Words)
# plt.xlabel('字詞')
# plt.ylabel('出現頻率')
# plt.show()