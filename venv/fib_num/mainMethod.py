def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)
import sys
n = int(50)
import time
start_time = time.time()
print(calc_fib(n))
print("--- %s seconds ---" % (time.time() - start_time))