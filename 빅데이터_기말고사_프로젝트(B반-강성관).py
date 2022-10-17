#!/usr/bin/env python
# coding: utf-8

# # 빅데이터 기말고사 프로젝트

# # 주제 : 빌보드 차트 분석
# 

# In[ ]:


#발표 링크
https://youtu.be/x0HeTvqLwvA


# In[1]:


#필요한 라이브러리 임포트
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import datetime as dt
matplotlib.rcParams['font.family'].insert(0, 'Malgun Gothic') 


# In[2]:


# 빌보드 차트 데이터 (Top100 까지 존재함)가져오기
bilboard = pd.read_csv('charts.csv', encoding = 'cp949')


# In[3]:


bilboard


# In[4]:


bilboard.info()


# In[5]:


#빌보드 차트에서 1등을 해 본적이 있는 노래 정보를 가져오기
bilboard['didTopRank'] = bilboard.peak_rank == 1
bilboard[bilboard.didTopRank == True]


# In[6]:


#연도 분리를 위해서 date컬럼의 데이터 타입을 datetime으로 변경하기 위한 연산 진행
bilboard['date'] = bilboard.date.apply(lambda X: dt.datetime.strptime(X, '%Y-%m-%d'))


# In[7]:


bilboard.info()


# In[8]:


# 2021년도 1월부터 가장 최근 저장된 데이터 까지의 데이터만 추출
bilb2021 = bilboard[bilboard.date.isin(pd.date_range(start = '2021-01-01', end = '2021-11-06'))]


# In[9]:


bilb2021


# In[10]:


#2021년도 10월 1, 2주차 빌보드 차트에서 빌보드에 존재한 기간이 가장 많은 순으로 차트 그리기 Top 5
weekBilb202110 = bilb2021[bilb2021.date.isin(pd.date_range(start = '2021-10-01', end = '2021-10-15'))]


# In[11]:


sortedbilb2020 = weekBilb202110.sort_values(by='weeks_on_board', ascending = False)


# In[12]:


sortedbilb2020.head(5)


# In[13]:


headbilb = sortedbilb2020.head(5)


# In[14]:


headbilb[['song','weeks_on_board']].plot(kind = 'barh', x = 'song', 
                                         color = 'red', title = '2021년 10월 1~2주차 빌보드에 가장 오래있었던 노래 Top 5')


# In[15]:


#위에서 했던 headbilb 데이터를 plotly를 이용하여 표현하기
import plotly
import plotly.express as px


# In[16]:


fig = px.bar(headbilb, x='date', y='weeks_on_board', barmode = 'group', color = 'song', hover_data = ['artist'], 
            labels = {'date' : '날짜', 'weeks_on_board' : '빌보드 순위에 있었던 기간'})
fig.show()


# In[17]:


#2019년 8월 1주차 순위에서 최초로 빌보드에 들어온 노래를 5개만 뽑은 뒤 순위 비교
weekBilb201908 = bilboard[bilboard.date.isin(pd.date_range(start = '2019-08-01', end = '2019-08-07'))]


# In[18]:


weekBilb201908


# In[19]:


sortedbilb2019 = weekBilb201908.sort_values(by='weeks_on_board')


# In[20]:


headbilb2 = sortedbilb2019.head(5)


# In[21]:


headbilb2


# In[31]:


headbilb2[['song','rank']].plot(kind = 'barh', x = 'song')


# In[23]:


#시각화 시 plotly를 활용 시 더 깔끔하게 데이터 시각화 가능
fig2 = px.bar(headbilb2, x='song', y='rank', barmode = 'group', hover_data = ['artist'],
              labels = {'song' : '곡 이름', 'peak_rank' : '최고 순위'})
fig2.show()


# In[ ]:


# 곡명이 Stay인 곡의 2021년도 빌보드 순위 변화 추이를 그래프로 표현해보기


# In[24]:


# 곡명이 Stay인지 아닌지 판별하기
bilb2021.song == 'Stay'


# In[25]:


stay2021 = bilb2021[bilb2021.song == 'Stay'].set_index('date')


# In[26]:


stay2021


# In[27]:


#비교를 위해 invert하지 않은 결과도 출력
stay2021['peak_rank'].plot(x = 'date')


# In[28]:


#순서 값을 반전시키기 위해서 invert_yaxis() 함수를 활용하여 3등에서 1등으로 증가하도록 그래프를 구성하였음
#이 예시는 최고순위를 기준으로 시각화 하였음
stay2021['peak_rank'].plot(x = 'date').invert_yaxis()


# In[29]:


#최고 순위가 아닌 그 주의 순위로도 그래프를 구성할 수 있음
stay2021['rank'].plot(x = 'date').invert_yaxis()


# In[50]:


# Y축 반전하기 전
fig3 = px.bar(stay2021.reset_index(), x='date', y='rank', barmode = 'group', 
              labels = {'date' : '날짜', 'rank' : '순위'})


# In[60]:


fig3


# In[48]:


fig3.update_yaxes(autorange = 'reversed')


# In[59]:


fig4 = px.line(stay2021.reset_index(), x = 'date', y = 'rank')
fig4.update_yaxes(autorange = 'reversed')

