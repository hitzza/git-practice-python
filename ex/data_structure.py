#stack
'''
a = [1, 2, 3, 4, 5]
a.append(10)
print(a)
a.append(20)
print(a)
a.pop()
print(a)
a.pop()
print(a)
'''
'''
word = input("Input a word: ")
word_list = list(word)

for _ in range(len(word_list)):
    print(word_list.pop())
    print(word_list)
'''
#Queue
'''
a = [1, 2, 3, 4, 5]
a.append(10)
a.append(20)
print(a)
print(a.pop(0))
a.pop(0)
print(a)
'''
#튜플 (값의 변경이 불가능한 리스트) 선언시 []가 아닌 () 사용
'''
t = (1, 2, 3)
print(type(t))
t = (1)
print(type(t))
t = (1,)
print(type(t))
'''
