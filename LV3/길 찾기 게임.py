###
# 길 찾기 게임
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/42892
# status : solved
# time : 00:47:11
###

mport sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    edge = {}
    for idx, (x, y) in enumerate(nodeinfo):
        if y not in edge : edge[y] = []
        edge[y].append((x, idx+1))
        
    level_list = list(edge.keys())
    level_list.sort(reverse=True)
    max_depth = len(level_list)
        
    def find_child(start, end, depth):
        if depth == max_depth :
            return
        
        y = level_list[depth]
        for x, idx in edge[y]:
            if start < x < end :
                return (x, idx)
        return
    
    def search(start, end, mid_x, mid_idx, depth, preorder):
        left_child = find_child(start, mid_x, depth+1)
        if left_child is not None :
            left_x, left_idx = left_child
            left_list = search(start, mid_x, left_x, left_idx, depth+1, preorder) 
        else :
            left_list = []
        
        right_child = find_child(mid_x, end, depth+1)
        if right_child is not None:
            right_x, right_idx = right_child
            right_list = search(mid_x, end, right_x, right_idx, depth+1, preorder)
        else :
            right_list = []
        
        if preorder :
            return [mid_idx] + left_list + right_list
        else :
            return left_list + right_list + [mid_idx]
        
    init_y = level_list[0]
    init_x, init_idx = edge[init_y][0]
        
    answer = [search(-1,1000001, init_x, init_idx, 0, True), search(-1,1000001, init_x, init_idx, 0, False)]
               
    return answer
