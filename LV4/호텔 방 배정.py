###
# 호텔 방 배정 (LV4)
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/64063
# status : solved
###

### trial 1 (union find, memory error)
def solution(k, room_number):
    rooms = list(range(k))
    answer = []
    def find(num):
        if rooms[num] == num :
            return num
        rooms[num] = find(rooms[num])
        return rooms[num]
    
    def union(num1, num2):
        rooms[num1] = num2
    
    for num in room_number :
        room_num = find(num-1)
        if room_num < k-1 :
            left_num = find(room_num+1)
            union(room_num, left_num)
        answer.append(room_num+1)
    return answer
 
### trial 2 (solved, union-find + dictionary)
import sys
sys.setrecursionlimit(10**6)

def solution(k, room_number):
    rooms = {}
    answer = []
    
    def find(num):
        if num not in rooms :
            rooms[num] = num+1
            return num
        rooms[num] = find(rooms[num])
        return rooms[num]
    
    for num in room_number :
        num = find(num)
        answer.append(num)

    return answer
