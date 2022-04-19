class SoccerPlayer(object):
    def __init__(self, name : str, position : str, back_number : int): #__init__은 객체 초기화 예약 함수
        self.name = name
        self.position = position
        self.back_number = back_number

    
    def change_back_number(self, new_number):#method(Action)추가는 기존 함수와 같으나 반드시★self★를 추가해야만 class함수로 인정됨!
        print("선수의 등번호를 변경합니다 : From %d to %d" % (self.back_number, new_number))
        self.back_number = new_number

    #__는 특수함 예약 함수나 변수 그리고 함수명 변경(맨글링)으로 사용
    def __str__(self):#__str__는 print함수를 호출할때 return값으로 출력
        return "Hello, My name is %s. My backnumber is %d" %\
            (self.name, self.back_number)#self = 생성된 instance 자신    
    def __add__(self, other): #__add__는 두 값을 더해주는 함수
        return self.name + other.name

son = SoccerPlayer("son", "FW", 7)
park = SoccerPlayer("park", "WF", 13)

print(son)
print(son + park)

#object(instance)사용하기
#Object이름 선언과 함께 초기값 입력하기
jinhyun = SoccerPlayer("Jinhyun", "MF", 10)
print("현재 선수의 등번호는 :", jinhyun.back_number)
jinhyun.change_back_number(5)
print("현재 선수의 등번호는 :", jinhyun.back_number)
