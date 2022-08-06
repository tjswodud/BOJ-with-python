nums = []
result = [0 for i in range(0, 10)]
num_count = 0

for i in range(0, 10):
    nums.append(int(input()))

for i in range(0, 10):
    result[i] = int(nums[i] % 42)

for i in range(0, 10):
    count = 0

    for j in range(i + 1, 10):
        if result[i] == result[j]:
            count += 1
    
    if count == 0:
        num_count += 1

print(num_count)