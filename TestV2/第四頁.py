import pygame as pg

def welcome_page():

	background_image0 = pg.image.load("第一頁背景.png")
	background_image = pg.transform.scale(background_image0, (1280, 720)).convert()
	bg.blit(background_image, (0, 0))

	title = my_titlefont.render("標題標題標題", True, (0, 0, 0))
	bg.blit(title, (475, 100))

	text1 = my_textfont.render("文字文字文字文字？", True, (0, 0, 0))
	bg.blit(text1, (540, 275))

	button_image = pg.image.load("真亮按鈕.png").convert()
	button_image.set_alpha(200)
	bg.blit(button_image, (330, 350))
	bg.blit(button_image, (330, 480))

	text2 = my_textfont.render("我想去", True, (255, 255, 255))
	bg.blit(text2, (570, 375))

	text2 = my_textfont.render("我還沒有想法", True, (255, 255, 255))
	bg.blit(text2, (570, 505))


def test_page():

	background_image0 = pg.image.load("第二頁背景.png")
	background_image = pg.transform.scale(background_image0, (1280, 720)).convert()
	bg.blit(background_image, (0, 0))

	title = my_titlefont1.render("心理測驗題目題目題目", True, (0, 0, 0))
	bg.blit(title, (90, 50))

	button_image0 = pg.image.load("亮按鈕.png").convert()
	button_image0.set_alpha(200)
	button_image = pg.transform.scale(button_image0, (1000, 100)).convert()
	bg.blit(button_image, (110, 160))
	bg.blit(button_image, (110, 293))
	bg.blit(button_image, (110, 426))
	bg.blit(button_image, (110, 560))

	#lightbutton0 = pg.image.load("亮按鈕.png").convert()
	#lightbutton0.set_alpha(150)
	#lightbutton = pg.transform.scale(lightbutton0, (1000, 100)).convert()
	#cum = 0

	text1 = my_textfont1.render("選項A", True, (255, 255, 255))
	bg.blit(text1, (130, 190))

	text2 = my_textfont1.render("選項B", True, (255, 255, 255))
	bg.blit(text2, (130, 323))

	text3 = my_textfont1.render("選項C", True, (255, 255, 255))
	bg.blit(text3, (130, 456))

	text4 = my_textfont1.render("選項D", True, (255, 255, 255))
	bg.blit(text4, (130, 590))

def roulette_page():
	background_image0 = pg.image.load("第三頁背景.png")
	background_image = pg.transform.scale(background_image0, (1280, 720)).convert()
	bg.blit(background_image, (0, 0))

	#roulette_image0 = pg.image.load("roulette.png")
	#roulette_image = pg.transform.scale(roulette_image0, (1150, 1150)).convert_alpha()
	#pg.transform.rotate(roulette_image, 10)
	#bg.blit(roulette_image,(50, 150))

	pg.draw.polygon(bg, (0, 0, 0), ((580, 50), (680, 50), (630, 260)))

def choose_page():

	background_image0 = pg.image.load("第四頁背景.png")
	background_image = pg.transform.scale(background_image0, (1280, 720)).convert()
	bg.blit(background_image, (0, 0))

	title = my_titlefont.render("選擇", True, (0, 0, 0))
	bg.blit(title, (580, 80))


pg.init()

Cum = 0
Cir = 0
Time = 0
width, height = 1280, 720
screen = pg.display.set_mode((width, height))
pg.display.set_caption("標題標題")
my_titlefont = pg.font.Font("myfont.ttf", 56)
my_textfont = pg.font.Font("myfont.ttf", 25)
my_titlefont1 = pg.font.Font("myfont.ttf", 35)
my_textfont1 = pg.font.Font("myfont.ttf", 23)

bg = pg.Surface(screen.get_size()).convert()

icon_image = pg.image.load("icon.png").convert()
pg.display.set_icon(icon_image)

running = True
while running:
	mouse = pg.mouse.get_pos()
	buttons = pg.mouse.get_pressed()
	
	for event in pg.event.get():
		
		#關閉程式
		if event.type == pg.QUIT:
			running = False
			
		#頁面控制
		if Cum == 0:
			welcome_page()
		if Cum == 1:
			test_page()
		if Cum == 2:
			roulette_page()
		if Cum == 3:
			choose_page()
		#開始畫面
		if 310 < mouse[0] < 950 and 480 < mouse[1] < 560 and Cum == 0:
			button_image = pg.image.load("按鈕.png").convert()
			button_image.set_alpha(150)
			bg.blit(button_image, (330, 480))
			text2 = my_textfont.render("我還沒有想法", True, (255, 255, 255))
			bg.blit(text2, (570, 505))
			screen.blit(bg, (0, 0))
			pg.display.update()
			if event.type == pg.MOUSEBUTTONDOWN:
				Cum = 1
		elif 310 < mouse[0] < 950 and 350 < mouse[1] < 430 and Cum == 0:
			button_image = pg.image.load("按鈕.png").convert()
			button_image.set_alpha(150)
			bg.blit(button_image, (330, 350))
			text2 = my_textfont.render("我想去", True, (255, 255, 255))
			bg.blit(text2, (570, 375))
			screen.blit(bg, (0, 0))
			pg.display.update()
			if event.type == pg.MOUSEBUTTONDOWN:
				Cum = 3
		#心理測驗頁面
		elif 110 < mouse[0] < 1110 and 160 < mouse[1] < 260 and Cum == 1:
			button_image0 = pg.image.load("選項.png").convert()
			button_image0.set_alpha(150)
			button_image = pg.transform.scale(button_image0, (1000, 100)).convert()
			bg.blit(button_image, (110, 160))
			text1 = my_textfont1.render("選項A", True, (255, 255, 255))
			bg.blit(text1, (130, 190))
			screen.blit(bg, (0, 0))
			pg.display.update()
			if event.type == pg.MOUSEBUTTONDOWN:
				Cum = 2
		elif 110 < mouse[0] < 1110 and 293 < mouse[1] < 393 and Cum == 1:
			button_image0 = pg.image.load("選項.png").convert()
			button_image0.set_alpha(150)
			button_image = pg.transform.scale(button_image0, (1000, 100)).convert()
			bg.blit(button_image, (110, 293))
			text1 = my_textfont1.render("選項B", True, (255, 255, 255))
			bg.blit(text1, (130, 323))
			screen.blit(bg, (0, 0))
			pg.display.update()
			if event.type == pg.MOUSEBUTTONDOWN:
				Cum = 2
		elif 110 < mouse[0] < 1110 and 426 < mouse[1] < 526 and Cum == 1:
			button_image0 = pg.image.load("選項.png").convert()
			button_image0.set_alpha(150)
			button_image = pg.transform.scale(button_image0, (1000, 100)).convert()
			bg.blit(button_image, (110, 426))
			text1 = my_textfont1.render("選項C", True, (255, 255, 255))
			bg.blit(text1, (130, 456))
			screen.blit(bg, (0, 0))
			pg.display.update()
			if event.type == pg.MOUSEBUTTONDOWN:
				Cum = 2
		elif 110 < mouse[0] < 1110 and 560 < mouse[1] < 660 and Cum == 1:
			button_image0 = pg.image.load("選項.png").convert()
			button_image0.set_alpha(150)
			button_image = pg.transform.scale(button_image0, (1000, 100)).convert()
			bg.blit(button_image, (110, 560))
			text1 = my_textfont1.render("選項D", True, (255, 255, 255))
			bg.blit(text1, (130, 590))
			screen.blit(bg, (0, 0))
			pg.display.update()
			if event.type == pg.MOUSEBUTTONDOWN:
				Cum = 2
		#轉盤頁面
		elif Cum == 2 and Cir == 0 and Time < 30:
			roulette_image0 = pg.image.load("roulette.png")
			roulette_image = pg.transform.scale(roulette_image0, (1150, 1150)).convert_alpha()
			# pg.transform.rotate(roulette_image, 10)
			bg.blit(roulette_image, (50, 150))
			screen.blit(bg, (0, 0))
			pg.display.update()
			Cir = 1
			Time += 1
		elif Cum == 2 and Cir == 1 and Time < 30:
			Cir = 0
			roulette_image0 = pg.image.load("roulette.png")
			roulette_image = pg.transform.scale(roulette_image0, (1150, 1150)).convert_alpha()
			a = pg.transform.rotate(roulette_image, 160)
			bg.blit(a, (-110, -11))
			screen.blit(bg, (0, 0))
			pg.display.update()
			Time += 1
		elif Cum == 2 and Time == 30:
			roulette_image0 = pg.image.load("roulette.png")
			roulette_image = pg.transform.scale(roulette_image0, (1150, 1150)).convert_alpha()
			# pg.transform.rotate(roulette_image, 10)
			bg.blit(roulette_image, (50, 150))
			window_image = pg.image.load("視窗.png")
			bg.blit(window_image, (190, 150))
			text1 = my_titlefont.render("某某區", True, (0, 0, 0))
			bg.blit(text1, (560, 230))
			screen.blit(bg, (0, 0))
			pg.display.update()
			if 682 < mouse[0] < 992 and 348 < mouse[1] < 458:
				sure_image0 = pg.image.load("確定.png")
				sure_image = pg.transform.scale(sure_image0, (310, 110))
				bg.blit(sure_image, (682, 348))
				screen.blit(bg, (0, 0))
				pg.display.update()
				if event.type == pg.MOUSEBUTTONDOWN:
					Time = 0
					Cum = 0
		#兩兩對比頁面
		elif Cum == 3:
			choose_card0 = pg.image.load("選擇卡.png")
			choose_card = pg.transform.scale(choose_card0, (400, 500)).convert()
			bg.blit(choose_card, (100, 150))
			bg.blit(choose_card, (800, 150))
			rect = choose_card.get_rect()
			rect.center = (100,150)
			x, y = rect.topleft
			speed = 3
			clock = pg.time.Clock()
			if event.type == pg.MOUSEBUTTONDOWN: #按下左邊圖
				x += speed
				rect_center = (x, y)
				
			
			'''
			image1 = pg.image.load("input().png")
			destination1 = pg.transform.scale(image1, (1150, 1150)).convert_alpha()
			image2 = pg.image.load("input().png")
			destination2 = pg.transform.scale(image2, (1150, 1150)).convert_alpha()
			'''
			
			text1 = my_titlefont.render("輸入景點名稱", True, (0, 0, 0))
			bg.blit(text1, (140, 560))
			bg.blit(text1, (840, 560))
			screen.blit(bg, (0, 0))
			pg.display.update()
			
		else:
			screen.blit(bg, (0, 0))
			pg.display.update()


pg.quit()

