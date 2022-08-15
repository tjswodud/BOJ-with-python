n = int(input())

if n == 1:
    print(1)
else:
    i = 1
    low = 2
    high = 7
    while not (n >= low and n <= high):
        i += 1
        low = high + 1
        high = low + (6 * i) - 1

    print(i + 1)