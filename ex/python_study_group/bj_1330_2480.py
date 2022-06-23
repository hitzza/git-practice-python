#1330
'''
a,b = map(int,input().split())

if a >= -10000 and a <=10000 and b >= -10000 and b <=10000:
    if a>b:
        print(">")
    elif a<b:
        print("<")
    elif a==b:
        print("==")
'''
#9498
'''
score = int(input())

if 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
elif 60 <= score < 70:
    print("D")
else:
    print("F")
'''
#2753
'''
check_year = int(input())
check_1 = check_year // 100
check_2 = check_year % 100
if check_year % 4 ==0:
    if check_1 % 4 != 0:
        if check_2 == 0:
            print('0')
        else:
            print('1')
    else:
        print('1')
else:
    print('0') 
'''
#14681
'''
a = int(input())
b = int(input())

if a > 0 and b > 0:
    print(1)
elif a < 0 and b > 0:
    print(2)
elif a < 0 and b < 0:
    print(3)
elif a > 0 and b < 0:
    print(4)
'''
#2884
'''
h, m = map(int,input().split())

if 0 <= h <= 23 and 0 <= m <= 59:
    if m - 45 < 0:
        if h == 0:
            h += 23
            m += 15
            print(h, m)
        else: 
            h -= 1
            m += 15
            print(h, m)
    else:
        m -= 45
        print(h, m)
'''
#2525
'''
h,m = map(int,input().split())
c = int(input())
m_timer = c % 60
h_timer = c // 60

m += m_timer
h += h_timer
if m >= 60:
    m -= 60
    h += 1
    h %= 24
    print(h,m)
else:
    h %= 24
    print(h,m)
'''
#2480

d1, d2, d3 = map(int,input().split())
check_max = [d1,d2,d3]
if d1 == d2 == d3:
    print(10000 + d1 * 1000)
elif d1 == d2:
    print(1000 + d1 *100)
elif d1 == d3:
    print(1000 + d1 *100)
elif d2 == d3:
    print(1000 + d2 *100)
else:
    print(max(check_max)*100)