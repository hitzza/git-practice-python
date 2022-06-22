import sys

_T = int(sys.stdin.readline().rstrip('\n'))

if _T <= 1000000:
    for i in range(0,_T):
        a,b = map(int,sys.stdin.readline().rstrip('\n').split())
        if a<=1000 and b<= 1000:
            print(a+b)
        else:
            print('1,000이하의 수를 입력해주세요')
else:
    print('1,000,000이하의 수를 입력해주세요')