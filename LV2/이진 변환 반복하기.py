###
# 이진 변환 반복하기
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/70129
# status: solved
# time : 00:05:20
###

import re

def solution(s):
    count_zero, times = 0, 0
    while s != '1' :
        times += 1
        count_zero += s.count('0')
        s = bin(len(re.sub('0+','',s)))[2:]
    return [times, count_zero]
