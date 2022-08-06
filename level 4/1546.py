n = int(input())
score_list = input().split()

max = int(score_list[0])

for score in score_list:
    if int(score) > max:
        max = int(score)

total_score = 0
for score in score_list:
    total_score += int(score) / max * 100

print(total_score / n)