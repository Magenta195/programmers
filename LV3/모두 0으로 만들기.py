###
# 모두 0으로 만들기
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/76503
# status : solved
# time : 00:22:00 + a
###

import sys
sys.setrecursionlimit(10**6)

def solution(a, edges):
    if sum(a) != 0 : return -1

    length = len(a)
    edge_dict = { key : [] for key in range(length)}
    visited = [False]*length
    visited[0] = True
    for x, y in edges :
        edge_dict[x].append(y)
        edge_dict[y].append(x)
        
    def dfs(node):
        diff = total_diff = 0
        
        for leaf in edge_dict[node]:
            if not visited[leaf]:
                visited[leaf] = True
                leaf_diff, leaf_total_diff = dfs(leaf)
                diff += leaf_diff
                total_diff += leaf_total_diff
        
        diff += a[node]
        total_diff += abs(diff)
        return diff, total_diff
    
    _, answer = dfs(0)
    
    return answer
