import pygame as pg

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


def test_page():
    """載入心理測驗頁面起始時所需的頁面及文字"""

    background_image0 = pg.image.load("第二頁背景.png")
    background_image = pg.transform.scale(background_image0, (1280, 720)).convert()
    bg.blit(background_image, (0, 0)) #載入背景畫面到bg上

    title = my_titlefont1.render("選出現在最符合你的一句話", True, (0, 0, 0))
    bg.blit(title, (90, 50)) #載入題目文字到bg上

    button_image0 = pg.image.load("亮按鈕.png").convert()
    button_image0.set_alpha(200)
    button_image = pg.transform.scale(button_image0, (1000, 100)).convert()
    bg.blit(button_image, (110, 160))
    bg.blit(button_image, (110, 293))
    bg.blit(button_image, (110, 426))
    bg.blit(button_image, (110, 560))   #載入經透明度及尺寸調整的選項按鈕四個到bg上

    text1 = my_textfont1.render("好熱好累好不想做事，好想躺在床上度過一整天", True, (255, 255, 255))
    bg.blit(text1, (130, 190)) #載入選項文字到bg上

    text2 = my_textfont1.render("被都市的喧囂所埋沒的社畜，每天漫無目的地遊走", True, (255, 255, 255))
    bg.blit(text2, (130, 323)) #載入選項文字到bg上

    text3 = my_textfont1.render("隨時調整心態，面對突然而來的挑戰", True, (255, 255, 255))
    bg.blit(text3, (130, 456)) #載入選項文字到bg上

    text4 = my_textfont1.render("太陽從東邊升起，從西邊落下", True, (255, 255, 255))
    bg.blit(text4, (130, 590)) #載入選項文字到bg上

def roulette_page():
    """載入輪盤頁面起始時所需的文字及圖片"""
    background_image0 = pg.image.load("第三頁背景.png")
    background_image = pg.transform.scale(background_image0, (1280, 720)).convert()
    bg.blit(background_image, (0, 0))  #載入背景畫面到bg上

    #roulette_image0 = pg.image.load("roulette.png")
    #roulette_image = pg.transform.scale(roulette_image0, (1150, 1150)).convert_alpha()
    #pg.transform.rotate(roulette_image, 10)
    #bg.blit(roulette_image,(50, 150))

    pg.draw.polygon(bg, (0, 0, 0), ((580, 50), (680, 50), (630, 260)))
    # 在bg上畫倒三角形作為指針用

def compare_page():
    """載入兩兩選擇起始時所需的靜態文字及圖片"""
    background_image0 = pg.image.load("第四頁背景.png")
    background_image = pg.transform.scale(background_image0, (1280, 720)).convert()
    bg.blit(background_image, (0, 0))


def spotintro_page():
    """載入景點介紹頁所需的文字及圖片"""
    background_image0 = pg.image.load("第五頁背景.png")
    background_image = pg.transform.scale(background_image0, (1280, 720)).convert()
    bg.blit(background_image, (0, 0)) #載入背景畫面到bg上

    location_image0 = pg.image.load("placeholder.png")
    location_image = pg.transform.scale(location_image0, (48, 48)).convert_alpha()
    bg.blit(location_image, (25, 110)) #載入地址圖示到bg上

    tickets_image0 = pg.image.load("tickets.png")
    ticket_image = pg.transform.scale(tickets_image0, (48, 48)).convert_alpha()
    bg.blit(ticket_image, (25, 165)) #載入門票圖示到bg上

    time_image0 = pg.image.load("001-time.png")
    time_image = pg.transform.scale(time_image0, (45, 45)).convert_alpha()
    bg.blit(time_image, (27, 245)) #載入營業時間圖示到bg上

    picture_image0 = pg.image.load("002-picture.png")
    picture_image = pg.transform.scale(picture_image0, (48, 48)).convert_alpha()
    bg.blit(picture_image, (25, 580)) #載入圖片來源圖示到bg上

    text2 = my_titlefont2.render("景點名", True, (0, 0, 0))
    bg.blit(text2, (50, 30))  #載入景點名稱到bg上

    text3 = my_textfont2.render("臺北市萬華區中華路一段", True, (0, 0, 0))
    bg.blit(text3, (80, 120)) #載入景點地址到bg上

    text3 = my_textfont2.render("門票：無", True, (0, 0, 0))
    bg.blit(text3, (80, 175)) #載入門票資訊到bg上

    text4 = my_textfont2.render("營業時間：", True, (0, 0, 0))
    bg.blit(text4, (80, 255)) #載入營業時間文字到bg上

    opentime1 = "(一)：09:00 - 17:30 "
    opentime2 = "(二)：09:00 - 17:30 "
    opentime3 = "(三)：09:00 - 17:30 "
    opentime4 = "(四)：09:00 - 17:30 "
    opentime5 = "(五)：09:00 - 17:30 "
    opentime6 = "(六)：09:00 - 17:30 "
    opentime7 = "(日)：09:00 - 17:30 "  #輸入一到日的營業時間

    text5 = my_textfont2.render(opentime1, True, (0, 0, 0))
    bg.blit(text5, (100, 300))  #載入營業時間文字到bg上

    text6 = my_textfont2.render(opentime2, True, (0, 0, 0))
    bg.blit(text6, (100, 340))#載入營業時間文字到bg上

    text7 = my_textfont2.render(opentime3, True, (0, 0, 0))
    bg.blit(text7, (100, 380))#載入營業時間文字到bg上

    text8 = my_textfont2.render(opentime4, True, (0, 0, 0))
    bg.blit(text8, (100, 420))#載入營業時間文字到bg上

    text9 = my_textfont2.render(opentime5, True, (0, 0, 0))
    bg.blit(text9, (100, 460)) #載入營業時間文字到bg上

    text10 = my_textfont2.render(opentime6, True, (0, 0, 0))
    bg.blit(text10, (100, 500)) #載入營業時間文字到bg上

    text11 = my_textfont2.render(opentime7, True, (0, 0, 0))
    bg.blit(text11, (100, 540))  #載入營業時間文字到bg上

    text12 = my_textfont2.render("圖片來源：", True, (0, 0, 0))
    bg.blit(text12, (80, 590)) #載入圖片來源文字到bg上

    text13 = my_textfont2.render("臺北旅遊網", True, (0, 0, 0))
    bg.blit(text13, (90, 640)) #載入圖片來源到bg上

    spot_image0 = pg.image.load("第一頁背景.png")
    spot_image = pg.transform.scale(spot_image0, (640, 360)).convert()
    bg.blit(spot_image, (540, 50))  #載入景點圖片到bg上

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
    bg.blit(text17, (540, 540))   #載入介紹文字到bg上


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
    mouse = pg.mouse.get_pos() #定位滑鼠所在位置
    if Acum == 1 and Cum == 3: #當在兩兩選擇頁面選擇右邊圖片時進入此if

        background_image0 = pg.image.load("第四頁背景.png")
        background_image = pg.transform.scale(background_image0, (1280, 720)).convert()
        bg.blit(background_image, (0, 0))
        a_image0 = pg.image.load("選擇卡.png")
        a_image = pg.transform.scale(a_image0, (400, 500))
        bg.blit(a_image, (100 - astep, 100))
        bg.blit(a_image, (800, 100))
        text1 = my_textfont.render("大安區", True, (0, 0, 0))
        bg.blit(text1, (950, 500))
        #讀取不會動的圖片及文字

        if move_time == 0 and astep > 600: #如果卡片向左完全移動出頁面外，則改變移動模式為1
            text1 = my_textfont.render("內湖區", True, (0, 0, 0))
            bg.blit(text1, (250 - astep, 500))
            move_time = 1
            if choose_time == 3: #若淘汰次數達三次，則跳至右邊卡片勝利頁面
                Acum = 3
        elif move_time == 0 and astep <= 600: # 若卡片未完全移出視窗外，則遞增astep值，使圖片位置持續左移
            astep += 50
            text1 = my_textfont.render("內湖區", True, (0, 0, 0))
            bg.blit(text1, (250 - astep, 500))
        elif move_time == 1 and astep > 0: #若移動模式為１，則astep遞減，使圖片向右移動，直到卡片回到原來位置
            astep -= 50
            text1 = my_textfont.render("南港區", True, (0, 0, 0))
            bg.blit(text1, (250 - astep, 500))
        elif move_time == 1 and astep < 0:  # 防止卡片向右過頭
            astep = 0
            text1 = my_textfont.render("南港區", True, (0, 0, 0))
            bg.blit(text1, (250 - astep, 500))
        elif move_time == 1 and astep == 0: # 如果卡片回到原來位置，則Acum跳回0，回到兩兩起始頁面，同時初始化移動模式，淘汰次數加一
            text1 = my_textfont.render("南港區", True, (0, 0, 0))
            bg.blit(text1, (250 - astep, 500))
            choose_time += 1
            Acum = 0
            move_time = 0
        screen.blit(bg, (0, 0)) # 將bg隨時的更動顯示在螢幕上
        pg.display.update()


    if Acum == 2 and Cum == 3: #右邊卡片的移動情形，跟左邊的移動差不多，只有astep的方向與判別有換

        background_image0 = pg.image.load("第四頁背景.png")
        background_image = pg.transform.scale(background_image0, (1280, 720)).convert()
        bg.blit(background_image, (0, 0))
        a_image0 = pg.image.load("選擇卡.png")
        a_image = pg.transform.scale(a_image0, (400, 500))
        bg.blit(a_image, (100, 100))
        bg.blit(a_image, (800 + astep, 100))
        text1 = my_textfont.render("內湖區", True, (0, 0, 0))
        bg.blit(text1, (250, 500))

        if move_time == 0 and astep >= 600:
            text1 = my_textfont.render("大安區", True, (0, 0, 0))
            bg.blit(text1, (950 + astep, 500))
            move_time = 1
            if choose_time == 3:
                Acum = 4
        elif move_time == 0 and astep < 600:
            astep += 50
            text1 = my_textfont.render("大安區", True, (0, 0, 0))
            bg.blit(text1, (950 + astep, 500))
        elif move_time == 1 and astep > 0:
            astep -= 50
            text1 = my_textfont.render("北投區", True, (0, 0, 0))
            bg.blit(text1, (950 + astep, 500))
        elif move_time == 1 and astep < 0:
            astep = 0
            text1 = my_textfont.render("北投區", True, (0, 0, 0))
            bg.blit(text1, (950 + astep, 500))
        elif move_time == 1 and astep == 0:
            text1 = my_textfont.render("北投區", True, (0, 0, 0))
            bg.blit(text1, (950 + astep, 500))
            choose_time += 1
            Acum = 0
            move_time = 0
        screen.blit(bg, (0, 0))
        pg.display.update()

    if Acum == 3 and Cum == 3:  #若右邊卡片獲勝則至此頁面，右卡隨著bstep的遞增會移到中間
        background_image0 = pg.image.load("第四頁背景.png")
        background_image = pg.transform.scale(background_image0, (1280, 720)).convert()
        bg.blit(background_image, (0, 0))
        a_image0 = pg.image.load("選擇卡.png")
        a_image = pg.transform.scale(a_image0, (400, 500))
        #bg.blit(a_image, (100 - astep, 100))
        bg.blit(a_image, (800 - bstep, 100))
        text1 = my_textfont.render("大安區", True, (0, 0, 0))
        bg.blit(text1, (950 - bstep, 500))
        if bstep < 350:
            bstep += 50
        screen.blit(bg, (0, 0))
        pg.display.update()
        for event in pg.event.get(): #卡片到中間時按下滑鼠，則跳至景點介紹頁面，並初始化變數，防止再度遊玩時出錯
            if event.type == pg.MOUSEBUTTONDOWN:
                Cum = 5
                Acum = 0
                choose_time = 0
                astep = 0
                bstep = 0
                move_time = 0

    if Acum == 4 and Cum == 3: #若左邊卡片獲勝則至此頁面，左卡隨著bstep的遞增會移到中間
        background_image0 = pg.image.load("第四頁背景.png")
        background_image = pg.transform.scale(background_image0, (1280, 720)).convert()
        bg.blit(background_image, (0, 0))
        a_image0 = pg.image.load("選擇卡.png")
        a_image = pg.transform.scale(a_image0, (400, 500))
        #bg.blit(a_image, (100 - astep, 100))
        bg.blit(a_image, (100 + bstep, 100))
        text1 = my_textfont.render("內湖區", True, (0, 0, 0))
        bg.blit(text1, (250 + bstep, 500))
        if bstep < 350:
            bstep += 50
        screen.blit(bg, (0, 0))
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                Cum = 5
                Acum = 0
                choose_time = 0
                astep = 0
                bstep = 0
                move_time = 0






    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if Cum == 0:            #用Cum在這做頁面的分涼
            welcome_page()
        if Cum == 0.5:
            test_page()
            if event.type:
                Cum = 4
        if Cum == 1:
            test_page()
        if Cum == 2:
            roulette_page()
        if Cum == 3:
            compare_page()
        if Cum == 4:
            test_page()
        if Cum == 5:
            spotintro_page()
        if Cum == 6:
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

            #以下是若滑鼠游標移到各個行政區的按鈕上，按鈕會變亮，若此時按下去，則會進入Cum = 0.5，心理測驗的過度頁面
            # 按下返回則會回到首頁
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
            #if event.type == pg.MOUSEBUTTONDOWN:
                # print(mouse)
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

        if 310 < mouse[0] < 950 and 480 < mouse[1] < 560 and Cum == 0: #用滑鼠游標位置判別亮、暗按鈕的切換，按下按鈕會到心理測驗
            button_image = pg.image.load("按鈕.png").convert()
            button_image.set_alpha(150)
            bg.blit(button_image, (330, 480))
            text2 = my_textfont.render("我還沒有想法", True, (255, 255, 255))
            bg.blit(text2, (570, 505))
            screen.blit(bg, (0, 0))
            pg.display.update()
            if event.type == pg.MOUSEBUTTONDOWN:
                Cum = 1
        elif 310 < mouse[0] < 950 and 350 < mouse[1] < 430 and Cum == 0:#用滑鼠游標位置判別亮、暗按鈕的切換，按下按鈕會到區選單
            button_image = pg.image.load("按鈕.png").convert()
            button_image.set_alpha(150)
            bg.blit(button_image, (330, 350))
            text2 = my_textfont.render("我想去___區", True, (255, 255, 255))
            bg.blit(text2, (570, 375))
            screen.blit(bg, (0, 0))
            pg.display.update()
            if event.type == pg.MOUSEBUTTONDOWN:
                Cum = 6
            #以下為用滑鼠游標位置，判別心理測驗選項的亮、暗按鈕的切換 ，按下去後隨著有無選擇行政區，會到不同頁面
        elif 110 < mouse[0] < 1110 and 160 < mouse[1] < 260 and (Cum == 1 or Cum == 4):
            button_image0 = pg.image.load("選項.png").convert()
            button_image0.set_alpha(150)
            button_image = pg.transform.scale(button_image0, (1000, 100)).convert()
            bg.blit(button_image, (110, 160))
            text1 = my_textfont1.render("好熱好累好不想做事，好想躺在床上度過一整天", True, (255, 255, 255))
            bg.blit(text1, (130, 190))
            screen.blit(bg, (0, 0))
            pg.display.update()
            if event.type == pg.MOUSEBUTTONDOWN and Cum == 1:
                Cum = 2
            if event.type == pg.MOUSEBUTTONDOWN and Cum == 4:
                Cum = 3
        elif 110 < mouse[0] < 1110 and 293 < mouse[1] < 393 and (Cum == 1 or Cum == 4):
            button_image0 = pg.image.load("選項.png").convert()
            button_image0.set_alpha(150)
            button_image = pg.transform.scale(button_image0, (1000, 100)).convert()
            bg.blit(button_image, (110, 293))
            text1 = my_textfont1.render("被都市的喧囂所埋沒的社畜，每天漫無目的地遊走", True, (255, 255, 255))
            bg.blit(text1, (130, 323))
            screen.blit(bg, (0, 0))
            pg.display.update()
            if event.type == pg.MOUSEBUTTONDOWN and Cum == 1:
                Cum = 2
            if event.type == pg.MOUSEBUTTONDOWN and Cum == 4:
                Cum = 3
        elif 110 < mouse[0] < 1110 and 426 < mouse[1] < 526 and (Cum == 1 or Cum == 4):
            button_image0 = pg.image.load("選項.png").convert()
            button_image0.set_alpha(150)
            button_image = pg.transform.scale(button_image0, (1000, 100)).convert()
            bg.blit(button_image, (110, 426))
            text1 = my_textfont1.render("隨時調整心態，面對突然而來的挑戰", True, (255, 255, 255))
            bg.blit(text1, (130, 456))
            screen.blit(bg, (0, 0))
            pg.display.update()
            if event.type == pg.MOUSEBUTTONDOWN and Cum == 1:
                Cum = 2
            if event.type == pg.MOUSEBUTTONDOWN and Cum == 4:
                Cum = 3
        elif 110 < mouse[0] < 1110 and 560 < mouse[1] < 660 and (Cum == 1 or Cum == 4):
            button_image0 = pg.image.load("選項.png").convert()
            button_image0.set_alpha(150)
            button_image = pg.transform.scale(button_image0, (1000, 100)).convert()
            bg.blit(button_image, (110, 560))
            text1 = my_textfont1.render("太陽從東邊升起，從西邊落下", True, (255, 255, 255))
            bg.blit(text1, (130, 590))
            screen.blit(bg, (0, 0))
            pg.display.update()
            if event.type == pg.MOUSEBUTTONDOWN and Cum == 1:
                Cum = 2
            if event.type == pg.MOUSEBUTTONDOWN and Cum == 4:
                Cum = 3
        # 以上為用滑鼠游標位置，判別心理測驗選項的亮、暗按鈕的切換 ，按下去後隨著有無選擇行政區，會到不同頁面

        #下面兩個ｅｌｉｆ用來交替兩張輪盤圖片，達到模擬旋轉效果，且變換時累加Time
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

        elif Cum == 2 and Time == 30: #當累加次數達一定，則跳出隨機結果，按下確定後跳到景點介紹頁面
            roulette_image0 = pg.image.load("roulette.png")
            roulette_image = pg.transform.scale(roulette_image0, (1150, 1150)).convert_alpha()
            # pg.transform.rotate(roulette_image, 10)
            bg.blit(roulette_image, (50, 150))
            window_image = pg.image.load("視窗.png")
            bg.blit(window_image, (190, 150))
            text1 = my_titlefont.render("內湖區", True, (0, 0, 0)) #此欄輸入隨機結果
            bg.blit(text1, (560, 230))
            screen.blit(bg, (0, 0))
            pg.display.update()
            if 682 < mouse[0] < 992 and 348 < mouse[1] < 458: # 此為用滑鼠判別確定鍵的亮、暗按鈕
                sure_image0 = pg.image.load("確定.png")
                sure_image = pg.transform.scale(sure_image0, (310, 110))
                bg.blit(sure_image, (682, 348))
                screen.blit(bg, (0, 0))
                pg.display.update()
                if event.type == pg.MOUSEBUTTONDOWN:
                    Time = 0
                    Cum = 5
        elif Cum == 5:   #此為載入再玩一次鍵的初始畫面，及滑鼠游標改變的亮、暗按鈕變化
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
                if event.type == pg.MOUSEBUTTONDOWN: # 若按下重玩鍵，回到首頁
                    Cum = 0

        elif Cum == 3 and Acum == 0:  # 此為兩兩選擇的初始頁面，及每次卡片更換完會顯示的頁面
            a_image0 = pg.image.load("選擇卡.png")
            a_image = pg.transform.scale(a_image0, (400, 500))
            bg.blit(a_image, (100, 100))
            bg.blit(a_image, (800, 100))
            text1 = my_textfont.render("內湖區", True, (0, 0, 0))
            bg.blit(text1, (250, 500))
            text1 = my_textfont.render("大安區", True, (0, 0, 0))
            bg.blit(text1, (950, 500))
            screen.blit(bg, (0, 0))
            pg.display.update()
            if event.type == pg.MOUSEBUTTONDOWN and 100 < mouse[0] < 500 and 100 < mouse[1] < 600:
                Acum = 2
            if event.type == pg.MOUSEBUTTONDOWN and 800 < mouse[0] < 1200 and 100 < mouse[1] < 600:
                Acum = 1
            # 若按下右卡片，左邊移動，按下左卡片，右邊移動



        else: #這兩行指令表示畫面的更新，若bg上的東西有更改，底下一定要加這兩行，才能從螢幕看到變化
            screen.blit(bg, (0, 0))
            pg.display.update()


pg.quit()

