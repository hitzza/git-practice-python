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
'''
print(np.arange(30))#range와 비슷
print(np.arange(0,5,0.5))#(시작, 미만, step)
print(np.arange(30).reshape(10,-1))#reshape가능