import sys

def get_kraft(params, b):
    return sum([p / (b ** (idx + 1)) for idx, p in enumerate(params)])

if __name__ == "__main__":
    params = [int(x) for x in sys.argv[1].split(',')]
    b = int(sys.argv[2])
    print(get_kraft(params, b))
