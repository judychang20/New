import pygame as pg

def welcome_page():
    pg.init()
    width, height = 1280, 720
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("標題標題")
    my_titlefont = pg.font.Font("myfont.ttf", 56)
    my_textfont = pg.font.Font("myfont.ttf", 25)

    bg = pg.Surface(screen.get_size()).convert()

    icon_image = pg.image.load("icon.png").convert()
    pg.display.set_icon(icon_image)

    background_image0 = pg.image.load("第一頁背景.png")
    background_image = pg.transform.scale(background_image0, (1280, 720)).convert()
    bg.blit(background_image, (0, 0))

    title = my_titlefont.render("標題標題標題", True, (0, 0, 0))
    bg.blit(title, (475, 100))

    text1 = my_textfont.render("文字文字文字文字？", True, (0, 0, 0))
    bg.blit(text1, (540, 275))

    button_image = pg.image.load("按鈕.png").convert()
    button_image.set_alpha(150)
    bg.blit(button_image, (330, 350))
    bg.blit(button_image, (330, 480))

    text2 = my_textfont.render("我想去", True, (255, 255, 255))
    bg.blit(text2, (570, 375))

    text2 = my_textfont.render("我還沒有想法", True, (255, 255, 255))
    bg.blit(text2, (570, 505))

    screen.blit(bg, (0, 0))
    pg.display.update()

    running = True
    while running:
        mouse = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN and 310 < mouse[0] < 950 and 475 < mouse[1] < 560:
                test_page()




def test_page():
    pg.init()
    width, height = 1280, 720
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("標題標題")
    my_titlefont = pg.font.Font("myfont.ttf", 35)
    my_textfont = pg.font.Font("myfont.ttf", 23)

    bg = pg.Surface(screen.get_size()).convert()

    icon_image = pg.image.load("icon.png").convert()
    pg.display.set_icon(icon_image)

    background_image0 = pg.image.load("第二頁背景.png")
    background_image = pg.transform.scale(background_image0, (1280, 720)).convert()
    bg.blit(background_image, (0, 0))

    title = my_titlefont.render("心理測驗題目題目題目", True, (0, 0, 0))
    bg.blit(title, (90, 50))

    button_image0 = pg.image.load("選項.png").convert()
    button_image0.set_alpha(150)
    button_image = pg.transform.scale(button_image0, (1000, 100)).convert()
    bg.blit(button_image, (110, 160))
    bg.blit(button_image, (110, 293))
    bg.blit(button_image, (110, 426))
    bg.blit(button_image, (110, 560))

    lightbutton0 = pg.image.load("亮按鈕.png").convert()
    lightbutton0.set_alpha(150)
    lightbutton = pg.transform.scale(lightbutton0, (1000, 100)).convert()
    cum = 0

    text1 = my_textfont.render("選項A", True, (255, 255, 255))
    bg.blit(text1, (130, 190))

    text2 = my_textfont.render("選項B", True, (255, 255, 255))
    bg.blit(text2, (130, 323))

    text3 = my_textfont.render("選項C", True, (255, 255, 255))
    bg.blit(text3, (130, 456))

    text4 = my_textfont.render("選項D", True, (255, 255, 255))
    bg.blit(text4, (130, 590))

    screen.blit(bg, (0, 0))
    pg.display.update()

    running = True
    while running:
        mouse = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN and 110 < mouse[0] < 1110 and 160 < mouse[1] < 260:
                # 選擇Ａ選項
                roulette_page()
            if event.type == pg.MOUSEBUTTONDOWN and 110 < mouse[0] < 1110 and 293 < mouse[1] < 393:
                # 選擇B選項
                roulette_page()
            if event.type == pg.MOUSEBUTTONDOWN and 110 < mouse[0] < 1110 and 426 < mouse[1] < 526:
                # 選擇C選項
                roulette_page()
            if event.type == pg.MOUSEBUTTONDOWN and 110 < mouse[0] < 1110 and 560 < mouse[1] < 660:
                # 選擇D選項
                roulette_page()

def roulette_page():
    pg.init()
    width, height = 1280, 720
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("標題標題")
    my_titlefont = pg.font.Font("myfont.ttf", 35)
    my_textfont = pg.font.Font("myfont.ttf", 23)

    bg = pg.Surface(screen.get_size()).convert()

    icon_image = pg.image.load("icon.png").convert()
    pg.display.set_icon(icon_image)

    background_image0 = pg.image.load("第三頁背景.png")
    background_image = pg.transform.scale(background_image0, (1280, 720)).convert()
    bg.blit(background_image, (0, 0))

    roulette_image0 = pg.image.load("roulette.png")
    roulette_image = pg.transform.scale(roulette_image0, (1150, 1150)).convert_alpha()
    pg.transform.rotate(roulette_image, 10)
    #bg.blit(roulette_image,(50, 150))

    pg.draw.polygon(bg, (0,0,0),((580,50), (680, 50), (630, 260)))

    #for i in range(50):
        #pg.transform.rotate(roulette_image, i)
        #bg.blit(roulette_image, (50, 150))
        #pg.display.update()

    screen.blit(bg, (0, 0))
    pg.display.update()

    running = True
    while running:

        mouse = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                spotintro_page()
        a = pg.transform.rotate(roulette_image, 40)
        screen.blit(a, (0, 0))
        #screen.blit(bg, (0, 0))
        pg.display.update()

def choosebetween_page():
    pass

def spotintro_page():
    pg.init()
    width, height = 1280, 720
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("標題標題")
    my_titlefont = pg.font.Font("myfont.ttf", 35)
    my_textfont = pg.font.Font("myfont.ttf", 23)

    bg = pg.Surface(screen.get_size()).convert()

    icon_image = pg.image.load("icon.png").convert()
    pg.display.set_icon(icon_image)

    screen.blit(bg, (0, 0))
    pg.display.update()



    running = True
    while running:
        mouse = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                pg.init()
                welcome_page()


welcome_page()

pg.quit()
