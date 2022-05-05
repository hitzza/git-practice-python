from pandas import Series, DataFrame
import pandas as pd
import numpy as np
'''
data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data' #Data URL

df_data = pd.read_csv(data_url, sep='\s+', header = None)#sep - 데이터를 나누는 기준(\s= 빈칸), header - 첫 칸에 컬럼명이 있는지

print(df_data.head())
df_data.columns = ['CRIM','ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO' ,'B', 'LSTAT', 'MEDV']#순서대로 컬럼명 지정
print(df_data.head())
print(type(df_data.values))#df_data = pandas.core.frame.DataFrame, .values= ndarray
#print(df_data.values)
'''
'''
#series - DataFrame 중 하나의 Column에 해당하는 데이터의 모음 Object
#DataFrame - Data Table 전체를 포함하는 Object
#series
list_data = [1,2,3,4,5]
list_name = ["a", "b", "c", "d", "e"]
example_obj = pd.Series(data = list_data, index = list_name)#index이름 지정 가능(잘 사용 x)
print(example_obj)
dict_data = {"a":1,"b":2,"c":3,"d":4,"e":5,}#dict타입으로도 가능
example_obj = pd.Series(dict_data, dtype = np.float32, name = "example_data")#index이름 지정 가능(잘 사용 x)
print(example_obj)

#exam_obj = pd.Series(data = df_data['CRIM'])
#print(exam_obj)
'''
#DataFrame
raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
        'age': [42, 52, 36, 24, 73],
        'city': ['San Francisco', 'Baltimore', 'Miami', 'Douglas', 'Boston']}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'city'])
#print(df)
print(DataFrame(raw_data, columns=['age', 'city']))#DataFrame에서는 원하는 컬럼만 가져오는것이 가능(numpy와 큰 차이점)
print(DataFrame(raw_data, columns=['first_name', 'last_name', 'age', 'city', 'debt']))#새로운 컬럼 추가 가능(default = NaN)
print(df.first_name)#column 선택- Series 추출
print(df["first_name"])#두 가지 방식으로 가능
print(df)
print(df.loc[:3])#index의 이름으로 해당값을 가져올 수 있다, loc - index location
print(df["age"].iloc[:3])#ilog - index position
print(df.age.iloc[1:])#마찬가지로 가능

s = pd.Series(np.nan, index=[49,48,47,46,45, 1, 2, 3, 4, 5])

print(s.loc[:3])#loc은 index의 이름이3인곳 까지
print(s.iloc[:3])#iloc은 실제 index번호가 2인곳 까지
#파이썬에서 :3은 3미만인데 loc에선 3까지 포함하네

#★★많이 사용하니까 중요★★
test_debt = DataFrame(raw_data, columns=['first_name', 'last_name', 'age', 'city', 'debt'])
print(test_debt)
test_debt.debt = df.age > 40 #Column에 새로운 데이터 할당
print(test_debt)#broadcasting처럼 boolean값을 반환후 할당


print(test_debt.T)#numpy의 transpose, 전치행렬로 바꿔주는것도 가능
print(test_debt.values)#values를 사용해서 ndarray로 바꿀 수 있음
print(test_debt.to_csv())#csv형태로 변환도 가능
del test_debt["debt"]#Column을 삭제함
print(test_debt)