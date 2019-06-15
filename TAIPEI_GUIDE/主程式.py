import pygame as pg
import random
import csv

class Word:

	def __init__(self, font, context, xplace, yplace, surface, color):
		"""文字包含字型、內容、擺放位置、擺放背景、顏色"""
		self.font = font
		self.context = context
		self.xplace = xplace
		self.yplace = yplace
		self.surface = surface
		self.color = color

	def buildup(self):
		"""將文字建立在背景上"""
		a = self.font.render(self.context, True, self.color)
		self.surface.blit(a, (self.xplace, self.yplace))


class Button:

	def __init__(self, darkimage, lightimage, xplace, yplace, surface, xsize, ysize, word, alpha):
		"""按鈕包含未觸發時的狀態、游標在上時的狀態、擺放位置、大小、擺放背景、文字、透明度"""
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
		"""按鈕的預設狀態，會載入圖片作為按鈕，在上面建立文字及調整透明度、大小"""
		a = pg.image.load(self.darkimage).convert()
		a.set_alpha(self.alpha)
		b = pg.transform.scale(a, (self.xsize, self.ysize)).convert()
		self.surface.blit(b, (self.xplace, self.yplace))
		Word.buildup(self.word)

	def MouseOver(self):
		"""當游標在上，會載入另張圖片蓋過原本圖片，再載入同樣文字及透明度、大小"""
		a = pg.image.load(self.lightimage)
		a.set_alpha(self.alpha)
		b = pg.transform.scale(a, (self.xsize, self.ysize)).convert()
		self.surface.blit(b, (self.xplace, self.yplace))
		Word.buildup(self.word)

	def isOver(self, x, y, z, k , theme):
		"""當游標在按鈕範圍內按下左鍵，則Cum會更新成新數字，回傳至Main後達成變換頁面的效果，按鈕按下後也可回傳主題，供生成景點時的參考"""
		global Cum , atheme
		if self.xplace <  x < self.xplace + self.xsize and self.yplace < y < self.yplace + self.ysize:
			# x, y為游標的座標，當座標介於按鈕上下左右界內，觸發MouseOver函數
			self.MouseOver()
			if z == pg.MOUSEBUTTONDOWN:
				# z為遊戲事件，當遊戲事件為按下左鍵時，Cum變為k
				Cum = k
				atheme = theme
		return Cum ,atheme

	def isOver_spot(self, x, y, z, k , dist):
		"""效果同isOver，但回傳值變為行政區域而非主題"""
		global Cum , adist
		if self.xplace <  x < self.xplace + self.xsize and self.yplace < y < self.yplace + self.ysize:
			self.MouseOver()
			if z == pg.MOUSEBUTTONDOWN:
				Cum = k
				adist = dist
				#print(adist)
		return Cum , adist

				
class Picture:

	def __init__(self, picture, xplace, yplace, xsize, ysize, surface):
		"""圖片包含檔名、擺放位置、大小、擺放背景"""
		self.picture = picture
		self.xplace = xplace
		self.yplace = yplace
		self.xsize = xsize
		self.ysize = ysize
		self.surface = surface

	def buildup(self):
		"""將圖片調整大小後建立在背景上"""
		a = pg.image.load(self.picture)
		b = pg.transform.scale(a, (self.xsize, self.ysize))
		self.surface.blit(b, (self.xplace, self.yplace))
		pg.display.update()


class Window:

	def __init__(self, width, height, caption, icon):
		"""視窗包含長度、寬度、標題、圖示"""
		self.width = width
		self.height = height
		self.caption = caption
		self.icon = icon
		self.screen = pg.display.set_mode((self.width, self.height))

	def setup(self):
		"""設定將被放在視窗內的背景的相關資訊，並回傳此Surface"""
		pg.init()
		pg.display.set_caption(self.caption)
		bg = pg.Surface(self.screen.get_size()).convert()
		icon_image = pg.image.load(self.icon)
		pg.display.set_icon(icon_image)
		return bg

	def bulidup(self):
		"""在視窗內建立此Surface"""
		self.screen.blit(Window.setup(self), (0,0))
		pg.display.update()


class Spot:

	def __init__(self, distinct, theme, name, intro, address, ticket, open1, open2, open3, open4, open5, open6, open7):
		"""景點包含行政區、名稱、介紹文字、地址、門票資訊、營業時間資訊"""
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


class ThemeToTest:
	"""心理測驗有題目及四個選項，將四個選項建為清單並給予屬性"""
	def __init__(self, random_test):
		self.name = random_test[0]
		self.list = [random_test[1], random_test[2],random_test[3], random_test[4]]
		self.history = random_test[1]
		self.art = random_test[2]
		self.fun = random_test[3]
		self.shop = random_test[4]



def Main(circumstance, x, y, z):
	"""藉由Cum值的不同，讓使用者進入不同的頁面，x, y為游標座標，ｚ為遊戲事件"""
	if circumstance == 0:
		welcome_page(x, y, z)
	if circumstance == 1:
		test_noidea_page(x, y, z)
	if circumstance == 2:
		test_haveidea_page(x, y, z)
	if circumstance == 6:
		roulette_page(x, y, z)	
	if circumstance == 7:
		spotintro_page(x, y, z)
	if circumstance == 8:
		choosedict_page(x, y, z)
	if circumstance == 9:
		bell_page(x, y, z)

def welcome_page(x, y, z):
	"""遊戲主頁，會隨機載入一背景圖片，加上標題圖片、文字、按鈕"""
	global Controller5, back_image
	font1 = pg.font.Font("myfont.ttf", 56)
	font2 = pg.font.Font("myfont.ttf", 25)
	# 設定該頁會用到的字型大小
	if Controller5 == 0:
		back_image0 = random.choice(["第一頁背景1.png", "第一頁背景2.png","第一頁背景3.png" , "第一頁背景4.png", "第一頁背景5.png", "第一頁背景6.png"])
		back_image = "Background/" + back_image0
		Controller5 = 1
		# 避免在迴圈內會不斷隨機出不同背景，設計Controller讓程式只會跑出一結果
	Picture(back_image, 0, 0, 1280, 720, bg).buildup()
	Picture("Resource/標題.png", 250, 80, 800, 150, bg).buildup()
	Word(font2, "今天要去哪裡玩？", 550, 260, bg, (0,0,0)).buildup()
	word1 = Word(font2, "我要去___區", 570, 375, bg, (255,255,255))
	a = Button("Resource/按鈕暗.png", "Resource/按鈕亮.png", 330, 350, bg, 624, 82, word1, 200)
	word2 = Word(font2, "我還沒有想法", 570, 505, bg, (255,255,255))
	b = Button("Resource/按鈕暗.png", "Resource/按鈕亮.png", 330, 480, bg, 624, 82, word2, 200)
	# 以上為將圖片、文字、按鈕建立在bg這個Surface上的過程
	a.WaitToMouseOver()
	a.isOver(x, y, z, 8, "")
	# 當使用者按下上面按鈕，則Cum會回傳8，進入區選單頁面，主題因為不適用於此，因此設定為空字串
	b.WaitToMouseOver()
	b.isOver(x, y, z, 1, "")
	# 當使用者按下下面按鈕，則Cum會回傳1，進入心理測驗，主題因為不適用於此，因此設定為空字串


def test_noidea_page(x, y, z):
	"""心理測驗的頁面，會載入題目文字及四個按鈕，按鈕上的文字各自為四個選項之一"""
	global Controller2, alist
	if Controller2 == 0:
		alist = psycho_test()
		random.shuffle(alist.list)
		Controller2 = 1
		# 避免在迴圈內會不斷隨機出不同結果，設計Controller讓程式只會跑出一結果，用psycho_test從檔案中隨機選一題心理測驗，用random將選項排序打亂
	font1 = pg.font.Font("myfont.ttf", 35)
	font2 = pg.font.Font("myfont.ttf", 23)
	Picture("Background/第二頁背景.png", 0, 0, 1280, 720, bg).buildup()
	Question = alist.name
	OptionA = alist.list[0]
	OptionB = alist.list[1]
	OptionC = alist.list[2]
	OptionD = alist.list[3]
	Word(font1, Question, 90, 50, bg, (0, 0, 0)).buildup()
	option1 = Word(font2, OptionA, 130, 190, bg, (255, 255, 255))
	option2 = Word(font2, OptionB, 130, 323, bg, (255, 255, 255))
	option3 = Word(font2, OptionC, 130, 456, bg, (255, 255, 255))
	option4 = Word(font2, OptionD, 130, 590, bg, (255, 255, 255))
	a = Button("Resource/選項暗.png", "Resource/選項亮.png", 110, 160, bg, 1000, 100, option1, 200)
	a.WaitToMouseOver()
	b = Button("Resource/選項暗.png", "Resource/選項亮.png", 110, 293, bg, 1000, 100, option2, 200)
	b.WaitToMouseOver()
	c = Button("Resource/選項暗.png", "Resource/選項亮.png", 110, 426, bg, 1000, 100, option3, 200)
	c.WaitToMouseOver()
	d = Button("Resource/選項暗.png", "Resource/選項亮.png", 110, 560, bg, 1000, 100, option4, 200)
	d.WaitToMouseOver()
	# 以上為建立背景圖片、文字、按鈕的過程，選項因為清單排序被打亂因此為隨機排列
	a.isOver(x, y, z, 6, test_choice(alist.list[0]))
	b.isOver(x, y, z, 6, test_choice(alist.list[1]))
	c.isOver(x, y, z, 6, test_choice(alist.list[2]))
	d.isOver(x, y, z, 6, test_choice(alist.list[3]))
	# test_choice這個函數，會回傳使用者按的選項文字所對應到的類別，按下後Cum = 6，並回傳類別給global的函數atheme


def test_haveidea_page(x, y, z):
	"""大致同test_haveidea_page，差別在會進入的下一個頁面的不同"""
	global Controller2, alist
	if Controller2 == 0:
		alist = psycho_test()
		random.shuffle(alist.list)
		Controller2 = 1
	font1 = pg.font.Font("myfont.ttf", 35)
	font2 = pg.font.Font("myfont.ttf", 23)
	Picture("Background/第二頁背景.png", 0, 0, 1280, 720, bg).buildup()
	Question = alist.name
	OptionA = alist.list[0]
	OptionB = alist.list[1]
	OptionC = alist.list[2]
	OptionD = alist.list[3]
	Word(font1, Question, 90, 50, bg, (0, 0, 0)).buildup()
	option1 = Word(font2, OptionA, 130, 190, bg, (255, 255, 255))
	option2 = Word(font2, OptionB, 130, 323, bg, (255, 255, 255))
	option3 = Word(font2, OptionC, 130, 456, bg, (255, 255, 255))
	option4 = Word(font2, OptionD, 130, 590, bg, (255, 255, 255))
	a = Button("Resource/選項暗.png", "Resource/選項亮.png", 110, 160, bg, 1000, 100, option1, 200)
	a.WaitToMouseOver()
	b = Button("Resource/選項暗.png", "Resource/選項亮.png", 110, 293, bg, 1000, 100, option2, 200)
	b.WaitToMouseOver()
	c = Button("Resource/選項暗.png", "Resource/選項亮.png", 110, 426, bg, 1000, 100, option3, 200)
	c.WaitToMouseOver()
	d = Button("Resource/選項暗.png", "Resource/選項亮.png", 110, 560, bg, 1000, 100, option4, 200)
	d.WaitToMouseOver()
	a.isOver(x, y, z, 9, test_choice(alist.list[0]))
	b.isOver(x, y, z, 9, test_choice(alist.list[1]))
	c.isOver(x, y, z, 9, test_choice(alist.list[2]))
	d.isOver(x, y, z, 9, test_choice(alist.list[3]))


def bell_page(x, y, z):
	"""鈴鐺頁面，會藉由搖動鈴鐺，在確定行政區及類別的情況下，給予使用者一個隨機的景點"""
	global aTime, Controller, aspot, Cir
	font1 = pg.font.Font("myfont.ttf", 45)
	font2 = pg.font.Font("myfont.ttf", 56)
	font3 = pg.font.Font("myfont.ttf", 50)
	if Cir == 0 and aTime != 10:
		Picture("Background/第三頁背景.png", 0, 0, 1280, 720, bg).buildup()
		Picture("Resource/左搖.png", 100, 50, 700, 700, bg).buildup()
		if aTime == 0:
			Picture("Resource/鈴鐺提醒.png", 170, 250, 900, 250, bg).buildup()
			# 在使用者尚未有任何動作時，會出現提醒圖片，提醒使用者應該移動滑鼠
		aTime += 1
		Cir = 1
	elif Cir == 1 and aTime != 10:
		Picture("Background/第三頁背景.png", 0, 0, 1280, 720, bg).buildup()
		Picture("Resource/右搖.png", 500, 50, 700, 700, bg).buildup()
		aTime += 1
		Cir = 0
	# 以上會藉由Cir值的不斷循環，讓兩個不同圖片交替出現，同時累加搖動的次數
	else :
		Picture("Background/第三頁背景.png", 0, 0, 1280, 720, bg).buildup()
		Picture("Resource/左搖.png", 100, 50, 700, 700, bg).buildup()
		word1 = Word(font1, "確定", 790, 370, bg, (0, 0, 0))
		Picture("Resource/視窗.png", 190, 150, 884, 350, bg).buildup()
		# 當達到一定搖動次數，會跳出一個仿視窗設計的圖片
		if Controller == 0:
			aspot = recommend_notknow(adist[0:2], atheme)
			Controller = 1
			# 避免在迴圈內會不斷隨機出不同結果，設計Controller讓程式只會跑出一景點結果
		if 10 >= len(aspot.name) > 7:
			Word(font3, aspot.name, 530, 235, bg, (0, 0, 0)).buildup()
		elif len(aspot.name) > 10:
			Word(font3, aspot.name[0:9], 530, 185, bg, (0, 0, 0)).buildup()
			Word(font3, aspot.name[9:], 530, 235, bg, (0, 0, 0)).buildup()
		else:
			Word(font2, aspot.name, 560, 230, bg, (0, 0, 0)).buildup()
		#以上的if-else，根據景點名稱，決定其在視窗上的呈現方式，可能會縮小字型或改成用兩行呈現
		a = Button("Resource/確定暗.png", "Resource/確定亮.png", 682, 348, bg, 310, 110, word1, 250)
		a.WaitToMouseOver()
		# 在視窗圖片上建立確定按鈕，按下後跳到景點介紹頁
		a.isOver(x, y, z, 7, "")

def roulette_page(x, y, z):
	"""輪盤頁面，會藉由轉動輪盤，在使用者不知道去哪的情況，隨機給予使用者一個行政區"""
	global Cir, Time, Controller, adist, aspot, location
	if Cir == 0 and Time < 10:
		Picture("Background/第三頁背景.png", 0, 0, 1280, 720, bg).buildup()
		roulette_image0 = pg.image.load("Resource/輪盤.png")
		roulette_image = pg.transform.scale(roulette_image0, (1150, 1150)).convert_alpha()
		bg.blit(roulette_image, (50, 150))
		pg.draw.polygon(bg, (0, 0, 0), ((580, 50), (680, 50), (630, 260)))
		if Time == 0:
			Picture("Resource/輪盤提醒.png", 170, 250, 900, 250, bg).buildup()
			# 在使用者尚未有任何動作時，會出現提醒圖片，提醒使用者應該移動滑鼠
		Time += 1
		Cir = 1
		window.screen.blit(bg, (0, 0))
		pg.display.update()
	elif Cir == 1 and Time < 10:
		Picture("Background/第三頁背景.png", 0, 0, 1280, 720, bg).buildup()
		roulette_image0 = pg.image.load("Resource/輪盤.png")
		roulette_image = pg.transform.scale(roulette_image0, (1150, 1150)).convert_alpha()
		a = pg.transform.rotate(roulette_image, 160)
		bg.blit(a, (-110, -11))
		# 將圖片轉動角度後的圖片大小會變換，因此需要更改擺放位置座標，讓圖片能在同一區域上顯示
		pg.draw.polygon(bg, (0, 0, 0), ((580, 50), (680, 50), (630, 260)))
		Time += 1
		Cir = 0
		window.screen.blit(bg, (0, 0))
		pg.display.update()
	# 以上會藉由Cir值的不斷循環，讓兩個不同圖片交替出現，同時累加轉動的次數
	elif Time == 10:
		font1 = pg.font.Font("myfont.ttf", 45)
		font2 = pg.font.Font("myfont.ttf", 56)

		if Controller == 0:
			adist = random.choice(["大安區","萬華區","士林區","中正區","文山區","南港區","大同區", "中山區", "松山區", "信義區","北投區", "內湖區"])
			aspot = recommend_notknow(adist[0:2], atheme)
			Controller = 1
			# 避免在迴圈內會不斷隨機出不同結果，設計Controller讓程式只會跑出一行政區結果，同時用此結果和先前心理測驗的成果，產出一個景點aspot
		word1 = Word(font1, "確定", 790, 370, bg, (0, 0, 0))
		Picture("Resource/視窗.png", 190, 150, 884, 350, bg).buildup()
		# 當達到一定轉動次數，會跳出一個仿視窗設計的圖片
		Word(font2, adist, 560, 230, bg, (0, 0, 0)).buildup()
		a = Button("Resource/確定暗.png", "Resource/確定亮.png", 682, 348, bg, 310, 110, word1, 250)
		a.WaitToMouseOver()
		a.isOver(x, y, z, 9, "")
		# 在視窗圖片上建立確定按鈕，按下後跳到鈴鐺頁

def spotintro_page(x, y, z):
	"""呈現景點相關資訊的頁面，有名稱、地址、門票、營業時間、介紹、圖片、圖片來源"""
	global Time, Cir, Controller, adist, location, aspot, Controller2, Controller3, Place, Controller4, aTime, Controller5
	font1 = pg.font.Font("myfont.ttf", 20)
	font2 = pg.font.Font("myfont.ttf", 33)
	font3 = pg.font.Font("myfont.ttf", 29)
	font4 = pg.font.Font("myfont.ttf", 25)
	Picture("Background/第四頁背景.png", 0, 0, 1280, 720, bg).buildup()
	Picture("Resource/地址.png", 25, 110, 48, 48, bg).buildup()
	Picture("Resource/門票.png", 25, 165, 48, 48, bg).buildup()
	Picture("Resource/營業時間.png", 27, 245, 45, 45, bg).buildup()
	Picture("Resource/圖片來源.png", 25, 580, 48, 48, bg).buildup()
	# 載入此頁會用到的字型大小及建立一些圖示到bg上
	spot = aspot.name
	address = aspot.address
	ticket = "門票："+ aspot.ticket
	if 11 >= len(aspot.name) > 9:
		Word(font3, spot, 50, 30, bg, (0, 0, 0)).buildup()
	elif len(aspot.name) > 11:
		Word(font4, spot[0:13], 50, 25, bg, (0, 0, 0)).buildup()
		Word(font4, spot[13:], 50, 50, bg, (0, 0, 0)).buildup()
	else:
		Word(font2, spot, 50, 30, bg, (0, 0, 0)).buildup()
	# 以上的if-else根據景點名稱的長度，決定是否縮小字型大小，或改成用兩行呈現
	if len(aspot.address) > 16:
		Word(font1, address[0:16], 80, 110, bg, (0, 0, 0)).buildup()
		Word(font1, address[16:], 80, 130, bg, (0, 0, 0)).buildup()
	else:
		Word(font1, address, 80, 120, bg, (0, 0, 0)).buildup()
	# 以上的if-else根據地址的長度，決定是否改成用兩行呈現
	Word(font1, ticket, 80, 175, bg, (0, 0, 0)).buildup()
	Word(font1, "營業時間", 80, 255, bg, (0, 0, 0)).buildup()
	Word(font1, "圖片來源", 80, 590, bg, (0, 0, 0)).buildup()
	Word(font1, "臺北旅遊網等網路資源", 90, 640, bg, (0, 0, 0)).buildup()
	# 以上為呈現一些固定出現之文字
	picture = "Picture/" + aspot.distinct + "/" + aspot.name + ".jpg"
	Picture(picture, 540,50, 640, 360, bg).buildup()
	# 根據行政區與景點名稱，會生成一圖片路徑，並用此路徑叫出對應的圖片並建立在bg上

	#輸出營業時間
	if aspot.open1 == "全日開放" or aspot.open1 == "全天開放": # 全天開放的景點
		Word(font1, aspot.open1, 100, 300, bg, (0, 0, 0)).buildup()
	elif aspot.open1 == "電話預約制": # 無固定營業時間的景點
		Word(font1, aspot.open1, 100, 300, bg, (0, 0, 0)).buildup()
	elif aspot.open1 == "全日開放，族人居住，注意禮儀": # 仍有住戶的景點
		print_list = []
		print_list.append(aspot.open1.split("，"))
		for i in range(len(print_list[0])):
			a = 300 + 40 * i
			Word(font1, print_list[0][i], 100, a, bg, (0, 0, 0)).buildup()
	elif aspot.open1 == "不開放" and "；" in aspot.open2: # 一日內多個段落的營業時間
		not_open = "星期一不開放"
		Word(font1, not_open, 100, 300, bg, (0, 0, 0)).buildup()
		Word(font1, "週二到週日開放時段：", 100, 340, bg, (0, 0, 0)).buildup()
		a = aspot.open2.split("；")
		for i in range(len(a)):
			b = 380 + 40 * i
			c = "(" + str(i + 1) + ") " + a[i]
			Word(font1, c, 100, b, bg, (0, 0, 0)).buildup()
	else:
		week_list = ["(一)", "(二)", "(三)", "(四)", "(五)", "(六)", "(日)"]#輸出營業時間
		time_list = [aspot.open1, aspot.open2, aspot.open3, aspot.open4, aspot.open5, aspot.open6, aspot.open7]
		for i in range(7):
			a = 300 + 40*i
			opentime = week_list[i] + " : " + time_list[i]
			Word(font1, opentime, 100, a, bg, (0, 0, 0)).buildup()
	# 以上的if-else根據營業時間的型態不同，決定呈現的方式

	# 輸出介紹文字，先按介紹字串的長度分類，再將每行的內容附加到清單，之後用迴圈變換建立的y座標，讓每行行距相等
	introduce_list = []
	if len(aspot.intro) < 30:
		introduce_list.append("      " + aspot.intro[0:])
	elif  30 <= len(aspot.intro) < 62:
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


	font1 = pg.font.Font("myfont.ttf", 25)
	word1 = Word(font1, "再玩一次", 1055, 620, bg, (0, 0, 0))
	a = Button("Resource/確定暗.png", "Resource/確定亮.png", 1000, 600, bg, 207, 72, word1, 250)
	# 建立再玩一次按鈕
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
	aTime = 0
	Controller5 = 0
	# 當按下按鈕後回到主頁，並將變數初始化，避免再次遊玩時程式出錯

def choosedict_page(x, y, z):
	"""區選單的頁面，會有12個行政區按鍵，以及一個返回鍵"""
	Picture("Resource/區選單.png", 50, 70, 1168, 570, bg).buildup()
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
	# 將12行政區按鈕建立於不同位置
	font1 = pg.font.Font("myfont.ttf", 35)
	word1 = Word(font1, "返回", 1015, 535, bg, (0, 0, 0))
	a = Button("Resource/確定暗.png", "Resource/確定亮.png", 959, 517, bg, 182, 82, word1, 250)
	a.WaitToMouseOver()
	a.isOver(x, y, z, 0, "")
	# 建立返回鍵，按下後返回主頁


def dict(name, xnameplace, ynameplace, xbuttonplace, ybuttonplace, x, y, z):
	"""因為12行政區按鈕的建立動作一致，將按鈕的函數打包在一起，並使用isOver_spot，讓按鈕文字對應的行政區可以被回傳"""
	font2 = pg.font.Font("myfont.ttf", 23)
	word1 = Word(font2, name, xnameplace, ynameplace, bg, (0, 0, 0))
	dict1 = Button("Resource/區按鈕暗.png", "Resource/區按鈕亮.png", xbuttonplace, ybuttonplace, bg, 238, 75, word1, 250)
	dict1.WaitToMouseOver()
	dict1.isOver_spot(x, y, z, 2, name)


def recommend_notknow(dist, theme):
	'''
    不知道去哪裡所回傳的景點
    需要傳入的值: 心理測驗的主題結果、輪盤的行政區
    '''
	fh1 = '完整景點資料庫.csv'
	fh1 = open(fh1, 'r', encoding='utf-8', newline='')
	csv1 = csv.reader(fh1)

	for a in csv1:
		location.append(Spot(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10], a[11], a[12]))
	# 先將csv內的資訊經處理弄成Spot，再附加到location清單
	speciallocation = []
	for data in location:
		if data.distinct == dist and data.theme == theme:
			speciallocation.append(data)
	# 按照傳入的行政區及景點類別，篩選出符合條件的景點，附加到清單
	location_item = random.choice(speciallocation)
	return location_item
	# 從符合條件的清單內的景點隨機挑選一並回傳


def psycho_test():
	"""讀取心理測驗的函數，會隨機回傳一個問題及對應的四個選項"""
	fh2 = '心理測驗.csv'
	fh2 = open(fh2, 'r', encoding='utf-8', newline='')
	csv2 = csv.reader(fh2)
	csv3 = next(csv2)
	Test = []

	for a in csv2:
		Test.append(ThemeToTest(a))
	atest = random.choice(Test)
	return atest


def test_choice(choice):
	"""根據回傳的選項文字，找出其在該題被歸類的主題為何，並回傳該主題"""
	if choice == alist.history:
		return "宗教與古蹟"
	elif choice == alist.art:
		return "藝文與文化"
	elif choice == alist.fun:
		return "休閒與生態"
	elif choice == alist.shop:
		return "商圈"

window = Window(1280, 720, "TAIPEI GUIDE", "Resource/圖示.png")
bg = window.setup()
# 建立視窗
Cum = 0
Cir = 0
Time = 0
Controller = 0
Controller2 = 0
Controller3 = 0
Controller4 = 0
Controller5 = 0
adist = ""
aspot = ""
atheme = ""
back_image = ""
alist = []
location = []
Test = []
Place = 0
spotlist =[]
aTime = 0
# 宣告local函數內會被用到的變數，以待後續local函數的呼叫

running = True
while running:
	mouse = pg.mouse.get_pos()
	# 不斷取得游標的座標

	for event in pg.event.get():
		Main(Cum, mouse[0], mouse[1], event.type)
		# 不斷將游標座標及遊戲事件傳入Main函數，再透過Main傳入各個頁面做使用
		if event.type == pg.QUIT:
			running = False
			# 退出遊戲
		else:
			window.screen.blit(bg, (0,0))
			pg.display.update()
			# 遊戲不斷更新畫面

pg.quit()