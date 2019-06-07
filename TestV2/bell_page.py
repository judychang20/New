def bell_page(x, y, z):
	font1 = pg.font.SysFont("myfont.ttf", 56)
	Time = 1
	if x < 500 and Time != 5:
		Picture("第四頁背景.png", 0, 0, 1280, 720, bg).buildup()
		Picture("左搖.png", 100, 50, 700, 700, bg).buildup()
		Time += 1
	elif x > 500 and Time != 5:
		Picture("第四頁背景.png", 0, 0, 1280, 720, bg).buildup()
		Picture("右搖.png", 500, 50, 700, 700, bg).buildup()
		Time += 1
	else :
		Picture("第四頁背景.png", 0, 0, 1280, 720, bg).buildup()
		Picture("左搖.png", 100, 50, 700, 700, bg).buildup()
		Picture("視窗.png", 190, 150, "尺寸", "尺寸", bg).buildup()
		result0 = "隨機結果"
		result = Word(font1, result0, 560, 230, bg, (0, 0, 0)).buildup()
		Picture("確定.png", 682, 348, 310, 110, bg).buildup()