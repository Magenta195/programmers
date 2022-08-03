###
# H-Index
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/42747
# status : solved
# time : 00:22:32
###

def solution(citations):
    length = len(citations)
    citations.sort(reverse=True)
    
    answer = 0
    for h in range(length):
        if citations[h] >= h+1 :
            answer = max(answer, h+1)
    
    return answer
