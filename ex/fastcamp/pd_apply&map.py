import pandas as pd
df = pd.DataFrame({'a': [1,2,3,4,5]})
#문제 a가 2보다 작으면 '2미만', 4보다 작으면 '4미만', 4이상이면 '4이상'이 저장된 b 컬럼을 추가하시오
df['b'] = 0
#print(df)
a = df[df['a']<2]
#print(a)
df['b'][a.index] = '2미만'
#print(df['a'])
a = df[(df['a']<4) & (df['a']>=2)] 
df['b'][a.index] = '4미만'
a = df[df['a']>=4]
df['b'][a.index] = '4이상'
#print(df)

def case_function(x):
    if x < 2:
        return '2미만'
    elif x < 4:
        return '4미만'
    else:
        return '4이상'

df['c'] = df['a'].apply(case_function)
print(df)
#문제 a가 1이면 'one', 2이면 'two', 3이면'''5이면 'five'를 출력하는 칼럼 d를 만드시오
def check_a(x):
    if x==1:
        return 'one'
    elif x==2:
        return 'two'
    elif x==3:
        return 'three'
    elif x==4:
        return 'four'
    elif x==5:
        return 'five'
df['d'] = df['a'].apply(check_a)
print(df)

#map을 이용한 해결 방법
a = {1:'one', 2:'two', 3: 'three', 4: 'four', 5:'five'}
df['e'] = df['a'].map(a)#key=a일때 value를 e에 추가하는거인듯
print(df)
