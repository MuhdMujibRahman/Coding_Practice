def new_solution(inner, outer, points_x, points_y):
    list_of_cSqr = []
    dict_of_cSqr = {}
    for i in range(len(points_x)):
        a = points_x[i]
        b = points_y[i]
        coordinates = '%s,%s'%(a,b)
        c_sqr = a*a + b*b # Pythagoras Theorem
        list_of_cSqr.append(c_sqr)
        dict_of_cSqr.update({c_sqr:coordinates})

    list_of_cSqr.sort()
    start = 0
    end = len(list_of_cSqr) - 1
    c1 = inner
    c2 = outer
    import math
    if math.sqrt(list_of_cSqr[start]) < outer:  # Check first in list before the search
        while(c1 <= inner or c2 >= outer):
            mid = (start + end) // 2
            c1 = math.sqrt(list_of_cSqr[mid])
            if c1 <= inner:
                start = mid + 1
            elif c1 >= outer:
                end = mid
            else:
                start = mid
    
            c1 = math.sqrt(list_of_cSqr[start])
            c2 = math.sqrt(list_of_cSqr[end])
    
            if c2 >= outer:
                end = end - 1
        for eacVal in list_of_cSqr[start:end + 1]:
            print(dict_of_cSqr.get(eacVal))

if __name__ == '__main__':
    # inner = input()
    # outer = input()
    # point_x = [int(x) for x in input().split(',')]
    # point_y = [int(x) for x in input().split(',')]
    # new_solution(int(inner), int(outer), point_x, point_y)
    new_solution(2, 4, [4, 0, 1, -2], [-4, 4, 3, 0])
    #new_solution(int(2), int(4), [4,4,1,3,4], [4,3,4,3,2])
    #new_solution(int(5), int(10), [4,4,1,3,4,4,3,4,3,2,2,3,2,1,3,2,3,1,1,3], [4,1,3,4,3,2,4,4,3,1,1,1,4,1,4,3,2,3,1,2])
# 2
# 4
# 4,4,1,3,4
# 4,3,4,3,2
# 2
# 4
# [4,4,1,3]
# [4,4,3,4]