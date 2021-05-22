
import math
def find_roots(a, b, c):
    # Solve the quadratic equation ax**2 + bx + c = 0

    # import complex math module

    # calculate the discriminant
    d = (b ** 2) - (4 * a * c)

    # find two solutions
    sol1 = (-b - math.sqrt(d)) / (2 * a)
    sol2 = (-b + math.sqrt(d)) / (2 * a)
    return (sol1,sol2)

print(find_roots(2, 10, 8))