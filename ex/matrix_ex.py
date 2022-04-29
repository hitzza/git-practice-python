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