import csv
import random

fh1 = 'C:\\Users\\User\\Desktop\\PBC.txt'
fh1 = open(fh1, 'r', encoding = 'utf-16', newline = '')
csv1 = csv.reader(fh1, delimiter = '\t')
reader = csv.DictReader(fh1, delimiter = '\t')

from PIL import Image
def recommend_know(dist, theme):
	'''
    知道去哪裡所回傳的景點
    需要傳入的值: 行政區、心理測驗的主題結果
    '''
	fh1 = 'C:\\Users\\Use\\Documents\\GitHub\\完整景點資料庫.csv'
	fh1 = open(fh1, 'r', encoding='utf-8', newline='')
	csv1 = csv.reader(fh1)
	reader = csv.DictReader(fh1)

	data = {}
	spot = []
	for row in reader:
		if row["行政區"] == dist:
			if row["主題"] not in data:
				data[row["主題"]] = [row["景點名稱"]]
			else:
				data[row["主題"]].append(row["景點名稱"])

	#print(data)
	count = 0
	for item in range(len(data[theme])):  # 隨機輸出兩兩比較
		if count == 0:  # 第一輪抽出兩個景點
			data_item = random.choice(data[theme])
			data[theme].remove(data_item)
			ano_item = random.choice(data[theme])
			data[theme].remove(ano_item)
			#print(data_item, ano_item)
			count += 1
			im1 = Image.open('C:\\Users\\User\\Documents\\GitHub\\New\\picture\\'+str(dist)+'\\'+str(data_item)
			im1.show()
			spot.append(data_item)
			im2 = Image.open('C:\\Users\\User\\Documents\\GitHub\\New\\picture\\'+str(dist)+'\\'+str(ano_item)
			im2.show()
			spot.append(ano_item)

		elif len(data[theme]) > 0:  # 其他輪抽出一個景點
			data_item = random.choice(data[theme])
			data[theme].remove(data_item)
			im1 = Image.open('C:\\Users\\User\\Documents\\GitHub\\New\\picture\\'+str(dist)+'\\'+str(data_item)
			im1.show()
			spot.append(data_item)
			
	return spot
			


def recommend_notknow(dist, theme):
	'''
	不知道去哪裡所回傳的景點
	需要傳入的值: 心理測驗的主題結果、輪盤的行政區
	'''
	location = []
	for row in reader:
		if row['行政區'] == dist and row['主題'] == theme:
			location.append(row['景點名稱'])

	location_item = random.choice(location)
	#print(location_item)
	return location_item
	

def show_info(locat):
	'''
	回傳景點資訊到最終頁面
	'''
	
	pass
		

