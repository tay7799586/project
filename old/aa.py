# from bs4 import BeautifulSoup
# import requests
# from soupsieve import select, select_one
# import csv
# import time
# import json

# url = "https://www.afurkid.com/Adoption/List"
# html = requests.get(url).text
# soup = BeautifulSoup(html, 'html.parser')
# items = soup.find_all('img', alt="Image Description")
# print(items)
# for p in items:
#         site = p.find("img","src")
#         print(site)

# photo = soup.find_all("img" ,class_="g-width-200 g-height-200 rounded-circle g-mb-30")
# # print(photo)
# for p in photo:
#     Photo=p.find("img",alt="Image Description").get("src")
#     print(Photo)
from bs4 import BeautifulSoup
import requests
from soupsieve import select, select_one
import csv
import time
import json
import os
with open("圖片網址.csv", "a+", encoding="utf-8",newline='') as fp:
    writer = csv.writer(fp)
    try:
        for b in range(3251,3699):
            LIST =[]
            response = requests.get("https://www.afurkid.com/Adoption/Details?id=7{}".format(b))
            soup = BeautifulSoup(response.text, "html.parser")
            results = soup.find_all("img",alt="領養")
                # print(results)
            for a in results:
                # print(a["src"])
                a["src"] = "<7{}>".format(b),a['src']
            LIST.append(a["src"])
            writer.writerows([LIST])
            print("<7{}>".format(b))
            time.sleep(3)
    except:
        pass
# print(photosite)
# if not os.path.exists("images"):
#                 os.mkdir("images")  # 建立資料夾
#                 print(image_links)
# for link in (image_links):
#                     print(link)
#                     img = requests.get(link)
#                     with open(path,'wb') as f:
#                         f.write(img.content)