#2739
'''
gugu = int(input())

for i in range(1,10):
    print(f"{gugu} * {i} = {gugu*i}")
'''
#10950
'''
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(a+b)
'''
#8393
'''
n = int(input())
result = 0
for i in range(1,n+1):
    result += i
print(result)
'''
#2741
'''
a = int(input())

for i in range(1,a+1):
    print(i)
'''
#2742
'''
a = int(input())

for i in range(a):
    print(a-i)
'''
#11021
'''
input_num = int(input())

for i in range(1,input_num+1):
    a,b = map(int,input().split())
    print(f'Case #{i}: {a+b}')
'''
#11022
'''
input_num = int(input())

for i in range(1,input_num+1):
    a,b = map(int,input().split())
    print(f'Case #{i}: {a} + {b} = {a+b}')
'''
#2438
'''
input_num = int(input())

for i in range(input_num):
    i = '*'*(i+1)
    print(i.rjust(input_num))
'''
#10871
a,b = map(int,input().split())
c = list(map(int,input().split()))

result = []
for i in range(a):
    if c[i] < b:
        result.append(c[i])
print(*result)