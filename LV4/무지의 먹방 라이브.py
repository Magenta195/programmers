###
# 무지의 먹방 라이브
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/42891
# status : solved
# time : ???
###

def solution(food_times, k):
    if sum(food_times) <= k :
        return -1
    length = len(food_times)
    sorted_food_times = sorted(food_times)
    cur = 0
    
    remain_time = k
    prev, prev_h = -1, 0 
    while cur < length :
        start = cur
        start_h = sorted_food_times[start]
        while start_h == sorted_food_times[cur] :
            cur += 1
            if cur == length :
                break
        
        if cur == length or remain_time <= (start_h - prev_h) * (length - start) :
            break
        remain_time -= (start_h - prev_h) * (length - start)
        prev, prev_h = cur-1, start_h

    remain_time %= max(length - start, 1)
    for i, times in enumerate(food_times) :
        if times < start_h :
            continue
        if remain_time == 0 :
            return i+1
        remain_time -= 1
    
    return -1
