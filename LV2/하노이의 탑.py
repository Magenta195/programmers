###
# 하노이의 탑
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/12946
# status : solved
# time : 00:10:12
###

tower_set = set([1, 2, 3])

def solve(cur, cur_h, target) :
    if cur_h == 1 :
        return [[cur, target]]
    new_target = 6 - cur - target
    result = solve(cur, cur_h-1, new_target)
    result.extend([[cur, target]])
    result.extend(solve(new_target, cur_h-1, target))
    
    return result

def solution(n):
    return solve(1, n, 3)
