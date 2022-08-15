x = int(input())

line_number = 0
last_index = 0
while x > last_index:
    line_number += 1
    last_index += line_number

difference = last_index - x

if line_number % 2 == 0: # n/1 ~ 1/n
    numerator = line_number - difference
    denominator = difference + 1
else: # 1/n ~ n/1
    numerator = difference + 1
    denominator = line_number - difference
    
print("%d/%d" % (numerator, denominator))