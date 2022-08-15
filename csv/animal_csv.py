# from bs4 import BeautifulSoup
# # from matplotlib.font_manager import json_dump 
# import requests
# from soupsieve import select, select_one
# import csv
# import time
# import json

# with open("專題資料.csv", "a+", encoding="utf-8",newline='') as fp:
#     writer = csv.writer(fp)
#     try:
#         for i in range(3000,3699):
#                 list=[]
#                 LIST =[]
#                 url = "https://www.afurkid.com/Adoption/Details?id=7{}".format(i)
#                 html = requests.get(url).text
#                 soup = BeautifulSoup(html, 'html.parser')
#                 animal = soup.find_all("li",class_="d-flex align-items-baseline g-mb-12")
#                 # print(animal)
#                 for n in animal:
#                     name= n.find("span").text
#                     Name = (("屬性: ") + name )
#                     # print(Name)
#                 info = soup.find_all("li",class_="d-flex align-items-baseline g-mb-10")
#                 # print(info)
#                 for t in info:
#                     type= t.find("span").text.strip()
#                     # print(type)
#                     list.append(type)
#                 TYPE = list[0]
#                 GENDER = list[1]
#                 BODY = list[2]
#                 COLOR = list[3]
#                 AGE = list[4]
#                 LIGRATION =list[5]
#                 VACCINE = list[6]

#                 p = soup.find_all("span" ,itemprop="name")
#                 place = p[2].text
#                 Place = ("地點: " + place)
#                 # print(Place)

#                 LIST=[Name,TYPE,GENDER,BODY,COLOR,AGE,LIGRATION,VACCINE,Place]
#                 print(LIST)
#                 # fp.write(List)
#                 writer.writerows([LIST])
#                 time.sleep(3)
#     except:
#         pass 

from bs4 import BeautifulSoup
# from matplotlib.font_manager import json_dump 
import requests
from soupsieve import select, select_one
import csv
import time
import json

with open("已更新專題資料.csv", "a+", encoding="utf-8",newline='') as fp:
    writer = csv.writer(fp)
    try:
        for i in range(3563,3726):
                list=[]
                LIST =[]
                url = "https://www.afurkid.com/Adoption/Details?id=7{}".format(i)
                html = requests.get(url).text
                soup = BeautifulSoup(html, 'html.parser')
                animal = soup.find_all("li",class_="d-flex align-items-baseline g-mb-12")
                # print(animal)
                for n in animal:
                    name= n.find("span").text
                    Name = (("屬性: ") + name )
                    # print(Name)
                info = soup.find_all("li",class_="d-flex align-items-baseline g-mb-10")
                # print(info)
                for t in info:
                    type= t.find("span").text.strip()
                    # print(type)
                    list.append(type)
                TYPE = list[0]
                GENDER = list[1]
                BODY = list[2]
                COLOR = list[3]
                AGE = list[4]
                LIGRATION =list[5]
                VACCINE = list[6]

                p = soup.find_all("span" ,itemprop="name")
                place = p[2].text
                Place = ("地點: " + place)
                # print(Place)
                results = soup.find_all("img",alt="領養")
                # print(results)
                for a in results:
                # print(a["src"])
                    a["src"] = "<7{}>".format(i),a['src']
                    PHOTOsite = a["src"]

                LIST=[Name,TYPE,GENDER,BODY,COLOR,AGE,LIGRATION,VACCINE,Place,PHOTOsite]
                # print(LIST)
                # fp.write(List)
                writer.writerows([LIST])
                print("<7{}>".format(i))
                time.sleep(3)
    except:
        pass 