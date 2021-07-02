import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_csv('data/chicken_07.csv') #데이터 불러오기
data2 = pd.read_csv('data/chicken_08.csv')
data3 = pd.read_csv('data/chicken_09.csv')

data4 = pd.concat([data1, data2, data3])
data4 = data4.reset_index(drop=True)

sum_of_calls_by_week = data4.groupby('요일')['통화건수'].sum() #요일별 통화건수의 합을 가져옴
groupdata = data4.groupby('요일')['통화건수'].sum() #요일별 통화건수의 합을 가져옴

print(sum_of_calls_by_week)

plt.figure(figsize=(8,5))
plt.bar(sum_of_calls_by_week.index, sum_of_calls_by_week) #괄호 안에 입력된 변수들의 의미는 (x축, y축)을 의미
plt.title('요일에 따른 치킨 주문량 합계')
plt.show() #여기까지 하면 한글이 깨져서 그래프가 출력됨(한글을 지원해주지 않는 폰트를 이용해서 그래프를 그렸기 때문)

plt.rcParams['font.size'] = 10 # 폰트 크기 변경
plt.rcParams['font.family']

plt.rcParams['font.family'] = "Malgun Gothic" #폰트 변경

plt.show() #다시 출력하면 폰트 문제 없이 정상 출력됨

sorted_sum_of_calls_by_week = sum_of_calls_by_week.sort_values(ascending=True) #오름차순으로 데이터들을 다시 정렬
print(sorted_sum_of_calls_by_week)

plt.figure(figsize=(8,5)) #정렬된 그래프 출력
plt.bar(sorted_sum_of_calls_by_week.index, sorted_sum_of_calls_by_week)
plt.title('요일에 따른 치킨 주문량 합계')
plt.show()

weeks = ['월', '화', '수', '목', '금', '토', '일'] #요일의 기준을 정함
sum_of_calls_by_weeks =data4.groupby('요일')['통화건수'].sum().reindex(weeks) #위에서 정한 요일 기준대로 데이터들을 다시 정렬하여 그룹화 함
print(sum_of_calls_by_weeks)

plt.figure(figsize=(8,5))
plt.bar(sum_of_calls_by_weeks.index, sum_of_calls_by_weeks)
plt.title('요일에 따른 치킨 주문량 합계')
plt.show()