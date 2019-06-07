import csv
import random

# =================心理測驗亂碼＆心理測驗配合景點類別=================

'''
class ThemeToTest:
    def __init__(self, random_test):
        self.name = random_test[0]
        self.hst = random_test[1]
        self.cltr = random_test[2]
        self.ntr = random_test[3]
        self.shp = random_test[4]

fn2 = "/Users/Apple/Desktop/商管程設/New/心理測驗.csv"
fh2 = open(fn2, 'r', newline = '', encoding = 'utf-8')
csv2 = csv.reader(fh2)
reader2 = csv.DictReader(fh2)

# 輸入："不知道去哪裡"
# 產出：a list of 題庫
test_questions = []
head = next(csv2)
for row in csv2:
    test_questions.append(row)
print(test_questions)

# 從題庫隨機選擇某個心理測驗題目
random_question = random.choice(test_questions)
print(random_question)

# 確定介面產生題目名稱和四個選項
test = ThemeToTest(random_question)
print(test.name)
print(test.hst)
print(test.cltr)
print(test.ntr)
print(test.shp)


# 接著使用者會輸入四個選項其中一個，
# 傳入值：四個選項其中一個選項的字串
# 輸出：景點類別
def test_choice(choice):
    if choice == test.hst:
        return "宗教與古蹟"
    elif choice == test.cltr:
        return "藝文與文化"
    elif choice == test.ntr:
        return "休閒與生態"
    elif choice == test.shp:
        return "商圈"


# 傳入值會在這裡呦
# 輸出：景點類別
print(test_choice(input()))


# =================輪盤（行政區）亂碼=================


# 生出12個行政區的list
# 輸出：隨機選擇的行政區
def random_dist():
    dist = []
    head2 = next(csv1)
    for line in csv1:
        column = line[0]
        if column not in dist and column != "":
            dist.append(column)
    return random.choice(dist)


fn1 = "/Users/Apple/Desktop/商管程設/New/完整景點資料庫.csv"
fh1 = open(fn1, 'r', newline='', encoding='utf-8')
csv1 = csv.reader(fh1)
reader1 = csv.DictReader(fh1)

print(random_dist())

'''
# =================景點細節回傳=================
class Spot:
    def __init__(self, detail):
        self.name = detail[0]
        self.intro = detail[1]
        self.address = detail[2]
        self.ticket = detail[3]
        self.open1 = detail[4]
        self.open2 = detail[5]
        self.open3 = detail[6]
        self.open4 = detail[7]
        self.open5 = detail[8]
        self.open6 = detail[9]
        self.open7 = detail[10]


fn2 = "/Users/Apple/Desktop/商管程設/New/完整景點資料庫.csv"
fh2 = open(fn2, 'r', newline = '', encoding = 'utf-8')
csv2 = csv.reader(fh2)
reader2 = csv.DictReader(fh2)
head = next(csv2)

# 輸入是景點名稱！

def show_info(spot_name):
    for row in csv2:
        if spot_name == row[2]:
            description = row[2:]
            print(description)
            return description

show_info("北投文物館") # 要使用這個來呼叫class

spot_info = Spot(show_info("北投文物館")) # Spot內要改成上述
print(spot_info.ticket)

# =================兩兩選擇回傳圖片=================
'''
from PIL import Image


def recommend_know(dist, theme):
    
    #知道去哪裡所回傳的景點
    #需要傳入的值: 行政區、心理測驗的主題結果
    
    fn1 = "/Users/Apple/Desktop/商管程設/New/完整景點資料庫.csv"
    fh1 = open(fn1, 'r', newline='', encoding='utf-8')
    reader1 = csv.DictReader(fh1)

    data = {}
    spot = []
    for row in reader1:
        if row["行政區"] == dist:
            if row["主題"] not in data:
                data[row["主題"]] = [row["景點名稱"]]
            else:
                data[row["主題"]].append(row["景點名稱"])

    # print(data)
    count = 0
    for item in range(len(data[theme])):  # 隨機輸出兩兩比較
        if count == 0:  # 第一輪抽出兩個景點
            data_item = random.choice(data[theme])
            data[theme].remove(data_item)
            ano_item = random.choice(data[theme])
            data[theme].remove(ano_item)
            # print(data_item, ano_item)
            count += 1
            im1 = Image.open('/Users/Apple/Desktop/商管程設/New/picture/' + str(dist) + '/' + str(data_item) + ".jpg")
            im1.show()
            spot.append(data_item)
            im2 = Image.open('/Users/Apple/Desktop/商管程設/New/picture/' + str(dist) + '/' + str(ano_item) + ".jpg")
            im2.show()
            spot.append(ano_item)

        elif len(data[theme]) > 0:  # 其他輪抽出一個景點
            data_item = random.choice(data[theme])
            data[theme].remove(data_item)
            im1 = Image.open('/Users/Apple/Desktop/商管程設/New/picture/' + str(dist) + '/' + str(data_item) + ".jpg")
            im1.show()
            spot.append(data_item)

    return spot

recommend_know("北投", "宗教與古蹟")
# 跑完可能會出現：LSOpenURLsWithRole() failed for the application /Applications/Preview.app with error -10810 for the file /var/folders/l1/0ktl75017bs2c19qpc64v7s40000gn/T/tmpj3y9z7io.PNG.
# 要請再注意
'''