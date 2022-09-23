###
# 스티커 붙이기
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/12971
# status : solved
# time : 00:15:27
###

def solution(sticker):
    length = len( sticker )
    if length == 1 :
        return sticker[0]

    dp = [[0]*2 for _ in range(length)]
    for i in range(1, length) :
        dp[i][0] = max(dp[i-1][0], dp[i-1][1])
        dp[i][1] = dp[i-1][0] + sticker[i]
    answer = max(dp[-1][0], dp[-1][1])
    
    dp = [[0]*2 for _ in range(length)]
    dp[0][1] = sticker[0]
    for i in range(1, length) :
        dp[i][0] = max(dp[i-1][0], dp[i-1][1])
        dp[i][1] = dp[i-1][0] + sticker[i]
    answer = max(answer, dp[-1][0])
    
    return answer
