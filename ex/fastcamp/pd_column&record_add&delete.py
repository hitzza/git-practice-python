import pandas as pd

'''
df = pd.DataFrame({'a' : [1,1,3,4,5], 'b' : [2,3,2,3,4], 'c' : [3,4,7,6,4]})

#문제 : 1,3,6,4,8로 이루어진 d 칼럼을 추가하시오
df['d'] = [1,3,6,4,8]
print(df)
#문제 : 1로 이루어진 e칼럼을 추가하시오
#df['e'] = [1,1,1,1,1]
#또는
df['e'] = 1
print(df)
#문제 : a+b-c의 결과로 이루어진 f칼럼을 추가하시오
df['f'] = df['a'] + df['b'] - df['c']
print(df)
#문제 : d,e,f칼럼을 삭제하시오
df.drop(['d','e','f'], axis=1, inplace=True)
print(df)
#문제 : a에는 6 b에는 7 c에는 8을 추가하시오
df = df.append({'a':6, 'b':7, 'c':8}, ignore_index= True)
print(df)
#문제 : a에는 7 b에는 8 c에는 9을 추가하시오
df.loc[6] = [7,8,9]
print(df)
#문제 : 첫 번쨰 레코드를 삭제하시오
#df.drop(0, inplace=True)
#print(df)
#문제 : 첫 번쨰, 두 번쨰 레코드를 삭제하시오
df = df.drop([0,1])
print(df)
'''
df = pd.DataFrame({'a' : [1,1,3,4,5], 'b' : [2,3,2,3,4], 'c' : [3,4,7,6,4]})
#문제 첫 번쨰에서 네 번째 레코드를 삭제하시오
#df = df.drop([i for i in range(4)])
#print(df)
#또는
#df = df.drop(df.index[:4])
#print(df)
#문제 a가 4 미만인 레코드를 삭제하시오
#df = df.drop(df[df['a']<4].index)
#print(df)
#문제 a가 3미만이고 c가 4인 레코드를 삭제하시오
df = df.drop(df[(df['a']<3) & (df['c']==4)].index)#*************
print(df)
