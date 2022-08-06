n = int(input())

list_number = input().split()

max = int(list_number[0])
min = int(list_number[0])

for num in list_number:
    if int(num) >= max:
        max = int(num)
    if int(num) <= min:
        min = int(num)

print(min, max)