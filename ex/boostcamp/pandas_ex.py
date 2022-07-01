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
'''
'''
#selection - indexing이랑 비슷함
df["account"].head(3)#한개의 Column 선택시 하나의 string값만 넣음
#output이 Series
df[["account","street","state"]].head(3)# 1개 이상의 column 선택시 two dimensional array로 해주어야함!
#output이 DataFrame
df[:3]#column 이름 없이 사용하는 index number는 row를 기준으로 표시
df["account"][:3]#column명과 함께 row index 사용시, 해당 column만 출력

'''
'''

data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data' #Data URL
df_data = pd.read_csv(data_url, sep='\s+', header = None)
df_data.columns = ['CRIM','ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO' ,'B', 'LSTAT', 'MEDV']#순서대로 컬럼명 지정
crim_serires = df_data["CRIM"]

print(crim_serires[:3])
print(crim_serires[[0,1,2,5]])#2 dimension array로 해당index값의 series 출력 가능
print(crim_serires[crim_serires < 0.02])#Boolean index도 가능!

df_data.index = df_data["CRIM"]#index번호가 해당column값으로 변경

print(df_data.head())#CRIM column이 남아있기 떄문에
del df_data["CRIM"] #del을 사영해서 제거
print(df_data.head())#이제 CRIM column이 없음

print(df_data[["ZN", "INDUS"]][:0.02729])#.loc과 같이 index의 이름으로 범위설정 해야함!
print(df_data.loc[[0.02731, 0.02729], ["ZN", "INDUS"]])#해당 index 이름과 column명으로 값 출력 가능
print(df_data.iloc[:2, :2])#해당 index number와 column number
#iloc은 column이 적을 때 편함
#column이 많아지면 loc을 많이 쓴다

df_data.index = list(range(0,506))#index재설정
print(df_data.head())
print(df_data.drop(1))#index number로 drop
print(df_data.drop([0,1,2,3]))#한개 이상의 index number로 drop
print(df_data.drop("ZN", axis=1))#axis 지정으로 축을 기준으로 drop -> column중에 city
print(df_data.head())#drop function을 사용해도 원본 데이터를 건들지 않음
df_data.drop("ZN", axis=1, inplace=True)#inplace=True를 사용해야 원본 데이터가 바뀜
print(df_data.head())
'''
'''
#series operation
s1 = Series(range(1,6), index = list("abced"))
print(s1)
s2 = Series(range(5,11), index= list("bcedef"))
print(s2)
print(s1.add(s2))#index 기준으로 연산 수행
print(s1 + s2)#겹치는 index가 없을 경우 NaN값으로 반환
'''
'''
#Dataframe operation
#operation types : add, sub, div, mul
df1 = DataFrame(np.arange(9).reshape(3,3), columns=list("abc"))
print(df1)

df2 = DataFrame(np.arange(16).reshape(4,4),columns=list("abcd"))
print(df2)

print(df1 + df2)
print(df1.add(df2, fill_value=0))#fill_value 0 - add operation의 fill_value값을 쓰면 NaN값을 0으로 변환
'''
'''
#Series + DataFrame column!을 기준으로 broadcasting이 발생함
df = DataFrame(
        np.arange(16).reshape(4,4),
        columns=list("abcd")
)
print(df)
s = Series(
        np.arange(10,14),
        index=list("abcd")
)
print(s)
print(df.add(s))#column을 기준으로 broadcasting이 발생
s2 = Series(np.arange(10,14))
print(df.add(s2, axis = 0))#axis = 0을 사용해서 row를 기준으로도 broadcasting이 가능
#Series + DataFrame을 합칠 때 row index명과 column명이 같아야 하는듯
'''
'''
#lambda 함수
#lambda argument : expression

#map for series
#Pandas의 series type의 데이터에도 map 함수 사용 가능
#function 대신 dict, sequence형 자료등으로 대체 가능
s1 = Series(np.arange(7,17))
print(s1.head(10))
print(s1.map(lambda x : x**2).head(5))

#dict type으로 데이터 교체
z = {1:'A', 2:'B', 3:'C'}
print(s1.map(z).head(5))#없는 값은 NaN, s1의  원소 번호 = z의 key 값으로 mapping이 일어남

s2 = Series(np.arange(10,20))

print(s1)
print(s2)
print(s1.map(s2).head(10))#s1의 value에 맞는 s2의 index값을 가진 s2의 value를 return
print(s2.map(s1).head(10))#s2의 value에 맞는 s1의 index값이 없어서 모두 NaN을 return
'''
#apply for dataframe
#map은 series data의 element단위로 함수를 적용시켰지만
#apply는 map과 달리,Series 전체(column)에 해당 함수를 적용
#입력값이 series 데이터로 입력받아 handling 가능

data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data' #Data URL
df_data = pd.read_csv(data_url, sep='\s+', header = None)
df_data.columns = ['CRIM','ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO' ,'B', 'LSTAT', 'MEDV']#순서대로 컬럼명 지정
'''
f1 = lambda x : x.max() - x.min()

print(df_data.apply(f1))
#scalar 값 이외에 series값의 반환도 가능함
def f(x):
    return Series([x.min(), x.max()], index=["min", "max"])
print(df_data.apply(f))
'''
'''
#applymap for dataframe
#series 단위가 아닌 element단위로 함수를 적용함
f = lambda x : -x
print(df_data.applymap(f))
#series 단위에 apply를 적용시킬 때와 같은 효과
print(df_data["CRIM"].apply(f))
#applymap은 전체 데이터를 뽑을 떄 유용하고, apply는 통계 데이터를 뽑을 때 유용
'''
#built-in
print(df_data.describe())#describe함수 -데이터의 요약 정보를 보여줌
print(df_data.unique())#series data의 유일한 값을 list를 반환함, 현재 데이터엔 유일한 값이 없어서 attribute error

np.array(dict(enumerate(df_data["CRIM"].unique())))#dict type으로 index

#label index값과 label값 각각 추출
value = list(map(int, np.array(list(enumerate(df_data["CRIM"].unique())))[:,0].tolist()))
key = np.array(list(enumerate(df_data["CRIM"].unique())), dtype=str)[:,1].tolist()
#복잡하다..
print(value, key)