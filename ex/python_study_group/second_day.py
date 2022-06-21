'''
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "메타종아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

value = dictionary.get("존재하지 않는 키")
print("값:", value)

if value == None:
    print("존재하지 않는 키에 접근했었습니다.")
#dictionary는 key를 기반으로 여러기자 지료를 저장하는 자료형이다.
#key는 dictionary내부에서 값에 접글할때 사용하는 것입니다.
#key : value
for i in dictionary:
    print(dictionary.get(i))
'''
#a = list(range(0,10,2))
#print(a)
''''
for i  in range(5):
    print(str(i) + "=반복변수")

print()
for i  in range(5,10):
    print(str(i) + "=반복변수")

print()
for i  in range(0,10,3):
    print(str(i) + "=반복변수")

print()
'''
'''
def print_n_time(n, *values):
    for i in range(n):
        for value in values:
            print(value)
            print()
print_n_time(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")
'''

def test():
    print("A지점 통과")
    yield 1
    print("B지점 통과")
    yield 2
    print("C지점 통과")

output = test()

print("D지점 통과")

a = next(output)
print(a)
print("E지점 통과")
b = next(output)
print(b)
print("F지점 통과")
c = next(output)
print(c)
next(output)
