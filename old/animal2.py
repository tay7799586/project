from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import jieba
from collections import Counter
# url = "https://www.businessweekly.com.tw/style/blog/8524"
# html = requests.get(url)
# html.encoding = 'UTF-8'
# sp = BeautifulSoup(html.text, 'html.parser')
# data = []
# for a in sp.find_all("p"):
#     a = a.text+"\n"
#     # print(a)
#     data.append(a)
# with open("3.txt", "w", encoding="utf-8", newline="") as fp:
#     for b in data:
#         fp.write(b)
data=[]
with open("2.txt", "r", encoding="utf-8") as fp:
    for word in fp.readlines():
        main = word.strip() 
        data.append(main)
data = ",".join(data)
jieba.load_userdict("dict2.txt")

# keyterms = [keyterm for keyterm in jieba.cut(data) ]
with open('stopwords.txt', 'rt', encoding='utf-8') as fp:
    stopwords = [word.strip() for word in fp.readlines()]

keyterms = [keyterm for keyterm in jieba.cut(data) 
            if keyterm not in stopwords 
                and keyterm.strip()!=""
                and keyterm.strip()!=","
                and keyterm.strip()!="◎"]
text = ",".join(keyterms)
print(text)

mask = np.array(Image.open('cloud.jpg'))
wordcloud = WordCloud(background_color="white",
                      width=1000, height=850, 
                      margin=2, font_path="simhei.ttf", 
                      mask=mask).generate(text)
plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()