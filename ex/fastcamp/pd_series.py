import pandas as pd
#Series
'''
df = pd.DataFrame({'a': [1,2,3], 'b': [4,5,6], 'c': [7,8,9]})

print(df['a'])
print(type(df['a']))

a= pd.Series([1,2,3,1,2,3])
print(a)
a= pd.Series([1,2,3,1,2,3], index= ['a','b','c','d','e','f'])
print(a)
'''
#find unique values
df = pd.DataFrame({'a': [1,2,3,1,2,3], 'b' : [4,5,6,6,7,8], 'c': [7,8,9,10,11,12]})
a =df['a']
print(a)
print(a.unique())
print(a.unique()[2])#uniuqe는 index값도 가지고 있음
