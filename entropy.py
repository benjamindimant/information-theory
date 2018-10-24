import sys
import math

def get_entropy(n, p):
    return -1 * sum([x * math.log(x, n) for x in p])

if __name__ == "__main__":
    p = [float(x) for x in sys.argv[1].split(',')]
    n = int(sys.argv[2])
    print(get_entropy(n, p))
