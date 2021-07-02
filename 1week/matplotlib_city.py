import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_csv('data/chicken_07.csv') #데이터 불러오기
data2 = pd.read_csv('data/chicken_08.csv')
data3 = pd.read_csv('data/chicken_09.csv')

data4 = pd.concat([data1, data2, data3])
data4 = data4.reset_index(drop=True)

sum_of_calls_by_city = data4.groupby('시군구')['통화건수'].sum()
sorted_sum_of_calls_by_city = sum_of_calls_by_city.sort_values(ascending=False) #descending이 있는 게 아니라 ascending의 false가 descending을 의미
print(sorted_sum_of_calls_by_city)

plt.figure(figsize=(10,5))
plt.rcParams['font.family'] = "Malgun Gothic"
plt.bar(sorted_sum_of_calls_by_city.index, sorted_sum_of_calls_by_city)
plt.xlabel('지역별')
plt.xticks(rotation = 45) #x축 글씨를 45도 기울임
plt.title("지역별 치킨 전체 주문량")
plt.show()