'''
a,b = map(int,input().split())
b_first = a * int(str(b)[2])
b_sec = a * int(str(b)[1])
b_third = a * int(str(b)[0])

print(b_first)
print(b_sec)
print(b_third)
print(b_first + b_sec*10 + b_third*100)
'''
'''
a,b = map(int,input().split())
b_first = b%10
b_sec = b //10 %10
b_third = b//100
b_first *= a
b_sec *= a
b_third *= a

print(b_first)
print(b_sec)
print(b_third)
print(b_first + b_sec*10 + b_third*100)
'''
a = int(input())
b = int(input())

b_first = b%10
b_sec = b //10 %10
b_third = b//100
b_first *= a
b_sec *= a
b_third *= a

print(b_first)
print(b_sec)
print(b_third)
print(b_first + b_sec*10 + b_third*100)
