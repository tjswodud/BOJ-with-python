import math
import sys

def is_prime(n: int):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

prime_number_list = []

for i in range(2, 123456 * 2 + 1):
    if is_prime(i):
        prime_number_list.append(i)

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break
    
    count = 0
    for i in prime_number_list:
        if i > 2 * n:
            break
        elif i > n and i <= 2 * n:
            count += 1

    print(count)