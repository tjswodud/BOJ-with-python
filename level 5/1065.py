def solution(n: int) -> int:
    count = 0

    for i in range(1, n + 1):
        if i < 100:
            count += 1
        else:
            size = 3 if i < 1000 else 4
            arr = [0 for i in range(size)]
            num = i

            for j in range(0, size):
                arr[j] = num % 10
                num //= 10

            if size == 3:
                if arr[2] - arr[1] == arr[1] - arr[0]:
                    count += 1
            else:
                if arr[3] - arr[2] == arr[2] - arr[1] and arr[2] - arr[1] == arr[1] - arr[0]:
                    count += 1
    
    return count

if __name__ == "__main__":
    n = int(input())

    print(solution(n))