#exception
#0으로 숫자를 나눌때 예외처리 하기
'''
for i in range(10):
    try:
        print(10/i)
    except ZeroDivisionError:#다른 error를 넣게되면 시스템이 잡아내질 못함
        print("Not divided by 0")
'''
#exception이 하나가 아닐 떄
'''
a = [1, 2, 3, 4, 5]
for i in range(10):
    try:
        print(i, 10 // i)
        print(a[i])
        print(v)
    except ZeroDivisionError:
        print("Error")
        print("Not divided by 0")
    except IndexError as e: #어떤 에러인지 알아내기 위해 에러를 출력함
        print(e)
    except Exception as e:# 보통 마지막에 exception e를 설정함(특별히 exception을 지정하지 않아도 잡아냄)
        print(e)#다른 사용자가 어디서 exception이 발생했는지 알기 어렵기 떄문에 사용 자제
'''
#else구문 예외가 발생하지 않을 때 동작하는 코드
'''
for i in range(10):
    try:
        result = 10 // i
    except ZeroDivisionError:
        print("Not divided by 0")
    else:
        print(10 // i )
'''
#finally 예외 발생 여부와 상관없이 실행됨
'''
for i in range(10):
    try:
        result = 10 // i
    except ZeroDivisionError:
        print("Not divided by 0")
    else:
        print(10 // i)
    finally:
        print(i, "-------", result)
'''
#raise 필요에 따라 강제로 exception을 발생
'''
while True:
    value = input("변환할 정수 값을 입력해주세요.")
    for digit in value:
        if digit not in "0123456789":
            raise ValueError("숫자값을 입려하지 않으셨습니다.")
    print("정수값으로 변환된 숫자 - ", int(value))
'''
#assert구문 특정 조건에 만족하지 않을 경우 예외 발생
'''
def get_binary_number(decimal_number : int):
    assert isinstance(decimal_number, int)#이 구문이 true나 false로 구분 가능하게 해서 구분, false면 error를 발생시킴
    return bin(decimal_number)

print(get_binary_number(10.0))
'''
#file read
'''
f = open("read_file_test.text", "r")
content = f.read()
print(content)
f.close()
'''
#with구문과 함께 사용하기
'''
with open("read_file_test.text", "r") as f:
    #content = f.read()#string
    content_list = f.readlines()#\n기준으로 잘라서 리스트에 저장

    print(content_list)
    print(content_list[0])
'''
#실행 시 마다 한 줄 씩 읽어 오기
'''
with open("read_file_test.text", "r") as f:
    i = 0
    while True:
        line = f.readline()
        if not line:
            break
        print(str(i) + "===" + line.replace("\n", ""))
        i += 1
'''
#갯수 세기
'''
with open("read_file_test.text", "r") as f:
    content = f.read()
    word_list = content.split(" ")
    line_list = content.split("\n")

print("Total Number of Characters : ", len(content))
print("Total Number of Words : ", len(word_list))
print("Total Number of Lines : ", len(line_list))
'''
#file write
'''
f = open("read_file_test.text", "w", encoding="utf-8")
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
'''
#mode = a (append)기존에 있던거에 추가
'''
with open("read_file_test.text", mode = "a", encoding= "utf-8") as f:
    for i in range(11,21):
        data = "{0}번째 줄입니다.\n".format(i)
        f.write(data)
'''
#3444