import pandas as pd
'''
df = pd.DataFrame({'a': [i for i in range(1,11)], 'b': [i for i in range(11,21)], 'c': [i for i in range(21,31)]})
#print(df[['a','b']])
print(df)
print(df.loc[0])
print(df.loc[2:4])
'''

index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'g', 'h', 'i']
df2 = pd.DataFrame({'a': [i for i in range(1,11)], 'b': [i for i in range(11,21)], 'c': [i for i in range(21,31)]}, index= index)
print(df2)
print(df2.loc['g'])
print('-'*30)
print(df2.loc['c':])
#문제 : 열이 a,c이면서 인덱스가 g,i인 데이터를 출력하시오
df2.columns = ['a','b','c']
print(df2.loc[['g','i'],['a','c']])
#문제 ㅣ 처음부터 5번째 까지의 데이터의 첫 번쨰 열과 세 번쨰 열의 데이터를 추출하시오
print(df2.iloc[:5,[0,2]])
print(df2.iloc[:5,:2])
