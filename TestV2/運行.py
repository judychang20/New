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

    text2 = my_textfont.render("我想去___區", True, (255, 255, 255))
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


def spotintro_page():
    background_image0 = pg.image.load("第五頁背景.png")
    background_image = pg.transform.scale(background_image0, (1280, 720)).convert()
    bg.blit(background_image, (0, 0))

    location_image0 = pg.image.load("placeholder.png")
    location_image = pg.transform.scale(location_image0, (48, 48)).convert_alpha()
    bg.blit(location_image, (25, 110))

    tickets_image0 = pg.image.load("tickets.png")
    ticket_image = pg.transform.scale(tickets_image0, (48, 48)).convert_alpha()
    bg.blit(ticket_image, (25, 165))

    time_image0 = pg.image.load("001-time.png")
    time_image = pg.transform.scale(time_image0, (45, 45)).convert_alpha()
    bg.blit(time_image, (27, 245))

    picture_image0 = pg.image.load("002-picture.png")
    picture_image = pg.transform.scale(picture_image0, (48, 48)).convert_alpha()
    bg.blit(picture_image, (25, 580))

    text2 = my_titlefont2.render("景點名", True, (0, 0, 0))
    bg.blit(text2, (50, 30))

    text3 = my_textfont2.render("臺北市萬華區中華路一段", True, (0, 0, 0))
    bg.blit(text3, (80, 120))

    text3 = my_textfont2.render("門票：無", True, (0, 0, 0))
    bg.blit(text3, (80, 175))

    text4 = my_textfont2.render("營業時間：", True, (0, 0, 0))
    bg.blit(text4, (80, 255))

    opentime1 = "(一)：09:00 - 17:30 "
    opentime2 = "(二)：09:00 - 17:30 "
    opentime3 = "(三)：09:00 - 17:30 "
    opentime4 = "(四)：09:00 - 17:30 "
    opentime5 = "(五)：09:00 - 17:30 "
    opentime6 = "(六)：09:00 - 17:30 "
    opentime7 = "(日)：09:00 - 17:30 "

    text5 = my_textfont2.render(opentime1, True, (0, 0, 0))
    bg.blit(text5, (100, 300))

    text6 = my_textfont2.render(opentime2, True, (0, 0, 0))
    bg.blit(text6, (100, 340))

    text7 = my_textfont2.render(opentime3, True, (0, 0, 0))
    bg.blit(text7, (100, 380))

    text8 = my_textfont2.render(opentime4, True, (0, 0, 0))
    bg.blit(text8, (100, 420))

    text9 = my_textfont2.render(opentime5, True, (0, 0, 0))
    bg.blit(text9, (100, 460))

    text10 = my_textfont2.render(opentime6, True, (0, 0, 0))
    bg.blit(text10, (100, 500))

    text11 = my_textfont2.render(opentime7, True, (0, 0, 0))
    bg.blit(text11, (100, 540))

    text12 = my_textfont2.render("圖片來源：", True, (0, 0, 0))
    bg.blit(text12, (80, 590))

    text13 = my_textfont2.render("臺北旅遊網", True, (0, 0, 0))
    bg.blit(text13, (90, 640))

    spot_image0 = pg.image.load("第一頁背景.png")
    spot_image = pg.transform.scale(spot_image0, (640, 360)).convert()
    bg.blit(spot_image, (540, 50))

    introtext1 = "      "+"木柵市場被作家劉克襄譽為台北盆地的清明上河圖，其生鮮食材來源"
    introtext2 = "除了周遭貓空、草湳山區的農作，石碇、深坑、平溪的產品，甚至宜蘭員"
    introtext3 = "山絲瓜、三星蔥皆由產地直銷而來。此外市場內外的美食也是不可錯過的"
    introtext4 = "去處。"
    text14 = my_textfont2.render(introtext1, True, (0, 0, 0))
    bg.blit(text14, (540, 450))
    text15 = my_textfont2.render(introtext2, True, (0, 0, 0))
    bg.blit(text15, (540, 480))
    text16 = my_textfont2.render(introtext3, True, (0, 0, 0))
    bg.blit(text16, (540, 510))
    text17 = my_textfont2.render(introtext4, True, (0, 0, 0))
    bg.blit(text17, (540, 540))


pg.init()

Cum = 0
Cir = 0
Time = 0
Acum = 0
width, height = 1280, 720
screen = pg.display.set_mode((width, height))
pg.display.set_caption("標題標題")
my_titlefont = pg.font.Font("myfont.ttf", 56)
my_textfont = pg.font.Font("myfont.ttf", 25)
my_titlefont1 = pg.font.Font("myfont.ttf", 35)
my_textfont1 = pg.font.Font("myfont.ttf", 23)
my_titlefont2 = pg.font.Font("myfont.ttf", 33)
my_textfont2 = pg.font.Font("myfont.ttf", 20)


bg = pg.Surface(screen.get_size()).convert()

icon_image = pg.image.load("icon.png").convert()
pg.display.set_icon(icon_image)

running = True
while running:
    mouse = pg.mouse.get_pos()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if Cum == 0:
            welcome_page()
        if Cum == 0.5:
            test_page()
            if event.type:
                Cum = 1
        if Cum == 1:
            test_page()
        if Cum == 2:
            roulette_page()
        if Cum == 5:
            spotintro_page()
        if Cum == 6:
            list_image0 = pg.image.load("區選單.png")
            #list_image = pg.transform.scale(list_image0, (1100, 550))
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
            if event.type == pg.MOUSEBUTTONDOWN:
                print(mouse)
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
            text2 = my_textfont.render("我想去___區", True, (255, 255, 255))
            bg.blit(text2, (570, 375))
            screen.blit(bg, (0, 0))
            pg.display.update()
            if event.type == pg.MOUSEBUTTONDOWN:
                Cum = 6

        #elif Acum == 1:
            #list_image0 = pg.image.load("區選單.png")
            #list_image = pg.transform.scale(list_image0,(350, 250)).convert()
            #list_image.set_alpha(200)
            #bg.blit(list_image, (650, 200))
            #screen.blit(bg, (0, 0))
            #pg.display.update()
        #elif event.type == pg.MOUSEBUTTONDOWN and Cum == 0 and Acum == 1:
            #welcome_page()
            #screen.blit(bg, (0, 0))
            #g.display.update()
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
                    Cum = 5
        elif Cum == 5:
            smallwindow_image0 = pg.image.load("再玩一次.png")
            smallwindow_image = pg.transform.scale(smallwindow_image0, (207, 72))
            bg.blit(smallwindow_image, (1000, 600))
            screen.blit(bg, (0, 0))
            pg.display.update()
            if 1000 < mouse[0] < 1207 and 600 < mouse[1] < 672:
                smallwindow_image0 = pg.image.load("亮再玩一次.png")
                smallwindow_image = pg.transform.scale(smallwindow_image0, (207, 72))
                bg.blit(smallwindow_image, (1000, 600))
                screen.blit(bg, (0, 0))
                pg.display.update()
                if event.type == pg.MOUSEBUTTONDOWN:
                    Cum = 0
        else:
            screen.blit(bg, (0, 0))
            pg.display.update()


pg.quit()

