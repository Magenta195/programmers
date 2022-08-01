###
# 전력망을 둘로 나누기
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/86971
# status : solved
# time : 00:10:17
###

def solution(n, wires):
    edge = { key : [] for key in range(1,n+1)}
    answer = float('inf')
    
    for a, b in wires:
        edge[a].append(b)
        edge[b].append(a)

    for a, b, in wires :
        visited = [False]*(n+1)
        visited[a] = visited[b] = True
        cnt_a, cnt_b = 0, 0
        q_a, q_b = [a], [b]
        while q_a :
            node = q_a.pop()
            cnt_a += 1
            for next in edge[node]:
                if not visited[next]:
                    visited[next] = True
                    q_a.append(next)
        while q_b : 
            node = q_b.pop()
            cnt_b += 1
            for next in edge[node]:
                if not visited[next]:
                    visited[next] = True
                    q_b.append(next)
        answer = min(answer, abs(cnt_a - cnt_b))
            
    return answer
