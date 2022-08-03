###
# 아이템 줍기
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/87694
# status : solved
###

def solution(rectangle, characterX, characterY, itemX, itemY):
    map_list = [[0]*102 for _ in range(102)]
    visited = [[False]*102 for _ in range(102)]
    visited[characterY*2][characterX*2] = True
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for left_x, left_y, right_x, right_y in rectangle :
        for i in range(left_y*2, right_y*2+1):
            for j in range(left_x*2, right_x*2+1):
                map_list[i][j] = 1
    for left_x, left_y, right_x, right_y in rectangle :
        for i in range(left_y*2+1, right_y*2):
            for j in range(left_x*2+1, right_x*2):
                map_list[i][j] = 0
                
    q = [(characterX*2, characterY*2, 0)]
    while q :
        x, y, cnt = q.pop(0)
        if (x, y) == (itemX*2, itemY*2) :
            return cnt//2
        for k in range(4):
            ax, ay = x+dx[k], y+dy[k]
            if map_list[ay][ax] == 1 and not visited[ay][ax] :
                visited[ay][ax] = True
                q.append((ax,ay,cnt+1))
                

    return -1
