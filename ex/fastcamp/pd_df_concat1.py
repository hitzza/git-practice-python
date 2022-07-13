import pandas as pd 
#상하 결합
df1 = pd.DataFrame({'A' : [1,2,3], 'B' : [11,12,13], 'C' : [21,22,23]})
df2 = pd.DataFrame({'A' : [4,5,6], 'B' : [14,15,16], 'C' : [24,25,26]})

print(pd.concat([df1,df2]))#순서대로 붙임
df = pd.concat([df1,df2], ignore_index= True)#ignore_index=True로 인덱스까지 초기화
print(df)
#순서가섞였을 때 결합 결과 학인
df1 = pd.DataFrame({'A' : [1,2,3], 'B' : [11,12,13], 'C' : [21,22,23]})
df2 = pd.DataFrame({'B' : [14,15,16], 'A' : [4,5,6], 'C' : [24,25,26]})
print(pd.concat([df1,df2]))#앞쪽 컬럼 중심으로 concat정렬
#서로 다른 필드로 구성되어 있는 데이터 프레임의 결합
df1 = pd.DataFrame({'A' : [1,2,3], 'B' : [11,12,13], 'C' : [21,22,23], 'D' : [31,32,33]})
df2 = pd.DataFrame({'B' : [14,15,16], 'A' : [4,5,6], 'C' : [24,25,26], 'E' : [41,42,43]})
print(pd.concat([df2,df1]))#맞지 않는 컬럼의 데이터는 결측값 처리
print(pd.concat([df2,df1], join= 'outer'))#결합 데이터 중 합집합 데이터를 저장
print(pd.concat([df2,df1], join= 'inner'))#결합 데이터 중 교집합 데이터를 저장