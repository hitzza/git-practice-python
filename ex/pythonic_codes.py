from functools import reduce
from operator import ge
import pprint#print문 시각적으로 정렬해서 실행하는 모듈
#XX
'''
colors = ['red', 'blue', 'green', 'yellow']
result = ''
for s in colors:
    result += s
print(result)
#pythonic codes ex
colors = ['red', 'blue', 'green', 'yellow']
result = ''.join(colors)
print(result)
#pythonic code
#split & join
#list comprehension
#enumerate & zip
#lambda & map & reduce
#generator
#asterisk
'''
'''
#string type의 값을 '기준값'으로 나눠서 list형태로 변환
items = 'zero one two three'.split() #빈칸을 기준으로 문자열 나누기
print(items)#list
print(type(items))#list
example = 'python, java, javascript'#','을 기준으로 문자열 나누기 
example.split(",")
print(example)#string

a, b, c = example.split(",")#리스트에 있는 각 값을 a, b, c로 unpacking
print(b)#string

example = 'teamlab.technology.io'
subdomain, domain, tld = example.split('.')
print(domain)
print(type(domain))#string
'''
#split으로 나누고 join으로 합친다.
'''
colors = ['red', 'blue', 'green', 'yellow']
print("-".join(colors))
print("    ".join(colors))
'''

#list comprehension★☆★☆★☆
#ex
'''
result = []
for i in range(10):
    result.append(i)
print(result)
#list comprehension
result = [i for i in range(10)]
print(result)
result = [i for i in range(10) if i % 2 == 0]#조건문도 사용 가능
print(result)

#다중 for문
word_1 = "Hello"
word_2 = "World"
result = [i + j for i in word_1 for j in word_2]
print(result)
#for i in word_1:
#   for j in word_2:
#       result = i + j

case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "A"]
result = [i + j for i in case_1 for j in case_2]
print(result)

result = [i + j for i in case_1 for j in case_2 if not(i==j)]
#Filter : i랑 j 가 같다면 List에 추가하지 않음
print(result)
result = [i + j if not(i == j) else i for i in case_1 for j in case_2]
#if i==j일 경우 i만 써라(if문 처리는 강의를 들어도 잘 모르겠다)
print(result)
result.sort()
print(result)
'''
'''
#two dimentional list
words = 'The quick brown fox jumps over the lazy dog'.split()
#문장을 빈칸 기준으로 나눠 list로 변환
print(words)
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
#list의 각 elemente들을 대문자, 소문자, 길이로 변환하여 two dimenstional list 로 변환
pprint.pprint(stuff)

case_1 = ["A", "B", "C"]
case_2 = ["C", "E", "A"]

result = [[j + i for i in case_2] for j in case_1]
pprint.pprint(result)
'''
#enumerate & zip
'''
my_str = "ABCD"
print({v : i for i, v in enumerate(my_str)})

text = "Samsung Group is a South Korean mulination conglomerate headquarterd in Samsung"
text_list = list(set(text.split()))#set을 사용해서 중복 제거
print({i : v.lower() for i , v in enumerate(text_list)})
#zip 두개의 리스트를 병렬로 병합
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a, b in zip(alist, blist):
    print(a, b)
for i , values in enumerate(zip(alist, blist)):
    print(i, values)
print([c for c in zip(alist, blist)])#튜플 타입으로 묶어서 c에 저장
print(list(enumerate(zip(alist, blist))))#2dimentional listfh enumerate와 중복사용 가능

math = (100 ,90, 80)
kor = (90, 90, 90)
eng = (90, 70 ,80)

print([sum(value) / 3 for value in zip(math, kor, eng)])    

a, b, c = zip((1, 10, 100), (2, 20, 200), (3, 30, 300))
print(a)
'''
#lambda & map $ reduce
'''
f  = lambda x, y : x + y# lambda(input): return
print((lambda x, y : x + y)(10, 50))
#map 시퀀스형 리스트에 함수를 각각 맵핑 해주는 함수
ex = [1, 2, 3, 4, 5]
f = lambda x: x**2
#map
print(list(map(f, ex))) #map(function, function의 input수 만큼 input)
print([f(value) for value in ex])#리스트로 묶지말고 처음부터 list_comprehension으로 선언가능
print([value**2 if value % 2 == 0 else value for value in ex])#value값이 짝수 일 때 값을 제곱해서 출력
#f = lambda x, y : x + y
#print(list(map(f, ex, ex)))#list형태로 출력해주어야함
'''
'''
#reduce: map_function 과 달리 list에 똑같은 함수를 적용해서 통합
print(reduce(lambda x, y : x+y, [1, 2, 3, 4, 5]))#1+2 -> 3+3 -> 6+4 -> 10+5

#iterable object -Sequence형 자료형에서 디이터를 순서대로 추출하는 object
cities = ["Seoul", "Busan", "Jeju"]

iter_obj = iter(cities)#내부적 구현으로  __iter__와 __next__가 사용됨(구현되어 있음)
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
#genearator - iterable object를 특수한 형태롤 사용해주는 함수
#element가 사용되는 시점에 값을 메모리에 반환
#:yield를 사용해 한번에 하나의 element를 반환함

#def general_list(value):
#    result = []
#    for i in range(value):
#        result.append(i)
#    return result

def general_list(value):
    result = []
    for i in range(value):
        yield i
print(general_list(50))#genearator형태로 반환
print([value for value in general_list(50)])#for문으로 풀어서 출력해야함
#차이점 호출할때만 메모리에 올림 일반 리스트는x
#genearator_comprehension
gen_ex = (n*n for n in range(500))
print(gen_ex)#for나list를 사용해서 출력가능
'''

#function passing arguments
#keyword arguments - 함수에 입력되는 parameter의 변수명을 사용, arguments를 넘김
def print_somthing(my_name, your_name):
    print("Hello {0}, My name is {1}".format(your_name, my_name))

print(print_somthing("Sungchul", "TEAMLAB"))
print(print_somthing(your_name="TEAMLAB", my_name="Sungchul"))

#default argument - parameter의 기본값을 사용, 입력하지 않을 경우 기본값 출력
def print_somthing2(my_name, your_name="TEAMLAB"):
    print("Hello {0}, My name is {1}".format(your_name, my_name))
print(print_somthing2("Sungchul"))

#variable-length-asterisk
#함수의  parameter가 정해지지 않을경우 가변인자 vaiable-length
def asterisk_test(a, b, *args):
    return a+b+sum(args)
print(asterisk_test(1, 2, 3, 4, 5, 6, 7))

#keyword varialbe-length
def kword_test(**kwargs):
    print(kwargs)

print(kword_test(first = 3, second = 4, third = 5))

def kwargs_text3(one, two, *args, **kwargs):
    print(one + two + sum(args))
    print(kwargs)

print(kwargs_text3(3, 4, 5, 6, 7, 8, first = 1, second = 3, third = 5))