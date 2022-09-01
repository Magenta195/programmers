###
# 단어 퍼즐
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/12983
# status : solved
# time : 00:15:47
###

def solution(strs, t):
    MAX = float('inf')

    t_len = len(t)
    str_dict = { key : set() for key in range(1, 6)}
    for s in strs :
        str_dict[len(s)].add(s)
    
    dp = [MAX]*(t_len+1)
    dp[0] = 0
    
    for i in range(1, t_len+1):
        for j in range(1, 6):
            if i < j : continue
            t_piece = t[i-j:i]
            if t_piece in str_dict[j] :
                dp[i] = min(dp[i], dp[i-j]+1)
            
    return dp[-1] if dp[-1] < MAX else -1
