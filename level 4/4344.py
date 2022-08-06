c = int(input())

for i in range(0, c):
    list = input().split()
    num_of_students = int(list[0])
    score_list = list[1:]
    total_score = 0

    for score in score_list:
        total_score += int(score)
    
    average = total_score / num_of_students

    count = 0
    for score in score_list:
        if int(score) > average:
            count += 1
    
    print("%.3f%%" % (count / num_of_students * 100))