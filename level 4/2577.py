a = int(input())
b = int(input())
c = int(input())
temp = a * b * c

arr = [0 for i in range(0, 10)]

while temp // 10 != 0:
    arr[int(temp % 10)] += 1
    temp /= 10

arr[int(temp % 10)] += 1

for i in range(0, 10):
    print(arr[i])