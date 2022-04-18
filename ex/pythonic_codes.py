import pprint #print문 시각적으로 정렬해서 실행하는 모듈
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
#two dimetional list
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