import pandas as pd

df = pd.DataFrame({'판매일' : ['5/11/21', '5/12/21', '5/13/21', '5/14/21', '5/15/21'],
                '판매량': ['10', '15', '20', '25', '30'],
                '방문자수': ['10', '-', '17', '23', '25'],
                '기온' : ['24', '24.3', '24.8', '25', '25.4']})
df = df.astype({'판매량': 'int'})#해당 컬럼 타입 변환
df['판매량 보정'] = df['판매량'] + 1
df['방문자수'] = pd.to_numeric(df['방문자수'],errors='coerce')#errors = 'cperce' 에러일때 NaN
df.fillna(0,inplace=True)
df = df.astype({'방문자수': 'int'})#해당 컬럼 타입 변환
df['판매일'] = pd.to_datetime(df['판매일'], format='%m/%d/%y')
print(df)
print(df.dtypes)
