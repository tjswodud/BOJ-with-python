def d(n: int):
    sum = 0
    sum += n

    while True:
        sum += int(n % 10)
        n //= 10

        if n // 10 == 0:
            break
        
    sum += n % 10

    return int(sum)

if __name__ == "__main__":
    arr = [False for i in range(10002)]
    
    for i in range(1, 10001):
        index = d(i)

        if index <= 10001:
            arr[index] = True
    
    for i in range(1, 10001):
        if arr[i] is False:
            print(i)