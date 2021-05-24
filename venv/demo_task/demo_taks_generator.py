import random
import sys
if __name__ == '__main__':
    n = int(sys.argv[1])
    inner = int(sys.argv[2])
    outer = int(sys.argv[3])
    myseed = int(sys.argv[4])
    random.seed(myseed)
    print(inner)
    print(outer)
    print(','.join([str(random.randint(1, 10)) for i in range(n)]))
    print(','.join([str(random.randint(1, 10)) for i in range(n)]))