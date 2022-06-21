#https://programmers.co.kr/learn/courses/30/lessons/77484?language=python3

def solution(lotto,win_nums):
    answer = []
    check_input_lotto = []
    for_count = 0

    for win_lotto in lotto:
        if win_lotto in win_nums:
            #print(win_lotto)
            check_input_lotto.append(lotto.pop(for_count))        
        for_count +=1

    return print(check_input_lotto)
solution([1,8,3,4,5,7], [1,3,4,7,8,9])