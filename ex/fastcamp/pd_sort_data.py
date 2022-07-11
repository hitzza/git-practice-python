import pandas as pd

#sort for index
'''
df = pd.DataFrame({'a': [2,3,2,7,4], 'b':[2,1,3,5,3], 'c': [1,1,2,3,5]})
df.sort_index(ascending=False, inplace= True)
print(df)
df.reset_index(inplace=True,drop=True)
print('-'*30)
print(df)
'''
#sort for value
df = pd.DataFrame({'a': [2,3,2,7,4], 'b':[2,1,3,5,3], 'c': [1,1,2,3,5]})
'''
print(df)
df.sort_values(by=['a'],inplace=True)
print('-'*30)
print(df)
'''
#문제 a,b열 기준으로 오름차순 정렬하시오
#print(df.sort_values(by=['a','b'],ascending=True))
#문제 a얄을 기준으로 오름차순 정렬 한 이후 ,b열 기준으로 내림차순 정력하시오
df.sort_values(by=['a','b'],ascending=[True,False], inplace=True)
df.reset_index(drop=True,inplace=True)
print(df)