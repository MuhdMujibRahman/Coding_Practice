def Fib(n):
    F = [0]*(n+1)
    F[0] = 0
    F[1] = 1

    for i in range(2,n+1):
        F[i] = (F[i-1] + F[i-2]) % 10

    return F[n]

import sys
n = int(sys.argv[1])
import time
start_time = time.time()
print(Fib(n))
print("--- %s seconds ---" % (time.time() - start_time))

