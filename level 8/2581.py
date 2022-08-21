def is_prime(n: int):
    b_is_prime = True

    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            b_is_prime = False
            break
    
    return b_is_prime

m = int(input())
n = int(input())
num_list = []

for i in range(m, n + 1):
    if is_prime(i):
        num_list.append(i)

sum = 0
for num in num_list:
    sum += num

if len(num_list) == 0:
    print(-1)
else:
    print(sum)
    print(num_list[0])