import numpy as np
#numpy
'''
test_array = np.array(["1", "3", 4, 5],float)
print(test_array)
print(test_array.dtype)#전체의 데이터 타입을 반환
print(test_array.shape)#tuple type으로 반환(4,)vector형태
matrix = np.array([[1,2,3,4],[1,2,3,4]])
print(matrix.shape)#(2,4)(row, column)matrix형태
three_rd_order_tensor = np.array([[[1,2,3,4],[1,2,3,4]],
                                 [[1,2,3,4],[1,2,3,4]],
                                 [[1,2,3,4],[1,2,3,4]]])
print(three_rd_order_tensor.shape)#(3,2,4)(tensor의 깊이(층),row,column)tensor
print(three_rd_order_tensor.ndim)#ndim =number of dimention(층 수)
print(three_rd_order_tensor.size)#전체 data 개수
print(three_rd_order_tensor.nbytes)#ndarray object의 메모리 크기를 반환함
print(three_rd_order_tensor.reshape(2,2,6))#원래 array의 크기만 같으면 reshape가
print(matrix.reshape(-1,2))#-1 = size를 기반으로!! row개수 선정
test_array = np.array(["1", "3", 4, 5],float)
print(test_array.reshape(-1,2))#vector를 matrix형태로 변환 가능
print(three_rd_order_tensor.flatten())#reshape을 써도 되지만 다차원의 array를 1차원으로 펴줄때 사용
'''
#indexing and slicing
#indexing
'''
a = np.array([[1,2,3],[4.5,5,6]],int)
print(a)
print(a[0,0])#Two dimentional array represention #1
print(a[0][0])#Two dimentional array represention #2
#indexing은 일반 파이썬 list와 같음
'''
#slicing
'''
a = np.array([[1,2,3,4,5],
              [6,7,8,9,10]],int)
print(a[:,2:])#전체Row의 2열 이상
print(a[1,1:3])#1번째Row의 1열~2열
print(a[1:3])#1번째Row ~ 2번째Row의 전체
#list와 달리 row와 column을 나눠서 slicing가능
print(a[:,::-1])#(:::)(이상,미만, 스텝)
print(a[::2::-1])#(:::)(이상,미만, 스텝)
print(np.arange(30))#range와 비슷
print(np.arange(0,5,0.5))#(시작, 미만, step),,floating point도 표시 가능
print(np.arange(30).reshape(10,-1))#reshape가능
'''
#ones, zeors and empty
#zeros = 0으로 가득찬 ndarray 생성
#ones를 써서 1로 가득찬 ndarray도 생성 가능
'''
print(np.zeros(shape=(10,), dtype=np.int8)) #np.zeors(shape, dtype, order)
print(np.zeros((2,5)))#2 by 5 -zero matrix 생성
'''
'''
#empty = shape만 주어지고, 비어있는 ndarray를 생성(memory initialization#메모리 초기화이 되지 않음)
print(np.empty(shape=(10,), dtype=np.int8)) #np.empty(shape, dtype, order) 메모리 초기화가 안되서 이상한 값이 나올 수도 있음
#something_like - 기존 ndarray 의 shape 크기 만큼 1,0 또는 empty array를 반환
test_matrix = np.arange(30).reshape(5, 6)
print(np.ones_like(test_matrix))
#identity - 단위행렬(i행렬)을 생성함
print(np.identity(n=3, dtype= int))
print(np.identity(5))
#eye - 대각선이 1인 행렬, k값의 시작 index의 변경이 가능
print(np.eye(N=3,M=5, dtype=np.int8))
print(np.eye(3))
print(np.eye(3,5, k=2))# k = start index
#diag - 대각 행렬의 값을 추출함
matrix = np.arange(9).reshape(3,3)
print(matrix)
print(np.diag(matrix))
print(np.diag(matrix, k=1))
#random sampling - 데이터 분포에 따른 sampling으로 array를 생성
print(np.random.uniform(0,1,10).reshape(2,5))#균등분포
print(np.random.normal(0,1,10).reshape(2,5))#정규분포
#sum , list의 sum과 동일
#mean() 평균 반환
#std() 표준편차 반환
#그 외 다양한 수학 연산자를 제공함
'''

#aixs 0= row, 1 = column ☆
'''
a = np.array([[1,2,3,4,5],
              [6,7,8,9,10]],int)
print(a.sum(axis=0))#row 기준으로 sum
print(a.sum(axis=1))#column 기준으로 sum
#(3,3,4)tensor의 형태면 axis(0,1,2)순서로 하나씩 밀린다 생각하면됨
#(3,4)matrix의 형태면 axis(0,1)
'''

#concatenate - numpy array를 합치는 함수
#vstack - axis=0을 기준으로 concat
#hstack - axis=1을 기준으로 concat
'''
a = np.array([1,2,3])#vector
b = np.array([4,5,6])#vector

print(np.vstack((a,b)))#metrix
print(np.concatenate((a,b), axis= 0))#vector위와 같이 만들려면 matrix로 합쳐야함
a = np.array([[1],[2],[3]])
b = np.array([[4],[5],[6]])
print(np.hstack((a,b)))

print(np.concatenate((a,b), axis= 1))
'''
#operation b/t arrays
#Element-wise operation - array간 shape이 같을 때 일어나는 연산
'''
test_a = np.array([[1,2,3], [4,5,6], [7,8,9]],float)
print(test_a)
print(test_a + test_a)#matrix + matrix 연산
print(test_a - test_a)#matrix - matrix 연산
print(test_a * test_a)#matrix내 element들 간 같은 위치에 있는 값들끼리 연산
'''

#Dot product - matirx의 기본연산(dot함수 사용)
test_a = np.arange(1,7).reshape(2,3)
test_b = np.arange(7,13).reshape(3,2)
print(test_a)
print(test_b)
print(test_a.dot(test_b))#일반 행렬 곱