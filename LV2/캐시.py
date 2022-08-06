###
# 캐시
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/17680
# status : solved
# time : 00:06:09
###

def solution(cacheSize, cities):
    if cacheSize == 0 :
        return 5*len(cities)
    cache = ['']*cacheSize
    answer = 0

    for city in cities :
        city = city.lower()
        if city in cache :
            answer += 1
            cache.remove(city)
        else :
            answer += 5
            cache.pop(0)
        cache.append(city)        
    return answer
