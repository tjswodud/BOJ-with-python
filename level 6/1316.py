n = int(input())
count = 0

for i in range(n):
    word = input()

    if len(word) <= 2:
        count += 1
    else:
        group_count = 0

        for j in range(2, len(word)):
            for k in range(j - 1):
                if word[k] == word[j] and word[k + 1] == word[j]:
                    continue
                elif word[k] == word[j]:
                    group_count += 1

        if group_count == 0:
            count += 1

print(count)