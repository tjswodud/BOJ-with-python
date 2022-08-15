import math

t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())

    floor = n % h
    if n % h == 0:
        floor = h

    print("%s%s" % (floor, str(math.ceil(n / h)).zfill(2)))