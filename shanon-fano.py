import sys
import math

def get_shannon_fano(b, p):
    return [math.ceil(math.log(1 / x, b)) for x in p]

if __name__ == "__main__":
    p = [float(x) for x in sys.argv[1].split(',')]
    b = int(sys.argv[2])
    print(get_shannon_fano(b, p))
