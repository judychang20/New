elif aspot.open1 == "不開放" and "；" in aspot.open2:
    not_open = "星期一不開放"
    Word(font1, not_open, 100, 300, bg, (0, 0, 0)).buildup()
    Word(font1, "其餘時間：", 100, 340, bg, (0, 0, 0)).buildup()
    a = aspot.open2.split("；")
    for i in range(len(a)):
        b = 340 + 40*i
        result = "  " + str(a[i])
        Word(font1, result, 100, b, bg, (0, 0, 0)).buildup()