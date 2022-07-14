import pandas as pd
import numpy as np
import random

#문제 다음 데이터 프레임은 A서비스의 월별 탈퇴 회원수를 가입 월별로 분류해 놓은 것이다.
#이 데이터 프레임을 이용하여 피벗 테이블을 만드시오.

df = pd.DataFrame({'가입월': [1,1,1,2,2,3], '탈퇴월': [1,2,3,2,3,3], '탈퇴회원수':[101,52,30,120,60,130]})

print(df)
pivot = pd.pivot_table(df, values= '탈퇴회원수', index=['가입월'], columns=['탈퇴월'])
print(pivot)
pivot = pd.pivot_table(df, values= '탈퇴회원수', index=['가입월'], columns=['탈퇴월'],fill_value=0)#fillvalue로 NaN값 채우기
print(pivot)

#문제 다음 데이터 프레임은 어느 과일 매장의 판매내역이다.
#각 상품 항목 별, 크기 별로 판매 개수와 판매 금액의 합을 구하시오.
a=[]
b=[]
for i in range(100):
    a.append(random.randint(1,3))
    b.append(random.randint(1,3))
ex_df = pd.DataFrame({'품목' : a, '크기': b})

ex_df['금액'] = ex_df['품목'] * ex_df['크기'] * 500
ex_df['수수료'] = ex_df['금액'] *0.1
print(ex_df)
frute_name = {1: '토마토', 2:'바나나', 3:'사과'}
frute_size = {1:'소', 2: '중', 3:'대'}
ex_df['품목'] = ex_df['품목'].map(frute_name)
ex_df['크기'] = ex_df['크기'].map(frute_size)
ex_df1 = pd.pivot_table(ex_df, values= '금액', index='품목', columns='크기', aggfunc=('count', 'sum'))
print(ex_df1)
#다음 데이터 프레임은 어느 과일 매장의 판매내역이다.
#각 상품 항목 별, 크기 별로 판매 개수와 판매 금액/수수료의 합을 구하시오
#피벗 테이블 대상 컬럼이 두개 이상일 때
ex_df2 = pd.pivot_table(ex_df, index='품목', columns='크기', aggfunc={'금액': ['count','sum'], '수수료': 'sum'})
print(ex_df2)#values를 없애고 aggfunc에 dict형으로 선언
