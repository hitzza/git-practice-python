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
'''
a,b = map(int,input().split())
c = list(map(int,input().split()))
result = []
for i in range(a):
    if c[i] < b:
        result.append(c[i])
print(*result)
'''
#10952
'''
while True:
    a, b = map(int,input().split())

    if a == 0 and b == 0:
        break
    else:
        print(a + b)
'''
#10951
'''
while True:
    try:
        a, b = map(int,input().split())
        print(a + b)
    except EOFError:
        break
'''
#1110
'''
a = int(input())
check_a = a
count = 0
if 0 <= a <= 99:
    while True:
        if a < 10:
            a = str(a).rjust(2,'0')
            b = int(a[0]) + int(a[1])
            a = int(a[1] + str(b%10))
            count += 1
            if a == check_a:
                print(count)
                break
        elif a > 10:
            a = str(a)
            b = int(a[0]) + int(a[1])
            a = int(a[1] + str(b%10))
            count += 1
            if a == check_a:
                print(count)
                break
#timeout!
'''
'''
a = int(input())
check_a = a
count = 0
if 0 <= a <= 99:
    while True:
        if a < 10:
            a = int(str(a) + str(a))
            count += 1
            if a == check_a:
                print(count)
                break
        else:
            b = (a//10) + (a%10)
            a = str(a%10) + str(b%10)
            a = int(a)
            count += 1
            if a == check_a:
                print(count)
                break
'''