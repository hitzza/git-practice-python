import numpy as np
'''
a = np.array([1,2,3,4,5,6], int)
print(a.nbytes)

b = np.array([[1,2,3,4],[5,6,7,8]])

print(b)
print(b.reshape(8,))
'''
'''
td_tensor = np.array([[[1,2,3,4],[1,2,3,4]],
                       [[1,2,3,4],[1,2,3,4]],
                       [[1,2,3,4],[1,2,3,4]]])

print(td_tensor.reshape(-1,3,2))

npy_array = np.load(file="npy_test.npy")
print(npy_array.reshape(-1,2,2))
print(npy_array.reshape(-1,2,2).shape)

td_tensor = td_tensor.reshape(12,2)
npy_array = npy_array.reshape(12,1)
sum_array = td_tensor + npy_array
concat_array = np.concatenate((td_tensor,npy_array), axis= 1)
print(td_tensor)
print(npy_array)
print(sum_array)
print(concat_array)
'''
'''
test_a = np.arange(1,7).reshape(2,3)
test_b = np.arange(7,13).reshape(3,2)

print(test_a.dot(test_b))
print(test_b.dot(test_a))
print(test_b.max())#스칼라값 반환
print(np.argmax(test_b))#index값 반환
'''
a = np.array([[1,3,5],
             [2,6,0],
             [9,15,7]])
print(np.argmax(a, axis= 0))#최대값의 index번호
print(np.argmin(a, axis= 0))#최소값의 index번호
