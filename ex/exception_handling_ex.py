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
#pickle
#파이썬의 객체를 영속화(persistence)하는 built-in객체
#메모리에 올라와있는 data, object등 실행중 정보를 저장->불러와서 사용
#import pickle
'''
f = open("read_file_test.text", "wb")#w=write,b=binary
test = [1, 2, 3, 4, 5]
pickle.dump(test, f)
f.close()
'''
'''
f = open("read_file_test.text", "rb")#r=read,b=binary
test_pickle = pickle.load(f)
print(test_pickle)
f.close()
'''
#logging 모듈
'''
import logging
logging.debug("틀렸잖아!")#디버깅
logging.info("확인해")#정보를 주는 것
logging.warning("조심해")#exception처럼 무언가 잘못 되었을떄 보내는 것
logging.error("에러 났어!")#에러가 난걸 알려줌
logging.critical("망했다..")#프로그램이 완전히 종료가 되었을 때
'''
#logging level
#debug > info > warning > error > critical
#개발시점/   운영시점   /    사용자시점

#debug = 개발시 처리 기록을 남겨야하는 로그 정보를 남김
#info = 처리가 진행되는 동안의 정보를 알림
#warning = 사용자가 잘못 입력한 정보나 처리는 가능하나 원래 개발시 의도치 않는 정보가 들어왔을 때 알림
#error = 잘못된 처리로 인해 에러가 났으나, 프로그램은 동작할 수 있음을 알림
#critical =  잘묏된 처리로 데이터 손실이나 더이상 프로그램이 동작할 수 없음을 알림

import logging

if __name__ == '__main__':
    logger = logging.getLogger("main") #logger 선언
    logging.basicConfig(level=logging.DEBUG)#사용자level에선 warning부터 보여주지만 basicconfig을 사용해 레벨을 조정 가능
    #logger.setLevel(logging.ERROR)

    stream_handler = logging.FileHandler( #출력을 어떻게 할지 정하는 것
        "my.log", mode="a", encoding="utf-8" #my.log라는 파일에 출력, a= append의 약자 w로 write형태도 가능
    )
    logger.addHandler(stream_handler)

    logging.debug("틀렸잖아!")
    logging.info("확인해")
    logging.warning("조심해")
    logging.error("에러 났어!")
    logging.critical("망했다..")
