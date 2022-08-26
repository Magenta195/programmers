###
# 방문 길이
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/49994
# status : solved
# time : ??? 
###

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
dr = {'U' : 0, 'D' : 1, 'R' : 2, 'L' : 3}
    
def solution(dirs):
    answer = 0
    row_visited = [[False]*10 for _ in range(11)]
    col_visited = [[False]*11 for _ in range(10)]
    x, y = 0, 0
    for _dirs in dirs :
        visited = row_visited if _dirs in ['R', 'L'] else col_visited
        ax, ay = x + dx[dr[_dirs]], y + dy[dr[_dirs]]
        if not (-6 < ax < 6 and -6 < ay < 6) : continue
        lower_x, lower_y = min(x, ax) + 5, min(y, ay) + 5
        if not visited[lower_y][lower_x] :
            answer += 1
            visited[lower_y][lower_x] = True
        x, y = ax, ay
        
    return answer
