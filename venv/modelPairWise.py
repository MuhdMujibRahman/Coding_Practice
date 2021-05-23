def max_pairwise_product_fast(numbers):
    sorted_list = sorted(numbers)
    first_max = 0
    second_max = 0
    first_max = max(sorted_list)
    sorted_list.pop()
    second_max = max(sorted_list)

    return first_max*second_max

import sys
if __name__ == '__main__':
    input_n = input()
    input_numbers = [int(x) for x in input().split(' ')]
    print(max_pairwise_product_fast(input_numbers))