from statistics import mean
import pandas as pd
'''
df1 = pd.DataFrame({'ID' : [1,2,3,4,5], '가입일' : ['2021-01-02', '2021-01-04', '2021-01-10', '2021-02-10', '2021-02-24'], '성별' : ['F', 'M', 'F', 'M', 'M']})
df2 = pd.DataFrame({'구매순서' : [1,2,3,4,5], 'ID' : [1,1,2,4,1], '구매월' : [1,1,2,2,3], '금액' : [1000,1500,2000,3000,4000]})
#문제 df1은 회원의 정보를 저장한 데이터 프레임이며, df2는 각 회원의 구매 내역을 저장한 데이터 프레임이다.
#각 회원의 누적 금액을 회원 ID별로 구하시오
print(df2)
s2 = df2.groupby(by = ['ID'])['금액'].sum()
print(s2)
print(pd.merge(df1,s2, how ='left', on = 'ID'))#결과 + 합산한 값 데이터 프레임 만들기

#문제 df1은 회원의 정보를 저장한 데이터 프레임이며, df2는 각 회원의 구매 내역을 저장한 데이터 프레임이다.
#각 회원의 월별 누적 금액을 회원 ID별로 구하시오
s2 = df2.groupby(by=['ID', '구매월'])['금액'].sum()
print(s2)
print(type(s2.index))
print(pd.merge(df1,s2,how='inner', on='ID'))#구입한 내역이 있는 ID만 출력

#문제 구매월 컬럼추가
s2 = df2.groupby(by=['ID', '구매월'], as_index= False)['금액'].sum()
df3 = pd.DataFrame(s2)

print(df3)
print(pd.merge(df1,df3, how = 'inner', on='ID'))
'''
#문제 df는 각 회원의 구매 내역을 저장한 데이터 프래임이다. 각 회원의 누적 금액과 누적 구매 횟수를 회원 ID별로 구하시오.
df = pd.DataFrame({'구매순서': [1,2,3,4,5], 'ID' : [1,1,2,4,1], '구매일': [1,1,2,2,3], '금액' : [1000,1500,2000,3000,4000], '수수료':[100,150,200,300,400]})

#df2 = df.groupby(by=['ID'])['금액'].sum()
#df3 = df.groupby(by=['ID'])['금액'].count()
#print(pd.merge(df2,df3,how='left', on='ID'))

df2 = df.groupby(by= ['ID'])['금액'].agg([sum,len])
print(df2)
df2.reset_index(inplace=True)
print(df2)
#문제 df는 각 회원의 구매 내역을 저장한 데이터 프레임이다. 
#각 회원의 최대/최소 사용금액과 최저 수수료의 값을 구하시오
print(df.groupby(by=['ID']).agg({'금액' : [max,min], '수수료': [min]}))
#agg에 여러 컬럼을 적용시킬떄는 dict데이터형 사용
df3 = df.groupby(by=['ID']).agg({'금액' : [max,min], '수수료': [min]})
#결과값 다듬기
df3.columns = ['_'.join(col) for col in df3.columns.values]
df3.reset_index(inplace=True)
print(df3)