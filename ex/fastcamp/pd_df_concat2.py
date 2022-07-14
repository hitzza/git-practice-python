import pandas as pd
#좌우 결합
'''
#df1 = pd.DataFrame({'A' : [1,2,3], 'B' : [11,12,13], 'C' : [21,22,23], 'D' : [31,32,33]})
#df2 = pd.DataFrame({'e' : [3,4,5], 'F' : [13,14,15], 'G' : [23,24,25], 'E' : [41,42,43]})

#print(pd.concat([df1,df2], axis=1))

df1 = pd.DataFrame({'ID' : [1,2,3], '성별' : ['F', 'M', 'F'], '나이' : [20,30,40]})
df2 = pd.DataFrame({'ID' : [1,2,3], '키' : [160.5, 170.3, 180.1], '몸무게' : [45.1, 50.3, 72.1]})

print(pd.concat([df1,df2], ignore_index= True))
'''
'''
df1 = pd.DataFrame({'ID' : [1,2,3,4,5], '성별' : ['F', 'M', 'F','M', 'F'], '나이' : [20,30,40, 25,42]})
df2 = pd.DataFrame({'ID' : [3,4,5,6,7], '키' : [160.5, 170.3, 180.1, 142.3, 153.7], '몸무게' : [45.1, 50.3, 72.1, 38, 42]})
print(pd.concat([df1,df2], axis=1))#A의 id값 범주에 해당하는 데이터만 concat

#문제 성별과 나이가 확인된 유저(df1)들을 대상으로 키와 몸무게 정보를 결합 하시오
print(pd.merge(df1,df2, how = 'left', on = 'ID'))#키 값을 ID로 잡고 left조인을 실행
#문제 키와 몸무게가 확인 된 유저들을 대상으로 성별과 나이의 정보를 결합 하시오
print(pd.merge(df2,df1, how = 'left', on = 'ID'))
#문제 키,몸무게, 성별, 나이 정보가 모두 확인 된 유저들의 정보를 출력하시오
print(pd.merge(df1,df2 , how= 'inner', on='ID'))
#문제 모든 유저들의 정보를 출력하시오
print(pd.merge(df1,df2, how = 'outer', on= 'ID'))
'''
#key 값이 다를 때
'''
df1 = pd.DataFrame({'USER_ID' : [1,2,3,4,5],'성별' : ['F', 'M', 'F','M', 'F'], '나이' : [20,30,40, 25,42]})
df2 = pd.DataFrame({'ID' : [3,4,5,6,7], '키' : [160.5, 170.3, 180.1, 142.3, 153.7], '몸무게' : [45.1, 50.3, 72.1, 38, 42]})

print(pd.merge(df1,df2,how='outer', left_on='USER_ID', right_on='ID'))
'''
#문제 df1은 회원의 정보를 저장한 데이터 프레임이며, df2는 각 회원의 구매 내역을 저장한 데이터 프레임이다.
#각 회원의 정보와 구매 내역을 취합하여 하나의 데이터 프레임으로 만드시오.
df1 = pd.DataFrame({'ID' : [1,2,3,4,5], '가입일' : ['2021-01-02', '2021-01-04', '2021-01-10', '2021-02-10', '2021-02-24'], '성별' : ['F', 'M', 'F', 'M', 'M']})
df2 = pd.DataFrame({'구매순서' : [1,2,3,4,5], 'ID' : [1,1,2,2,3], '구매월' : [1,1,2,2,3], '금액' : [1000,1500,2000,3000,4000]})

print(pd.merge(df1,df2, how='outer', on= 'ID'))
print(pd.merge(df1,df2, how='left', on= 'ID'))