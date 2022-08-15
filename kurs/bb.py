tem = int(input("溫度: "))
hum = int(input("濕度: "))
wea = str(input( "天氣是否多雲(輸入是or否): "))
x = "適合打球~ "
y = "不適合打球 :( "

if tem > 25:

    if hum  >=58:

        if wea == "多雲":
            print(x)

    else:
        print(y)

else:
    if wea == "是" or  wea == "否" :
        print(x)

    else:
        print(y)