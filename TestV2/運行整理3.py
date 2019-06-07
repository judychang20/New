import pygame as pg

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

	def isOver(self, x, y, z, k):
		global Cum
		if self.xplace <  x < self.xplace + self.xsize and self.yplace < y < self.yplace + self.ysize:
			self.MouseOver()
			if z == pg.MOUSEBUTTONDOWN:
				Cum = k
		return Cum

				
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
				Flag = True
		return Flag

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
	font1 = pg.font.SysFont("myfont.ttf", 56)
	font2 = pg.font.SysFont("myfont.ttf", 25)
	Picture("第一頁背景.png", 0, 0, 1280, 720, bg).buildup()
	Word(font1, "標題標題標題", 475, 100, bg, (0,0,0)).buildup()
	Word(font2, "今天要去哪裡玩？", 540, 275, bg, (0,0,0)).buildup()
	word1 = Word(font2, "我要去___區", 570, 375, bg, (255,255,255))
	a = Button("真亮按鈕.png", "按鈕.png", 330, 350, bg, 624, 82, word1, 200)
	a.WaitToMouseOver()
	a.isOver(x, y, z, 3)
	word2 = Word(font2, "我還沒有想法", 570, 505, bg, (255,255,255))
	b = Button("真亮按鈕.png", "按鈕.png", 330, 480, bg, 624, 82, word2, 200)
	b.WaitToMouseOver()
	b.isOver(x, y, z, 1)


def test_noidea_page(x, y, z):
	font1 = pg.font.SysFont("myfont.ttf", 35)
	font2 = pg.font.SysFont("myfont.ttf", 23)
	Picture("第二頁背景.png", 0, 0, 1280, 720, bg).buildup()
	Question = "選出現在最符合你的一句話"
	OptionA = "好熱好累好不想做事，好想躺在床上度過一整天"
	OptionB = "被都市的喧囂所埋沒的社畜，每天漫無目的地遊走"
	OptionC = "隨時調整心態，面對突如其來的挑戰"
	OptionD = "太陽從東邊升起，從西邊落下"
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
	a.isOver(x, y, z, 6)
	b.isOver(x, y, z, 6)
	c.isOver(x, y, z, 6)
	d.isOver(x, y, z, 6)


def test_haveidea_page(x, y, z):
	font1 = pg.font.SysFont("myfont.ttf", 35)
	font2 = pg.font.SysFont("myfont.ttf", 23)
	Picture("第二頁背景.png", 0, 0, 1280, 720, bg).buildup()
	Question = "選出現在最符合你的一句話"
	OptionA = "好熱好累好不想做事，好想躺在床上度過一整天"
	OptionB = "被都市的喧囂所埋沒的社畜，每天漫無目的地遊走"
	OptionC = "隨時調整心態，面對突如其來的挑戰"
	OptionD = "太陽從東邊升起，從西邊落下"
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
	a.isOver(x, y, z, 3)
	b.isOver(x, y, z, 3)
	c.isOver(x, y, z, 3)
	d.isOver(x, y, z, 3)

def compare_page(x, y ,z):
	font1 = pg.font.SysFont("myfont.ttf", 25)
	Picture("第四頁背景.png", 0, 0, 1280, 720, bg).buildup()
	Spot1 = "龍山寺"
	Spot2 = "西門紅樓"
	spot1 = Word(font1, Spot1, 150, 500, bg, (0, 0, 0)).buildup()
	spot2 = Word(font1, Spot2, 850, 500, bg, (0, 0, 0)).buildup()
	a = Picture("選擇卡.png", 100, 100, 400, 500, bg).buildup()
	b = Picture("選擇卡.png", 800, 100, 400, 500, bg).buildup()


def roulette_page(x, y, z):



def spotintro_page(x, y, z):
	font1 = pg.font.SysFont("myfont.ttf", 20)
	Picture("第五頁背景.png", 0, 0, 1280, 720, bg).buildup()
	Picture("placeholder.png", 25, 110, 48, 48, bg).buildup()
	Picture("tickets.png", 25, 165, 48, 48, bg).buildup()
	Picture("001-time.png", 27, 245, 45, 45, bg).buildup()
	Picture("002-picture.png", 25, 580, 48, 48, bg).buildup()
	spot = "景點名"
	address = "地址"
	ticket = "門票"
	Word(font1, spot, 50, 30, bg, (0, 0, 0)).buildup()
	Word(font1, address, 80, 120, bg, (0, 0, 0)).buildup()
	Word(font1, ticket, 80, 175, bg, (0, 0, 0)).buildup()
	Word(font1, "營業時間", 80, 255, bg, (0, 0, 0)).buildup()
	Word(font1, "圖片來源", 80, 590, bg, (0, 0, 0)).buildup()
	Word(font1, "網路資源", 90, 640, bg, (0, 0, 0)).buildup()
	picture = "第一頁背景.png"#景點圖片
	Picture(picture, 540,50, 640, 360, bg).buildup()
	
	#輸出營業時間
	week_list = ["(一)", "(二)", "(三)", "(四)", "(五)", "(六)", "(日)"]#輸出營業時間
	#time_list = []
	for i in range(7):
		y = 300 + 40*i
		opentime = week_list[i] + ":" + "9:00 - 17:30"
		Word(font1, opentime, 100, y, bg, (0, 0, 0)).buildup()

	#輸出介紹文字	
	introduce_list = ["      木柵市場被作家劉克襄譽為台北盆地的清明上河圖，其生鮮食材來源",
	"除了周遭貓空、草湳山區的農作，石碇、深坑、平溪的產品，甚至宜蘭員",
	"山絲瓜、三星蔥皆由產地直銷而來。此外市場內外的美食也是不可錯過的",
	"去處。"]
	for j in range(4):
		y = 450 + 30*j
		Word(font1, introduce_list[j], 540, y, bg, (0, 0, 0)).buildup()

	# no_word = Word(font2, " ", 1000, 600, bg, (255, 255, 255))
	# a = Button("亮再玩一次.png", "再玩一次.png", 1000, 600, bg, 207, 72, no_word, 200)
	# a.WaitToMouseOver()
	# a.isOver(x, y, z, 0)

def choosedict_page(x, y, z):
	font2 = pg.font.SysFont("myfont.ttf", 23)
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



def dict(name, xnameplace, ynameplace, xbuttonplace, ybuttonplace, x, y, z):
	font2 = pg.font.SysFont("myfont.ttf", 23)
	word1 = Word(font2, name, xnameplace, ynameplace, bg, (0, 0, 0))
	dict1 = Button("區按鈕.png", "亮區按鈕.png", xbuttonplace, ybuttonplace, bg, 238, 75, word1, 250)
	dict1.WaitToMouseOver()
	dict1.isOver(x, y, z, 2)


window = Window(1280, 720, "標題標題", "icon.png")
bg = window.setup()
Cum = 0

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







