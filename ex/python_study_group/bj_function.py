#15596
'''
def solve(a):
    ans = sum(a)
    return ans
'''
#4673
natural_num = set(range(1,10001))
general_num = set()

for i in range(1,10001):
    for j in str(i):
        i+= int(j)
    general_num.add(i)
self_num = sorted(natural_num - general_num)
for i in self_num:
    print(i)