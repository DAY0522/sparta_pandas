import pandas as pd

data1 = pd.read_csv('data/chicken_07.csv') #데이터 불러오기
print(data1)

print(data1.tail(5)) #데이터의 맨 뒤에있는 5개만 불러오기
print(data1.describe())

print(set(data1['성별']), len(set(data1['성별'])))
print(set(data1['연령대']), len(set(data1['연령대'])))
print(set(data1['요일']), len(set(data1['요일'])))
print(set(data1['시군구']), len(set(data1['시군구'])))

data2 = pd.read_csv('data/chicken_08.csv')
data3 = pd.read_csv('data/chicken_09.csv')

data4 = pd.concat([data1, data2, data3])
print(data4)

data4 = data4.reset_index(drop=True)
print(data4)
