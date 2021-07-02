import pandas as pd
commercial = pd.read_csv('data/commercial.csv')

commercial.groupby('상가업소번호')['상권업종소분류명'].count().sort_values(ascending=True)
print(commercial)
#출력 결과 모든 상가업소번호의 개수가 1인 것으로 보아 상가마다 고유의 상가업소번호가 존재 -> 가게의 수를 셀 때 유용

#하나의 column인 도로명(시+군+구)을 각각 시, 군, 구 3개의 column으로 분리 하여 새로운 열로 저장
commercial[['시','구','상세주소']] = commercial['도로명'].str.split(' ', n=2,expand=True) #도로명(string)을 ' '에 대해 나누고(split) 분리한 string을 컬럼으로 생성(expand=True)

seoul_data = commercial[commercial['시'] == '서울특별시'] # '시'에 해당하는 column이 '서울특별시'인 것만 데이터를 따로 저장

#서울특별시에 해당하는 데이터만 있는지 확인하기 위한 코드
city_type = set(seoul_data['시'])
print(city_type)

#치킨집만 분류
seoul_chicken_data=seoul_data[seoul_data['상권업종소분류명'] =='후라이드/양념치킨']
print(seoul_chicken_data)

#구에 따라 치킨집을 그룹화
groupdata=seoul_chicken_data.groupby('구')
group_by_category=groupdata['상권업종소분류명']
chicken_count_gu = group_by_category.count()
sorted_chicken_count_gu=chicken_count_gu.sort_values(ascending=False)
print(sorted_chicken_count_gu)

import matplotlib.pyplot as plt
plt.rcParams['font.family'] = "Malgun Gothic"
plt.figure(figsize=(10,5))
plt.bar(sorted_chicken_count_gu.index,sorted_chicken_count_gu)
plt.title('구에 따른 치킨 가게 수의 합계')
plt.xticks(rotation=45) #x축 글씨 회전
plt.show()

#지도로 그래프를 그리기 위해 라이브러리 import
import folium
import json
import webbrowser

#지리데이터를 불러옴
seoul_state_geo = './data/seoul_geo.json'
geo_data = json.load(open(seoul_state_geo, encoding='utf-8')) #서울의 구에 대한 위도 경도 데이터(지리정보)

map = folium.Map(location=[37.5502, 126.982], zoom_start=11)
folium.Choropleth(geo_data=geo_data,
                  data=chicken_count_gu,
                  columns=[chicken_count_gu.index, chicken_count_gu],
                  fill_color='PuRd',
                  key_on='properties.name').add_to(map)

#웹브라우저로 지도 출력
seoul_chicken = 'seoul_chicken.html'
map.save('seoul_chicken.html')
webbrowser.open(seoul_chicken)