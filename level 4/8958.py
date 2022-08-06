test_case_count = int(input())

for i in range(0, test_case_count):
    count = 0
    score = 0
    test_case = input()

    for j in range(0, len(test_case)):
        if test_case[j] == 'O':
            count += 1
            score += count
        else:
            count = 0

    print(score)