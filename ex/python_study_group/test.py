'''
a = [5,4,3,2,1]

b = [1,2,3,4,5]
b = a[:]

a.sort()

print(a)
print(b)

a = 1,2,3

print(type(a))
print(a)

def kwpacking(**kwargs):
    print(kwargs)
    print(type(kwargs))

kwpacking(a=1,b=2,c=3)#dict type
'''

a = [1,2,3,4,4,5,1,2]

print(set(a))
print(1e-2)