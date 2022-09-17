###
# 양과 늑대
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/92343
# status : solved
# time : 00:30:33
###

def solution(info, edges):
    length = len(info)
    dp = [(-1,-1)]*(1 << length)
    dp[1] = (1,0)
    max_sheep = 1
    
    edge_dict = { key : [] for key in range(length)}
    for parent, leaf in edges :
        edge_dict[parent].append(leaf)
        
    for i in range(1, 1 << length ) :
        sheep, wolf = dp[i]
        if sheep == wolf == -1 : continue
        for j in range(length) :
            if i & (1 << j) : 
                for leaf in edge_dict[j] :
                    if i & (1 << leaf) : continue
                    next_sheep, next_wolf = sheep, wolf
                    if info[leaf] == 0 :
                        next_sheep += 1
                    else :
                        next_wolf += 1
                    if next_sheep <= next_wolf : continue
                    if (( dp[i | (1 << leaf)][0] < next_sheep ) or
                        ( dp[i | (1 << leaf)][0] == next_sheep and
                         dp[i | (1 << leaf)][1] > next_wolf)) :
                         
                        dp[i | (1 << leaf)] = (next_sheep, next_wolf)
                        max_sheep = max(max_sheep, next_sheep)
    
    return max_sheep
