###
# 땅따먹기
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/12949
# status : solved
# time : 00:04:49
###

def solution(land):
    length = len(land)
    max_answer = [land[0][:] for _ in range(length)]
    
    for i in range(length-1) :
        for j in range(4) :
            for k in range(4) :
                if j == k :
                    continue
                max_answer[i+1][k] = max(max_answer[i+1][k], max_answer[i][j] + land[i+1][k])

    return max(max_answer[-1])
