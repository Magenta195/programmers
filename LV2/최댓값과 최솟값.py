###
# 최댓값과 최솟값
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/42891
# status : solved
# time : 00:02:02
###

def solution(s):
    num_list = list(map(int, s.split()))
    return str(min(num_list)) + ' ' + str(max(num_list))
