###
# 구명보트
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/42885
# status : solved
# time : 00:05:14
###

def solution(people, limit):
    left, right = 0, len(people)-1
    people.sort()
    cnt = 0
    while left <= right :
        if left < right :
            candidate = people[left] + people[right]
            if candidate <= limit :
                cnt += 1
                left += 1
                right -= 1
            else :
                cnt += 1
                right -= 1
        else :
            cnt += 1
            break
    return cnt
