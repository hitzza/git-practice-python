#1d = Series, 2d= DataFrame
import pandas as pd

#Series
'''
obj = pd.Series([10,20,30,40,50])
obj_2 = pd.Series([10,20,30,40,50],
    index = ['a','b','c','d','e'])
print(obj)
print(obj.index)
print(obj.values)
print(obj[1])
print(obj_2)
print(obj_2[['a','e']])
print(obj_2[1:3])
'''
'''
obj = pd.Series([10,20,30,40])
print(obj*10)
print('-'*30)
print(obj>=20)
'''
'''
data = pd.Series({'유재석':35, '박명수': 60, '태진아': 85},
    index = ['유재석', '박명수', '태진아', '정형돈', '하하'])
data['정형돈'] = 52
print(data)
print(data[3])
'''
#DataFrame
'''
data = {'이름':['유재석', '박명수', '정형돈','하하'],
    '나이':[35, 60, 52, 38],
    '키':[180, 175, 160, 150]}
frame = pd.DataFrame(data)
frame_2 = pd.DataFrame(data, columns=['이름','나이','키','몸무게'])
print(data)
print(frame)
print(frame_2)
print(frame.head(2))
print(frame.tail(2))
'''
#loc = index이름으로 추출, iloc = index주소로 추출
'''
data = {'이름':['유재석', '박명수', '정형돈','하하'],
    '나이':[35, 60, 52, 38],
    '키':[180, 175, 160, 150]}
frame = pd.DataFrame(data, index = ['첫째','둘째','셋째','넷째'])
print(frame)
print(frame.loc['둘째','이름'])
print(frame.loc['넷째', ['나이', '키']])
print('-'*30)
print(frame.iloc[2,0])
print(frame.iloc[3,:2])
print(frame.iloc[:,[0,2]])
'''
#합계와 평균/정력하기
data = {'이름':['유재석', '박명수', '정형돈','하하'],
    '나이':[35, 60, 52, 38],
    '키':[180, 175, 160, 150]}
frame = pd.DataFrame(data)
frame_2 = frame.iloc[:,[1,2]]
rank = frame.sort_values(by=['나이'],ascending=False)#ascending=False는 내림차순으로 정렬
total = frame_2.sum(axis=0)
avg = frame_2.mean(axis=0)

print(frame_2)
print(rank)
print(total)
print(avg)