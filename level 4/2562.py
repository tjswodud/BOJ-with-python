list_number = []
index = 0

for i in range(0, 9):
    list_number.append(int(input()))

max = list_number[0]

for i in range(1, 9):
    if list_number[i] > max:
        max = list_number[i]
        index = i

print(max)
print(index + 1)