import csv
import pandas as pd

with open("已更新專題資料.csv","r",encoding="utf-8" ,newline='') as fp:
    data =[]
    CAT =[]
    DOG =[]
    # readerr  = csv.reader(fp)
    readerr = csv.DictReader(fp)
    
    for i in readerr:
        data.append(i["品種"])
    for cat in data:
        # print(cat)
        if cat == str("品種：混種貓"):
            CAT.append(cat)
        else:
            DOG.append(cat)
    print(len(CAT))
    print(len(DOG))