###
# 행렬의 곱셈
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/12949
# status : solved
# time : 00:02:57
###

def solution(arr1, arr2):
    col, row, row_2 = len(arr1), len(arr1[0]), len(arr2[0])
    new_arr = [[0]*row_2 for _ in range(col)]
    
    for i in range(col) :
        for j in range(row_2) :
            for k in range(row) :
                new_arr[i][j] += arr1[i][k] * arr2[k][j]
    
    return new_arr
