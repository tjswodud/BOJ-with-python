n = int(input())
count = 0

while n >= 0:
    if n % 5 == 0:
        print(n // 5 + count)
        break
    else:
        count += 1
        n -= 3

if n < 0:
    print(-1)