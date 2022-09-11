
###
# 숫자 블록
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/12923
# status : solved
# time : 00:38:12
###

def solution(begin, end):
    answer = []
    
    for num in range(begin, end+1) :
        for i in range(2, int(num**(1/2))+1) :
            if num % i == 0 :
                if num//i > 10000000 :
                    continue
                answer.append(num//i)
                break
        else :
            answer.append(1 if num > 1 else 0)
                
    return answer
