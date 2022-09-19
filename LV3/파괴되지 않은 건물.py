###
# 파괴되지 않은 건물
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/92344
# status : solved
# time : 00:33:57
###


def solution(board, skill):
    row, col = len(board[0]), len(board)
    
    sum_mat = [[0]*(row+1) for _ in range(col+1)]
    
    for _type, r1, c1, r2, c2, degree in skill :
        _t = -1 if _type == 1 else 1
        sum_mat[r1][c1] += _t * degree
        sum_mat[r1][c2+1] -= _t * degree
        sum_mat[r2+1][c1] -= _t * degree
        sum_mat[r2+1][c2+1] += _t * degree
        
    for i in range(1, row+1) :
        sum_mat[0][i] += sum_mat[0][i-1]
    for i in range(1, col+1) :
        sum_mat[i][0] += sum_mat[i-1][0]
    
    for i in range(1, col+1) :
        for j in range(1, row+1) :
            sum_mat[i][j] += sum_mat[i][j-1] + sum_mat[i-1][j] - sum_mat[i-1][j-1]
    
    answer = 0
    for i in range(col) :
        for j in range(row) :
            if board[i][j] + sum_mat[i][j] > 0 :
                answer += 1
    
    return answer
