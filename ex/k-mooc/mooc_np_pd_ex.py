import numpy as np
import pandas as pd
'''
data = np.array([1,2,3,4,5,6])
data_2d = np.array([[1,2,3],[4,5,6]])
data_random = np.random.randn(2,3)
data_zeros = np.zeros(6)
data_ones = np.ones((2,3))
print(data)
print(data_2d)
print(data_2d.shape)
print(data_random)
print(data_zeros)
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
#broadcasting
'''
data = np.array([[5,9,7], [-7,-6,19], [6,8.9,11]])
data_2 = data*2
data_3 = data+3
print(data)
print(data_2)
print(data_3)
print(data > data_2)
'''
#배열의 통계 method
'''
data = np.array([[5,9,7], [-7,-6,19], [6,8.9,11]])
print(data)
print(data.sum())
print(data.mean())
print(data.max())
print(data.min())
print(data.max(axis=0))
index_1 = np.argmax(data,axis=0)
print(index_1)
'''
#Pandas
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
