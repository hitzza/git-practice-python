# 점수별로 학점을 나누어보자 95점이상 A+ 60점 미만 F
'''
score = [38, 37, 7, 16, 97, 71, 63, 48, 49, 66, 37]
number = 0
for i in score:
    number = number + 1
    if i >= 95:
        print(f"{number}번째 학생 A+")
    elif i >= 90:
        print(f"{number}번째 학생 A")
    elif i >= 80:
        print(f"{number}번째 학생 B")
    elif i >= 70:
        print(f"{number}번째 학생 C")
    elif i >= 60:
        print(f"{number}번째 학생 D")
    elif i < 60:
        print(f"{number}번째 학생 F")
'''
#is는 메모리 주소 비교, 파이썬 4.0버전은 -5 ~ 256 넘어도 주소가 같은듯
'''
a = 100
b = 100

print(a is b)

a = 400
b = 400

print(a is b)
'''
#sring 비교 연산
'''
a = "hello"

if a in "o":
    print("o!")
elif a in "hello":
    print("hello!")
else:
    print("no")
'''
#리스트 내 다중 비교 연산일 경우
'''
boolean_list = [True, False, True, False, False]
print(all(boolean_list))#and연산
print(any(boolean_list))#or연산
'''
#삼항 연산자(조건문을 사용하여 참일 경우와 거짓의 경우 결과를 한줄에 표현)
'''
value = 13
is_event = True if value % 2 == 0 else False
print(is_event)
'''
#태어난 연도를 계산하여 학교 종류를 맞추는 프로그램
'''
birth_year = int(input("당신이 태어난 연도를 입력하세요"))
def school(x):
    age = 2022 - x + 1
    school_position = ""
    if age <= 26 and age >= 20:
        school_position = "대학생"
        return school_position
    elif age <= 20 and age > 17:
        school_position = "고등학생"
        return school_position
    elif age <= 17 and age > 14:
        school_position = "중학생"
        return school_position
    elif age <= 14 and age > 8:
        school_position = "초등학생"
        return school_position
    else:
        school_position = "학생이 아닙니다."
        return school_position
print(school(birth_year))
'''
#for = 반복횟수를 명확하게 알 때, while = 반복횟수가 명확하지 않을 때 
#break, countinue
'''
for i in range(0, 10):
    if i == 5:
        break
    print(i)
print("End Of Program")

for i in range(0, 10):
    if i == 5:
        continue
    print(i)
print("End Of Program")
'''
#숫자를 입력받아 구단을 출력하는 프로그램을 만드시오
gugu = int(input("구구단 몇단을 계산할까요?"))
print(f"구구단 {gugu}단을 계산합니다.")
for i in range(1, 10):
    print(f"{gugu} X {i} = {gugu * i}")