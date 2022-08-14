string = list(input())

for alphabet in range(ord('a'), ord('z') + 1):
    for i in range(0, len(string)):
        if chr(alphabet) == string[i]:
            print(i, end=' ')
            break
        
        if i == len(string) - 1:
            print(-1, end=' ')