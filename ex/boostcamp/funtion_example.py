#하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라
'''
def print_with_smile(input_smile):
    return input_smile + ":D"

input_smile = input("smile : ")
print(print_with_smile(input_smile))
'''
#현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라.
'''
def print_upper_price(now_price):
    upper_price = now_price * 1.3
    return upper_price

now_price = float(input("현재 가격을 상한가로 :"))
print(print_upper_price(now_price))
'''
#주어진 자연수가 홀수인지 짝수인디 판별해주는 함수 is_odd를 작성해 보자
'''
def is_odd(x):
    if x % 2 == 0:
        print(f"{x}는 짝수 입니다.")
    else :
        print(f"{x}는 홀수 입니다.")
x = int(input("숫자를 입력 하세요 :"))
print(is_odd(x))
'''
#입력으로 들어오는 모든 수의 평균 겂을 계산해주는 함수를 작성해보자
'''
def avg(*args):
    arr = []
    for i in args:
        arr.append(i)
    
    temp = 0
    for j in arr:
        temp += j
    
    result = temp / len(arr)
    
    return result
avg(1, 3, 5, 6, 6, 7, 9)    

print(f"평균 : {avg(1, 3, 5, 6, 6, 7, 9):.2f}")

'''
#다음 두 입력값의 오류를 수정해 보자
input1 = int(input("첫번째 숫자를 입력하세요 :"))
input2 = int(input("두번째 숫자를 입력하세요 :"))
total = input1 +input2
print(f"두 수의 합은 {total}입니다.")