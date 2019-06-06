import pygame as pg
import random
import csv

class Word:

	def __init__(self, font, context, xplace, yplace, surface, color):
		self.font = font
		self.context = context
		self.xplace = xplace
		self.yplace = yplace
		self.surface = surface
		self.color = color

	def buildup(self):
		a = self.font.render(self.context, True, self.color)
		self.surface.blit(a, (self.xplace, self.yplace))
		
	def x_move(self, x_bound):
		a = self.font.render(self.context, True, self.color)
		for i in range(self.xplace, x_bound):
			self.surface.blit(a, (i, self.yplace))

class Button:

	def __init__(self, darkimage, lightimage, xplace, yplace, surface, xsize, ysize, word, alpha):
		self.darkimage = darkimage
		self.lightimage = lightimage
		self.xplace = xplace
		self.yplace = yplace
		self.surface = surface
		self.xsize = xsize
		self.ysize = ysize
		self.word = word
		self.alpha = alpha

	def WaitToMouseOver(self):
		a = pg.image.load(self.darkimage).convert()
		a.set_alpha(self.alpha)
		b = pg.transform.scale(a, (self.xsize, self.ysize)).convert()
		self.surface.blit(b, (self.xplace, self.yplace))
		Word.buildup(self.word)

	def MouseOver(self):
		a = pg.image.load(self.lightimage)
		a.set_alpha(self.alpha)
		b = pg.transform.scale(a, (self.xsize, self.ysize)).convert()
		self.surface.blit(b, (self.xplace, self.yplace))
		Word.buildup(self.word)

	def isOver(self, x, y, z, k , theme):
		global Cum , atheme
		if self.xplace <  x < self.xplace + self.xsize and self.yplace < y < self.yplace + self.ysize:
			self.MouseOver()
			if z == pg.MOUSEBUTTONDOWN:
				Cum = k
				atheme = theme
		return Cum ,atheme

	def isOver_spot(self, x, y, z, k , dist):
		global Cum , adist
		if self.xplace <  x < self.xplace + self.xsize and self.yplace < y < self.yplace + self.ysize:
			self.MouseOver()
			if z == pg.MOUSEBUTTONDOWN:
				Cum = k
				adist = dist
				print(adist)
		return Cum , adist

				
class Picture:

	def __init__(self, picture, xplace, yplace, xsize, ysize, surface):
		self.picture = picture
		self.xplace = xplace
		self.yplace = yplace
		self.xsize = xsize
		self.ysize = ysize
		self.surface = surface

	def buildup(self):
		a = pg.image.load(self.picture)
		b = pg.transform.scale(a, (self.xsize, self.ysize))
		self.surface.blit(b, (self.xplace, self.yplace))
		pg.display.update()

	def x_move(self, x_bound):
		a = pg.image.load(self.picture)
		b = pg.transform.scale(a, (self.xsize, self.ysize))
		for i in (x_place, x_bound):
			self.surface.blit(b, (i, self.yplace))

	def choose(self, x, y, z):
		if self.xplace < x < self.xplace + self.xsize and self.yplace < y < self.yplace + self.ysize:
			if z == pg.MOUSEBUTTONDOWN:
				return True	

class Window:

	def __init__(self, width, height, caption, icon):
		self.width = width
		self.height = height
		self.caption = caption
		self.icon = icon
		self.screen = pg.display.set_mode((self.width, self.height))

	def setup(self):
		pg.init()
		pg.display.set_caption(self.caption)
		bg = pg.Surface(self.screen.get_size()).convert()
		icon_image = pg.image.load(self.icon).convert()
		pg.display.set_icon(icon_image)
		return bg

	def bulidup(self):
		self.screen.blit(Window.setup(self), (0,0))
		pg.display.update()


class Spot:

	def __init__(self, distinct, theme, name, intro, address, ticket, open1, open2, open3, open4, open5, open6, open7):
		self.distinct = distinct
		self.theme = theme
		self.name = name
		self.intro = intro
		self.address = address
		self.ticket = ticket
		self.open1 = open1
		self.open2 = open2
		self.open3 = open3
		self.open4 = open4
		self.open5 = open5
		self.open6 = open6
		self.open7 = open7



def Main(circumstance, x, y, z):
	if circumstance == 0:
		welcome_page(x, y, z)
	if circumstance == 1:
		test_noidea_page(x, y, z)
	if circumstance == 2:
		test_haveidea_page(x, y, z)
	if circumstance == 3:
		compare_page(x, y, z)
	if circumstance == 4:
		compare_lose_page(x, y, z)
	if circumstance == 5:
		compare_win_page(x, y, z)
	if circumstance == 6:
		roulette_page(x, y, z)	
	if circumstance == 7:
		spotintro_page(x, y, z)
	if circumstance == 8:
		choosedict_page(x, y, z)

def welcome_page(x, y, z):
	font1 = pg.font.Font("myfont.ttf", 56)
	font2 = pg.font.Font("myfont.ttf", 25)
	Picture("第一頁背景.png", 0, 0, 1280, 720, bg).buildup()
	Word(font1, "標題標題標題", 475, 100, bg, (0,0,0)).buildup()
	Word(font2, "今天要去哪裡玩？", 540, 275, bg, (0,0,0)).buildup()
	word1 = Word(font2, "我要去___區", 570, 375, bg, (255,255,255))
	a = Button("真亮按鈕.png", "按鈕.png", 330, 350, bg, 624, 82, word1, 200)
	a.WaitToMouseOver()
	a.isOver(x, y, z, 8, "")
	word2 = Word(font2, "我還沒有想法", 570, 505, bg, (255,255,255))
	b = Button("真亮按鈕.png", "按鈕.png", 330, 480, bg, 624, 82, word2, 200)
	b.WaitToMouseOver()
	b.isOver(x, y, z, 1, "")


def test_noidea_page(x, y, z):
	global Controller2, alist
	if Controller2 == 0:
		alist = psycho_test()
		Controller2 = 1
	font1 = pg.font.Font("myfont.ttf", 35)
	font2 = pg.font.Font("myfont.ttf", 23)
	Picture("第二頁背景.png", 0, 0, 1280, 720, bg).buildup()
	Question = alist[0]
	OptionA = alist[1]
	OptionB = alist[2]
	OptionC = alist[3]
	OptionD = alist[4]
	Word(font1, Question, 90, 50, bg, (0, 0, 0)).buildup()
	option1 = Word(font2, OptionA, 130, 190, bg, (255, 255, 255))
	option2 = Word(font2, OptionB, 130, 323, bg, (255, 255, 255))
	option3 = Word(font2, OptionC, 130, 456, bg, (255, 255, 255))
	option4 = Word(font2, OptionD, 130, 590, bg, (255, 255, 255))
	a = Button("亮按鈕.png", "選項.png", 110, 160, bg, 1000, 100, option1, 200)
	a.WaitToMouseOver()
	b = Button("亮按鈕.png", "選項.png", 110, 293, bg, 1000, 100, option2, 200)
	b.WaitToMouseOver()
	c = Button("亮按鈕.png", "選項.png", 110, 426, bg, 1000, 100, option3, 200)
	c.WaitToMouseOver()
	d = Button("亮按鈕.png", "選項.png", 110, 560, bg, 1000, 100, option4, 200)
	d.WaitToMouseOver()
	a.isOver(x, y, z, 6, "宗教與古蹟")
	b.isOver(x, y, z, 6, "藝文與文化")
	c.isOver(x, y, z, 6, "休閒與生態")
	d.isOver(x, y, z, 6, "商圈")


def test_haveidea_page(x, y, z):
	global Controller2, alist
	if Controller2 == 0:
		alist = psycho_test()
		Controller2 = 1
	font1 = pg.font.Font("myfont.ttf", 35)
	font2 = pg.font.Font("myfont.ttf", 23)
	Picture("第二頁背景.png", 0, 0, 1280, 720, bg).buildup()
	Question = alist[0]
	OptionA = alist[1]
	OptionB = alist[2]
	OptionC = alist[3]
	OptionD = alist[4]
	Word(font1, Question, 90, 50, bg, (0, 0, 0)).buildup()
	option1 = Word(font2, OptionA, 130, 190, bg, (255, 255, 255))
	option2 = Word(font2, OptionB, 130, 323, bg, (255, 255, 255))
	option3 = Word(font2, OptionC, 130, 456, bg, (255, 255, 255))
	option4 = Word(font2, OptionD, 130, 590, bg, (255, 255, 255))
	a = Button("亮按鈕.png", "選項.png", 110, 160, bg, 1000, 100, option1, 200)
	a.WaitToMouseOver()
	b = Button("亮按鈕.png", "選項.png", 110, 293, bg, 1000, 100, option2, 200)
	b.WaitToMouseOver()
	c = Button("亮按鈕.png", "選項.png", 110, 426, bg, 1000, 100, option3, 200)
	c.WaitToMouseOver()
	d = Button("亮按鈕.png", "選項.png", 110, 560, bg, 1000, 100, option4, 200)
	d.WaitToMouseOver()
	a.isOver(x, y, z, 3, "宗教與古蹟")
	b.isOver(x, y, z, 3, "藝文與文化")
	c.isOver(x, y, z, 3, "休閒與生態")
	d.isOver(x, y, z, 3, "商圈")

def compare_page(x, y, z):
	global Controller3, Place, spotlist, Controller4
	font1 = pg.font.Font("myfont.ttf", 25)
	Picture("第四頁背景.png", 0, 0, 1280, 720, bg).buildup()
	if Controller3 == 0:
		spotlist = recommend_know(adist[0:2], atheme)
		Controller3 = 1
		print(spotlist)
	C = Word(font1, spotlist[0], 250, 500, bg, (0, 0, 0))
	D = Word(font1, spotlist[1], 950, 500, bg, (0, 0, 0))
	if Controller4 < 2:
		E = Button("選擇卡.png", "選擇卡.png", 100, 100,bg, 400, 500, C, 250)
		E.WaitToMouseOver()
		E.isOver(x, y, z, 7,"")
		F = Button("選擇卡.png", "選擇卡.png", 800, 100,bg, 400, 500, D, 250)
		F.WaitToMouseOver()
		E.isOver(x, y, z, 7, "")
		print(Controller4)
	aspot = location[32]

	#Place = 0
	#local1 = Place
	#A = Word(font1, spotlist[local1], 250, 500, bg, (0, 0, 0))
	#Place = 1
	#local2 = Place
	#B = Word(font1, spotlist[local2], 950, 500, bg, (0, 0, 0))
	#a = Button("選擇卡.png", "選擇卡.png", 100, 100,bg, 400, 500, A,250)
	#a.WaitToMouseOver()
	#b = Button("選擇卡.png", "選擇卡.png", 800, 100,bg, 400, 500, B, 250)
	#b.WaitToMouseOver()
	#a.isOver(x, y, z , 4,"")
	#b.isOver(x, y, z, 4, "")



	
	

def compare_lose_page(x, y ,z):
	# font1 = pg.font.SysFont("myfont.ttf", 35)
	# font2 = pg.font.SysFont("myfont.ttf", 23)
	Picture("第五頁背景.png", 0, 0, 1280, 720, bg).buildup()
	# a = Picture("選擇卡.png", 100, 100, 400, 500, bg).buildup()
	# b = Picture("選擇卡.png", 800, 100, 400, 500, bg).buildup()
	# if a.choose(x, y, z):
		# a.x_move(-500).buildup()
	# elif b.choose(x, y, z):
		# b.x_move(1300).buildup()

# def compare_win_page():
	# font1 = pg.font.SysFont("myfont.ttf", 35)
	# font2 = pg.font.SysFont("myfont.ttf", 23)
	# Picture("第四頁背景.png", 0, 0, 1280, 720, bg).buildup()
	# if Picture("選擇卡.png", 100, 100, 400, 500, bg).choose(x, y, z) == True:
		# Picture("選擇卡.png", 100, 100, 400, 500, bg).x_move(#中間)
		# Picture("選擇卡.png", 800, 100, 400, 500, bg).buildup()
	# if Picture("選擇卡.png", 800, 100, 400, 500, bg).choose(x, y, z) == True:
		# Picture("選擇卡.png", 800, 100, 400, 500, bg).x_move(#中間)
		# Picture("選擇卡.png", 100, 100, 400, 500, bg).buildup()

def roulette_page(x, y, z):
	global Cir, Time, Controller, adist, aspot, location
	if Cir == 0 and Time < 10:
		Picture("第三頁背景.png", 0, 0, 1280, 720, bg).buildup()
		roulette_image0 = pg.image.load("roulette.png")
		roulette_image = pg.transform.scale(roulette_image0, (1150, 1150)).convert_alpha()
		bg.blit(roulette_image, (50, 150))
		pg.draw.polygon(bg, (0, 0, 0), ((580, 50), (680, 50), (630, 260)))
		Time += 1
		Cir = 1
		window.screen.blit(bg, (0, 0))
		pg.display.update()
	elif Cir == 1 and Time < 10:
		Picture("第三頁背景.png", 0, 0, 1280, 720, bg).buildup()
		roulette_image0 = pg.image.load("roulette.png")
		roulette_image = pg.transform.scale(roulette_image0, (1150, 1150)).convert_alpha()
		a = pg.transform.rotate(roulette_image, 160)
		bg.blit(a, (-110, -11))
		pg.draw.polygon(bg, (0, 0, 0), ((580, 50), (680, 50), (630, 260)))
		Time += 1
		Cir = 0
		window.screen.blit(bg, (0, 0))
		pg.display.update()
	elif Time == 10:
		font1 = pg.font.Font("myfont.ttf", 45)
		font2 = pg.font.Font("myfont.ttf", 56)

		if Controller == 0:
			adist = random.choice(["大安區","萬華區","士林區","中正區","文山區","南港區","大同區", "中山區", "松山區", "信義區","北投區", "內湖區"])
			aspot = recommend_notknow(adist[0:2], atheme)
			Controller = 1
		#print(atheme)
		word1 = Word(font1, "確定", 790, 370, bg, (0, 0, 0))
		Picture("視窗2.png", 190, 150, 884, 350, bg).buildup()
		Word(font2, adist, 560, 230, bg, (0, 0, 0)).buildup()
		a = Button("確定暗.png", "確定亮.png", 682, 348, bg, 310, 110, word1, 250)
		a.WaitToMouseOver()
		a.isOver(x, y, z, 7, "")





def spotintro_page(x, y, z):
	global Time, Cir, Controller, adist, location, aspot, Controller2, Controller3, Place, Controller4
	font1 = pg.font.Font("myfont.ttf", 20)
	font2 = pg.font.Font("myfont.ttf", 33)
	font3 = pg.font.Font("myfont.ttf", 29)
	font4 = pg.font.Font("myfont.ttf", 17)
	Picture("第五頁背景.png", 0, 0, 1280, 720, bg).buildup()
	Picture("placeholder.png", 25, 110, 48, 48, bg).buildup()
	Picture("tickets.png", 25, 165, 48, 48, bg).buildup()
	Picture("001-time.png", 27, 245, 45, 45, bg).buildup()
	Picture("002-picture.png", 25, 580, 48, 48, bg).buildup()
	spot = aspot.name
	address = aspot.address
	ticket = "門票："+ aspot.ticket
	if len(aspot.name) > 9:
		Word(font3, spot, 50, 30, bg, (0, 0, 0)).buildup()
	else:
		Word(font2, spot, 50, 30, bg, (0, 0, 0)).buildup()
	if len(aspot.address) > 16:
		Word(font1, address[0:16], 80, 110, bg, (0, 0, 0)).buildup()
		Word(font1, address[16:], 80, 130, bg, (0, 0, 0)).buildup()
	else:
		Word(font1, address, 80, 120, bg, (0, 0, 0)).buildup()
	Word(font1, ticket, 80, 175, bg, (0, 0, 0)).buildup()
	Word(font1, "營業時間", 80, 255, bg, (0, 0, 0)).buildup()
	Word(font1, "圖片來源", 80, 590, bg, (0, 0, 0)).buildup()
	Word(font1, "臺北旅遊網等網路資源", 90, 640, bg, (0, 0, 0)).buildup()
	picture = "/Users/arcwarriors/Documents/GitHub/New/picture/" + aspot.distinct + "/" + aspot.name + ".jpg"
	Picture(picture, 540,50, 640, 360, bg).buildup()
	
	#輸出營業時間
	week_list = ["(一)", "(二)", "(三)", "(四)", "(五)", "(六)", "(日)"]#輸出營業時間
	time_list = [aspot.open1, aspot.open2, aspot.open3, aspot.open4, aspot.open5, aspot.open6, aspot.open7]
	for i in range(7):
		a = 300 + 40*i
		opentime = week_list[i] + " : " + time_list[i]
		Word(font1, opentime, 100, a, bg, (0, 0, 0)).buildup()

	#輸出介紹文字	
	introduce_list = []
	if  30 <= len(aspot.intro) < 62:
		introduce_list.append("      " + aspot.intro[0:30])
		introduce_list.append(aspot.intro[30:])
	elif 62<= len(aspot.intro) < 94:
		introduce_list.append("      " + aspot.intro[0:30])
		introduce_list.append(aspot.intro[30:62])
		introduce_list.append(aspot.intro[62:])
	elif 94 <= len(aspot.intro) < 128:
		introduce_list.append("      " + aspot.intro[0:30])
		introduce_list.append(aspot.intro[30:62])
		introduce_list.append(aspot.intro[62:94])
		introduce_list.append(aspot.intro[94:])
	elif len(aspot.intro) > 128:
		introduce_list.append("      " + aspot.intro[0:30])
		introduce_list.append(aspot.intro[30:62])
		introduce_list.append(aspot.intro[62:94])
		introduce_list.append(aspot.intro[94:126])
		introduce_list.append(aspot.intro[126:])
	for j in range(len(introduce_list)):
		b = 450 + 30*j
		Word(font1, introduce_list[j], 540, b, bg, (0, 0, 0)).buildup()

	# no_word = Word(font2, " ", 1000, 600, bg, (255, 255, 255))
	# a = Button("亮再玩一次.png", "再玩一次.png", 1000, 600, bg, 207, 72, no_word, 200)
	# a.WaitToMouseOver()
	# a.isOver(x, y, z, 0)

	font1 = pg.font.Font("myfont.ttf", 25)
	word1 = Word(font1, "再玩一次", 1055, 620, bg, (0, 0, 0))
	a = Button("確定暗.png", "確定亮.png", 1000, 600, bg, 207, 72, word1, 250)
	a.WaitToMouseOver()
	a.isOver(x, y, z, 0, "")
	Time = 0
	Cir = 0
	Controller = 0
	adist = ""
	location = []
	Controller2 = 0
	Controller3 = 0
	Place = 0
	Controller4 = 0

def choosedict_page(x, y, z):
	Picture("區選單2.png", 50, 70, 1168, 570, bg).buildup()
	dict("大安區", 190, 225, 111, 205, x, y, z)
	dict("中正區", 190, 323, 111, 303, x, y, z)
	dict("萬華區", 190, 420, 111, 400, x, y, z)
	dict("士林區", 455, 225, 375, 205, x, y, z)
	dict("內湖區", 455, 323, 375, 303, x, y, z)
	dict("大同區", 455, 420, 375, 400, x, y, z)
	dict("文山區", 720, 225, 638, 205, x, y, z)
	dict("北投區", 720, 323, 638, 303, x, y, z)
	dict("南港區", 720, 420, 638, 400, x, y, z)
	dict("信義區", 985, 225, 903, 205, x, y, z)
	dict("中山區", 985, 323, 903, 303, x, y, z)
	dict("松山區", 985, 420, 903, 400, x, y, z)
	font1 = pg.font.Font("myfont.ttf", 35)
	word1 = Word(font1, "返回", 1015, 535, bg, (0, 0, 0))
	a = Button("確定暗.png", "確定亮.png", 959, 517, bg, 182, 82, word1, 250)
	a.WaitToMouseOver()
	a.isOver(x, y, z, 0, "")




def dict(name, xnameplace, ynameplace, xbuttonplace, ybuttonplace, x, y, z):
	font2 = pg.font.Font("myfont.ttf", 23)
	word1 = Word(font2, name, xnameplace, ynameplace, bg, (0, 0, 0))
	dict1 = Button("區按鈕.png", "亮區按鈕.png", xbuttonplace, ybuttonplace, bg, 238, 75, word1, 250)
	dict1.WaitToMouseOver()
	dict1.isOver_spot(x, y, z, 2, name)


def recommend_know(dist, theme):
	'''
    知道去哪裡所回傳的景點
    需要傳入的值: 行政區、心理測驗的主題結果
    '''
	fh1 = '完整景點資料庫.csv'
	fh1 = open(fh1, 'r', encoding='utf-8', newline='')
	csv1 = csv.reader(fh1)
	reader = csv.DictReader(fh1)

	data = {}
	spot = []
	for row in reader:
		if row["行政區"] == dist:
			if row["主題"] not in data:
				data[row["主題"]] = [row["景點名稱"]]
			else:
				data[row["主題"]].append(row["景點名稱"])

	#print(data)
	count = 0
	for item in range(len(data[theme])):  # 隨機輸出兩兩比較
		if count == 0:  # 第一輪抽出兩個景點
			data_item = random.choice(data[theme])
			data[theme].remove(data_item)
			ano_item = random.choice(data[theme])
			data[theme].remove(ano_item)
			print(data_item, ano_item)
			count += 1
			spot.append(data_item)
			spot.append(ano_item)


		elif len(data[theme]) > 0:  # 其他輪抽出一個景點
			data_item = random.choice(data[theme])
			data[theme].remove(data_item)
			spot.append(data_item)
	return spot



def recommend_notknow(dist, theme):
	'''
    不知道去哪裡所回傳的景點
    需要傳入的值: 心理測驗的主題結果、輪盤的行政區
    '''
	fh1 = '完整景點資料庫.csv'
	fh1 = open(fh1, 'r', encoding='utf-8', newline='')
	csv1 = csv.reader(fh1)
	#reader = csv.DictReader(fh1)

	for a in csv1:
		location.append(Spot(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10], a[11], a[12]))
	speciallocation = []
	#print(location)
	for data in location:
		#if row["行政區"] == dist and row["主題"] == theme:
			#location.append(row["景點名稱"])
			#print(location)
		if data.distinct == dist and data.theme == theme:
			speciallocation.append(data)
	location_item = random.choice(speciallocation)
	#print(speciallocation)
	return location_item


def psycho_test():

	fh2 = '心理測驗.csv'
	fh2 = open(fh2, 'r', encoding='utf-8', newline='')
	csv2 = csv.reader(fh2)
	reader2 = csv.DictReader(fh2)

	for a in csv2:
		Test.append([a[0], a[1], a[2], a[3], a[4]])
	atest = random.choice(Test)
	return atest


window = Window(1280, 720, "標題標題", "icon.png")
bg = window.setup()
Cum = 0
Cir = 0
Time = 0
Controller = 0
Controller2 = 0
Controller3 = 0
Controller4 = 0
adist = ""
aspot = ""
atheme = ""
alist = []
location = []
Test = []
Place = 0
spotlist =[]

fh1 = '完整景點資料庫.csv'
fh1 = open(fh1, 'r', encoding='utf-8', newline='')
csv1 = csv.reader(fh1)
reader = csv.DictReader(fh1)

for a in csv1:
	location.append(Spot(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10], a[11], a[12]))

fh2 = '心理測驗.csv'
fh2 = open(fh2, 'r', encoding='utf-8', newline='')
csv2 = csv.reader(fh2)
reader2 = csv.DictReader(fh2)

for a in csv2:
	Test.append([a[0], a[1], a[2], a[3], a[4]])

#print(location[0].name)



running = True
while running:
	mouse = pg.mouse.get_pos()

	for event in pg.event.get():
		Main(Cum, mouse[0], mouse[1], event.type)
		if event.type == pg.QUIT:
			running = False
		else:
			window.screen.blit(bg, (0,0))
			pg.display.update()

pg.quit()







