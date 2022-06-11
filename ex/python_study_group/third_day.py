'''
inch_input = int(input("Inch를 입력해주세요 :"))

change_cm = inch_input * 2.54

print(inch_input,"Inch는", change_cm,"cm입니다.")

number = int(input("정수입력 :"))

if number < 0:
  print("음수입니다.")

if number > 0:
  print("양수입니다.")
  
if number == 0:
  print("0입니다.")


input_num = input("정수 입력>")
last_num = int(input_num[-1])
check_num = last_num % 2

if check_num == 1:
  print("홀수입니다")
if check_num == 0:
  print("짝수입니다")


list_a = [1,2,3]
list_b = [4,5,6]

print("# 리스트")
print("list_a =", list_a)
print("list_b =", list_b)
print()

#기본 연산자
print("#리스트 기본 연산자")
print("list_a + list_b = ", list_a + list_b)
print("list_a * 3", list_a * 3)
print()

#함수
print("#길이 구하기")
print("len(list_a)", len(list_a))
'''
