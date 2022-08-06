import sys

n = int(sys.stdin.readline())

if n > 0 and n <= 100000:
    for i in range(1, n + 1):
        print(i)