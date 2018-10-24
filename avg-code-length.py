import sys

def get_avg_code_length(lengths, p):
    sum = 0
    for i in range(len(lengths)):
        sum += lengths[i] * p[i]
    return sum

if __name__ == "__main__":
    p = [float(x) for x in sys.argv[1].split(',')]
    lengths = [int(x) for x in sys.argv[2].split(',')]
    print(get_avg_code_length(lengths, p))
