###
# 빛의 경로 사이클
# problem :  https://school.programmers.co.kr/learn/courses/30/lessons/86052
# status : solved
# time : 00:11:21
###

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
dd = { 'L' : -1, 'S' : 0, 'R' : 1}
def solution(grid):
    col, row = len(grid), len(grid[0])
    visited = [[[False]*4 for _ in range(row)] for _ in range(col)]
    answer = []
    for i in range(col) :
        for j in range(row) :
            for k in range(4) :
                if not visited[i][j][k] :
                    x, y, d = j, i, k
                    cnt = 0
                    while True :
                        visited[y][x][d] = True
                        x, y = (x + dx[d]) % row, (y + dy[d]) % col
                        d = (d + dd[grid[y][x]]) % 4
                        cnt += 1
                        if visited[y][x][d] :
                            break
                    answer.append(cnt)
    answer.sort()
    return answer
