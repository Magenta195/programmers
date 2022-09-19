###
# 지형 편집
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/12984
# status : solved
# time : over 01:30:00
###

def solution(land, P, Q):
    land_list = []
    
    for _land in land :
        land_list.extend(_land)
        
    land_list.sort()
    if land_list[0] == land_list[-1] :
        return 0
    
    length = len(land_list)
    p_cost = 0
    q_cost = sum(land_list) - length * land_list[0]
    answer = Q * q_cost
    for i in range(length-1) :
        if land_list[i] != land_list[i+1] :
            p_cost += ( land_list[i+1] - land_list[i] ) * (i + 1)
            q_cost -= ( land_list[i+1] - land_list[i] ) * (length - i - 1)
            cost = P * p_cost + Q * q_cost
            if cost >= answer :
                break
            answer = cost
    
    return answer
