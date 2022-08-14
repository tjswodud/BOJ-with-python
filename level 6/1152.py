import sys

count = 0
string = list(sys.stdin.readline().rstrip())

if len(string) == 0:
    print(0)
else:
    for char in string:
        if char == ' ':
            count += 1
    
    if string[0] == ' ' or string[len(string) - 1] == ' ':
        count -= 1

    count += 1

    print(count)