import numpy as np

#matrix multiplication
x = np.array([[1, -2, 3],
             [7, 5, 0],
             [-2, -1, 2]])
y = np.array([[0,-1],
             [1, -1],
             [-2, 1]])
            
print(x @ y)#numpy에선 행렬곱에 @연산 사용 
#수학에서의 내적은 i번째 행벡터와 j번째 열벡터의 곱이지만
#numpy.inner는 i번쨰 행벡터와 j번째 행벡터의 곱
#그래서 y는 전치행렬을 사용해야함!★★
print(np.inner(x, y.T))#.T함수는 전치행렬
#22.00

print(np.linalg.inv(x))#np.linalg.inv()역행렬
#역행렬은 행렬의 n과m이 같아야하고 determinant가 0이 아니어야함
print(x @ np.linalg.inv(x))#행렬 * 역행렬 = 항등행렬

#만약 역행렬을 계산할 수 없다면 유사 역행렬(pseudo-inverse)또는
#무어-펜로즈(Moore-Penrose)역행렬 A+을 이용한다
#n >= m인 경우 A+ = (AT*A)-1승 * AT
#n <= m인 경우 A+ =  AT * (A*AT)-1승
#n >= m이면 A+ * A = I가 성립한다
#n <= m이면 A * A+ = I가 성립한다

print(np.linalg.pinv(y))#n=m이 아닐 때 역행렬
print(np.linalg.pinv(y) @ y) #n>=m이기 때문에 np.linalg.pinv(y) @ y
#n<=m이면 y @ np.linalg.pinv(y)

#Scikit Learn을 활용한 회귀분석
from sklearn.linear_model import LinearRegression
model = LinearRegression()
x_test = model.fit(x,y)
y_test = model.predict(x_test)
print(y_test)

#Moore-Penrose 역행렬
#moore-penrose를 사용할때는 y절편(intercept)항울 직접 추가해야한다!
x_ = np.array([np.append(x,[1]) for x1 in x])#intercept항 추가
beta = np.linalg.pinv(x_) @ y
y_test = np.append(x, [1]) @ beta