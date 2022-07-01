'''
a = "Artifical Intelligence and Marchine Learning"
print(a[0:6], "AND", a[-9:])
print(a[:])
print(a[-50:50])
print(a[::-1])
a = "TEAM"
b = "LAB"
print(a + b)
print("T" in a)
'''
#문자열 명령어 예시
'''
title = "TEAMLAB X Upstage"
print(title.upper())
print(title.lower())
print(title.split(" "))#list
print(len(title))
print(title.isdigit())#숫자인지 확인
print("1234".isdigit())
'''
'''
a = 'It\'s OK' #\를 사용하면 어퍼스트로피 프린트
print(a)
a = "It's OK"
print(a) #큰 따옴표를 사용하면 어퍼스트로피로 프린트 가능
raw_string = "백슬래시 기능 활성화 \n가능?"
print(raw_string)
raw_string = r"백슬래시 기능 활성화 \n가능?"
print(raw_string)
'''
#ex[1, 2, 3, 4, 5]일 때 아래 함수 중 실제 swap이 일어나는 함수는?
'''
def swap_value(x,y):
    temp = x
    x = y
    y = temp

def swap_offset(offset_x, offset_y):
    temp = ex[offset_x]
    ex[offset_x] = ex[offset_y]
    ex[offset_y] = temp

def swap_reference(list_ex, offset_x, offset_y):
    temp_list = list_ex[:]#복사를 하고 시작하는걸 권장
    temp = list_ex[offset_x]
    list_ex[offset_x] = list_ex[offset_y]
    list_ex[offset_y] = temp

ex = [1, 2, 3, 4, 5]
swap_value(ex[0], ex[1])
print(ex)
swap_offset(0, 1)
print(ex)
ex = [1, 2, 3, 4, 5]
swap_reference(ex, 3, 4)
print(ex)
swap_reference(ex, 3, 4)
print(ex)
'''
#재귀함수(팩토리얼)
'''
def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)
calculation = int(input("Input Number for Factorial Calculation: "))
print(factorial(calculation))
'''
#위 재귀함수 코드를 일반 loop 코드로 변경

calculation = int(input("Input Number for Factorial Calculation: "))
factorial = 1
for i in range(0, calculation):
    factorial *= calculation
    calculation -= 1 

print(factorial)
