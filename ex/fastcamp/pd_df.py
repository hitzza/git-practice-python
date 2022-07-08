from numpy import NaN
import pandas as pd

df = pd.DataFrame({'a': [1,2,3], 'b' : [4,5,6], 'c': [7,8,9]})
print(df)
print(type(df))

dummy = {'a': [1,2,3], 'b':[4,5,6], 'c' : [7,88,9]}
df2= pd.DataFrame(dummy)
print(df2)

a = [[1,4,7],[3,5,6],[3,6,9]]
df3 = pd.DataFrame(a)
print(df3)
print('-'*30)
df3.columns = ['a','b','c']
print(df3)

test_df = pd.DataFrame({'company':['abc', '회사', 123], '직원수':[400, 10, 6]})
print(test_df)

a = {'company':['abc', '회사', 123], '직원수':[400, 10, 6], '위치': ['Seoul',NaN , 'Busan']}#numpy를 선언해서 np.NaN으로도 대체 가능
test_df = pd.DataFrame(a)
print(test_df)

