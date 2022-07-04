import numpy as np
'''
data = np.array([1,2,3,4,5,6])
print(data)
data_2d = np.array([[1,2,3],[4,5,6]])
print(data_2d)
print(data_2d.shape)
data_random = np.random.randn(2,3)
print(data_random)
data_zeros = np.zeros(5)
print(data_zeros)
data_ones = np.ones((2,3))
print(data_ones)
'''
'''
data = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print(data)
print(data[0][1])
print(data[0][1:])
data[0] = 100
print(data)
data[:] = 300
print(data)
'''
'''
data = np.array([[5,9,7],
                [-7,-6,19],
                [6,8.9,11]])

data_2 = data*2
data_3 = data +3
print(data)
print(data_2)
print(data_3)
print(data > data_2)
'''
