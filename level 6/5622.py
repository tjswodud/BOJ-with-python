sum = 0
dial = input()

for char in dial:
    if char == 'A' or char == 'B' or char == 'C':
        sum += 3
    if char == 'D' or char == 'E' or char == 'F':
        sum += 4
    if char == 'G' or char == 'H' or char == 'I':
        sum += 5
    if char == 'J' or char == 'K' or char == 'L':
        sum += 6
    if char == 'M' or char == 'N' or char == 'O':
        sum += 7
    if char == 'P' or char == 'Q' or char == 'R' or char == 'S':
        sum += 8
    if char == 'T' or char == 'U' or char == 'V':
        sum += 9
    if char == 'W' or char == 'X' or char == 'Y' or char == 'Z':
        sum += 10

print(sum)