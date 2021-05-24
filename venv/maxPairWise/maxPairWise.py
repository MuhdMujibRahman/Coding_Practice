def max_pairwise_product(numbers):
    sorted_list = sorted(numbers)
    first_max = 0
    second_max = 0
    first_max = max(sorted_list)
    sorted_list.pop()
    second_max = max(sorted_list)

    return first_max*second_max

import random
import sys
if __name__ == '__main__':
    input_n = '138-583-868-822-783-65-262-121-508-780'
    input_numbers = [int(x) for x in input_n.split('-')]

    print(max_pairwise_product(input_numbers))
