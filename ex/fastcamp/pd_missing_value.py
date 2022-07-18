import pandas as pd
import numpy as np
'''
df = pd.DataFrame({'a': [1,1,3,4,5], 'b':[2,3,np.NaN, 3, 4], 'c': [3,4,7,6,4]})

print(df.isnull())
print(df.isnull().sum())#null값 개수 확인
#count를 사용하게 되면 모든 값을 세기 떄문에 sum을 사용
#False는 0 True는 1 이기 떄문에 sum을 사용하면 원하는 값이 나옴
df.dropna(inplace=True)
print(df)
'''
df = pd.DataFrame({'a': [1,1,3,4,5], 'b':[2,3,np.NaN, 3, 4], 'c': [3,4,7,6,4]})
print(df.dropna(axis=1))#열을 기준으로 결측값 지우기
#print(df.fillna(0))#결측값 채우기(0)

'''
df = pd.DataFrame({'a': [1,1,3,4,np.NaN], 'b': [2,3,np.NaN,np.NaN, 4], 'c': [np.NaN, 4,1,1,4]})

print(df.fillna(method='bfill'))#뒤의 값으로 결측값 채우기
print(df.fillna(method='ffill'))#앞의 값으로 결측값 채우기
print('-'*30)
print(df)
print(df.fillna(method='ffill',limit=1))#앞의 값을 기준으로 1개만 결측값 채우기
'''
'''
df = pd.DataFrame({'a': [1,1,3,4,np.NaN], 'b': [2,3,np.NaN,np.NaN, 4], 'c': [np.NaN, 4,1,1,4]})
#문제 : 데이터 프레임에 존재하는 결측값을 뒤의 값으로 대체한 이후 앞의 값으로 대체하시오
df.fillna(method='bfill',inplace=True)
df.fillna(method='ffill',inplace=True)
print(df)
'''
'''
df = pd.DataFrame({'a': [1,1,3,4,np.NaN], 'b': [2,3,np.NaN,np.NaN, 4], 'c': [np.NaN, 4,1,1,4]})
print(df.fillna(df.mean()))#각 컬럼의 평균값으로 대체
print(df.fillna(df.mean()['a']))#a 컬럼의 평균값으로 대체
#문제 b,c의 결측값들을 각 컬럼의 평균으로 치환하시오
print(df.fillna(df.mean()[['b','c']]))
'''