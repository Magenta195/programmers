###
# 교점에 별 만들기
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/87377
# status : solved
###

def solution(line):
    length = len(line)
    answer_dot = []
    for i in range(length-1):
        for j in range(1, length):
            A, B, E = line[i]
            C, D, F = line[j]
            if A*D == B*C : continue
            denom = A*D-B*C
            if (B*F-E*D) % denom == (E*C-A*F) % denom == 0 :
                answer_dot.append(((B*F-E*D)//denom,(E*C-A*F)//denom))
    min_x = min_y = float('inf')
    max_x = max_y = -float('inf')
    
    for x, y in answer_dot :
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
        
    answer = [['.']*(max_x-min_x+1) for _ in range(max_y-min_y+1)]
    for x, y in answer_dot :
        answer[y-min_y][x-min_x] = '*'
    
    for i in range(len(answer)) :
        answer[i] = ''.join(answer[i])
        
    answer.reverse()
    return answer
