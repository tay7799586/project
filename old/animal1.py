from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
# from tomlkit import key
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import jieba
import collections
import pandas as pd
import seaborn as sns
# url = "https://richbobi.com/pet/behavior/1082/"
# html = requests.get(url)
# html.encoding = 'UTF-8'
# sp = BeautifulSoup(html.text, 'html.parser')

# for a in sp.find_all("p"):
#         a = a.text+"\n"
data=[]
jieba.load_userdict("dict.txt")

with open("1.txt", "r", encoding="utf-8") as fp:
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
                and keyterm.strip()!=";"]
text = ",".join(keyterms)
# print(text)
mask = np.array(Image.open('cloud.jpg'))
wordcloud = WordCloud(background_color="white",
                      width=1000, height=1000, 
                      margin=2, font_path="simhei.ttf", 
                      mask=mask).generate(text)

plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

#做成圖
word_counts = collections.Counter(keyterms) # 對分詞做詞頻統計
word_counts_top10 = word_counts.most_common(10) # 獲取前10最高頻的詞
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
sns.set_context("talk")

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
   word_counts_top10[9]],columns=['出現的詞', '次數'])
ax = sns.barplot(x='出現的詞', y='次數', data=df)
ax.set_title('前10名出現的詞')
plt.show()

# Words=[]
# for i in range(0,10):
#     Words.append(word_counts_top10[i][0])

# Sta=[]
# for i in range(0,10):
#     Sta.append(word_counts_top10[i][1])

# x = np.arange(len(Words))

# plt.bar(x, Sta, color=['red', 'green', 'blue', 'yellow','red', 'green', 'blue', 'yellow','red', 'green'])
# plt.xticks(x, Words)
# plt.xlabel('字詞')
# plt.ylabel('出現頻率')
# plt.show()