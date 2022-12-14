def apartment(k: int, n: int) -> int:
    floor_0 = [i for i in range(1, n + 1)]

    for i in range(k):
        for j in range(1, n):
            floor_0[j] += floor_0[j - 1]

    return floor_0[-1]

t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    print(apartment(k, n))