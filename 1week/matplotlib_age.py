import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_csv('data/chicken_07.csv')
data2 = pd.read_csv('data/chicken_08.csv')
data3 = pd.read_csv('data/chicken_09.csv')

data4= pd.concat([data1,data2,data3])
data4 = data4.reset_index(drop=True)

sum_of_calls_by_age = data4.groupby('연령대')['통화건수'].sum() #연령대 별 통화건수의 총합
sorted_sum_of_calls_by_age = sum_of_calls_by_age.sort_values(ascending=True)
print(sorted_sum_of_calls_by_age)

plt.figure(figsize=(8,5))
plt.rcParams['font.family'] = "Malgun Gothic"
plt.xlabel('연령대') #x축이 어떤 값을 의미하는지 출력하도록 함
plt.bar(sorted_sum_of_calls_by_age.index, sorted_sum_of_calls_by_age)
plt.title('연령대에 따른 치킨 주문량 합계')
plt.show()