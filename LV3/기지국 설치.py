###
# 기지국 설치
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/12979
# status : solved
# time : 00:21:09
###

def solution(n, stations, w):
    wave_radius = 2*w + 1
    
    prev = 1
    answer = 0
    for station in stations :
        min_radius, max_radius = station - w, station + w
        if prev < min_radius :
            empty_length = min_radius - prev
            answer += (empty_length - 1) // wave_radius + 1
        prev = max_radius + 1
    
    if max_radius < n :
        answer += (n - prev) // wave_radius + 1
    
    return answer
