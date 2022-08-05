a, b = input().split()
a = int(a)
b = int(b)

if (a >= -10000 and b >= -10000) and (a <= 10000 and b <= 10000):
    if a > b:
        print('>')
    elif a < b:
        print('<')
    else:
        print('==')