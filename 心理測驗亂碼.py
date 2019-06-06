import csv
import random

# =================心理測驗亂碼＆心理測驗配合景點類別=================


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


# =================程式碼歷史紀錄=================
'''
dist = input()

fn1 = "/Users/Apple/Desktop/PBC.txt"
fh1 = open(fn1, 'r', newline = '', encoding = 'utf-16')
csv1 = csv.reader(fh1, delimiter = '\t')
#print(next(csv1))
reader1 = csv.DictReader(fh1, delimiter = '\t')
'''

'''
attr = dict()
for row in reader1:
    #print(row)
    if row['行政區'] == dist:
        #print(dist)

        if row['主題'] not in attr:
            attr[row['主題']] = [row['景點名稱'], row['簡介'], row['地址'], row['有無門票'], row['門票費用'], row['開放時間-一']]
        else:
            attr[row['主題']].append([row['景點名稱'], row['簡介'], row['地址'], row['有無門票'], row['門票費用'], row['開放時間-一']])
print(attr)
'''
# 景點類別為key，心理測驗為value（一個list）的dictionary


'''
test = dict()

for theme in next(reader2):
    print(theme)
    test[theme] = []
for row in reader2:
    print(row)
    test['宗教與古蹟'].append(row['宗教與古蹟'])
    test['藝文與文化'].append(row['藝文與文化'])
    test['休閒與生態'].append(row['休閒與生態'])
    test['商圈'].append(row['商圈'])
print(test)

# 心理測驗亂數，用list去randomize（random.），各個類別產出一個心理測驗答案
test_hsty = random.choice(test['宗教與古蹟'])
test_cltr = random.choice(test['藝文與文化'])
test_ntr = random.choice(test['休閒與生態'])
test_shp = random.choice(test['商圈'])
print(test_hsty)
print(test_cltr)
print(test_ntr)
print(test_shp)

# 傳入的值會是哪個心理測驗答案
'''






