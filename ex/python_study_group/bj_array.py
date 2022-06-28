#10818
'''
input_num = int(input())
input_list = list(map(int,input().split()))
output_list = []
for i in range(input_num):
    output_list.append(input_list[i])
print(min(output_list), max(output_list))
'''
#2562
'''
input_list = []
for i in range(9):
    input_list.append(int(input()))
print(max(input_list))
print(input_list.index(max(input_list))+1)
'''
#2577
'''
a = int(input())
b = int(input())
c = int(input())
count = [0,0,0,0,0,0,0,0,0,0]
mul = a * b * c
str_mul = str(mul)
for i in str_mul:
    count[int(i)] += 1
for j in count:
    print(j)
'''
#3052
'''
num_list = []
for i in range(10):
    num_list.append(int(input())%42)
num_list = set(num_list)
print(len(num_list))
'''
#1546
'''
a = int(input())
score = list(map(int, input().split()))
result = 0
for i in score:
    result += i / max(score) * 100
print(result/a)
'''
#8958
a = int(input())
count = 1
score = 0
for i in range(a):
    input_list = list(input().upper())
    for j in input_list:
        if j =='O':
            score += count
            count += 1
        else :
            count = 1
    print(score)
    score = 0
    count = 1