from traceback import print_tb
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
'''test_a = np.arange(1,7).reshape(2,3)
test_b = np.arange(7,13).reshape(3,2)
print(test_a)
print(test_b)
print(test_a.dot(test_b))#일반 행렬 곱
'''

#broadcating- shape이 다른 배열 간 연산을 지원하는 기능
#scalar - vector 외에도, vector - matrix 간의 연산도 지원
'''
test_matrix = np.array([[1,2,3], [4,5,6], [7,8,9]],float)
scalar = 3
print(test_matrix + scalar)
print(test_matrix * scalar)
'''
#concat은 numpy에서는 비효율적

#comparisons 비교
'''
#all & any
a = np.arange(10)
print(a>5)#broadcasting형식으로 비교한다고 생각하면 됨
#any = 하나라도 만족되면 TRUE
print(np.any(a>5), np.any(a < 0))
#all = 모두 만족되면 TRUE
print(np.all(a>5), np.all(a < 10))

#np.where - 조건에 만족하는 index값을 반환
a = np.array([1,3,0])
print(np.where(a > 0, 3,2))#where(조건, true일 경우 리턴값, false일 경우 리턴값)
print(np.where(a > 0))#리턴 값을 설정 안할경우 true의 Index값을 반환 false는 아무거도 반환하지 않음
'''
#argmax & argmin 
'''
#array내 최대값 또는 최소값으 index를 반환함
a = np.array([1,2,4,5,7,14,66,73,88,3])
print(np.argmax(a))#최대값의 index번호
print(np.argmin(a))#최소값의 index번호
#axis를 이용해 axis축에 맞는 최소 최대값 찾기 가능
a = np.array([[1,3,5],
             [2,6,0],
             [9,15,7]])
print(np.argmax(a, axis= 0))#최대값의 index번호
print(np.argmin(a, axis= 0))#최소값의 index번호
#일반적인 axis와 기준이 반대인듯
'''
#boolean index- numpy 배열은 특정 조건에 따른 값을 배열 형태로 추출 할 수 있음
#comparison operation함수들도 모두 사용 가눙
'''
test_array = np.array([1,3,4,9,0,12,2],float)
print(test_array > 3)
print(test_array[test_array > 3])
condition = test_array > 3
print(test_array[condition])
print(condition.astype(np.int0))#0,1아웃풋으로도 수정 가능!
'''
#fancy index - numpy는 array를 index value로 사용해서 값을 추출하는 방법
a = np.array([2,4,6,8], float)
b = np.array([0,0,1,3,2,1], int)#반드시 int형으로 선언
print(a[b])#b 배열의 값을 index로 하여 a의 값들을 추출함
print(a.take(b))#위와 같은 효과
a = np.array([[1,4], [9,16]], float)
b = np.array([0,0,1,1,0], int)
c = np.array([0,1,1,1,1], int)
print(a[b,c])# b를 row index, c를 column index로 변환하여 표시함
#[(0,0), (0,1), (1,1), (1,1), (0,1)]
#[  1       4      16   16      4]

#numpy object - npy
#numpy object(pickle)형태롤 데이터를 저장하고 불러옴
#binary형태로 저장함
#a_int = np.array([[1900, 30000, 4000, 48300],
#                  [1901, 47200, 6100, 48200],
#                  [1902, 70200, 9800, 41500]])
#np.save("npy_test", arr=a_int)

npy_array = np.load(file="npy_test.npy")
print(npy_array[:])