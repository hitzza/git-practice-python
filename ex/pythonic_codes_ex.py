#Project Euler 16번 문제 2^1000의 각 자릿수를 모두 더하면 얼마 입니까?

'''
num = 2**1000
list_num = list(str(num))
plus_num = 0
for i in list_num:
    int_num = int(i)
    plus_num += int_num
print(plus_num)
'''
##change_pythonic?_code
'''
num = 2**1000
list_num = list(str(num))
int_list = [int(i) for i in list_num]
result = sum(int_list)
print(result)
#other code
'''
'''
num=pow(2,1000)
num_list = list(map(int, str(num)))

print(sum(num_list))
'''