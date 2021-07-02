import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/pizza_09.csv')

sum_of_calls_by_week = data.groupby('요일')['통화건수'].sum()
sorted_sum_of_calls_by_week = sum_of_calls_by_week.sort_values(ascending=True)

print(sorted_sum_of_calls_by_week)

plt.figure(figsize=(8,5))
plt.rcParams['font.family'] = "Malgun Gothic"
plt.bar(sorted_sum_of_calls_by_week.index, sorted_sum_of_calls_by_week)
plt.title('요일에 따른 피자 주문량 합계')
plt.xlabel('요일')
plt.show()

sum_of_calls_by_city = data.groupby('발신지_구')['통화건수'].sum()
sorted_sum_of_calls_by_city = sum_of_calls_by_city.sort_values(ascending = True)

print(sorted_sum_of_calls_by_city)

plt.figure(figsize=(10,5))
plt.bar(sorted_sum_of_calls_by_city.index, sorted_sum_of_calls_by_city)
plt.title('구에 따른 피자 주문량 합계')
plt.xlabel('구')
plt.xticks(rotation = 45)
plt.show()