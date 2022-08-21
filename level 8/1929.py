def is_prime(n: int):
    b_is_prime = True

    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            b_is_prime = False
            break
    
    return b_is_prime

m, n = map(int, input().split())

for i in range(m, n + 1):
    if is_prime(i):
        print(i)