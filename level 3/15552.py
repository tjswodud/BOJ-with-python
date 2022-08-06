import sys

t = int(sys.stdin.readline())

if t >= 1 and t <= 1000000:
    for i in range(0, t):
        a, b = sys.stdin.readline().rstrip().split()
        a = int(a)
        b = int(b)

        print(a + b)