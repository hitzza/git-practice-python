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