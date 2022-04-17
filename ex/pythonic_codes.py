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
colors = ['red', 'blue', 'green', 'yellow']
print("-".join(colors))
print("    ".join(colors))
