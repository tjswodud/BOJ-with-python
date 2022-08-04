a, b = input().split()
a = int(a)
b = int(b)

if (a >= 1 and b >= 1) and (a <= 10000 and b <= 10000):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)