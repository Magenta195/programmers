###
# 가장 큰 정사각형
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/12905
# status : solved
# time : 00:31:21
###

def solution(board):
    col, row = len(board), len(board[0])
    
    for i in range(1, col):
        for j in range(1, row):
            if board[i][j] == 1:
                min_len = min(board[i][j-1],board[i-1][j],board[i-1][j-1])
                if min_len > 0 :
                    board[i][j] = min_len + 1
    
    return max(map(max, board))**2
