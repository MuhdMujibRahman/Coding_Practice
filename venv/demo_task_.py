# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import re
import inverter
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

def solution4(inner, outer,points_x,points_y):
    x = 1
    range_neg = -inner,-outer
    range_pos = inner, outer
    for i in range(len(points_x)):
        coordinates= points_x[i],points_y[i]
        valx = points_x[i],points_y[i] in range(range_pos[0],range_pos[1])
        valy = points_y[i],points_y[i] in range(range_neg[0],range_neg[1])

        if valx[1] is True or valy[1] is True:
            print(coordinates)

A = [100,102,103]
S = "123 abs b123"

x= [0,1,2,-2,3]
y = [0,1,4,1,0]
solution3()
solution4(2, 4, [4, 0, 1, -2], [-4, 4, 3, 0])
solution2(S)
