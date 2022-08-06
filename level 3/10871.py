n, x = input().split()
n = int(n)
x = int(x)

a = input().split()

for i in a:
    if int(i) < x:
        print(i, end=" ")