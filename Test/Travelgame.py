import pygame as pg
import tkinter as tk

def welcome_page():
    pg.init()

    Cum = 0
    width, height = 1280, 720
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("臺北隨便玩")
    my_font = pg.font.Font("myfont.ttf", 56)
    my_font1 = pg.font.Font("myfont.ttf", 25)
    mouse = pg.mouse.get_pos()

    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((140, 186, 191))

    image0 = pg.image.load("第一頁背景.png")
    image = pg.transform.scale(image0, (1280, 720))
    image.convert()
    bg.blit(image, (0,0))

    image1 = pg.image.load("icon.png")
    image1.convert()
    pg.display.set_icon(image1)

    text_surface = my_font.render("標題標題標題", True, (0,0,0))
    bg.blit(text_surface, (475, 100))

    text1 = my_font1.render("文字文字文字文字？", True, (0, 0, 0))
    bg.blit(text1, (540, 275))

    image2 = pg.image.load("按鈕.png").convert()
    image2.set_alpha(150)
    bg.blit(image2, (330, 350))

    image3 = pg.image.load("按鈕.png").convert()
    image2.set_alpha(150)
    bg.blit(image2, (330, 480))

    text2 = my_font1.render("我還沒有想法", True, (255, 255, 255))
    bg.blit(text2, (570, 505))

    image4 = pg.image.load("第一頁背景.png")
    image5 = pg.transform.scale(image4, (1280, 720))
    image5.convert()
    if Cum == 1:
        bg.blit(image5, (0, 0))


    button = tk.Button(width = 100, height = 100)
    screen.blit(button, (500, 500))

    screen.blit(bg, (0,0))
    pg.display.update()


    running = True
    while running:
        mouse = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                print(mouse[0], mouse[1])
            if event.type == pg.MOUSEBUTTONDOWN and 350 < mouse[0] < 850 and 500 < mouse[1] < 650:
                second_page()

def second_page():
    pg.init()

    Cum = 0
    width, height = 1280, 720
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("臺北隨便玩")
    my_font = pg.font.Font("myfont.ttf", 56)
    my_font1 = pg.font.Font("myfont.ttf", 25)
    x, y = pg.mouse.get_pos()
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    image0 = pg.image.load("第二頁背景.png")
    image = pg.transform.scale(image0, (1280, 720))
    image.convert()
    bg.blit(image, (0,0))

    screen.blit(bg, (0, 0))
    pg.display.update()



welcome_page()



pg.quit()
