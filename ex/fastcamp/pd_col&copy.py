import pandas as pd
import copy
'''
df = pd.DataFrame({'a' : [1,2,3], 'b': [4,5,6], 'c':[7,8,9]})
print(df.columns[:])
df.columns= ['d','e','f']
print(df.columns)
df.columns= ['디','e','에프']
print(df)
df.columns= ['d','이','f']
print(df)
'''
'''
df = pd.DataFrame({'a': [1,2,3], 'b': [4,5,6], 'c': [7,8,9]})
df.columns = ['d','e','f']
print(df.columns)
print(df.rename(columns= {'d': '디', 'f' : '에프'}))#변경 값 return안됨!
df.rename(columns= {'d': '디', 'f' : '에프'}, inplace=True)#inplace =True면 리턴
print(df)
'''
#copy
df = pd.DataFrame({'a': [1,2,3], 'b': [4,5,6], 'c': [7,8,9]})
df2 =copy.deepcopy(df)
df3 = df[:]
df.rename(columns={'a': '에이'},inplace = True)
print(df)
print(df2)
print(df3)
