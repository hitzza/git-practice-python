#2022.06.01 최재혁
import datetime
'''
#입력 자료형 확인하기 
string = input("입력>")

#출력합니다.
print("입력값:", string)
print("자료형:", type(string))

print("입력 + 100", string + 100)

output_a = int("52")
output_b = float("52.273")

print(type(output_a), output_a)
print(type(output_b), output_b)

input_a = float(input("첫 번째 숫자>"))
input_b = float(input("두 번째 숫자>"))

print("덧셈", input_a + input_b)
print("뺼셈", input_a - input_b)
print("곱셈", input_a * input_b)
print("나눗셈", input_a / input_b)
'''
'''
now = datetime.datetime.now()

print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")

if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다!".format(now.hour))

if now.hour >= 12:
    print("현재 시각은 {}시로 오후입니다!".format(now.hour))

month = now.month
if 3 <= month <= 5:
    print("현재는 봄입니다.")
elif 6 <= month <= 8:
    print("현재는 여름입니다.")
elif 9 <= month <= 11:
    print("현재는 가을입니다.")
else:
    print("현재는 겨울입니다.")
'''
'''
list_a = [1,2,3,4,5]
del list_a[1]
print(list_a)
'''
array = [273, 32, 103, 57, 52]
for element in array:
    print(element)