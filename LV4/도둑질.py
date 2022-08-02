###
# 도둑질
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/42897
# status : solved
# time : 00:19:08
###

def solution(money):
    length = len(money)
    answer = 0
    for i in range(2):
        dp = [[0]*2 for _ in range(length)]
        for j in range(length):
            if j == 0 :
                dp[j][1] = money[j] if i == 1 else 0
            else :
                dp[j][0] = max(dp[j-1][1], dp[j-1][0])
                dp[j][1] = dp[j-1][0] + money[j]
                if i == 0 :
                    answer = max(answer, dp[j][0], dp[j][1])
                else :
                    answer = max(answer, dp[j][0])
    return answer
