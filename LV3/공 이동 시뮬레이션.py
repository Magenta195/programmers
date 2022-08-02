### 
# 공 이동 시뮬레이션 
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/87391
# status : solved
# time : 00:16:49
###

def solution(n, m, x, y, queries):
    end = len(queries)-1
    queries.reverse()
    left_x, left_y, right_x, right_y = y, x, y, x
    
    for direction, move in queries :
        if direction == 0 :
            right_x += move
            left_x = 0 if left_x == 0 else left_x+move
        elif direction == 1 :
            left_x -= move
            right_x = m-1 if right_x == m-1 else right_x-move
        elif direction == 2 :
            right_y += move
            left_y = 0 if left_y == 0 else left_y+move
        else :
            left_y -= move
            right_y = n-1 if right_y == n-1 else right_y-move
        
        if left_x > m-1 or left_y > n-1 or right_x < 0 or right_y < 0 : return 0
    
        left_x = max(left_x,0)
        left_y = max(left_y,0)
        right_x = min(right_x, m-1)
        right_y = min(right_y, n-1)
    
    return (right_x-left_x+1)*(right_y-left_y+1)
