import pandas as pd 

df = pd.DataFrame({'a': [i for i in range(1,11)], 'b': [i for i in range(11,21)], 'c': [i for i in range(21,31)]})

#문제 a,c열을 출력 하시오
#print(df[['a','c']])
#문제 a가 3이상인 데이터를 출력하시오
#print(df[df['a']>=3])
#문제 a가 3 이상인 데이터 중 a,c열만 출력하시오
#print(df[df['a']>=3][['a','c']])
#문제 a가 3이상이고 b가 16미만인 데이토를 출력하시오
#print(df[(df['a']>=3) & (df['b']<16)])
#문제 a가 3 이하이거나 a가 7 이상인 데이터룰 츨력
#print(df[(df['a']<=3) | (df['a']>=7)])
#문제 a가 3이상이고 b가 16 미만이거나 c가 30인 데이터를 출력하시오
print(df[(df['a']>=3) & ((df['b']<16) | (df['c']==30))])
