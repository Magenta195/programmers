###
# 최적의 행렬 곱셈
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/12942
# status : solved
# time : 00:17:40
###

def solution(matrix_sizes):
    MAX = float('inf')
    mat_length = len(matrix_sizes)
    dp = [[MAX]*mat_length for _ in range(mat_length)]
    
    for i in range(mat_length) :
        dp[i][i] = 0
        if i == mat_length - 1 : break
        dp[i][i+1] = matrix_sizes[i][0] * matrix_sizes[i][1] * matrix_sizes[i+1][1]

    for k in range(2, mat_length) :
        for i in range(mat_length - k) :
            for j in range(i,i+k) :
                dp[i][i+k] = min(dp[i][i+k], dp[i][j] + dp[j+1][i+k] + matrix_sizes[i][0]*matrix_sizes[j][1]*matrix_sizes[i+k][1])
                
    return dp[0][-1]
