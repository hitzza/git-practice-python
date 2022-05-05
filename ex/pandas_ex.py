import pandas as pd

data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data' #Data URL

df_data = pd.read_csv(data_url, sep='\s+', header = None)#sep - 데이터를 나누는 기준(\s= 빈칸), header - 첫 칸에 컬럼명이 있는지

print(df_data.head())
df_data.columns = ['CRIM','ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO' ,'B', 'LSTAT', 'MEDV']#순서대로 컬럼명 지정
print(df_data.head())
print(type(df_data.values))#df_data = pandas.core.frame.DataFrame, .values= ndarray

