n = int(input())
num_list = list(map(int, input().split()))

count = 0
for num in num_list:
    if num == 1:
        continue
    elif num == 2:
        count += 1
    else:
        is_prime_number = True
        for i in range(2, num):
            if num % i == 0:
                is_prime_number = False
                break
        
        if is_prime_number is True:
            count += 1

print(count)