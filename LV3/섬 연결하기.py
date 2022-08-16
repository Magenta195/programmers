###
# 섬 연결하기
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/42861
# status : solved
# time: 00:13:48
###

from heapq import heappush, heappop

def prim(start, edge, n):
    visited = [False]*n
    visited[start] = True
    q = []
    result = 0
    
    for cost, node in edge[start]:
        heappush(q, (cost, node))
    while q:
        cost, node = heappop(q)
        if visited[node] : continue
        visited[node] = True
        result += cost
        for next_cost, next_node in edge[node]:
            if not visited[next_node]:
                heappush(q, (next_cost, next_node))
    return result
    

def solution(n, costs):
    edge = { key : [] for key in range(n)}
    for a, b, cost in costs :
        edge[a].append((cost, b))
        edge[b].append((cost, a))

    return prim(0, edge, n)
