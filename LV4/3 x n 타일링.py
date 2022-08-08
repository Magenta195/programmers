###
# 3 x n 타일링
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/12902
# status : solved
# time : 00:25:08
###

def solution(n):
    if n%2 == 1 : return 0
    
    dp = [0]*(n+1)
    dp[0] = 1
    dp[2] = 3
    for i in range(4, n+1, 2):
        dp[i] += (dp[i-2]*3) % 1000000007
        for j in range(0, i-3, 2):
            dp[i] += (dp[j]*2) % 1000000007
    return dp[-1] % 1000000007
