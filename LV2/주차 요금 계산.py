###
# 주차 요금 계산
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/92341
# status : solved
# time : 00:13:51
###

from collections import defaultdict
import math

def solution(fees, records):
    park_dict = defaultdict(int)
    time_dict = defaultdict(int)
    for recode in records :
        time, num, act = recode.split(' ')
        h, m = map(int, time.split(':'))
        total_time = 60*h + m
        
        if act == 'IN' :
            park_dict[num] = total_time
        else :
            start_time = park_dict[num]
            del park_dict[num]
            time_dict[num] += total_time - start_time
    
    for num, start_time in park_dict.items() :
        time_dict[num] += 60*23 + 59 - start_time
    
    basic_time, basic_fee, unit_time, unit_fee = fees
    fee_list = []
    for _, total_time in sorted(time_dict.items()) :
        total_fee = 0
        if total_time <= basic_time :
            total_fee = basic_fee
        else :
            total_fee = basic_fee + math.ceil(( total_time - basic_time) / unit_time ) * unit_fee
        fee_list.append(total_fee)
