import math

def is_prime(n: int):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

t = int(input())

for _ in range(t):
    n = int(input())

    low, high = n // 2, n // 2

    while low >= 2:
        if is_prime(low) and is_prime(high):
            print(low, high, sep=' ')
            break
        else:
            low -= 1
            high += 1