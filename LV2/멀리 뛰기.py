###
# 멀리 뛰기
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/12914
# status: solved
# time : 00:02:00
###

def solution(n):
    if n == 1 :
        return 1
    elif n == 2 :
        return 2
    
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1) :
        dp[i] = ( dp[i-1] + dp[i-2] ) % 1234567
    return dp[-1] 
