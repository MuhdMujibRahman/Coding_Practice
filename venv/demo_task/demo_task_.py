# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import re
# import inverter
def solution(A):
    sortA = sorted(list(dict.fromkeys(A)))
    max_of_A = max(A)
    min_of_A = min(A)
    if min_of_A is not 1:
        return print(1)

    count = 1
    for val in range(len(A)):
        if sortA[val] != count:
            return print(count)

        else:
            count+=1
    return print(max_of_A+1)

def solution2(S):
    regex = re.compile(r'\d{3}\-\d{3}\-\d{3}')
    return bool(regex.fullmatch(S))

def solution3():
    inverted = invert(None)
    string = "".join(reversed(string))
    return string

def solution5(inner, outer,points_x,points_y):
    import math
    x = 1
    range_neg = -inner,-outer
    range_pos = inner, outer
    for i in range(len(points_x)):
        a = points_x[i]
        b = points_y[i]
        c = math.sqrt(a*a + b*b)
        valx = a,b in range(range_pos[0],range_pos[1])
        valy = a,b in range(range_neg[0],range_neg[1])

        if valx[1] is True or valy[1] is True:
            print('%s,%s'%(a,b))

def solution4(inner, outer,points_x,points_y):
    import math
    x = 1
    range_neg = -inner,-outer
    range_pos = inner, outer
    dict_of_c = {}
    list_of_c = []
    for i in range(len(points_x)):
        a = points_x[i]
        b = points_y[i]
        coordiantes = "%s,%s"%(a,b)
        c_square = a*a + b*b
        list_of_c.append(c_square)
        dict_of_c.update({coordiantes:c_square})

    start = 0
    end = len(list_of_c) - 1
    list_of_c.sort()
    c1 = 1
    c2 = 5
    while (c1<=inner and c2>=outer):
        mid = (start + end) // 2
        c1 = math.sqrt(list_of_c[mid])

        if (c1 <= inner):
            start = mid - 1
        else:
            start = mid

        c2 = math.sqrt(list_of_c[end])
        if (c2 >= 4):
            end = end - 1

    
    print(list_of_c[start:end])


A = [100,102,103]
S = "123 abs b123"

x= [0,1,2,-2,3]
y = [0,1,4,1,0]
# solution3()
# solution4(2, 4, [4, 0, 1, -2], [-4, 4, 3, 0])
if __name__ == '__main__':
    inner = input()
    outer = input()
    point_x = [int(x) for x in input().split(',')]
    point_y = [int(x) for x in input().split(',')]
    solution5(int(inner), int(outer), point_x, point_y)
# solution5(2, 4, [4, 0, 1, -2], [-4, 4, 3, 0])
# solution2(S)
