###
# N-Queen
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/12952
# status : solved
# time : 00:31:28
###


from collections import deque

def solution(n):
    answer = 0
    q = deque([(0,0,0,0)])
    diagonal = n*2-1
        
    while q :
        col, row_visited, diag_visited_1, diag_visited_2 = q.pop()
        for row in range(n) :
            diag_1 = 1 << (row + col)
            diag_2 = 1 << (n - col + row)
            row = 1 << row
            
            if diag_1 & diag_visited_1 or diag_2 & diag_visited_2 or row & row_visited :
                continue
            if col == n-1 :
                answer += 1
            else :
                q.append((col+1, row_visited | row, diag_visited_1 | diag_1, diag_visited_2 | diag_2))
    
    return answer
