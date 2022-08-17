###
# 쿼드압축 후 개수 세기
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/68936
# status : solved
# time : 00:08:51
###

def solution(arr):
    length = len(arr)
    standard = arr[0][0]
    result = [0]*2
    
    if length == 1 :
        result[standard] += 1
        return result
    
    flg = True
    for i in range(length):
        for j in range(length):
            if arr[i][j] != standard :
                flg = False
                break
        if not flg : break
    if flg :
        result[standard] += 1
        return result
    
    sub_arr1 = [[arr[y][x] for x in range(length//2)] for y in range(length//2)]
    sub_arr2 = [[arr[y][x] for x in range(length//2, length)] for y in range(length//2)]
    sub_arr3 = [[arr[y][x] for x in range(length//2)] for y in range(length//2, length)]
    sub_arr4 = [[arr[y][x] for x in range(length//2, length)] for y in range(length//2, length)]
    
    for sub_arr in [sub_arr1, sub_arr2, sub_arr3, sub_arr4] :
        sub_result = solution(sub_arr)
        for i in range(2):
            result[i] += sub_result[i]
    
    return result
