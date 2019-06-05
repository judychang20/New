import pygame as pg

class Welcome():
	
	def welcome_page():
	
		"""載入歡迎畫面起始時所需的圖片及文字"""

		background_image0 = pg.image.load("第一頁背景.png")
		background_image = pg.transform.scale(background_image0, (1280, 720)).convert()
		bg.blit(background_image, (0, 0)) #載入背景畫面到bg上

		title = my_titlefont.render("標題標題標題", True, (0, 0, 0))
		bg.blit(title, (475, 100)) #載入標題到bg上

		text1 = my_textfont.render("今天要去哪裡玩？", True, (0, 0, 0))
		bg.blit(text1, (540, 275)) #載入文字到bg上

		button_image = pg.image.load("真亮按鈕.png").convert()
		button_image.set_alpha(200)
		bg.blit(button_image, (330, 350))
		bg.blit(button_image, (330, 480)) #載入透明度200的按鈕兩個到bg上

		text2 = my_textfont.render("我想去___區", True, (255, 255, 255))
		bg.blit(text2, (570, 375)) #載入文字到bg上

		text2 = my_textfont.render("我還沒有想法", True, (255, 255, 255))
		bg.blit(text2, (570, 505)) #載入文字到bg上
		
	def no_idea():

		"""選擇沒有想法"""

		button_image = pg.image.load("按鈕.png").convert()
		button_image.set_alpha(150)
		bg.blit(button_image, (330, 480))
		text2 = my_textfont.render("我還沒有想法", True, (255, 255, 255))
		bg.blit(text2, (570, 505))
		screen.blit(bg, (0, 0))
		pg.display.update()

	def have_idea():

		"""已經有想法"""
	
		button_image = pg.image.load("按鈕.png").convert()
		button_image.set_alpha(150)
		bg.blit(button_image, (330, 350))
		text2 = my_textfont.render("我想去___區", True, (255, 255, 255))
		bg.blit(text2, (570, 375))
		screen.blit(bg, (0, 0))
		pg.display.update()

	def choose_district():

		"""區域選單"""

		list_image0 = pg.image.load("區選單.png")
		bg.blit(list_image0, (50, 70))
		text2 = my_titlefont1.render("返回", True, (0, 0, 0))
		bg.blit(text2, (1015, 535))
		text2 = my_textfont.render("大安區", True, (0, 0, 0))
		bg.blit(text2, (190, 225))
		text2 = my_textfont.render("中正區", True, (0, 0, 0))
		bg.blit(text2, (190, 323))
		text2 = my_textfont.render("萬華區", True, (0, 0, 0))
		bg.blit(text2, (190, 420))
		text2 = my_textfont.render("士林區", True, (0, 0, 0))
		bg.blit(text2, (455, 225))
		text2 = my_textfont.render("內湖區", True, (0, 0, 0))
		bg.blit(text2, (455, 323))
		text2 = my_textfont.render("大同區", True, (0, 0, 0))
		bg.blit(text2, (455, 420))
		text2 = my_textfont.render("文山區", True, (0, 0, 0))
		bg.blit(text2, (720, 225))
		text2 = my_textfont.render("北投區", True, (0, 0, 0))
		bg.blit(text2, (720, 323))
		text2 = my_textfont.render("南港區", True, (0, 0, 0))
		bg.blit(text2, (720, 420))
		text2 = my_textfont.render("信義區", True, (0, 0, 0))
		bg.blit(text2, (985, 225))
		text2 = my_textfont.render("中山區", True, (0, 0, 0))
		bg.blit(text2, (985, 323))
		text2 = my_textfont.render("松山區", True, (0, 0, 0))
		bg.blit(text2, (985, 420))
		screen.blit(bg, (0,0))
		pg.display.update()
		#以上為區選單頁面的預設畫面，會載入12個暗按鈕及12個數字
		
		if 959 < mouse[0] < 1140 and 517 < mouse[1] < 599:
			exit_image0 = pg.image.load("亮返回.png")
			exit_image = pg.transform.scale(exit_image0, (182, 82))
			bg.blit(exit_image, (959, 517))
			text2 = my_titlefont1.render("返回", True, (0, 0, 0))
			bg.blit(text2, (1015, 535))
			screen.blit(bg, (0, 0))
			pg.display.update()
			if event.type == pg.MOUSEBUTTONDOWN:
				Cum = 0
		if 111 < mouse[0] < 348 and 205 < mouse[1] < 278:
			exit_image0 = pg.image.load("亮區按鈕.png")
			exit_image = pg.transform.scale(exit_image0, (238, 75))
			bg.blit(exit_image, (111, 205))
			text2 = my_textfont.render("大安區", True, (0, 0, 0))
			bg.blit(text2, (190, 225))
			screen.blit(bg, (0, 0))
			pg.display.update()
			if event.type == pg.MOUSEBUTTONDOWN:
				Cum = 0.5
		if 111 < mouse[0] < 348 and 303 < mouse[1] < 376:
			exit_image0 = pg.image.load("亮區按鈕.png")
			exit_image = pg.transform.scale(exit_image0, (238, 75))
			bg.blit(exit_image, (111, 303))
			text2 = my_textfont.render("中正區", True, (0, 0, 0))
			bg.blit(text2, (190, 323))
			screen.blit(bg, (0, 0))
			pg.display.update()
			if event.type == pg.MOUSEBUTTONDOWN:
				Cum = 0.5
		if 111 < mouse[0] < 348 and 400 < mouse[1] < 473:
			exit_image0 = pg.image.load("亮區按鈕.png")
			exit_image = pg.transform.scale(exit_image0, (238, 75))
			bg.blit(exit_image, (111, 400))
			text2 = my_textfont.render("萬華區", True, (0, 0, 0))
			bg.blit(text2, (190, 420))
			screen.blit(bg, (0, 0))
			pg.display.update()
			if event.type == pg.MOUSEBUTTONDOWN:
				Cum = 0.5
		if 375 < mouse[0] < 612 and 205 < mouse[1] < 278:
			exit_image0 = pg.image.load("亮區按鈕.png")
			exit_image = pg.transform.scale(exit_image0, (238, 75))
			bg.blit(exit_image, (375, 205))
			text2 = my_textfont.render("士林區", True, (0, 0, 0))
			bg.blit(text2, (455, 225))
			screen.blit(bg, (0, 0))
			pg.display.update()
			if event.type == pg.MOUSEBUTTONDOWN:
				Cum = 0.5
		if 375 < mouse[0] < 612 and 303 < mouse[1] < 376:
			exit_image0 = pg.image.load("亮區按鈕.png")
			exit_image = pg.transform.scale(exit_image0, (238, 75))
			bg.blit(exit_image, (375, 303))
			text2 = my_textfont.render("內湖區", True, (0, 0, 0))
			bg.blit(text2, (455, 323))
			screen.blit(bg, (0, 0))
			pg.display.update()
			if event.type == pg.MOUSEBUTTONDOWN:
				Cum = 0.5
		if 375 < mouse[0] < 612 and 400 < mouse[1] < 473:
			exit_image0 = pg.image.load("亮區按鈕.png")
			exit_image = pg.transform.scale(exit_image0, (238, 75))
			bg.blit(exit_image, (375, 400))
			text2 = my_textfont.render("大同區", True, (0, 0, 0))
			bg.blit(text2, (455, 420))
			screen.blit(bg, (0, 0))
			pg.display.update()
			if event.type == pg.MOUSEBUTTONDOWN:
				Cum = 0.5
		if 638 < mouse[0] < 875 and 205 < mouse[1] < 278:
			exit_image0 = pg.image.load("亮區按鈕.png")
			exit_image = pg.transform.scale(exit_image0, (238, 75))
			bg.blit(exit_image, (638, 205))
			text2 = my_textfont.render("文山區", True, (0, 0, 0))
			bg.blit(text2, (720, 225))
			screen.blit(bg, (0, 0))
			pg.display.update()
			if event.type == pg.MOUSEBUTTONDOWN:
				Cum = 0.5
		if 638 < mouse[0] < 875 and 303 < mouse[1] < 376:
			exit_image0 = pg.image.load("亮區按鈕.png")
			exit_image = pg.transform.scale(exit_image0, (238, 75))
			bg.blit(exit_image, (638, 303))
			text2 = my_textfont.render("北投區", True, (0, 0, 0))
			bg.blit(text2, (720, 323))
			screen.blit(bg, (0, 0))
			pg.display.update()
			if event.type == pg.MOUSEBUTTONDOWN:
				Cum = 0.5
		if 638 < mouse[0] < 875 and 400 < mouse[1] < 473:
			exit_image0 = pg.image.load("亮區按鈕.png")
			exit_image = pg.transform.scale(exit_image0, (238, 75))
			bg.blit(exit_image, (638, 400))
			text2 = my_textfont.render("南港區", True, (0, 0, 0))
			bg.blit(text2, (720, 420))
			screen.blit(bg, (0, 0))
			pg.display.update()
			if event.type == pg.MOUSEBUTTONDOWN:
				Cum = 0.5
		if 903 < mouse[0] < 1140 and 205 < mouse[1] < 278:
			exit_image0 = pg.image.load("亮區按鈕.png")
			exit_image = pg.transform.scale(exit_image0, (238, 75))
			bg.blit(exit_image, (903, 205))
			text2 = my_textfont.render("信義區", True, (0, 0, 0))
			bg.blit(text2, (985, 225))
			screen.blit(bg, (0, 0))
			pg.display.update()
			if event.type == pg.MOUSEBUTTONDOWN:
				Cum = 0.5
		if 903 < mouse[0] < 1140 and 303 < mouse[1] < 376:
			exit_image0 = pg.image.load("亮區按鈕.png")
			exit_image = pg.transform.scale(exit_image0, (238, 75))
			bg.blit(exit_image, (903, 303))
			text2 = my_textfont.render("中山區", True, (0, 0, 0))
			bg.blit(text2, (985, 323))
			screen.blit(bg, (0, 0))
			pg.display.update()
			if event.type == pg.MOUSEBUTTONDOWN:
				Cum = 0.5
		if 903 < mouse[0] < 1140 and 400 < mouse[1] < 473:
			exit_image0 = pg.image.load("亮區按鈕.png")
			exit_image = pg.transform.scale(exit_image0, (238, 75))
			bg.blit(exit_image, (903, 400))
			text2 = my_textfont.render("松山區", True, (0, 0, 0))
			bg.blit(text2, (985, 420))
			screen.blit(bg, (0, 0))
			pg.display.update()
			if event.type == pg.MOUSEBUTTONDOWN:
				Cum = 0.5
		# 以上是若滑鼠游標移到各個行政區的按鈕上，按鈕會變亮，若此時按下去，則會進入Cum = 0.5，心理測驗的過度頁面
		# 按下返回則會回到首頁

#初始設定
pg.init() #將pygame初始化

Cum = 0 # Cum:用來判別應處在哪個遊戲頁面，0.歡迎頁面 1.沒想法後的心理測驗 2.輪盤頁面 3.兩兩選擇頁面 4.選好行政區後的心理測驗
# 5. 景點介紹頁面 6.首頁的區選單頁面， 0.5: 選好行政區後的心理測驗（防止玩家按完行政區後按到心理測驗選項，因此設此過渡頁面）
Cir = 0 # Cir:用來交替輪盤圖片，使輪盤達旋轉效果
Time = 0 # Time:用來計算輪盤圖片已交替出現次數，若滿30次則輪盤停止，跳出結果視窗
Acum = 0 #Acum: 用於判別兩兩選擇時，頁面應出現的狀態，Acum = 0為靜止畫面，等於1時為左邊畫面移動，2時為右邊移動，3時為右邊卡片移到正中間
# 4時為左邊卡片移到正中間
astep = 0  #在Acum = 1 or 2時，用來作為失敗卡片移動速度的變數
bstep = 0  #在Acum = 3 or 4時，用來作為勝利卡片移動速度的變數
move_time = 0 #在Acum = 1 or 2時，用來判斷astep此時應為遞增或遞減的變數
choose_time = 0 #在Acum = 1 or 2時，用來記錄此時玩家已經淘汰掉幾張牌
width, height = 1280, 720
screen = pg.display.set_mode((width, height))
pg.display.set_caption("標題標題")
my_titlefont = pg.font.Font("myfont.ttf", 56)
my_textfont = pg.font.Font("myfont.ttf", 25)
my_titlefont1 = pg.font.Font("myfont.ttf", 35)
my_textfont1 = pg.font.Font("myfont.ttf", 23)
my_titlefont2 = pg.font.Font("myfont.ttf", 33)
my_textfont2 = pg.font.Font("myfont.ttf", 20)  #建立視窗及標題及建立各個字型大小以供後續使用

bg = pg.Surface(screen.get_size()).convert()  #將bg設定為視窗的surface

icon_image = pg.image.load("icon.png").convert()
pg.display.set_icon(icon_image)      #設定程式的icon

running = True
while running:

	mouse = pg.mouse.get_pos()
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False

		if Cum == 0:#用Cum在這做頁面的分辨
			Welcome.welcome_page()
		if Cum == 1:
			Welcome.choose_district()
		if 310 < mouse[0] < 950 and 480 < mouse[1] < 560 and Cum == 0: #用滑鼠游標位置判別亮、暗按鈕的切換，按下按鈕會到心理測驗
			Welcome.no_idea()
			if event.type == pg.MOUSEBUTTONDOWN:
				Cum = 1
		elif 310 < mouse[0] < 950 and 350 < mouse[1] < 430 and Cum == 0:
			Welcome.have_idea()
			if event.type == pg.MOUSEBUTTONDOWN:
				Cum = 1



