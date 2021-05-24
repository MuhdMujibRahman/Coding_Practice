def solution(inner, outter, points_x,points_y):
    list_of_c_sqr = []
    dict_of_c_sqr = {}

    for i in range(len(points_x)):
        a,b = points_x[i],points_y[i]
        c_sqr = a*a + b*b
        coordinates = '%s,%s'%(a,b)
        list_of_c_sqr.append(c_sqr)
        dict_of_c_sqr.update({c_sqr:coordinates})

    list_of_c_sqr.sort()

    start = 0
    end = len(list_of_c_sqr) - 1
    c1 = inner
    c2 = outter

    import math
    if math.sqrt(list_of_c_sqr[start]) < outter:
        while(c1 <= inner or c2 >= outter):
            mid = (start + end) // 2
            c1 = math.sqrt(list_of_c_sqr[mid])

            if c1 <= inner:
                start = mid + 1
            elif c1 >= outter:
                end = mid
            else:
                start = mid

            c1 = math.sqrt(list_of_c_sqr[start])
            c2 = math.sqrt(list_of_c_sqr[end])

            if c2 >= outter:
                end = end - 1

        if start != end:
            for eachVal in list_of_c_sqr[start:end]: print(dict_of_c_sqr.get(eachVal))
        else:
            print(dict_of_c_sqr.get(list_of_c_sqr[start]))





# solution(int(2), int(4), [4,4,1,3,4], [4,3,4,3,2])
solution(2, 4, [4, 0, 1, -2], [-4, 4, 3, 0])

