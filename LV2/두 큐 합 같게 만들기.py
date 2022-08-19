###
# 두 큐 합 같게 만들기
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/118667
# status : solved
# time : 00:20:56
###

def solution(queue1, queue2):
    total_queue = queue1 + queue2
    target = sum(total_queue)
    if target % 2 > 0 : return -1
    target //= 2
    
    answer = 0
    current_sum = sum(queue1)
    start, end = 0, len(queue1)
    
    while current_sum > 0 and start < len(total_queue) :
        if current_sum == target :
            return answer
        elif current_sum < target :
            current_sum += total_queue[end]
            end = (end + 1) % len(total_queue)
        else  :
            current_sum -= total_queue[start]
            start += 1
        answer += 1
    
    return -1
